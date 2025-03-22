import json
import os
import logging
from typing import Dict, Any, Optional, List
import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from breeze_connect import BreezeConnect

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("icici-direct-mcp-server")

# Initialize FastAPI
app = FastAPI(title="ICICI Direct MCP HTTP Server")

# Get API key from environment
ICICI_API_KEY = os.environ.get("ICICI_API_KEY", "")

# Initialize Breeze Connect client
breeze = BreezeConnect(api_key=ICICI_API_KEY)

# Global state
ws_connected = False
latest_ticks = {}

# Define request model for tool calls
class ToolCallRequest(BaseModel):
    tool_name: str
    parameters: Dict[str, Any]

# Callback to receive ticks
def on_ticks(ticks):
    global latest_ticks
    logger.debug(f"Received ticks: {len(ticks)} items")
    for tick in ticks:
        if "stock_token" in tick:
            latest_ticks[tick["stock_token"]] = tick

# Set up the callback
breeze.on_ticks = on_ticks

#######################
# Tool Implementations
#######################

# Initialize session
async def initialize_session(api_secret: str, session_token: str) -> str:
    """Initialize the ICICI Direct Breeze API session.

    Args:
        api_secret: Your API secret key
        session_token: Your API session token
    """
    try:
        breeze.generate_session(api_secret=api_secret, session_token=session_token)
        return "Session initialized successfully"
    except Exception as e:
        logger.error(f"Failed to initialize session: {e}")
        return f"Failed to initialize session: {str(e)}"

# Connect WebSocket
async def connect_websocket() -> str:
    """Connect to the ICICI Direct Breeze WebSocket for real-time data."""
    global ws_connected
    try:
        breeze.ws_connect()
        ws_connected = True
        return "WebSocket connected successfully"
    except Exception as e:
        ws_connected = False
        logger.error(f"Failed to connect to WebSocket: {e}")
        return f"Failed to connect to WebSocket: {str(e)}"

# Disconnect WebSocket
async def disconnect_websocket() -> str:
    """Disconnect from the ICICI Direct Breeze WebSocket."""
    global ws_connected
    try:
        breeze.ws_disconnect()
        ws_connected = False
        return "WebSocket disconnected successfully"
    except Exception as e:
        logger.error(f"Failed to disconnect from WebSocket: {e}")
        return f"Failed to disconnect from WebSocket: {str(e)}"

# Subscribe stock feeds
async def subscribe_stock_feeds(stock_token: str, interval: Optional[str] = None) -> str:
    """Subscribe to real-time stock feeds by stock token.

    Args:
        stock_token: Stock token (e.g., "4.1!2885")
        interval: Optional interval for OHLCV data (e.g., "1minute")
    """
    global ws_connected
    if not ws_connected:
        return "WebSocket is not connected. Please connect first."

    try:
        if interval:
            breeze.subscribe_feeds(stock_token=stock_token, interval=interval)
            return f"Successfully subscribed to {stock_token} with interval {interval}"
        else:
            breeze.subscribe_feeds(stock_token=stock_token)
            return f"Successfully subscribed to {stock_token}"
    except Exception as e:
        logger.error(f"Failed to subscribe to feeds: {e}")
        return f"Failed to subscribe to feeds: {str(e)}"

# Unsubscribe stock feeds
async def unsubscribe_stock_feeds(stock_token: str, interval: Optional[str] = None) -> str:
    """Unsubscribe from real-time stock feeds by stock token.

    Args:
        stock_token: Stock token (e.g., "4.1!2885")
        interval: Optional interval for OHLCV data (e.g., "1minute")
    """
    global ws_connected
    if not ws_connected:
        return "WebSocket is not connected."

    try:
        if interval:
            breeze.unsubscribe_feeds(stock_token=stock_token, interval=interval)
            return f"Successfully unsubscribed from {stock_token} with interval {interval}"
        else:
            breeze.unsubscribe_feeds(stock_token=stock_token)
            return f"Successfully unsubscribed from {stock_token}"
    except Exception as e:
        logger.error(f"Failed to unsubscribe from feeds: {e}")
        return f"Failed to unsubscribe from feeds: {str(e)}"

# Get latest ticks
async def get_latest_ticks(stock_token: Optional[str] = None) -> str:
    """Get the latest received ticks from the WebSocket.

    Args:
        stock_token: Optional stock token to filter ticks for a specific stock
    """
    global ws_connected, latest_ticks
    if not ws_connected:
        return "WebSocket is not connected. Please connect first."

    if stock_token:
        if stock_token in latest_ticks:
            return json.dumps(latest_ticks[stock_token], indent=2)
        else:
            return f"No ticks received for {stock_token} yet"
    else:
        return json.dumps(latest_ticks, indent=2)

# Get customer details
async def get_customer_details(api_session: str) -> str:
    """Get customer details.

    Args:
        api_session: API session value
    """
    try:
        response = breeze.get_customer_details(api_session=api_session)
        return json.dumps(response, indent=2)
    except Exception as e:
        logger.error(f"Failed to get customer details: {e}")
        return f"Failed to get customer details: {str(e)}"

# Get demat holdings
async def get_demat_holdings() -> str:
    """Get demat holdings."""
    try:
        response = breeze.get_demat_holdings()
        return json.dumps(response, indent=2)
    except Exception as e:
        logger.error(f"Failed to get demat holdings: {e}")
        return f"Failed to get demat holdings: {str(e)}"

# Get funds
async def get_funds() -> str:
    """Get account funds."""
    try:
        response = breeze.get_funds()
        return json.dumps(response, indent=2)
    except Exception as e:
        logger.error(f"Failed to get funds: {e}")
        return f"Failed to get funds: {str(e)}"

