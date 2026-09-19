with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

# safer with file open(...) and calling file.close() at the end