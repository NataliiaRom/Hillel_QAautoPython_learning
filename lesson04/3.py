def check_file_format(file_list: str | list, extention: str):
    new_list = []
    # YOUR CODE HERE
    for i in file_list:
        if i.endswith(extention):
            new_list.append(i)


    return new_list

#files = ["a.txt", "b.txt", "c.log", "d.html", "e.log", ".diff"]
files = 56
stri = ".txt"

print(check_file_format(files,stri))