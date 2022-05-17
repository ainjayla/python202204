text = 'aias sadas    saia'

print(str(text).replace(' ', '') == text[::-1].replace(' ', ''))

"""
if text == text[::-1]:
    print('tegemist on palindroomiga')
else:
    print('tegemist ei ole palindroomiga')
"""