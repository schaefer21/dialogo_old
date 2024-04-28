from tkinter import *
import tkinter as tk
#import RPi.GPIO as GPIO
from time import sleep

# master
master = Tk()
master.geometry("1600x480") # pixels

# design variables
background_color = "#FFFFFF"

# button variables
""" button_right = 12 # GREEN
button_continue = 13 # WHITE
button_wrong = 21 # RED
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_right, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_continue, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO .setup(button_wrong, GPIO.IN, pull_up_down = GPIO.PUD_UP)"""

# logic variables
stage = 3 # {0, 1, 2} as the stages
explanation_stage = 0 # {0, ...} as the explanations stages
task_stage = 0 # which images are shown
rounds = 3

# separation line
canvas0 = Canvas(master, width = 1600, height = 480, bg = background_color)
canvas0.create_text(100, 100, text = "stage 0")
canvas0.pack()

#canvas.create_line(800, 0, 800, 480, fill="black", width = 5)
#canvas.pack()

while True:
	# EXPLANATION STAGE
	while (stage == 0):
		print("stage 0")
		if False: 
        #if GPIO.input(button_right) != GPIO.HIGH:
			canvas0.delete("all")
			canvas0.create_text(100, 100, text = "stage 0")
			canvas0.pack()
			stage += 1 % 2
			print("switched state to 1")
		# UPDATE THE WINDOW
		master.update()
		
		# SWITCH FROM EXPLANATION STAGE TO EXPLANATION STAGE WHEN CONTINUE CLICKED
		
	# GAME STAGE
	while stage == 1:
		print("stage 1")
		if False:
        #if GPIO.input(button_continue) != GPIO.HIGH:
			canvas0.delete("all")
			canvas0.create_text(100, 100, text = "stage 1")
			canvas0.pack()
			stage = 0
			print(stage)
			print("switched state to 0")
		# UPDATE THE WINDOW
		master.update()
		
		# IF EITHER OF THE BUTTONS PRESSED SWITCH TO DIFFERENT GAME STAGE
			# DEPENDING ON WHICH BUTTON, UPDATE TEAM SCOR
			
		# UPDATE ROUND COUNTER
					
	# HAND OVER STAGE
	while stage == 2:
        #print("stage 2")
        #canvas0.delete("all")
        #canvas0.create_text(100, 100, text = "stage 0")
        #canvas0.pack()
	# IF THERE ARE ROUNDS LEFT SWITCH TO STAGE 1
 		
	# FINAL STAGE
	while stage == 3:
		print("stage 3")
		canvas0.delete("all")
		
		
		# SHOWING GAME RESULTS
		# WAITING ON CONTINUE TO GO TO STAGE 0 AGAIN
