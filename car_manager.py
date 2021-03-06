from turtle import Turtle
from car import Car
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

STARTING_CAR_SPEED = 5
MOVE_INCREMENT = 3

LANE_POSITIONS = [ (300,-100) , ( 300,0) ,  (300 , 100 ) , (300, 200 ) ]

class CarManager(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.create_roadways()
        self.car_positions =  [ ]
        self.cars = [ ]
        self.car_speed = 1
        self.number_of_cars =  len(self.cars)

        
            
        
    def create_cars(self , numb_of_car):
        for _ in range(numb_of_car):
            self.create_car()    


    
    def create_car(self):
        car = Car()
        self.set_car_position(car)
        self.cars.append(car)



    def move_cars(self):
        for car in self.cars:
            car.forward( STARTING_CAR_SPEED + MOVE_INCREMENT * self.car_speed )
    
    

    def refresh_cars(self):
        for car in self.cars:
            car_position = car.position()
            pos_x = car_position[0]
            pos_y = car_position[1]
            if pos_x > 320:
                car.goto(-300 , pos_y)



    def set_car_position(self,car):
        pos_y = random.choice(LANE_POSITIONS)[1]
        pos_x = random.randint(-300 , 300)

        while not( self.is_position_proper(pos_x , pos_y)):
            pos_y = random.choice(LANE_POSITIONS)[1]
            pos_x = random.randint(-300 , 300)

        self.car_positions.append((pos_x , pos_y))

        car.goto( pos_x , pos_y)

     

    def is_position_proper(self , pos_x , pos_y):

        for position in self.car_positions:
            if abs(position[0] - pos_x) <= 100 and pos_y == position[1]:
                return False
        
        return True

    def increase_car_speed(self):
        self.car_speed += 1

    
    def is_there_collision(self , player):
        for car in self.cars:
            if abs(car.xcor() - player.xcor() ) < car.length / 2 and abs( car.ycor() - player.ycor() ) <= 20:
              
                return True

        return False


    def create_roadways(self):

        self.color('black')
        self.setheading(180)
        self.width(2)

        for position in LANE_POSITIONS:
            self.penup()
            self.goto(position)

            index = 0
            # Draw roads
            for length in range(300,-350,-50):
                if index % 2 == 0:
                    self.pendown()

                else:
                    self.penup()

                self.goto(position[0] + length * 2 ,position[1])
                index += 1

        
                

    