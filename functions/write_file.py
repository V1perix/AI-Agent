import os

def write_file(working_directory, file_path, content):
    target_path = os.path.join(working_directory, file_path)

    abs_file = os.path.abspath(target_path)
    abs_working_directory = os.path.abspath(working_directory)
    

    if not abs_file.startswith(abs_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    

    dir_path = os.path.dirname(abs_file)

    if not os.path.exists(abs_file):
        try:
            os.makedirs(dir_path, exist_ok=True)
        except Exception as e:
            return f"Error: Failed to create a directory path {dir_path}\n{e}"
    
    try:
        with open(abs_file, "w") as file:
            file.write(content)
    
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: Failed to write to file {abs_file}\n{e}"

    
    #Need to create a file via the dir_path path
    #Need to overwrite its content with content from func argument
    #Need to return the string from the website (not the file itself, or it's content)