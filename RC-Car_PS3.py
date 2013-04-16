#!/usr/bin/python

import pygame
import sys
from time import sleep
import RPi.GPIO as GPIO
import wiringpi

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
#GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

pygame.init()

j = pygame.joystick.Joystick(0)
j.init()

PWM  = 1 # gpio pin 12 = wiringpi no. 1
wiringpi.wiringPiSetup()
wiringpi.pinMode(PWM, 2) # PWM

try:

  while j.get_button(3) == 0:

		pygame.event.pump()	
		speed= j.get_axis(13)
		pwmout= speed * 1023		

	#Speed	
		if j.get_axis(13) != 0.00:
			wiringpi.pwmWrite(PWM,int(pwmout))
			print int(pwmout)

			
		elif j.get_axis(13) == 0.00:
			wiringpi.pwmWrite(PWM,0)

			
	#Richtungen			
		if j.get_button(4) != 0 :	#VOR	
			GPIO.output(22, True)
			GPIO.output(24, True)

			print "Vor"
			sleep(0.01)

		elif j.get_button(5) != 0  :		#RECHTS

			GPIO.output(24, True)
			GPIO.output(23, True)

			print "RECHTS"
			sleep(0.01)
			
		elif j.get_button(7) != 0	:	#Links
			
			GPIO.output(22, True)
			GPIO.output(17, True)

			print "Links"
			sleep(0.01)
			
		elif j.get_button(6) != 0	:	#Zurueck
			
			GPIO.output(23, True)
			GPIO.output(17, True)

			print "Zurueck"
			sleep(0.01)
		
	# Stillstand
			
		elif j.get_button(4) == 0 or j.get_button(5) == 0 or j.get_button(6) == 0 or j.get_button(7) == 0:		
				
			GPIO.output(22, False)
			GPIO.output(24, False)

			GPIO.output(23, False)
			GPIO.output(17, False)

			print "Stillstand"
			sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()	
	j.quit()
	sys.exit()
