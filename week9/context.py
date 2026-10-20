def analyze_log(filename):
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if "ERROR" in line:
                print(line)
            if "WARNING" in line:
                print(line)


analyze_log("sample.log")

# Mode	Purpose
# "r"	Read an existing file
# "w"	Write to a file, replacing existing contents
# "a"	Append to a file
# "x"	Create a new file; fail if it already exists