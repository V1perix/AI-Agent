import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()

    #args:

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("Please, provide a prompt")
        sys.exit(1)
    
    user_prompt = " ".join(args)

    #Setting up the API and AI:

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    #List of messages:

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    #AI Answer:

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )

    #Check for flags:

    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    #Output:

    print(response.text)




if __name__ == "__main__":
    main()