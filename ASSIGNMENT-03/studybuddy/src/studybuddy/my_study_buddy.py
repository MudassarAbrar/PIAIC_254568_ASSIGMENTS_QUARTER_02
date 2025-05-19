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
    agent = Agent(
    name = "StudyBuddy",
    instructions = """"
    You are StudyBuddy, a helpful and friendly AI tutor for students.
    You help students stay focused, provide study tips, and break down tough concepts.
    Always encourage them to keep going and be supportive like a mentor.
    """,
    model = model)
    
    
    print("🤖 StudyBuddy is ready to chat! Type 'exit' to quit.\n")

    while True:
        user_input = input("👨‍🎓 You: ")

        if user_input.lower() in ['exit', 'quit']:
            print("🤖 StudyBuddy: Goodbye, and happy studying! 👋")
            break

        result = Runner.run_sync(agent, user_input)
        print("🤖 StudyBuddy:", result.final_output)
        with open("study_buddy_conversation.md", "a", encoding="utf-8") as f:
            f.write(f"You: {user_input}\n")
            f.write(f"StudyBuddy: {result.final_output}\n")