from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message)
