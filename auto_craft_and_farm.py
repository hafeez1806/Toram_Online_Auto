#### Created By Hafeez Khan #### Don't Change This Line -_-

############### Imports ###############
from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con


####### Random Everything ########

#----------------------------Random Time------------------------------#
def random_time(low,high):
	time = np.random.uniform(low,high)
	return time

#----------------------------Random Pixel------------------------------#
def random_pixel_in_button(x,y):
	n1 = np.random.uniform(0,5)
	n2 = np.random.uniform(0,5)
	x = x + n1
	y = y + n2
	return x,y

#----------------------------Random Click on image------------------------------#
def find_image_and_random_click(img_path,fun_name):
	box = pyautogui.locateOnScreen(img_path, grayscale=True, confidence=0.7)
	if box != None:
		print("image found")
		pyautogui.moveTo(randomClick(box),duration = random_time(0.4,0.7))
		pyautogui.mouseDown()
		time.sleep(random_time(0.2,0.5))
		pyautogui.mouseUp() 

#----------------------------Random Click Location------------------------------#
def randomClick(box):
	x_click = int(random.uniform(box.left + get_five_percent(box.left), box.left + box.width - get_five_percent(box.width)))
	y_click = int(random.uniform(box.top + get_five_percent(box.left), box.top+box.height - get_five_percent(box.width)))
	return (x_click, y_click)

########## Input/Output ############

#----------------------------Mouse input------------------------------#
def m_click(x,y):
	pyautogui.moveTo(x,y,duration = random_time(0.4,0.7))
	pyautogui.mouseDown()
	time.sleep(random_time(0.2,0.5))
	pyautogui.mouseUp() 

#----------------------------Keyboard input------------------------------#
def key_click(value_k):
	if isinstance(value_k,int):
		value_k = str(value_k)
	pyautogui.keyDown(value_k)
	time.sleep(random_time(0.2,0.5))
	pyautogui.keyUp(value_k)
	time.sleep(random_time(0.3,0.7))

######### Image Processing ###############

#----------------------------Find Image------------------------------#
def find_image(img_path):
	box = pyautogui.locateOnScreen(img_path, grayscale=True, confidence=0.7)
	if box != None:
		return True
	else:
		return False

#----------------------------Check Color------------------------------#
def check_color_at(x,y,color_code,rgb_v):
	if pyautogui.pixel(x,y)[rgb_v] == color_code:
		return True
	else:
		return False

####### Calculations #############

#----------------------------Get 5%------------------------------#
def get_five_percent(o_data):
	percent = int((o_data/100)*5)
	return percent


########## In Game Dynamic Detection #############

#----------------------------Check MP 1100-2000 ------------------------------#
def chcek_mp_double():
	fix_y = 912
	start_x1 = 1210 
	start_x2 = 1210 
	mid_center = 55
	total_mp = 0
	for i in range(10,0,-1):
		c_x = start_x1
		if check_color_at(c_x,fix_y,95,2) == True:
			total_mp = (i*100)+1000
			break
		start_x1 = start_x1 - mid_center
	return(total_mp)

#----------------------------Check MP 100-1000 ------------------------------#
def chcek_mp_single():
	fix_y = 912
	start_x1 = 1210
	start_x2 = 1210
	mid_center = 55
	total_mp = 0
	for i in range(10,0,-1):
		c_x = start_x1
		if check_color_at(c_x,fix_y,211,2) == True:
			total_mp = i*100
			break
		start_x1 = start_x1 - mid_center
	return(total_mp)

#----------------------------Check Total MP ------------------------------#
def check_total_mp():
	c_mp = chcek_mp_double()
	if c_mp == 0:
		c_mp = chcek_mp_single
	return(c_mp)

############### Game skills ############################

#----------------------------Blizzard------------------------------#
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

#----------------------------Familia------------------------------#
def check_familia(total_mp):
	fam_logo = 'F:\\Games\\python\\images\\craft_farm\\familia.PNG'
	rr = find_image(fam_logo)
	if rr == True:
		print("found")
	else:
		key_click(1)
		total_mp = total_mp - 300


######### Development only ############
#----------------------------Check pointer loaction and color------------------------------#
def look_mouse_position_color():
	pyautogui.displayMousePosition()


############ Main Funtions ##################

#----------------------------Check Equipment_bag ------------------------------#
def Equip_bag_Armors():
	key_click('i')
	Equipment_full_logo = 'F:\\Games\\python\\images\\craft_farm\\Equipment_Full.PNG'
	rr = find_image(Equipment_full_logo)
	if rr == True:
		print("Equipment bag is full")
	else:
		print("Equipment bag not full")



#----------------------------Check BagFull------------------------------#
def bag_full_check():
	Bag_full_logo = 'F:\\Games\\python\\images\\craft_farm\\bag_full.PNG'
	rr = find_image(Bag_full_logo)
	if rr == True:
		return("FULL")
	else:
		return("NOT_FULL")

#----------------------------Proc Item------------------------------#


#----------------------------Craft Item ------------------------------#
# def Craft_Armors():



# total_mp = 2000
# time.sleep(random_time(10,12))
# while keyboard.is_pressed('q') == False:
# 	time.sleep(10)
# 	print(chcek_mp_double())
# 	print(chcek_mp_single())



# look_mouse_position_color()
time.sleep(random_time(10,12))
bag_status = bag_full_check()
if bag_status == "FULL":
	Proc_Armors()

