from Person import *

persons = [Person('37212210230'), Person('47212210231')]

for person in persons:
    print(person.getBirthYear(), person.getBirthMonth(),
          person.getBirthDay(), person.getGender())
