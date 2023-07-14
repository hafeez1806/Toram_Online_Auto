from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con



def random_time(low,high):
	time = np.random.uniform(low,high)
	return time

def random_pixel_in_button(x,y):
	n1 = np.random.uniform(0,5)
	n2 = np.random.uniform(0,5)
	x = x + n1
	y = y + n2
	return x,y


def m_click(x,y):
	pyautogui.moveTo(x,y,duration = random_time(0.4,0.7))
	pyautogui.mouseDown()
	time.sleep(random_time(0.2,0.5))
	pyautogui.mouseUp() 

	# win32api.SetCursorPos((x,y))
	# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	# time.sleep(random_time(0.3,0.9))

def key_click(value_k):
	if isinstance(value_k,int):
		value_k = str(value_k)
	pyautogui.keyDown(value_k)
	time.sleep(random_time(0.2,0.5))
	pyautogui.keyUp(value_k)
	time.sleep(random_time(0.3,0.7))

def look_mouse_position_color():
	pyautogui.displayMousePosition()

def find_image_and_random_click(img_path,fun_name):
	box = pyautogui.locateOnScreen(img_path, grayscale=True, confidence=0.7)
	if box != None:
		print("image found")
		pyautogui.moveTo(randomClick(box),duration = random_time(0.4,0.7))
		pyautogui.mouseDown()
		time.sleep(random_time(0.2,0.5))
		pyautogui.mouseUp() 
		# pyautogui.leftClick()
	else:
		print("image not found")
		if fun_name == "libra":
			quit()
			libra_manual_click()

		elif fun_name == "tenert":
			quit()
			tenert_manual_click()

		elif fun_name == "virgo":
			quit()
			virgo_manual_click()

		elif fun_name == "flame":
			quit()
			flame_manual_click()

		elif fun_name == "frozen":
			quit()
			frozen_manual_click()

		elif fun_name == "rock":
			quit()
			rock_manual_click()

		elif fun_name == "pre_battle":
			pre_battle()
		else:
			battle_strategy()
			end_battle()



	# 	print("Retrying in 1-3 seconds")
	# 	key_click('f')
	# 	time.sleep(random_time(1,3))
	# 	find_image_and_random_click(img_path)


def find_image(img_path):
	box = pyautogui.locateOnScreen(img_path, grayscale=True, confidence=0.7)
	if box != None:
		return True
	else:
		return False


def move_to_portal():
	pyautogui.keyDown('w','d')
	time.sleep(random_time(0.9,12))
	pyautogui.keyUp('d')
	time.sleep(random_time(0.5,0.9))
	pyautogui.keyUp('w')

def back_to_origine():
	pyautogui.keyDown('s','a')
	time.sleep(random_time(0.9,12))
	pyautogui.keyUp('a')
	time.sleep(random_time(0.5,0.9))
	pyautogui.keyUp('s')

def randomClick(box):
	x_click = int(random.uniform(box.left + get_five_percent(box.left), box.left + box.width - get_five_percent(box.width)))
	y_click = int(random.uniform(box.top + get_five_percent(box.left), box.top+box.height - get_five_percent(box.width)))
	#print(f"box_left:{box.left},box_top:{box.top},width:{box.width}, height:{box.width} ")
	return (x_click, y_click)

def battle_strategy():
	libra_manual_click()
	time.sleep(random_time(1,3))
	tenert_manual_click()
	time.sleep(random_time(1,3))
	virgo_manual_click()
	time.sleep(random_time(1,3))
	flame_manual_click()
	time.sleep(random_time(1,3))
	frozen_manual_click()
	time.sleep(random_time(1,3))
	rock_manual_click()
	time.sleep(random_time(1,3))
	start_battle()
	time.sleep(random_time(1,3))


def get_five_percent(o_data):
	percent = int((o_data/100)*5)
	return percent

def libra_manual_click():
	print("libra")
	key_click('tab')
	time.sleep(random_time(0.5,1))
	x = int(random.uniform(1380,1580))
	y = int(random.uniform(370,405))
	m_click(x,y)
	time.sleep(random_time(1,3))
	key_click('f')
	time.sleep(random_time(3,5))
	key_click('f')
	time.sleep(random_time(0.2,0.5))
	next_loc = 'F:\\Games\\python\\images\\Hanami\\next_loc.PNG'
	find_image_and_random_click(next_loc,"libra")
	time.sleep(random_time(2,5))
	key_click('f')
	time.sleep(random_time(0.2,0.5))
	next_loc = 'F:\\Games\\python\\images\\Hanami\\next_loc.PNG'
	find_image_and_random_click(next_loc,"libra")
	time.sleep(random_time(2,5))
	key_click('f')
	time.sleep(random_time(0.2,0.5))
	yes = 'F:\\Games\\python\\images\\Hanami\\yes.PNG'
	find_image_and_random_click(yes,"libra")
	time.sleep(random_time(5,7))

