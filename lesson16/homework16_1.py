class Employee:
    title = "Employee"
    emp = 9

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def say_smth(self):
        return "I am Employee."


class Manager(Employee):
    title = "Manager"
    man = 5

    def __init__(self, department, **kwargs):
        super().__init__(**kwargs)
        self.department = department

    def say_smth(self):
        return "I a Manager."


class Developer(Employee):
    title = "Developer"
    dev = 6

    def __init__(self, programming_language, **kwargs):
        super().__init__(**kwargs)
        self.programming_language = programming_language

    def say_smth(self):
        return "I am Developer."


class TeamLead(Manager, Developer):
    title = "TeamLead"

    def __init__(self, team_size, **kwargs):
        super().__init__(**kwargs)
        self.team_size = team_size

    def say_smth(self):
        return (f"I am TeamLead. My colleagues say: "
                f"'{Employee.say_smth(self)}',"
                f"'{Manager.say_smth(self)}', "
                f"'{Developer.say_smth(self)}'")

    def __str__(self):
        return (f"Teamlead {self.name} works in {self.department} department, earns {self.salary} per month, "
        f"knows {self.programming_language}, is a lead for {self.team_size} people")


tl = TeamLead(80, name="Bobby", salary=8000, department="IT", programming_language="Python")
print(tl)
print(tl.say_smth())
print(TeamLead.mro())
