def change_params(old_value: str, new_value: str):
    filetext = """\
    screen_size = 800x600
    paralel_processes = 10
    db_conection = localhost:5432"""
    # YOUR CODE HERE

    if old_value in filetext:
        filetext = filetext.replace(old_value, new_value)

    return filetext


old = "db_conection = localhost:5432"
new = "db_conection = localhost:5432999"

new_text = change_params(old, new)
print(new_text)