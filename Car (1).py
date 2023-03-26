
# Online Python - IDE, Editor, Compiler, Interpreter
# Khalil Bonilla, 3/25/2023, Code defining 3 cars and illustrating them going and stopping.
class Car:   # Class defined as Car
    def __init__(self, name):   # Constructor method initializing data
        self.name = name

    def go(self):   # First function of car class
        print("The " +self.name + " is moving.")

    def stop(self):   # Second function of the car class
        print("The " + self.name + " is stoping.")

def main():   # Names defining the car objects and functions allowing them to stop and go printing text.
    car1 = Car("Chevy")
    car1.go()
    car1.stop()
    car2 = Car("Kia")
    car2.go()
    car2.stop()
    car3 = Car("Honda")
    car3.go()
    car3.stop()

if __name__ == "__main__":
  main()