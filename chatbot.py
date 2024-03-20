from transformers import pipeline     #did not know how to install trasformers, if it could get installed then i could use the lirary in  my python projects so its showing an error 
                                     #the idea is very bacis, basically instagrams clone but an AI chatbot can be a revelation in the world of instagrammers getting left on read due to their poor communication skills
# Load the pre-trained GPT-2 model for text generation   

chatbot = pipeline("text-generation", model="gpt2")

def generate_response(user_input):
    # Generate a response based on user input
    response = chatbot(user_input, max_length=50, num_return_sequences=1)[0]['generated_text']
    return response

def main():                                               #the idea was basically to build a chatbot that would generate messages and help people reply easily
    print("Welcome to the Chatbot!")
    print("Type 'quit' to exit.")

    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        
        response = generate_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
