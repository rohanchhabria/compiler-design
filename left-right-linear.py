def convert(string):
    retsting = ''
    string = string.split('=')
    string[0] = string[0].strip()
    string[1] = string[1].strip()
    
    temp = ''
    for char in string[1]:
        if char.islower():
            temp += char
            string[1] = string[1].replace(char, '')
    retsting = string[1] + ' = ' + string[0] + temp 
    
    return retsting


string = 'B = cD + Ab'
ret = convert(string)
print(f'left linear string: {string}')
print(f'right linear string: {ret}')
