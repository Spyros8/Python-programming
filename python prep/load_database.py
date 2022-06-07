""" Employee database

Author: Josiah Wang
"""

def load_database(filename):
    """ Load a database from a text file.
    
    Assume that for each line, the file contains the ID and the name of the
    employee, separated by a comma.
    
    Args:
        filename (str) : The path to the database
        
    Returns:
        dict : The dictionary should have the employee ID as its key 
                (should be a str), and the employee name as its value
    """
    employee_dict = {}
    
    for line in open(filename, encoding="utf8"):
        (identifier, name) = line.strip().split(",")
        employee_dict[identifier] = name
    
    return employee_dict


def query_employees(employee_dict={}, ids=[]):
    """ Retrieve employee names from a database, given a list of IDs.
    
    Args:
        employee_dict (dict) : A dictionary with employee ID as its key 
            (a str), and the employee name as its value
        ids (list) : A list of employee IDs to query
        
    Returns:
        list : The names of the employees retrieved from queries. 
               The name will be None is an employee ID is not found.
    """
    names = []
    
    for identifier in ids:
        names.append(employee_dict.get(identifier, None))
        
    return names
    

def test_load():
    result = load_database("employees.txt")
    print(result)
    
    assert len(result) == 20
    assert result["14835634"] == "Slađana Ellsworth"
    assert result["37935295"] == "Gwallter Choungxaim"
    
    
    
def test_query():
    employee_dict = {
                     "14835634": "Slađana Ellsworth",
                     "25872463": "Rosa Burgess",
                     "28836869": "Fàtima Gulyás",
                     "37935295": "Gwallter Choungxaim",
                     "54835190": "Neelima Voll"
                    }
    
    result = query_employees(employee_dict, ["25872463", "54835190", "28836869"])
    expected = ["Rosa Burgess", "Neelima Voll", "Fàtima Gulyás"]
    print(result)
    assert result == expected


def test_unknown_query():
    employee_dict = {
                     "14835634": "Slađana Ellsworth",
                     "25872463": "Rosa Burgess",
                     "28836869": "Fàtima Gulyás",
                     "37935295": "Gwallter Choungxaim",
                     "54835190": "Neelima Voll"
                    }
    
    result = query_employees(employee_dict, ["25872463", "1234567", "28836869"])
    expected = ["Rosa Burgess", None, "Fàtima Gulyás"]
    print(result)
    assert result == expected


    
    
test_load()
test_query()
test_unknown_query()
