# Abstraction
# Reduce complexity by hiding unnecessary details.

class EmailService:
    def _connect(self):
        print("Connecting to email server..")

    def _authenticate(self):
        print("Authenticating..")

    def send_email(self):
        self._connect()
        self._authenticate()
        print("Sending email..")
        self._disconnect()

    def _disconnect(self):
        print("Disconnecting from email server..")

email = EmailService()
email.send_email()

#Inheritance
#Inheritance is a fundamental concept in OOP that involves creating new classes based on existing classes.

class Vehicle:
    def __init__(self, brand, model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting")

    def stop(self):
        print("Vehicle is stopping")

class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors, number_of_wheels):
        super().__init__(brand,model,year)
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels

class Bike(Vehicle):
    def __init__(self, brand, model, year, number_of_wheels):
        super().__init__(brand,model,year)
        self.number_of_wheels = number_of_wheels

car = Car("Ford", "Focus", 2008, 5, 4)
bike = Bike("Honda", "Scoopy", 2018, 2)
print(car.__dict__)
print(bike.__dict__)
car.start()
bike.start()