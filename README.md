# Content Pipeline Project

## Overview
This project implements an automated content creation pipeline using CrewAI, a framework for orchestrating AI agents. The system consists of multiple specialized agents that work together to research, write, optimize, and review content on given topics.

## Features
- **Multi-Agent Collaboration**: Four specialized agents handle different aspects of content creation
- **Sequential Workflow**: Research → Writing → SEO Optimization → Quality Review
- **Web Search Integration**: Uses SerperDevTool for real-time information gathering
- **LLM-Powered**: Utilizes HuggingFace's Llama-3.1-8B-Instruct model for content generation
- **Modular Design**: Easily extensible with additional agents, tasks, or tools

## Project Structure
```
content pipeline/
├── README.md          # This file
├── crew.py            # Main orchestration script
├── agents.py          # Agent definitions
├── tasks.py           # Task definitions
├── llm.py             # LLM configuration
└── tools.py           # Tool definitions
```

## Agents
1. **Market Research Agent**: Gathers accurate, recent information using web search
2. **Content Writer**: Creates structured, engaging articles based on research
3. **SEO Specialist**: Optimizes content for search engines
4. **Content Quality Reviewer**: Ensures accuracy, clarity, and professionalism

## Requirements
- Python 3.8+
- CrewAI
- crewai-tools
- python-dotenv
- HuggingFace API access
- SerperDev API key

## Installation
1. Clone or navigate to the project directory
2. Install dependencies:
   ```bash
   pip install crewai crewai-tools python-dotenv
   ```
3. Set up environment variables in a `.env` file:
   ```
   HUGGINGFACE_API_KEY=your_huggingface_api_key
   SERPER_API_KEY=your_serper_api_key
   ```

## Usage
Run the main script to generate content on a specified topic:

```bash
python crew.py
```

The script is currently configured to generate content about "current application of AI in beauty industry." Modify the `inputs` dictionary in `crew.py` to change the topic.

## Configuration
- **LLM Settings**: Adjust model parameters in `llm.py` (e.g., max tokens, temperature)
- **Agent Customization**: Modify agent roles, goals, and backstories in `agents.py`
- **Task Flow**: Update task descriptions and dependencies in `tasks.py`
- **Tools**: Add or modify tools in `tools.py`

## Output
The pipeline produces a polished, SEO-optimized article in markdown format, ready for publication.