from keyword import iskeyword

def check(string):
    reserved = []
    keys = [word for word in string.split()]
    
    for i in range(len(keys)):
        if iskeyword(keys[i]):
            reserved.append(keys[i])
            print(keys[i] + ' is a reserved keyword')
        else:
            print(keys[i] + ' is not a reserved keyword')
    print()
        
    return reserved

string = 'for rohan try something else return lambda x'

result = check(string)
print(f'`reserved keywords` from string: {" ".join(result)}')