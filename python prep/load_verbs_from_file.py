def add_suffixes(words, suffixes):
    """ Append each suffix in suffixes to each string in words
    
    Args:
        words (list): A list of str
        suffixes (list): A list of str containing the suffix to append
    
    Returns:
        list: A nested list, each element in the outer list is a list of str containing all words appended with a suffix in suffixes.   
    """
    suffixed_words = []
    for suffix in suffixes:
        single_suffixed_words = []
        for word in words:
            single_suffixed_words.append(word + suffix)
        suffixed_words.append(single_suffixed_words)
        
    return suffixed_words


def load_verbs_from_file(filename):
    verbs = []
    for line in open(filename):
        verb = line.strip()  # strips off the "\n" at the end of each line
        verbs.append(verb)
    return verbs


def test_function():
    words = ["consult", "print", "walk"]
    suffixes = ["ed", "ing"]
    result = add_suffixes(words, suffixes)
    expected_result = [["consulted", "printed", "walked"],
        ["consulting", "printing", "walking"]]
    print(result)
    assert result == expected_result
    
    
def run_program():
    verbs = load_verbs_from_file("verbs1.txt")
    suffixes = ["ing", "ed"]
    suffixed_verbs_list = add_suffixes(verbs, suffixes)
    for suffixed_verbs in suffixed_verbs_list:
        for verb in suffixed_verbs:
            print(verb)

#test_function()
run_program()
