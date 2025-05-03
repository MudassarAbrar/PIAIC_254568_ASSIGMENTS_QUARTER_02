from agents import Agent, Runner , AsyncOpenAI , set_default_openai_client , set_tracing_disabled , OpenAIChatCompletionsModel
from dotenv import load_dotenv
import os

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(api_key=gemini_api_key,base_url = "https://generativelanguage.googleapis.com/v1beta/openai/" )

set_default_openai_client(external_client)

set_tracing_disabled(True)



model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash", 
    openai_client=external_client 
)


def my_first_agent():
    
    agent = Agent(name = "assistant",instructions = "You are supposed to respond with only Hello World nothing less nor more to every single prompt you get" , model = model)
    result= Runner.run_sync(agent ,"Hi! My name is Mudassir Abrar! Greetings",)
    print(result.final_output)

