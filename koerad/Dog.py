class Dog:

    def bark(self):
        print('woof woof')


class TurkishDog(Dog):

    def bark(self):
        print('hev hev')


class EstonianDog(Dog):

    def bark(self):
        print('auh auh')


def main():
    dogs = [Dog(), TurkishDog(), EstonianDog()]
    for dog in dogs:
        dog.bark()


if __name__ == '__main__':
    main()
