from agents import Agent, Runner

research_agent = Agent(
      name="ResearchAgent",
      instructions="You are a research assistant. Gather and summarize information on given topics.",
)

summary_agent = Agent(
      name="SummaryAgent",
      instructions="You are a summarization assistant. Condense research into clear bullet points.",
)

if __name__ == "__main__":
      result = Runner.run_sync(research_agent, "Summarize recent AI trends.")
      print(result.final_output)
  
