import os
import sqlite3
from django.shortcuts import render
from django.http import HttpResponse
import subprocess
from django.conf import settings


# Create your views here.
def execute_script(request):
    try:
        # Execute the standalone script
        os.system("python rat/chrome.py")

        # Read the results from the file
        with open("result.txt", "r") as file:
            results = file.read()

        return HttpResponse(f"Results: {results}")

    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}")
    

# from django.shortcuts import render
# from django.http import HttpResponse
# import subprocess

# def run_executable(request):
#     try:
#         # Replace 'path/to/your_program.exe' with the actual path to your executable
#         executable_path = 'path/to/your_program.exe'
        
#         # Run the executable using subprocess
#         result = subprocess.run([executable_path], capture_output=True, text=True)
        
#         # Display the result
#         output = result.stdout
#         error = result.stderr

#         return HttpResponse(f"Output: {output}\nError: {error}")

#     except Exception as e:
#         return HttpResponse(f"An error occurred: {str(e)}")


