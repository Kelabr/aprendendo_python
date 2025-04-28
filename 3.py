words = ['radar', 'python', 'level', 'world', 'madam']

def palindroma_function(list):
    palindromas = []
    for word in list:
        revert = word[::-1]
        if word == revert:
            palindromas.append(revert)
        
    print(palindromas)

palindroma_function(words)