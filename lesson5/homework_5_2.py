# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record to the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]
def print_list():
    for tup in people_records:
        print(tup)


print('Task 1\n' + "#"*8+ '\n')

new_record = ('Nataliia','Romaniuk',36, 'QA Automation Engineer', 'Kyiv')
people_records.insert(0,new_record)
print_list()
##############################
print('Task 2\n' + "#"*8+ '\n')

people_records[1], people_records[5] = people_records[5], people_records[1]
print_list()
###############################

print('Task 3\n' + "#"*8+ '\n')

def check_age(record_number):
    control_age = 30
    persons_age = people_records[record_number][2]
    persons_name = people_records[record_number][0]
    if persons_age > control_age:
        print(f'{persons_name} is over 30. This person is {persons_age} years old.')
    else:
        print(f'{persons_name} is under 30. This person is {persons_age} years old.')


records_list = [6, 10, 13]
for index in records_list:
    check_age(index)



