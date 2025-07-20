from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)