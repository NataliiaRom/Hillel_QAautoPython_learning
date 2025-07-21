def calculate_sum_from_file(filename):
    # Ваш код тут
    try:
        with open(filename) as file:
            sum_lines = 0
            for line in file:
                try:
                    sum_lines += int(line)
                except ValueError as ve:
                    sum_lines = None
                    print(f"Invalid data in the file")
                    break

            return sum_lines
    except FileNotFoundError as fnf:
        return "File not found"

file = "./data.txt"
# calculate_sum_from_file(file)
print(calculate_sum_from_file(file))