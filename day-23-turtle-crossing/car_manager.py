import turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(turtle.Turtle):
    
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = turtle.Turtle("tyrone")
            new_car.penup()
            new_car.goto(300, randint(-250, 250))
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.speed)

    def level_up(self):
        self.speed += MOVE_INCREMENT

    def reset(self):
        for car in self.cars:
            car.goto(300, randint(-250, 250))
        self.speed = STARTING_MOVE_DISTANCE

    def check_collision(self, player):
        for car in self.cars:
            if car.distance(player) < 20:
                return True
        return False
    
    def clear(self):
        for car in self.cars:
            car.hideturtle()
        self.cars.clear()

    
