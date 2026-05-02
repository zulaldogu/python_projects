class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Whoof whoof")

class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.phone_number = contact_number


owner1 = Owner("Danny", "122 Springfield Drive", "888-999")
dog1 = Dog("Bruce", "Scottish Terrier", owner1)
print(dog1.owner.name)

owner2 = Owner("Sally", "122 Springfield Drive", "888-999")
dog2 = Dog("Freya", "Greyhound", owner2)
print(dog2.owner.name)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")

person1 = Person("Alice", 30)
person1.greet()

person2 = Person("Bob", 42)
person2.greet()

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    def say_hi_to_user(self, user):
        print(f"Sending message to {user.username}: Hi {user.username}, it's {self.username}.")

user1 = User("dantheman", "dan@gmail.com", "123")
user2 = User("batman", "bat@outlook.com", "abc")
user1.say_hi_to_user(user2)