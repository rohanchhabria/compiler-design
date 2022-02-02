def identifier(string):
    if (ord(string[0]) >= ord('a') and ord(string[0]) <= ord('z') or ord(string[0]) >= ord('A') and ord(string[0]) <= ord('Z') or ord(string[0]) == ord('_')) == False:
        return False
    
    for i in range(1, len(string)):
        if (ord(string[i]) >= ord('a') and ord(string[i]) <= ord('z') or ord(string[i]) >= ord('A') and ord(string[i]) <= ord('Z') or ord(string[i]) >= ord('0') and ord(string[i]) <= ord('9') or ord(string[i]) == ord('_')) == False:
            return False
    
    return True
    
string = '$_compiler101'

status = identifier(string)
print(f'identifier status: {status}')
