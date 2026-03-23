from langchain_aws import ChatBedrockConverse

# function to connect to Bedrock model
def demo_chatbot(messages):
    demo_llm = ChatBedrockConverse(
        credentials_profile_name='default',
        region_name="us-east-1",
        model="us.amazon.nova-pro-v1:0",
        temperature=0.1,
        max_tokens=1000
    )
    return demo_llm.invoke(messages)

# test input
messages = [
    {
        "role": "user",
        "content": [{"text": "What is the capital of France?"}],
    }
]

# call chatbot
response = demo_chatbot(messages)

# print only answer
print(response.content)