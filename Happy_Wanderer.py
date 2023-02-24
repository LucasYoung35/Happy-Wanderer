import openai

#Replace "KEY" with personal api key
openai.api_key = "KEY"

def get_prompt():
    user_input = input("Tell me a story about... ")
    return "Tell me story about " + user_input + " from the first person perspective of a happy traveler"

my_prompt = get_prompt()

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=my_prompt,
    temperature = 0.4,
    max_tokens=500
)

#print (response)
print(response["choices"][0]["text"])