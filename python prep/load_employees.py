""" List of employees

Author: Josiah Wang
"""

def load_employees(filename):
    """ Load a list of employees from a text file.
    
    Assume that for each line, the file contains the ID, name, age and nationality of the employee, separated by a comma.
    
    Args:
        filename (str) : The path to the database
        
    Returns:
        list : Each element should be a dict with keys "id", "name", "age", and "nationality" of each employee. The value of "age" should be an int, the others str.
    """
    employees = []
    
    with open(filename, encoding = "utf8") as textfile:
        for line in textfile:
            identifier, name, age, nationality = line.strip().split(",")
            age = int(age) # age needs to be an integer
            employees.append({"id": identifier,
                              "name": name,
                              "age": age,
                              "nationality": nationality
                            })
    
    return employees


def filter_employees(employees, attribute_value):
    """ Filter list of employees, given an attribute and value
    
    Args:
        employees (list) : Each element should be a dict with keys "id",
            "name", "age", and "nationality" of each employee. The value 
            of "age" should be an int, the others str.
        attribute_value (tuple) : The (key, value) to match. Only employees
            fitting this criteria value will be retained.
        
    Returns:
        list : A list of employees, filtered by a criteria value.
    """
    filtered_employees = []
    
    (attribute, value) = attribute_value 
    
    for employee in employees:
        if attribute in employee:
            if employee[attribute] == value:
                filtered_employees.append(employee)
        
    return filtered_employees
    
    
def test_load():
    result = load_employees("employees_detail.txt")
    
    assert len(result) == 20
    assert result[0] == {"id": "14835634", "name": "Slađana Ellsworth", 
                         "age": 24, "nationality": "poland"}
    assert result[19] == {"id": "54835190", "name": "Neelima Voll", 
                         "age": 37, "nationality": "portugal"}
    print(result)


def test_filter():
    employees = [{"id": "111", "name": "Joe", "age": 24},
                 {"id": "222", "name": "Luca", "age": 26}, 
                 {"id": "333", "name": "Harry", "age": 24}, 
                 {"id": "444", "name": "William", "age": 23}
                ] 
    
    result = filter_employees(employees, ("age", 24))
    expected = [{"id": "111", "name": "Joe", "age": 24},
                {"id": "333", "name": "Harry", "age": 24}
               ] 
    assert result == expected


def test_pipeline():
    employees = load_employees("employees_detail.txt")
    result = filter_employees(employees, ("nationality", "japan"))
    expected = [
        {'id': '06106396', 'name': 'Monika Moray', 'age': 37, 
         'nationality': 'japan'}, 
        {'id': '87491761', 'name': 'Bernarda Alexander', 'age': 43,
         'nationality': 'japan'}, 
        {'id': '14817102', 'name': 'Agathe Davies', 'age': 39, 
         'nationality': 'japan'}
    ]
    print(result)
    assert result == expected
    
    
test_load()
test_filter()
test_pipeline()
