import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    target_path = os.path.join(working_directory, file_path)

    abs_file = os.path.abspath(target_path)
    abs_working_directory = os.path.abspath(working_directory)
    

    if not abs_file.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_file):
        f'Error: File not found or is not a regular file: "{file_path}"'

    content = ""
    try:
        with open(abs_file, 'r') as file:
            content = file.read(MAX_CHARS)

            if os.path.getsize(abs_file) > MAX_CHARS:
                content += f'[...File "{file_path}" truncated at 10000 characters]'
    
        return content
    
    except Exception as e:
        return f"Error: Can't access a file, please try again\n{e}"