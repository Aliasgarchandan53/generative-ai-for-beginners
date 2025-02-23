from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv('AZURE_OPENAI_API_KEY'),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION")
)

deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

#Start with the prompt here
language = input("Enter the language you want to generate code in :")
version = input("Enter the version of the language :")
question = input("Enter the question/algorithm you want the code for :")

instructions = input('Enter additional instructions : ')

message_list=[
    {
        "role":"system",
        "content":f"You are a technical assistant in a university who will help the students generate the code in language: {language}, version:{version}. Keep in mind following additional instructions : {instructions if instructions else "No instructions given."} "
    },
    {
        "role":"user",
        "content":question
    }
]

response = client.chat.completions.create(
    model=deployment,
    messages=message_list,
    max_tokens=500,
    temperature=0.1
)

print(f"Response : {response}")
print(f"Result:\n{response.choices[0].message.content}")