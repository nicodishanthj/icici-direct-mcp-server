# Input/Output Parameters by Paragraph - CGCXS540

## 1. MAIN PROCEDURE DIVISION

### Input Parameters
| Variable Path | Name | Type | Length | Business Name | Description |
|--------------|------|------|--------|---------------|-------------|
| LINKAGE | STANDARD-PIN-ROUTINE-PARMS | GROUP | - | PIN Routine Interface | Complete copybook structure |
| LINKAGE | MAINLINE | CONTROL | - | Main Control | Program control parameter |

### Outgoing Calls
| Function Name | Parameters |
|---------------|------------|
| PERFORM CHECK-FUNCTION | Internal paragraph call |

### Output Parameters
| Variable Path | Name | Type | Length | Business Name | Description |
|--------------|------|------|--------|---------------|-------------|
| SYSTEM | GOBACK | CONTROL | - | Program Return | Return to calling program |

---

## 2. CHECK-FUNCTION Paragraph

### Input Parameters
| Variable Path | Name | Type | Length | Business Name | Description |
|--------------|------|------|--------|---------------|-------------|
| STANDARD-PIN-ROUTINE-PARMS | PIN-FUNCTION | ALPHANUMERIC | 1 | Function Code | PIN operation indicator |
| STANDARD-PIN-ROUTINE-PARMS | GENERATE-PINS | CONDITION | - | Generate Flag | 88-level condition ('G') |
| STANDARD-PIN-ROUTINE-PARMS | SCRAMBLE-PINS | CONDITION | - | Scramble Flag | 88-level condition ('S') |

### Outgoing Calls
| Function Name | Parameters |
|---------------|------------|
| PERFORM PIN-GENERATION-ROUTINE | Internal paragraph call |
| PERFORM PIN-SCRAMBLING-ROUTINE | Internal paragraph call |

### Output Parameters
| Variable Path | Name | Type | Length | Business Name | Description |
|--------------|------|------|--------|---------------|-------------|
| STANDARD-PIN-ROUTINE-PARMS | PIN-OK | CONDITION | - | Success Status | Success indicator flag |
| STANDARD-PIN-ROUTINE-PARMS | PIN-INVALID-FUNCTION | CONDITION | - | Error Status | Invalid function error flag |

---

## 3. PIN-GENERATION-ROUTINE Paragraph

### Input Parameters
| Variable Path | Name | Type | Length | Business Name | Description |
|--------------|------|------|--------|---------------|-------------|
| WORKING-STORAGE | FIRST-TIME | CONDITION | - | First Time Flag | Initialization indicator |
| WORKING-STORAGE | BATCH | CONDITION | - | Batch Mode | Execution mode flag |
| RESULTS | JOB-NUMBER | ALPHANUMERIC | 8 | Job Number | System job identifier |
| RESULTS | MICRO-SECONDS | PACKED DECIMAL | 15 | Microseconds | System timing value |
| WORKING-STORAGE | WS-SEED | NUMERIC | 10 | Random Seed | Random number seed |

### Outgoing Calls
| Function Name | Parameters |
|---------------|------------|
| PERFORM ACCESS-SYSTEM-CONTROL-INFO | Internal paragraph call |
| FUNCTION RANDOM | WS-SEED (first call) |
| FUNCTION RANDOM | None (subsequent calls) |

### Output Parameters
| Variable Path | Name | Type | Length | Business Name | Description |
|--------------|------|------|--------|---------------|-------------|
| STANDARD-PIN-ROUTINE-PARMS | PGR-PIN-1 | NUMERIC | 4 | Generated PIN 1 | First generated PIN |
| STANDARD-PIN-ROUTINE-PARMS | PGR-PIN-2 | NUMERIC | 4 | Generated PIN 2 | Second generated PIN |
| WORKING-STORAGE | NOT-FIRST-TIME | CONDITION | - | Init Complete Flag | Initialization complete indicator |
| WORKING-STORAGE | WS-PIN-1 | NUMERIC | - | Work PIN 1 | First random work value |
| WORKING-STORAGE | WS-PIN-2 | NUMERIC | - | Work PIN 2 | Second random work value |
| WORKING-STORAGE | WS-MICRO | ALPHANUMERIC | 15 | Work Microseconds | Microseconds work area |

---

## 4. ACCESS-SYSTEM-CONTROL-INFO Paragraph