def tenert_manual_click():
	print("tenert")
	key_click('tab')
	time.sleep(random_time(0.5,1))
	x = int(random.uniform(1380,1580))
	y = int(random.uniform(305,345))
	m_click(x,y)
	key_click('f')
	time.sleep(random_time(3,5))
	key_click('f')
	time.sleep(random_time(0.2,0.5))
	prev_loc = 'F:\\Games\\python\\images\\Hanami\\prev_loc.PNG'
	find_image_and_random_click(prev_loc,"tenert")
	time.sleep(random_time(2,5))
	key_click('f')
	time.sleep(random_time(0.2,0.5))
	prev_loc = 'F:\\Games\\python\\images\\Hanami\\prev_loc.PNG'
	find_image_and_random_click(prev_loc,"tenert")
	time.sleep(random_time(2,5))
	key_click('f')
	time.sleep(random_time(0.2,0.5))
	yes = 'F:\\Games\\python\\images\\Hanami\\yes.PNG'
	find_image_and_random_click(yes,"tenert")
	time.sleep(random_time(5,7))

def virgo_manual_click():
	print("virgo")
	key_click('tab')
	time.sleep(random_time(0.5,1))
	x = int(random.uniform(1380,1580))
	y = int(random.uniform(430,470))
	m_click(x,y)
	key_click('f')
	time.sleep(random_time(3,5))
	key_click('f')
	time.sleep(random_time(0.2,0.5))
	prev_loc = 'F:\\Games\\python\\images\\Hanami\\prev_loc.PNG'
	find_image_and_random_click(prev_loc,"virgo")
	time.sleep(random_time(2,5))
	key_click('f')
	time.sleep(random_time(0.2,0.5))
	prev_loc = 'F:\\Games\\python\\images\\Hanami\\prev_loc.PNG'
	find_image_and_random_click(prev_loc,"virgo")
	time.sleep(random_time(2,5))
	key_click('f')
	time.sleep(random_time(0.2,0.5))
	yes = 'F:\\Games\\python\\images\\Hanami\\yes.PNG'
	find_image_and_random_click(yes,"virgo")
	time.sleep(random_time(5,7))


def flame_manual_click():
	print("flame")
	key_click('tab')
	time.sleep(random_time(0.5,1))
	x = int(random.uniform(1380,1580))
	y = int(random.uniform(560,600))
	m_click(x,y)
	key_click('f')
	time.sleep(random_time(4,6))
	key_click('f')
	time.sleep(random_time(0.2,0.5))
	prev_loc = 'F:\\Games\\python\\images\\Hanami\\prev_loc.PNG'
	find_image_and_random_click(prev_loc,"flame")
	time.sleep(random_time(2,5))
	key_click('f')
	time.sleep(random_time(0.2,0.5))
	prev_loc = 'F:\\Games\\python\\images\\Hanami\\prev_loc.PNG'
	find_image_and_random_click(prev_loc,"flame")
	time.sleep(random_time(2,5))
	key_click('f')
	time.sleep(random_time(0.2,0.5))
	prev_loc = 'F:\\Games\\python\\images\\Hanami\\prev_loc.PNG'
	find_image_and_random_click(prev_loc,"flame")
	time.sleep(random_time(2,5))
	key_click('f')
	time.sleep(random_time(0.2,0.5))
	prev_loc = 'F:\\Games\\python\\images\\Hanami\\prev_loc.PNG'
	find_image_and_random_click(prev_loc,"flame")
	time.sleep(random_time(2,5))
	key_click('f')
	time.sleep(random_time(0.2,0.5))
	prev_loc = 'F:\\Games\\python\\images\\Hanami\\prev_loc.PNG'
	find_image_and_random_click(prev_loc,"flame")
	time.sleep(random_time(2,5))
	key_click('f')
	time.sleep(random_time(0.2,0.5))
	yes = 'F:\\Games\\python\\images\\Hanami\\yes.PNG'
	find_image_and_random_click(yes,"flame")
	time.sleep(random_time(5,7))



