from crewai.llm import LLM
from dotenv import load_dotenv

load_dotenv()

# Initialize the LLM with huggingface model
llm = LLM(
    model="huggingface/meta-llama/Llama-3.1-8B-Instruct",
    max_new_tokens=512,
    temperature=0.7
)