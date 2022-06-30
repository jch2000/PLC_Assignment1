from FileSeparator import separate_file

# Input file goes in parenthesis here here
with open(r"C:\Users\justi\Documents\TestFile.txt", "r") as input_file:
        file_content = input_file.read()

separate_file(file_content)