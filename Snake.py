from sense_hat import ACTION_RELEASED,SenseHat, ACTION_HELD
import atexit
from random import randint
from time import sleep

#SenseHat instance
sense = SenseHat()

snake = Snake()

food = [1,1]

score = 0

def set_up_variables():
	
	#Set joystick functions
	sense.stick.direction_up = go_up
	sense.stick.direction_down = go_down
	sense.stick.direction_left = go_left
	sense.stick.direction_right = go_right


	atexit.register(exint_handler)


def exint_handler():
	#Clear leds
	sense.clear()

def game_over():
	global score 
	print("Game over, your score = %s" % score)

def move():
	global snake,food,score

	while True:

		head_x = snake.positions[0][0]
		head_y = snake.positions[0][1]

		checker = 0
		last_position = [0,0]

		#If snake direction is Up
		if snake.direction == 1:
			
			#Check if next postion isnt wall or snake tail
			if head_y < 1 or [head_x,head_y - 1] in snake.positions:
				game_over()
				return

			#Move snake in array
			for i in snake.postions:
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
			if food == snake.postions[0]:
				#Snake has eaten food so add new elemnt to snake 
				snake.positions += last_position

				#Random new food
				random_food

		#If snake direction is Right
		if snake.direction == 2:
			
			#Check if next postion isnt wall or snake tail
			if head_x > 6 or [head_x + 1,head_y] in snake.positions:
				game_over()
				return

			#Move snake in array
			for i in snake.postions:
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
			if food == snake.postions[0]:
				#Snake has eaten food so add new elemnt to snake 
				snake.positions += last_position

				#Random new food
				random_food

		#If snake direction is Down
		if snake.direction == 3:
			
			#Check if next postion isnt wall or snake tail
			if head_y > 6 or [head_x,head_y + 1] in snake.positions:
				game_over()
				return

			#Move snake in array
			for i in snake.postions:
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
			if food == snake.postions[0]:
				#Snake has eaten food so add new elemnt to snake 
				snake.positions += last_position

				#Random new food
				random_food

		#If snake direction is Left
		if snake.direction == 4:
			
			#Check if next postion isnt wall or snake tail
			if head_x < 1 or [head_x - 1,head_y] in snake.positions:
				game_over()
				return

			#Move snake in array
			for i in snake.postions:
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
			if food == snake.postions[0]:
				#Snake has eaten food so add new elemnt to snake 
				snake.positions += last_position

				#Random new food
				random_food

		#Set new layout
		layout()

		#Wait 
		sleep(0.5)

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
	move()

def layout():
	global snake,food
	
	#Clear old layout
	sense.clear()

	#incrementation checker
	checker = 0

	#Layout new snake postions 
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

start_game()


# 1.Postaw węża i losuj pierwszą malinkę
# 2.Ruszaj węża co 0.5s
# 3.Sprawdzaj czy nie wleciał w śianę albo nie zjadł malinki albo nie wjevahł w siebie
# 4.1.Jeżeli w ścianę lub w siebie to Game Over
# 4.2.Jeżeli malinka to losuj nową i wydłuż węża
# 5.Jeżeli rusza się dalej to
# 5.1.Sprawdź kierunek i zmień wszystkie wartości w tablicy positions
# 5.2.Wyczyść ekran
# 5.3Rozmieńś nowe pola według tablicy postiions