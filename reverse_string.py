def reverse(input=''):
    length = len(input)
    output = ''
    for step in range(length):
        output += input[-1*(step+1)]
    return output
    pass
