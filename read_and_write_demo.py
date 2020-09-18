file_name = "data.txt"

with open(file_name) as f:
    for line in f:
        print(line.strip())

# I then looked at how to append a new line to the file:
record_to_add = "jane,doe:c,ruby,javascript"
with open(file_name, "a+") as to_write:
    to_write.write(record_to_add+"\n")