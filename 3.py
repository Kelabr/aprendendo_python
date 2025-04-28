# Desafio: Palavras Palíndromas
# Objetivo: Escrever uma função em Python que receba uma lista de palavras e retorne uma nova lista contendo apenas as palavras que são palíndromas.

# Uma palavra é considerada palíndroma se ela for igual à sua inversão. Por exemplo, "radar", "level" e "madam" são palíndromas.

words = ['radar', 'python', 'level', 'world', 'madam']

def palindroma_function(list):
    palindromas = []
    for word in list:
        revert = word[::-1]
        if word == revert:
            palindromas.append(revert)
        
    print(palindromas)

palindroma_function(words)