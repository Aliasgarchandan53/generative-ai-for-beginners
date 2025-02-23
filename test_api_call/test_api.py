from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = AzureOpenAI(
    azure_endpoint= os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version=os.environ["AZURE_OPENAI_API_VERSION"]
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]

prompt = "Complete the following : Javascript is a ..."
messages = [
    {
    "role":"user",
    "content":prompt
    },
    {
        "role":"system",
        "content":"You are a creative assistant."
    }
]

print("Initiating conversation :\n")

completion = client.chat.completions.create(
    model=deployment,
    messages=messages
)

print("Response : \n")
print(completion.choices[0].message.content)
