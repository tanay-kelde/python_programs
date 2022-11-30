# Using splitext() method from os module #
import os
file_details = os.path.splitext('/path/file.ext')
print(file_details)
print(file_details[1])

# Using pathlib module # 
import pathlib
print(pathlib.Path('/path/file.ext').suffix)