def capitalize_words(string):
    up_string = ''
    for s in string.split():
        up_string += s[0].upper() + (s[1:] + ' ')
    
    return up_string

result = capitalize_words("hello, world!")
print(result)
