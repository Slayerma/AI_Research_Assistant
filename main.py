from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
import azure.identity
import openai
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool
import os

load_dotenv(override=True)
API_HOST = os.getenv("API_HOST", "github")

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str] = []  # Make sources optional with default empty list
    tools_used: list[str] = []  # Make tools_used optional with default empty list

# ...existing code...

if API_HOST == "github":
    client = ChatOpenAI(
        base_url="https://models.inference.ai.azure.com",
        api_key=os.environ["GITHUB_TOKEN"],
        model_name=os.getenv("GITHUB_MODEL", "gpt-4o"),
        temperature=0.7,
        max_tokens=500,
        streaming=True
    )
else:
    client = ChatOpenAI(
        api_key=os.environ["OPENAI_KEY"],
        model_name=os.environ["OPENAI_MODEL"],
        temperature=0.7,
        max_tokens=500,
        streaming=True
    )


# ...existing code...
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are an AI agent tasked with creating a compelling, medium-length blog post about generative AI, aimed specifically at tech enthusiasts. 
            Your blog post should effectively execute a user query by exploring key topics such as current trends, innovative applications, future predictions, 
            and the societal impacts of generative AI technology. 
            Write in a clear, engaging, and insightful style that balances technical depth with accessibility. 
            Enhance the content with SEO keywords and phrases to boost online visibility, and structure the post with clear sections, headings, and bullet points as needed. 
            Additionally, incorporate engaging elements such as a little humor, storytelling, analogies, and rhetorical questions to make the content lively and relatable. 
            My previous communications emphasize iterative improvements, clarity, and precise detail, so please ensure these qualities are reflected in your response.\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool, wiki_tool, save_tool]
agent = create_tool_calling_agent(
    llm=client,
    prompt=prompt,
    tools=tools
)

# ...existing code...

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
query = input("What can i help you research? ")
raw_response = agent_executor.invoke({"query": query})

try:
    # The output is directly in raw_response['output'], not as a list
    structured_response = parser.parse(raw_response["output"])
    print(structured_response)
except Exception as e:
    print("Error parsing response:", e)
    print("\nRaw Response Structure:")
    print(f"Keys available: {raw_response.keys()}")
    print("\nFull Response:")
    print(raw_response["output"])