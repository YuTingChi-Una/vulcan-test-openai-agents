"""Agent definitions for vulcan-test-openai-agents."""
from agents import Agent, Runner
from agents.mcp import MCPServerStreamableHttp
from agents import function_tool

# ===== MCP SERVERS =====
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

# ===== AGENTS =====
research_agent = Agent(
          name="ResearchAgent",
          instructions="You are a research assistant. Gather and summarize information on given topics.",
          model="gpt-4o",
          tools=[web_search, summarize_text],
          mcp_servers=[knowledge_base_mcp],
)
