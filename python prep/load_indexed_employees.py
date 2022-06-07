""" Dictionary of employees

Author: Josiah Wang
"""

import pprint # for pretty printing dictionaries

def load_indexed_employees(filename):
    """ Load a dict of employees from a text file.
    
    Assume that for each line, the file contains the ID, name, age and nationality of the employee, separated by a comma.
    
    Args:
        filename (str) : The path to the database
        
    Returns:
        dict : keys should be the employee id, value is a dict representation of the employee (keys: "id", "name", "age", and "nationality")
    """
    employee_dict = {}
    
    with open(filename, encoding = "utf8") as textfile:
        for line in textfile:
            identifier, name, age, nationality = line.strip().split(",")
            age = int(age) # age needs to be an integer
            employee_dict[identifier] = {"id": identifier,
                                         "name": name,
                                         "age": age,
                                         "nationality": nationality
                                        }
    
    return employee_dict


def index_employees_by_attribute(employee_dict, attribute_name):
    """ Index employees by a certain attribute.
    
    Args:
        employee_dict (dict) : keys should be the employee id, value is a dict representation of the employee (keys: "id", "name", "age", and "nationality")
        attribute_name (str) : The attribute you want to index
        
    Returns:
        dict : The keys are all possible attribute values, each value is a list of employee id (`str`).
    """

    attribute_dict = {}

    for (employee_id, employee) in employee_dict.items():
        attribute_value = employee[attribute_name]
        
        attribute_dict.setdefault(attribute_value, []).append(employee_id)
        
        ## a more readable version of the above line
        #if attribute_value not in attribute_dict:
        #    attribute_dict[attribute_value] = []
        #attribute_dict.append(employee_id)
            
    return attribute_dict
    
    
def test_load():
    result = load_indexed_employees("employees_detail.txt")
    
    assert len(result) == 20
    assert result["14835634"] == {"id": "14835634", "name": "Slađana Ellsworth", 
                                  "age": 24, "nationality": "poland"}
    assert result["54835190"] == {"id": "54835190", "name": "Neelima Voll", 
                                  "age": 37, "nationality": "portugal"}
    pprint.pp(result)


def test_indexing():
    employees = {"111": {"id": "111", "name": "Joe", "nationality": "uk"},
                 "222": {"id": "222", "name": "Luca", 
                         "nationality": "italy"}, 
                 "333": {"id": "333", "name": "Harry", 
                         "nationality": "uk"}, 
                 "444": {"id": "444", "name": "William", 
                         "nationality": "scotland"}
                } 
    
    result = index_employees_by_attribute(employees, "nationality")
    expected = {"uk": ["111", "333"],
                "italy": ["222"],
                "scotland": ["444"]
               }
                
    assert result == expected


def test_pipeline():
    employee_dict = load_indexed_employees("employees_detail.txt")
    result = index_employees_by_attribute(employee_dict, "nationality")
    pprint.pp(result)
    expected = {
        'poland': ['14835634'],
        'brazil': ['69983058'],
        'russia': ['69448225'],
        'india': ['83512249', '51904155', '55327620'],
        'sweden': ['28836869'],
        'portugal': ['82660090', '54835190'],
        'usa': ['61098940', '15304638'],
        'italy': ['50196408', '37935295', '84819522'],
        'switzerland': ['14973705'],
        'iran': ['25872463'],
        'japan': ['06106396', '87491761', '14817102'],
        'singapore': ['30195178']
    }
    assert result == expected
    
    
test_load()
test_indexing()
test_pipeline()
