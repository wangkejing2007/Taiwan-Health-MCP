import asyncio
import os
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    server_script = r"d:\Taiwan-Health-MCP\src\server.py"
    server_dir = os.path.dirname(server_script)
    
    env = os.environ.copy()
    if "PYTHONPATH" in env:
        env["PYTHONPATH"] = f"{server_dir};{env['PYTHONPATH']}"
    else:
        env["PYTHONPATH"] = server_dir
    
    server_params = StdioServerParameters(
        command="python",
        args=["-u", server_script],
        env=env
    )
    
    print(f"Connecting to {server_script}...")
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                print("Session initialized!")
                
                # List tools to check if it's working
                tools = await session.list_tools()
                print(f"Found {len(tools.tools)} tools.")
                for t in tools.tools:
                    print(f" - {t.name}")
                    
                # Try a simple search
                print("\nTesting search_health_food for '銀杏'...")
                res = await session.call_tool("search_health_food", {"keyword": "銀杏"})
                print("Response received!")
                print(str(res)[:500])
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
