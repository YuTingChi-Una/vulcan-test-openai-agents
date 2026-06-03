---
name: research-agent
license: MIT
description: >
  Research agent skill for gathering, analyzing, and summarizing information
    from the web. Uses web search and text summarization tools to produce
      structured research reports.
      tools:
        - name: web_search
            description: Search the web for information on any topic
              - name: summarize_text
                  description: Summarize long text into concise bullet points
                    - name: send_notification
                        description: Send notification when research is complete
                        ---

                        # Research Agent Skill

                        Skill for researching topics and producing structured summaries.

                        ## Tools
                        - **web_search**: Search the web for current information on any topic.
                        - **summarize_text**: Condense long text into concise bullet points.
                        - **send_notification**: Notify stakeholders when research is complete.

                        ## MCP Servers
                        - **Knowledge Base Server**: Retrieve domain-specific knowledge via HTTP MCP.
                        
