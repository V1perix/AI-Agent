import os


def get_files_info(working_directory, directory=None):
    if directory == None:
        directory = working_directory
    
    target_path = os.path.join(working_directory, directory)
    

    abs_working_directory = os.path.abspath(working_directory)
    abs_target = os.path.abspath(target_path)

    
    if not abs_target.startswith(abs_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(target_path):
        return (f'Error: "{directory}" is not a directory')
    
    try:
        dir_list = os.listdir(abs_target)
    except Exception as e:
        return f"Error: Can't get the content of the directory, please try again\n {e}"
        
    output_array = []
    try:
        for name in dir_list:
            item_path = os.path.join(abs_target, name)
            file_size = 0
            is_dir = ""

            try:
                if os.path.isdir(item_path):
                    is_dir = True
                else:
                    is_dir = False
                
                file_size = os.path.getsize(item_path)
            except Exception as e:
                return f"Error: Can't find the file {name}, please try again\n {e}"
            
            output_array.append(f"- {name}: file_size={file_size} bytes, is_dir={is_dir}")
    except Exception as e:
        return f"Error: Can't list the content of the directory, please try again\n {e}"
    
    return "\n".join(output_array)