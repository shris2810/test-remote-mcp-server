from fastmcp import FastMCP
import random
import json

mcp = FastMCP("Simple calculator")

# tool : add two numbers
@mcp.tool
def add(a: int, b: int) -> int:
    """
    Add two numbers together.

    args:
        a: first number
        b: second number

    returns:
        the sum of a and b
    """
    return a + b

# tool : generate random number
@mcp.tool
def random_number(min_val: int = 1 ,max_val: int =100) -> int:
    """
    generate a random number within a range

    args:
        min_val: minimum value (default = 1)
        max_val: maximum value (default = 100)

    returns:
        random integer between min_val and max_val
    """
    return random.randint(min_val, max_val)

# resource: server information
@mcp.resource("info://server")
def server_info() -> str:
    """
    get information about this server
    """
    info = {
        "name": "simple calculator",
        "tools": ["add","random_numbe"]
    }
    return json.dumps(info, indent=2)



# Start the server
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
    # mcp.run()
