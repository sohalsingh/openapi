import openai

def generate_article(prompt):
    openai.api_key = 'YOUR_API_KEY'  # Replace with your OpenAI API key

    response = openai.Completion.create(
        engine='text-davinci-003',  # Use the GPT-3.5 model
        prompt=prompt,
        max_tokens=500,  # Control the length of the generated article
        n = 1,  # Generate a single response
        stop=None,  # Stop generating after reaching the maximum tokens
        temperature=0.7,  # Control the randomness of the output
        top_p=1.0  # Control the diversity of the output
    )

    return response.choices[0].text.strip()

def main():
    print("Welcome to the AI Article Builder!")
    prompt = input("Enter the article prompt or introduction: ")

    generated_article = generate_article(prompt)

    print("\nGenerated Article:")
    print(generated_article)

if __name__ == "__main__":
    main()
