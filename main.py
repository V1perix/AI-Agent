import os
import sys
from functions.config import system_prompt
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()

    #args:
    
    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    user_prompt = " ".join(args)

    if not user_prompt:
        print("Please, provide a prompt")
        sys.exit(1)

    #Setting up the API and AI:

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    #List of messages:

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    #AI Answer:
    model_name="gemini-2.0-flash-001"

    schema_get_files_info = types.FunctionDeclaration(
        name="get_files_info",
        description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),
            },
        ),
    )

    # schema_get_file_content = types.FunctionDeclaration(
    #     name="get_file_content",
    #     description="Returns content of a file in a specified directory, up to 1000 bites",
    #     parameters=types.Schema(
    #         type=types.Type.OBJECT,
    #         properties={
    #             "file_path": types.Schema(
    #                 type=types.Type.STRING,
    #                 description="Relative path to a file from which we want to get content"
    #             )
    #         }
    #     )

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            ]
        )

    


    response = client.models.generate_content(
    model=model_name,
    contents=messages,
    config=types.GenerateContentConfig(
    tools=[available_functions], system_instruction=system_prompt))


    #Output:

    #Check for function calls:
    if response.function_calls != None:
        print(f"Calling function: {response.function_calls[0].name}({response.function_calls[0].args})")
    else:
        print(response.text)

    #Check for flags:

    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    




if __name__ == "__main__":
    main()