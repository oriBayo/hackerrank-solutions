line = input()
while line != "END":
    count = 1
    string = line
    number = int(string)
    len_string = len(string)
    while number != len_string:
        count += 1
        string = str(len_string)
        number = int(string)
        len_string = len(string)
    print(count)
    line = input()
