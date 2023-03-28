def file_handling():
    with open('files.txt', 'w') as new_file:
        new_file.write('This is line one.\nThis is line two.\nThis is the last line.')

    with open('files.txt', 'r') as new_file:
        file_content = new_file.read()
        print(file_content)

    with open('files.txt') as modified_file:
        line_num = 1
        for line in modified_file:
            print("{}. {}".format(line_num, line.rstrip()))
            line_num += 1

    with open('files.txt', 'a+') as append_file:
        append_file.write("\nThis is the new 4th line")


file_handling()

