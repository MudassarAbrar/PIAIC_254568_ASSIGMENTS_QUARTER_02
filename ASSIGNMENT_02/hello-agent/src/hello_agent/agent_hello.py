#import important components from the sdk and dotenv
from agents import Agent, Runner , AsyncOpenAI , set_default_openai_client , set_tracing_disabled , OpenAIChatCompletionsModel
from dotenv import load_dotenv
import os

#load the env variable
load_dotenv()

#get the key
gemini_api_key = os.getenv("GEMINI_API_KEY")

#create external api client using api key and base url(model url)
external_client = AsyncOpenAI(api_key=gemini_api_key,base_url = "https://generativelanguage.googleapis.com/v1beta/openai/" )


#set client as default open client for sdk
set_default_openai_client(external_client)
#disabled tracing as gemini doesnt provide the service 
set_tracing_disabled(True)

#initialize char model

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash", 
    openai_client=external_client 
)

#function to create and run  the simple agent 
def my_first_agent():
    #creats agent
    agent = Agent(name = "assistant",instructions = "You are supposed to respond with only Hello World nothing less nor more to every single prompt you get" , model = model)

    #run agent using test prompt
    result= Runner.run_sync(agent ,"Hi! My name is Mudassir Abrar! Greetings",)
    print(result.final_output)