# Get historical data
async def get_historical_data(
        interval: str,
        from_date: str,
        to_date: str,
        stock_code: str,
        exchange_code: str,
        product_type: str,
        expiry_date: Optional[str] = None,
        right: Optional[str] = None,
        strike_price: Optional[str] = None
) -> str:
    """Get historical price data.

    Args:
        interval: Interval (e.g., "1minute", "5minute", "30minute", "1day")
        from_date: From date (e.g., "2025-02-03T09:20:00.000Z")
        to_date: To date (e.g., "2025-02-03T09:22:00.000Z")
        stock_code: Stock code (e.g., "NIFTY" or "RELIND")
        exchange_code: Exchange code (e.g., "NSE" or "NFO")
        product_type: Product type (e.g., "cash", "futures", "options")
        expiry_date: Expiry date for derivatives (e.g., "2025-02-27T07:00:00.000Z")
        right: Option right (e.g., "call", "put", "others")
        strike_price: Strike price for options (e.g., "23200")
    """
    try:
        kwargs = {
            "interval": interval,
            "from_date": from_date,
            "to_date": to_date,
            "stock_code": stock_code,
            "exchange_code": exchange_code,
            "product_type": product_type
        }

        # Add optional parameters if provided
        if expiry_date:
            kwargs["expiry_date"] = expiry_date
        if right:
            kwargs["right"] = right
        if strike_price:
            kwargs["strike_price"] = strike_price

        response = breeze.get_historical_data(**kwargs)
        return json.dumps(response, indent=2)
    except Exception as e:
        logger.error(f"Failed to get historical data: {e}")
        return f"Failed to get historical data: {str(e)}"

# Get quotes
async def get_quotes(
        stock_code: str,
        exchange_code: str,
        expiry_date: Optional[str] = None,
        product_type: Optional[str] = None,
        right: Optional[str] = None,
        strike_price: Optional[str] = None
) -> str:
    """Get quotes for a stock or derivative.

    Args:
        stock_code: Stock code (e.g., "NIFTY")
        exchange_code: Exchange code (e.g., "NSE" or "NFO")
        expiry_date: Expiry date for derivatives (e.g., "2025-02-27T06:00:00.000Z")
        product_type: Product type (e.g., "cash", "futures", "options")
        right: Option right (e.g., "call", "put", "others")
        strike_price: Strike price for options (e.g., "0" for futures)
    """
    try:
        kwargs = {
            "stock_code": stock_code,
            "exchange_code": exchange_code
        }

        # Add optional parameters if provided
        if expiry_date:
            kwargs["expiry_date"] = expiry_date
        if product_type:
            kwargs["product_type"] = product_type
        if right:
            kwargs["right"] = right
        if strike_price:
            kwargs["strike_price"] = strike_price

        response = breeze.get_quotes(**kwargs)
        return json.dumps(response, indent=2)
    except Exception as e:
        logger.error(f"Failed to get quotes: {e}")
        return f"Failed to get quotes: {str(e)}"

# Register all tools
TOOLS = {
    "initialize_session": initialize_session,
    "connect_websocket": connect_websocket,
    "disconnect_websocket": disconnect_websocket,
    "subscribe_stock_feeds": subscribe_stock_feeds,
    "unsubscribe_stock_feeds": unsubscribe_stock_feeds,
    "get_latest_ticks": get_latest_ticks,
    "get_customer_details": get_customer_details,
    "get_demat_holdings": get_demat_holdings,
    "get_funds": get_funds,
    "get_historical_data": get_historical_data,
    "get_quotes": get_quotes
}

#######################
# FastAPI Routes
#######################

@app.get("/")
async def root():
    return {"status": "healthy", "service": "ICICI Direct MCP HTTP Server"}

@app.get("/info")
async def get_info():
    """Get server info and available tools"""
    tools = []
    for name, func in TOOLS.items():
        tools.append({
            "name": name,
            "description": func.__doc__ or "",
            # Get parameters from function signature
            "parameters": {
                k: {"type": "string", "description": ""}
                for k in func.__annotations__ if k != "return"
            }
        })

    return {
        "name": "icici-direct-breeze",
        "description": "ICICI Direct Breeze API MCP Server",
        "tools": tools
    }

@app.post("/tools/call")
async def call_tool(request: ToolCallRequest):
    """Call an MCP tool by name with parameters"""
    tool_name = request.tool_name
    parameters = request.parameters

    if tool_name not in TOOLS:
        raise HTTPException(status_code=404, detail=f"Tool {tool_name} not found")

    try:
        # Get the tool function
        tool_func = TOOLS[tool_name]

        # Call the tool function with the provided parameters
        result = await tool_func(**parameters)

        return {"result": result}
    except Exception as e:
        logger.error(f"Error calling tool {tool_name}: {e}")
        raise HTTPException(status_code=500, detail=f"Error calling tool: {str(e)}")

# Add each tool as a direct HTTP endpoint
for tool_name, tool_func in TOOLS.items():
    # Define a closure to capture the current tool_func
    def create_endpoint(func):
        async def endpoint(request: Request):
            try:
                # Parse request body
                body = await request.json()
                # Call the tool function
                result = await func(**body)
                return {"result": result}
            except Exception as e:
                logger.error(f"Error in endpoint {func.__name__}: {e}")
                raise HTTPException(status_code=500, detail=str(e))
        return endpoint

    # Register the endpoint
    endpoint_handler = create_endpoint(tool_func)
    app.post(f"/tools/{tool_name}")(endpoint_handler)

# Run the server if this file is executed directly
if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    logger.info(f"Starting ICICI Direct MCP HTTP Server on port {port}")
    uvicorn.run(app, host="0.0.0.0", port=port)
