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
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(random_time(0.3,0.9))

def key_click(value_k):
	if isinstance(value_k,int):
		value_k = str(value_k)
	pyautogui.keyDown(value_k)
	time.sleep(random_time(0.2,0.5))
	pyautogui.keyUp(value_k)
	time.sleep(random_time(0.3,0.7))

def look_mouse_position_color():
	pyautogui.displayMousePosition()


def check_color_at(x,y,color_code,rgb_v):
	if pyautogui.pixel(x,y)[rgb_v] == color_code:
		return True
	else:
		return False

def find_image_at(img_path):
	if pyautogui.locateOnScreen(img_path, grayscale=True, confidence=0.6) != None:
		print("image match true")
		return True
	else:
		print("image match False")
		return False


def blizzard(total_mp,mp_charge_time):
	key_click(7)
	time.sleep(random_time(0.2,0.5))
	key_click(7)
	total_mp = total_mp-1
	if total_mp < random.randint(2, 6):
		total_mp = mp_charge(total_mp,mp_charge_time)
		time.sleep(random_time(5,11))
	else:
		time.sleep(random_time(11,16))
	return total_mp

def mp_charge(total_mp,mp_charge_time):
	key_click(1)
	time.sleep(random_time(0.5,0.9)+mp_charge_time)
	key_click(2)
	total_mp = total_mp+15
	return total_mp


def main_loop(total_mp,mp_charge_time):
	print("main loop called")
	print(f"total_mp is {total_mp}")
	flag = 0
	print(f"flag set to {flag}")
	flag_reset = 0
	print(f"flag_reset set to {flag_reset}")
	while keyboard.is_pressed('q') == False:
		flag = flag + 1
		print(f"flag value {flag}")
		if flag_reset == 0:
			flag_reset = random.randint(5, 89)
			print(f"flag_reset set to {flag_reset}")
		if flag_reset == flag:
			print(f"flag_reset matched to flag")
			flag_reset = random.randint(5, 59)
			flag = 0
			time.sleep(random_time(4,27))
		time.sleep(random_time(0.5,3))
		img_path1 = 'F:\\Games\\python\\images\\fam1.PNG'
		img_path2 = 'F:\\Games\\python\\images\\fam2.PNG'
		result1 = find_image_at(img_path1)
		result2 = find_image_at(img_path2)
		if result1 == False and result2 == False and total_mp > 3:
			print("familia is not active activating")
			key_click(6)
			total_mp = total_mp-3
			print(f"total_mp is {total_mp}")
			time.sleep(random_time(1,3))
		elif result1 == True or result2 == True and total_mp > 1:
			print("familia is active atacking ")
			total_mp = blizzard(total_mp)
			print(f"total_mp is {total_mp}")
		else:
			total_mp = mp_charge(total_mp,mp_charge_time)
			print(f"total_mp is {total_mp}")



time.sleep(random_time(5,7))
print("random sleep between 5 to 7 seconds")
total_mp = 19 #int value in 100
print(f"Total mp set to {total_mp}")
mp_charge_time = 4 # time in seconds
print(f"mp charge time set to {mp_charge_time} seconds")
main_loop(total_mp,mp_charge_time)
