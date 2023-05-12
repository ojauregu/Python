import openai

# Define OpenAI API key 
openai.api_key = "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"

# Set up the model and prompt
model_engine = "text-davinci-003"
prompt = "Once upon a time, in a land far, far away, there was a princess who..."

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)