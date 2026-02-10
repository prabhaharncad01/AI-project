import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "You are an AI business growth expert."},
        {"role": "user", "content": "Suggest growth strategies for a small textile shop in Chennai."}
    ]
)

print(response.choices[0].message.content)