### Input Parameters
| Variable Path | Name | Type | Length | Business Name | Description |
|--------------|------|------|--------|---------------|-------------|
| LINKAGE | CB1 | GROUP | - | Control Block 1 | System control block |
| LINKAGE | CB2 | GROUP | - | Control Block 2 | System control block |
| LINKAGE | PTR1 | POINTER ARRAY | 256 | Pointer Array 1 | System pointer array |
| LINKAGE | PTR2 | POINTER ARRAY | 256 | Pointer Array 2 | System pointer array |
| WORKING-STORAGE | FULL-WORD | NUMERIC | 8 | Full Word Work | System access work area |

### Outgoing Calls
| Function Name | Parameters |
|---------------|------------|
| SET ADDRESS OF CB1/CB2 | System control block navigation |

### Output Parameters
| Variable Path | Name | Type | Length | Business Name | Description |
|--------------|------|------|--------|---------------|-------------|
| RESULTS | JOB-NAME | ALPHANUMERIC | 8 | Job Name | Process identifier |
| RESULTS | PROC-STEP | ALPHANUMERIC | 8 | Procedure Step | Procedure step name |
| RESULTS | STEP-NAME | ALPHANUMERIC | 8 | Step Name | Step name |
| RESULTS | PROGRAM-NAME | ALPHANUMERIC | 8 | Program Name | Executing program name |
| RESULTS | JOB-NUMBER | ALPHANUMERIC | 8 | Job Number | System job number |
| RESULTS | PROGRAM-NAME2 | ALPHANUMERIC | 8 | Program Name 2 | Alternate program name |
| RESULTS | JOB-CLASS | ALPHANUMERIC | 1 | Job Class | Job classification |
| RESULTS | MSG-CLASS | ALPHANUMERIC | 1 | Message Class | Message classification |
| RESULTS | USER-ID | ALPHANUMERIC | 8 | User ID | User identification |
| RESULTS | GROUP-NAME | ALPHANUMERIC | 8 | Group Name | Security group name |
| RESULTS | USER-NAME | ALPHANUMERIC | 20 | User Name | Full user name |
| RESULTS | PROGRAMMER-NAME | ALPHANUMERIC | 20 | Programmer Name | Programmer identification |
| RESULTS | MICRO-SECONDS | PACKED DECIMAL | 15 | Microseconds | Calculated timing value |
| WORKING-STORAGE | BATCH | CONDITION | - | Batch Mode Flag | Batch execution indicator |
| WORKING-STORAGE | CICS | CONDITION | - | CICS Mode Flag | CICS execution indicator |
| WORKING-STORAGE | PTR4 | POINTER | - | Work Pointer | System navigation pointer |
| WORKING-STORAGE | FOUR-BYTES | ALPHANUMERIC | 4 | Four Byte Work | Field extraction work area |

---

## 5. PIN-SCRAMBLING-ROUTINE Paragraph

### Input Parameters
| Variable Path | Name | Type | Length | Business Name | Description |
|--------------|------|------|--------|---------------|-------------|
| STANDARD-PIN-ROUTINE-PARMS | PSS-KEY-1 | NUMERIC | 8 | Scramble Key 1 | First scrambling key |
| STANDARD-PIN-ROUTINE-PARMS | PSS-KEY-2 | NUMERIC | 8 | Scramble Key 2 | Second scrambling key |
| STANDARD-PIN-ROUTINE-PARMS | PSS-PIN-OFFSET-1 | ALPHANUMERIC | 8 | PIN Offset 1 | First PIN offset data |
| STANDARD-PIN-ROUTINE-PARMS | PSS-PIN-OFFSET-2 | ALPHANUMERIC | 8 | PIN Offset 2 | Second PIN offset data |

### Outgoing Calls
| Function Name | Parameters |
|---------------|------------|
| None | Pure computational logic |

### Output Parameters
| Variable Path | Name | Type | Length | Business Name | Description |
|--------------|------|------|--------|---------------|-------------|
| STANDARD-PIN-ROUTINE-PARMS | PSR-PIN-OFFSET-1 | ALPHANUMERIC | 8 | Scrambled Result 1 | First scrambled output |
| STANDARD-PIN-ROUTINE-PARMS | PSR-PIN-OFFSET-2 | ALPHANUMERIC | 8 | Scrambled Result 2 | Second scrambled output |
| WORKING-STORAGE | SS1 | NUMERIC | 1 | Subscript 1 | Loop counter |
| WORKING-STORAGE | SS2 | NUMERIC | 1 | Subscript 2 | Target index from key |
