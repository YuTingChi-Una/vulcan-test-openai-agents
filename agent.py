"""Agent definitions for vulcan-test-openai-agents."""
from agents import Agent, Runner
from agents.mcp import MCPServerStdio, MCPServerStreamableHttp
from agents import function_tool

# ===== MCP SERVERS =====
filesystem_mcp = MCPServerStdio(
          name="Filesystem Server",
          params={"command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"]},
)

knowledge_base_mcp = MCPServerStreamableHttp(
          name="Knowledge Base Server",
          params={"url": "http://localhost:8010/mcp"},
)

# ===== TOOLS =====
@function_tool
def web_search(query: str) -> str:
          """Search the web for information on the given query.

              Args:
                      query: The search query string.
                          """
          return f"Search results for: {query}"

@function_tool
def summarize_text(text: str) -> str:
          """Summarize the given text into concise bullet points.

              Args:
                      text: The text content to summarize.
                          """
          return f"Summary: {text[:200]}"

@function_tool
def send_notification(message: str, channel: str = "slack") -> str:
          """Send a notification message to the specified channel.

              Args:
                      message: The notification message to send.
                              channel: Target channel - slack, email, or teams.
                                  """
          return f"Notification sent to {channel}: {message}"

# ===== AGENTS =====
research_agent = Agent(
          name="ResearchAgent",
          instructions="You are a research assistant. Gather and summarize information on given topics.",
          model="gpt-4o",
          tools=[web_search, summarize_text],
          mcp_servers=[knowledge_base_mcp],
)

summary_agent = Agent(
          name="SummaryAgent",
          instructions="You are a summarization assistant. Condense research into clear bullet points.",
          model="gpt-4o-mini",
          tools=[summarize_text, send_notification],
          mcp_servers=[filesystem_mcp],
)

writer_agent = Agent(
          name="WriterAgent",
          instructions="You are a content writer. Produce clear and engaging articles from research.",
          model="gpt-4o",
          tools=[web_search],
          mcp_servers=[filesystem_mcp],
)
