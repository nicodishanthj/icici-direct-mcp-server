import asyncio
import json
import httpx
import ollama
import sys
from typing import Dict, Any

MCP_SERVER_URL = "http://localhost:8080"
OLLAMA_MODEL = "llama3"


class MCPDemoClient:
    def __init__(self):
        self.http_client = httpx.AsyncClient(timeout=30.0)
        self.ollama_client = ollama.Client()
        self.tools = {}

    async def initialize(self):
        response = await self.http_client.get(f"{MCP_SERVER_URL}/info")
        response.raise_for_status()

        server_info = response.json()
        self.tools = {
            tool["name"]: {
                "description": tool.get("description", ""),
                "parameters": tool.get("parameters", {})
            }
            for tool in server_info.get("tools", [])
        }

        print(f"Connected to MCP server with {len(self.tools)} available tools")

    async def call_tool(self, tool_name: str, params: Dict[str, Any]):

        response = await self.http_client.post(
            f"{MCP_SERVER_URL}/tools/{tool_name}",
            json=params
        )
        response.raise_for_status()
        return response.json()["result"]

    def get_tool_definitions(self):

        return [
            {
                "name": tool_name,
                "description": tool_info["description"],
                "parameters": {
                    "type": "object",
                    "properties": {
                        param_name: {
                            "type": "string",
                            "description": param_info.get("description", "")
                        }
                        for param_name, param_info in tool_info.get("parameters", {}).items()
                    },
                    "required": []
                }
            }
            for tool_name, tool_info in self.tools.items()
        ]

    async def process_query(self, user_query: str):

        print(f"\n🔍 Processing query: {user_query}")
        system_prompt = """You are a Financial Market Assistant with access to real-time and historical market data from ICICI Direct.
Use the available tools to help users with their financial data requests. Remember to:
1. First initialize the session if needed
2. Connect to WebSocket before trying to access real-time data
3. Format responses to be easy to read
4. Explain what you're doing at each step
5. Don't make up information - use the tools to get real data

When you need to use a tool, respond with JSON in this format:
{
  "tool": "tool_name",
  "parameters": {
    "param1": "value1",
    "param2": "value2"
  }
}
"""


        tools_description = "Available tools:\n\n"
        for tool_name, tool_info in self.tools.items():
            tools_description += f"- {tool_name}: {tool_info['description']}\n"
            if tool_info['parameters']:
                tools_description += "  Parameters:\n"
                for param_name, param_info in tool_info['parameters'].items():
                    tools_description += f"  - {param_name}: {param_info.get('description', '')}\n"
            tools_description += "\n"

        messages = [
            {"role": "system", "content": system_prompt + "\n\n" + tools_description},
            {"role": "user", "content": user_query}
        ]

        print("\n🤖 Sending query to LLM...")
        response = self.ollama_client.chat(model=OLLAMA_MODEL, messages=messages)
        model_response = response["message"]["content"]

        try:
            tool_call = self.extract_tool_call(model_response)

            if tool_call:
                tool_name = tool_call.get("tool")
                parameters = tool_call.get("parameters", {})

                print(f"\n🔧 LLM is calling tool: {tool_name}")
                print(f"   with parameters: {json.dumps(parameters, indent=2)}")

                tool_result = await self.call_tool(tool_name, parameters)
                print(f"\n📊 Tool result: {tool_result[:100]}...")


                messages.append({"role": "assistant", "content": model_response})
                messages.append({"role": "user", "content": f"Tool result: {tool_result}"})

                print("\n🤖 Getting final response from LLM with tool results...")
                response = self.ollama_client.chat(model=OLLAMA_MODEL, messages=messages)
                return response["message"]["content"]
            else:
                return model_response
        except Exception as e:
            print(f"Error processing tool call: {e}")
            return model_response

    def extract_tool_call(self, content):
        try:
            return json.loads(content)
        except:
            import re
            json_matches = re.findall(r'```(?:json)?\s*({\s*"tool"\s*:.*?})\s*```', content, re.DOTALL)
            if json_matches:
                try:
                    return json.loads(json_matches[0])
                except:
                    pass

            all_json_matches = re.findall(r'{.*"tool".*}', content, re.DOTALL)
            for match in all_json_matches:
                try:
                    obj = json.loads(match)
                    if "tool" in obj:
                        return obj
                except:
                    pass

            return None

    async def close(self):
        await self.http_client.aclose()


async def run_demo():
    client = MCPDemoClient()

    try:
        await client.initialize()

        print("\n===== MCP DEMONSTRATION =====")
        print("This demo shows how MCP enables language models to use specialized tools")
        print("Type your financial data query or 'exit' to quit")

        while True:
            user_input = input("\n💬 Your query: ")
            if user_input.lower() in ["exit", "quit"]:
                break

            response = await client.process_query(user_input)
            print("\n🔹 LLM Response:")
            print(response)

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(run_demo())
