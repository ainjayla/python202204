def p(s):
    print(s)
    if len(s) > 0:
        p(s[:len(s) - 1])

p('#####ksjerhgwerhgbweh###')

"""
print('######')
print('#####')
print('####')
print('###')
print('##')
print('#')
"""