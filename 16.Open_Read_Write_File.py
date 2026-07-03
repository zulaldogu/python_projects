with open("my_file.txt") as file: # dont need to close the file
    contents = file.read()
    print(contents)
    # file.close()