def frozen_manual_click():
	print("frozen")
	key_click('tab')
	time.sleep(random_time(0.5,1))
	x = int(random.uniform(1380,1580))
	y = int(random.uniform(625,670))
	m_click(x,y)
	key_click('f')
	time.sleep(random_time(4,6))
	key_click('f')
	time.sleep(random_time(0.2,0.5))
	prev_loc = 'F:\\Games\\python\\images\\Hanami\\prev_loc.PNG'
	find_image_and_random_click(prev_loc,"frozen")
	time.sleep(random_time(2,5))
	key_click('f')
	time.sleep(random_time(0.2,0.5))
	prev_loc = 'F:\\Games\\python\\images\\Hanami\\prev_loc.PNG'
	find_image_and_random_click(prev_loc,"frozen")
	time.sleep(random_time(2,5))
	key_click('f')
	# time.sleep(random_time(0.2,0.5))
	# prev_loc = 'F:\\Games\\python\\images\\Hanami\\prev_loc.PNG'
	# find_image_and_random_click(prev_loc)
	# time.sleep(random_time(2,5))
	# key_click('f')
	time.sleep(random_time(0.2,0.5))
	yes = 'F:\\Games\\python\\images\\Hanami\\yes.PNG'
	find_image_and_random_click(yes,"frozen")
	time.sleep(random_time(5,7))

def rock_manual_click():
	print("rock")
	key_click('tab')
	time.sleep(random_time(0.5,1))
	x = int(random.uniform(1380,1580))
	y = int(random.uniform(685,730))
	m_click(x,y)
	key_click('f')
	time.sleep(random_time(4,6))
	key_click('f')
	time.sleep(random_time(0.2,0.5))
	next_loc = 'F:\\Games\\python\\images\\Hanami\\next_loc.PNG'
	find_image_and_random_click(next_loc,"rock")
	time.sleep(random_time(2,5))
	key_click('f')
	time.sleep(random_time(0.2,0.5))
	next_loc = 'F:\\Games\\python\\images\\Hanami\\next_loc.PNG'
	find_image_and_random_click(next_loc,"rock")
	time.sleep(random_time(2,5))
	key_click('f')
	time.sleep(random_time(0.2,0.5))
	next_loc = 'F:\\Games\\python\\images\\Hanami\\next_loc.PNG'
	find_image_and_random_click(next_loc,"rock")
	time.sleep(random_time(2,5))
	key_click('f')
	time.sleep(random_time(0.2,0.5))
	yes = 'F:\\Games\\python\\images\\Hanami\\yes.PNG'
	find_image_and_random_click(yes,"rock")
	time.sleep(random_time(5,7))

def start_battle():
	key_click('tab')
	time.sleep(random_time(0.5,1))
	x = int(random.uniform(1380,1580))
	y = int(random.uniform(495,540))
	m_click(x,y)
	time.sleep(random_time(0.5,1))
	key_click('f')
	time.sleep(random_time(3,5))
	start_battle = 'F:\\Games\\python\\images\\Hanami\\start_bt.PNG'
	find_image_and_random_click(start_battle,"start_battle")

def pre_battle():
	key_click('tab')
	time.sleep(random_time(0.5,1))
	x = int(random.uniform(1380,1580))
	y = int(random.uniform(325,355))
	m_click(x,y)
	key_click('f')
	time.sleep(random_time(3,5))
	enter_battle = 'F:\\Games\\python\\images\\Hanami\\enter_battle.PNG'
	find_image_and_random_click(enter_battle,"pre_battle")
	time.sleep(random_time(10,13))

def end_battle():
	print("sleeping 320-330 seconds")
	time.sleep(random_time(320,330))
	quest_reward = 'F:\\Games\\python\\images\\Hanami\\quest_reward.PNG'
	rr = find_image(quest_reward)
	if rr == True:
		x = int(random.uniform(670,1170))
		y = int(random.uniform(900,970))
		m_click(x,y)
		time.sleep(random_time(5,7))
	else:
		start_battle()
		end_battle()


def quit():
	key_click('esc')
	time.sleep(random_time(0.5,1))
	quit = 'F:\\Games\\python\\images\\Hanami\\quite.PNG'
	find_image_and_random_click(quit,"quit")
	time.sleep(random_time(2,3))





time.sleep(random_time(10,12))
while keyboard.is_pressed('q') == False:
	pre_battle()
	battle_strategy()
	end_battle()




# key_click('tab')
# libera = 'F:\\Games\\python\\images\\Hanami\\Libra_test.PNG'
# find_image_and_random_click(libera)
# key_click('f')

# look_mouse_position_color()