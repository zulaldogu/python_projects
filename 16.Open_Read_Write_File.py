with open("C:/Users/zulal/OneDrive/Masaüstü/my_file.txt") as file: # dont need to close the file
    contents = file.read()
    print(contents)
    # file.close()

# with open("my_file.txt", mode = "a") as file: # w is for write, a is for append
#    file.write("\nNew text.")