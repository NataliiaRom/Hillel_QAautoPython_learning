import pytest
from lesson16.homework16_1 import *


def test_mro_order():
    expected_mro = (TeamLead, Manager, Developer, Employee, object)
    assert TeamLead.__mro__ == expected_mro, "MRO order is wrong"


@pytest.mark.parametrize("team_size,name,salary,department,programming_language",
                         [(30, "Kelly", 30000, "IT", "Python")])
def test_teamlead_instance_all_positional_attr_present(team_size, name, salary, department, programming_language):
    with pytest.raises(TypeError, match="required positional argument"):
        tl = TeamLead(team_size=team_size,
                      name=name,
                      salary=salary,
                      department=department)


def test_teamlead_instance_wrong_attr_handling():
    with pytest.raises(TypeError, match="unexpected keyword argument"):
        tl = TeamLead(10,
                      name11111="Teddy",
                      salary=10000,
                      department="IT",
                      programming_language="Ruby")


tl = TeamLead(10,
              name="Teddy",
              salary=10000,
              department="IT",
              programming_language="Ruby")


@pytest.mark.parametrize('attribute', [
    "man", "dev", "emp"
])
def test_teamlead_attr_inheritance(attribute):
    assert hasattr(tl, attribute), f"Missing attribute: {attribute}"


def test_teamlead_method_inheritance():
    assert tl.say_smth() == "I am TeamLead. My colleagues say: 'I am Employee.','I a Manager.', 'I am Developer.'", \
        "Smth went wrong with the methods inheritance."
