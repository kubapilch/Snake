from sense_hat import ACTION_RELEASED,SenseHat, ACTION_HELD
import atexit
from random import randint
from time import sleep
from SnakeModel import Snake
import threading
from signal import pause

#SenseHat instance
sense = SenseHat()

snake = Snake()

food = [1,1]

score = 0

t = None


def set_up_variables():
    global t,sense

    #Set joystick functions
    sense.stick.direction_up = go_up
    sense.stick.direction_down = go_down
    sense.stick.direction_left = go_left
    sense.stick.direction_right = go_right

    t = threading.Timer(1.0,move)
    t.daemon = True

    atexit.register(exint_handler)


def exint_handler():
    #Clear leds
    sense.clear()

def game_over():
    global score 
    print("Game over, your score = %s" % score)

def move():
        global snake,food,score,t

        head_x = snake.positions[0][0]
        head_y = snake.positions[0][1]

        checker = 0
        last_position = [0,0]

        #If snake direction is Up
        if snake.direction == 1:
            
            #Check if next postion isnt wall or snake tail
            if head_y < 1 or [head_x,head_y - 1] in snake.positions:
                game_over()
                t.cancel()
                return

            #Move snake in array
            for i in snake.positions:
                #If its head
                if checker == 0:
                    last_position = i

                    snake.positions[checker] = [head_x,head_y - 1]

                    checker += 1

                    continue

                #It is not head
                new_position = last_position

                last_position = i

                snake.positions[checker] = new_position

                checker += 1

            #Check if snake ate food
            if food == snake.positions[0]:
                #Snake has eaten food so add new elemnt to snake 
                snake.positions += last_position

                score += 1

                #Random new food
                random_food

        #If snake direction is Right
        if snake.direction == 2:
            
            #Check if next postion         
            if head_x > 6 or [head_x + 1,head_y] in snake.positions:
                game_over()
                t.cancel()
                return

            #Move snake in array
            for i in snake.positions:
                #If its head
                if checker == 0:
                    last_position = i

                    snake.positions[checker] = [head_x + 1,head_y]

                    checker += 1

                    continue

                #It is not head
                new_position = last_position

                last_position = i

                snake.positions[checker] = new_position

                checker += 1

            #Check if snake ate food
            if food == snake.positions[0]:
                #Snake has eaten food so add new elemnt to snake 
                snake.positions += last_position

                score += 1

                #Random new food
                random_food

        #If snake direction is Down
        if snake.direction == 3:
            
            #Check if next postion isnt wall or snake tail
            if head_y > 6 or [head_x,head_y + 1] in snake.positions:
                game_over()
                t.cancel()
                return

            #Move snake in array
            for i in snake.positions:
                #If its head
                if checker == 0:
                    last_position = i

                    snake.positions[checker] = [head_x,head_y + 1]

                    checker += 1

                    continue

                #It is not head
                new_position = last_position

                last_position = i

                snake.positions[checker] = new_position

                checker += 1

            #Check if snake ate food
            if food == snake.positions[0]:
                #Snake has eaten food so add new elemnt to snake 
                snake.positions += last_position

                score += 1

                #Random new food
                random_food

        #If snake direction is Left
        if snake.direction == 4:
            
            #Check if next postion isnt wall or snake tail
            if head_x < 1 or [head_x - 1,head_y] in snake.positions:
                game_over()
                t.cancel()
                return

            #Move snake in array
            for i in snake.positions:
                #If its head
                if checker == 0:
                    last_position = i

                    snake.positions[checker] = [head_x - 1,head_y]

                    checker += 1

                    continue

                #It is not head
                new_position = last_position

                last_position = i

                snake.positions[checker] = new_position

                checker += 1

            #Check if snake ate food
            if food == snake.positions[0]:
                #Snake has eaten food so add new elemnt to snake 
                snake.positions += last_position

                score += 1

                #Random new food
                random_food

        #Set new layout
        layout()

        t.start()

def random_food():
    global snake,food

    #Random food position 
    while food in snake.positions:
        x = randint(0,7)
        y = randint(0,7)

        food = [x,y]

def start_game():

    #random first food
    random_food()

    #Set up first layout
    layout()

    #Start the game
    #move()
    t.start()

def layout():
    global snake,food
    
    #Clear old layout
    sense.clear()

    #incrementation checker
    checker = 0

    #Layout new snake positions
    for i in snake.positions:
        #X pos
        x = i[0]

        #Y pos
        y = i[1]

        #Led color
        color = snake.color

        if checker == 0:
            color = snake.head_color

        sense.set_pixel(x,y,color)

        checker += 1

    #Layout food
    sense.set_pixel(food[0],food[1],255,0,0)

def go_up(event):
    global snake
    
    if event.action == ACTION_RELEASED or event.action == ACTION_HELD:
        return

    #Chenge direction to Up
    snake.direction = 1

def go_right(event):
    global snake
    
    if event.action == ACTION_RELEASED or event.action == ACTION_HELD:
        return

    #Change direction to Right
    snake.direction = 2

def go_down(event):
    global snake
    
    if event.action == ACTION_RELEASED or event.action == ACTION_HELD:
        return

    #Change direction to Down
    snake.direction = 3

def go_left(event):
    global snake
    
    if event.action == ACTION_RELEASED or event.action == ACTION_HELD:
        return

    #Change direction to Left
    snake.direction = 4

set_up_variables()
start_game()

pause()

