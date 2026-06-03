from agents import Agent, Runner, function_tool
from agents.mcp import MCPServerStdio

# ===== AGENT =====
research_agent = Agent(
      name="ResearchAgent",
      instructions="You are a research assistant. Gather and summarize information.",
)
writer_agent = Agent(
      name="WriterAgent",
      instructions="You are a writer. Produce clear and engaging content.",
)

# ===== TOOL =====
@function_tool
def web_search(query: str) -> str:
      """Search the web for information on the given query."""
      return f"Search results for: {query}"

@function_tool
def summarize_text(text: str) -> str:
      """Summarize the given text into key bullet points."""
      return f"Summary: {text[:200]}"

@function_tool
def send_email(to: str, subject: str, body: str) -> str:
      """Send an email to the specified recipient."""
      return f"Email sent to {to}"

# ===== SKILL =====
async def research_skill(topic: str) -> str:
      """Skill: Research a topic and return a summary."""
      agent = Agent(
          name="ResearchSkillAgent",
          instructions="Research the topic and summarize findings.",
          tools=[web_search, summarize_text],
      )
      result = await Runner.run(agent, topic)
      return result.final_output

async def writing_skill(brief: str) -> str:
      """Skill: Write content from a brief."""
      agent = Agent(
          name="WritingSkillAgent",
          instructions="Write engaging content based on the brief.",
      )
      result = await Runner.run(agent, brief)
      return result.final_output

# ===== MCP SERVER =====
filesystem_mcp = MCPServerStdio(
      name="FilesystemServer",
      params={"command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"]},
)
brave_search_mcp = MCPServerStdio(
      name="BraveSearchServer",
      params={"command": "npx", "args": ["-y", "@modelcontextprotocol/server-brave-search"]},
)

# ===== AI MODEL =====
gpt4o_agent = Agent(
      name="GPT4oAgent",
      instructions="Advanced reasoning and analysis.",
      model="gpt-4o",
)
gpt4o_mini_agent = Agent(
      name="GPT4oMiniAgent",
      instructions="Fast, efficient responses for simple tasks.",
      model="gpt-4o-mini",
)

# ===== OTHER =====
class DataTransformer:
      """Utility for transforming and cleaning data outputs."""

    def clean(self, text: str) -> str:
              return text.strip()

    def to_markdown(self, data: dict) -> str:
              return "\n".join(f"- **{k}**: {v}" for k, v in data.items())
      
