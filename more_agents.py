"""Additional agents, tools, and MCP servers."""
from agents import Agent, function_tool
from agents.mcp import MCPServerStreamableHttp, MCPServerSse

# ===== MCP SERVERS =====
database_mcp = MCPServerStreamableHttp(
    name="Database Server",
    params={"url": "http://localhost:8020/mcp"},
)

analytics_mcp = MCPServerSse(
    name="Analytics Server",
    params={"url": "http://localhost:8030/sse"},
)

# ===== TOOLS =====
@function_tool
def read_file(filepath: str) -> str:
    """Read and return the contents of a local file.

    Args:
        filepath: Absolute or relative path to the file.
    """
    return f"Contents of: {filepath}"

@function_tool
def execute_sql(query: str, database: str = "default") -> str:
    """Execute a SQL query against the specified database.

    Args:
        query: The SQL query to execute.
        database: Target database name.
    """
    return f"Query result on {database}: {query[:100]}"

@function_tool
def translate_text(text: str, target_language: str = "en") -> str:
    """Translate text into the specified target language.

    Args:
        text: The text to translate.
        target_language: ISO language code (e.g. zh-tw, ja, ko).
    """
    return f"Translated to {target_language}: {text[:200]}"

# ===== AGENTS =====
data_analyst_agent = Agent(
    name="DataAnalystAgent",
    instructions="You are a data analyst. Query databases and generate insights.",
    model="gpt-4o",
    tools=[execute_sql],
    mcp_servers=[database_mcp, analytics_mcp],
)

translation_agent = Agent(
    name="TranslationAgent",
    instructions="You are a translation specialist. Accurately translate content.",
    model="gpt-4o-mini",
    tools=[translate_text],
    mcp_servers=[database_mcp],
)

notification_agent = Agent(
    name="NotificationAgent",
    instructions="You are a notification dispatcher. Send alerts to the right channels.",
    model="gpt-4o-mini",
    tools=[read_file],
    mcp_servers=[analytics_mcp],
)
