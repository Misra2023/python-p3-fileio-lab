# lib/file_io.py
from pathlib import Path

def write_file(file_name, file_content):
    # Add the .txt extension to the file_name
    file_name = str(file_name) + '.txt'
    
    # Open the file in write mode ('w')
    with open(file_name, 'w') as file:
        # Write the content to the file
        file.write(file_content)

def append_file(file_name, file_content):
    # Add the .txt extension to the file_name
    file_name = str(file_name) + '.txt'
    
    # Open the file in append mode ('a')
    with open(file_name, 'a') as file:
        # Append the content to the file
        file.write(file_content)

def read_file(file_name):
    # Add the .txt extension to the file_name
    file_name = str(file_name) + '.txt'
    
    try:
        # Open the file in read mode ('r')
        with open(file_name, 'r') as file:
            # Read the content of the file
            content = file.read()
            return content
    except FileNotFoundError:
        # Handle the case where the file does not exist
        return "File not found"
