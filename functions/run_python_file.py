import os
import subprocess


def run_python_file(working_directory, file_path):
    target_path = os.path.join(working_directory, file_path)

    abs_file = os.path.abspath(target_path)
    abs_working_directory = os.path.abspath(working_directory)
    

    if not abs_file.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_file):
        return f'Error: File "{file_path}" not found.'
    
    if not os.path.isfile(abs_file):
        return f"Error: {file_path} is not a file"

    name, extension = os.path.splitext(abs_file)

    if extension != ".py":
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result = subprocess.run(["python3", abs_file], capture_output = True, timeout = 30, cwd = abs_working_directory)

        output_str = ""
        out_decoded = result.stdout.decode()
        err_decoded = result.stderr.decode()

        if out_decoded != "":
            output_str += f"STDOUT:{out_decoded.rstrip()}"

        if err_decoded != "":
            if output_str != "":
                output_str += "\n"
            output_str += f"STDERR:{err_decoded.rstrip()}"

        if out_decoded == "" and err_decoded == "":
            output_str += f"No output produced."

        if result.returncode != 0:
            output_str += f"\nProcess exited with code {result.returncode}"
        
        return output_str

    except Exception as e:
        return f"Error: executing Python file: {e}"