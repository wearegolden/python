def is_isogram(string):
    string = string.upper()
    for index in range(26):
        if string.count(chr(index+65)) > 1: 
            return False
    return True
    pass
