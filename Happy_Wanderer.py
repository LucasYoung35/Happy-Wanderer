import openai

#Replace "KEY" with personal api key
openai.api_key = "KEY"

modes = ["NORMAL", "SCARY", "MYSTERY", "FANTASY", "ROMANCE", "SCI-FI", "THRILLER"]

#allows the user to select what type of story they want to generate
def select_mode():

    #print menu choices
    print("What kind of story would you like to hear?")
    for i in range(len(modes)):
        print("- "+modes[i])


    #ask user for input until a valid choice is selected
    valid_input = False
    while(not valid_input):
        user_choice = input("Choose an option: ")
        user_choice = user_choice.upper().strip()
        valid_input = user_choice in modes
        if not valid_input:
            print("Invalid input: "+user_choice)
        else:
            return user_choice

#returns a prompt to the GPT-3 api
def get_prompt():

    #first get mode from user
    mode = select_mode()

    #generate a prompt
    user_input = input("Tell me a story about... ")
    return "Tell me a "+mode+" story about " + user_input + " from the first person perspective of a happy traveler"

my_prompt = get_prompt()

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=my_prompt,
    temperature = 0.4,
    max_tokens=500
)

#print (response)
print(response["choices"][0]["text"])