from agents import Agent, function_tool

# ===== AGENT =====
research_agent = Agent(
      name="ResearchAgent",
      instructions="You are a research assistant. Gather and summarize information.",
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

# ===== OTHER =====
class DataTransformer:
      """Utility for transforming and cleaning data outputs."""

    def clean(self, text: str) -> str:
              return text.strip()

    def to_markdown(self, data: dict) -> str:
              return "\n".join(f"- **{k}**: {v}" for k, v in data.items())
      
