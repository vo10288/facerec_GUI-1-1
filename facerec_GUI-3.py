#!/opt/virtualenv/computer_vision/bin/python3

# 20250610-H17.18
# https://tsurugi-linux.org
# by Visi@n
# LICENSE
# THIS SCRIPT HAS BEEN CREATED BY Antonio 'Visi@n' Broi [antonio@tsurugi-linux.org] and it's licensed under the MIT License

import face_recognition
from face_recognition import face_locations
import argparse
from tkinter import *

#import tkinter, Tkconstants, tkFileDialog
import tkinter
from tkinter import filedialog
from tkinter import constants

import tkinter as tk
import sys
import os
import cv2
import subprocess
#import tkMessageBox
from tkinter import messagebox

import time
#from datetime import datetime

sximage=""
dximage=""

global face_distancess
face_distancess= ''
global matchess
matchess= ''

def openImagesx():
	os.chdir(os.path.expanduser('~/02.computer_vision/'))
	if not os.path.exists("03.reports/reconunknown"):
		os.makedirs("03.reports/reconunknown")
	if not os.path.exists("03.reports/reconknown"):
		os.makedirs("03.reports/reconknown")

	global imagesx
	imagesx = tkinter.filedialog.asksaveasfilename(initialdir = "~/02.computer_vision/",title = "Select file",filetypes = (("all files","*.jpg"),("all files","*.png"),("all files","*.jpeg")))
	print (imagesx)
	
	global imagesxGIF
	#imagesxGIF = = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") +'.gif'
	imagesxGIF = 'unknown.gif'
	print(imagesxGIF)
	
	command = ('convert '+ 'jpeg:'+'\"'+imagesx +'\"'+ ' -resize 300x200 gif:'+'03.reports/reconunknown/\"'+imagesxGIF+'\"')
	subprocess.Popen(command, shell=True)
	print('03.reports/reconunknown/\"'+imagesxGIF+'\"')
	
	command = ('file '+'\"'+ imagesx+'\"')
	subprocess.Popen(command, shell=True)
	
	command = ('file '+'03.reports/reconunknown/\"'+ imagesxGIF+'\"')
	subprocess.Popen(command, shell=True)

	
def openImagedx():
	os.chdir(os.path.expanduser('~/02.computer_vision/'))
	if not os.path.exists("03.reports/reconunknown"):
		os.makedirs("03.reports/reconunknown")
	if not os.path.exists("03.reports/reconknown"):
		os.makedirs("03.reports/reconknown")

	global imagedx
	imagedx = tkinter.filedialog.asksaveasfilename(initialdir = "~/02.computer_vision/",title = "Select file",filetypes = (("all files","*.jpg"),("all files","*.png"),("all files","*.jpeg")))
	print (imagedx)

	global imagedxGIF
	imagedxGIF = 'known.gif'
	print(imagedxGIF)
	
	command = ('convert  '+ 'jpeg:'+'\"'+imagedx +'\"'+ ' -resize 300x200 gif:'+'03.reports/reconknown/\"'+imagedxGIF+'\"')
	subprocess.Popen(command, shell=True)
	print('03.reports/reconknown/\"'+imagedxGIF+'\"')
	
	command = ('file '+'\"'+ imagedx+'\"')
	subprocess.Popen(command, shell=True)
	
	command = ('file '+'03.reports/reconknown/\"'+ imagedxGIF+'\"')
	subprocess.Popen(command, shell=True)

	
def show_image():
	radice1 = Tk()
	os.chdir(os.path.expanduser('~/02.computer_vision/'))
 
	canvas1 = Canvas(radice1,  width=300, height=200)
	canvas1.pack()
 
	img = PhotoImage(master = canvas1, file='03.reports/reconknown/'+imagedxGIF)
	canvas1.create_image(0, 0, anchor=NW, image=img)
 
	radice1.mainloop()
 
def show_image2():
	radice1 = Tk()
	os.chdir(os.path.expanduser('~/02.computer_vision/'))
 
	canvas1 = Canvas(radice1,  width=300, height=200)
	canvas1.pack()
 
	img = PhotoImage(master = canvas1, file='03.reports/reconknown/'+imagedxGIFrec)
	canvas1.create_image(0, 0, anchor=NW, image=img)
 
	radice1.mainloop()
 
	
def facerecognition():
		# Load an image sx
		global sximage
		sximage = face_recognition.load_image_file(imagesx)
		# Find all faces and face encodings in the image sx
		face_locationssx = face_recognition.face_locations(sximage)
		face_encodingssx = face_recognition.face_encodings(sximage, face_locationssx)
		
		# Load an image dx
		dximage = face_recognition.load_image_file(imagedx)
		# Find all faces and face encodings in the unknown image
		face_locationsdx = face_recognition.face_locations(dximage)
		face_encodingsdx = face_recognition.face_encodings(dximage, face_locationsdx)[0]
		
		face_distances = face_recognition.face_distance(face_encodingssx, face_encodingsdx)
		face_distancess =((1-face_distances)*100)
	
		
		matches = face_recognition.compare_faces(face_encodingssx, face_encodingsdx)
		print(face_distances)
		print(matches)
		print(str(face_distancess)+' %')
		
		os.chdir(os.path.expanduser('~/02.computer_vision/'))
		# Mostra immagine SX (unknown)
		canvas_sx = tk.Canvas(root, width=300, height=200)
		img_sx = PhotoImage(master=canvas_sx, file='03.reports/reconunknown/' + imagesxGIF)
		canvas_sx.create_image(0, 0, anchor=NW, image=img_sx)
		canvas_sx.configure(bg="black")
		canvas_sx.image = img_sx  # evita garbage collection
		canvas_sx.place(x=10, y=150)

		# Mostra immagine DX (known)
		canvas_dx = tk.Canvas(root, width=300, height=200)
		img_dx = PhotoImage(master=canvas_dx, file='03.reports/reconknown/' + imagedxGIF)
		canvas_dx.create_image(0, 0, anchor=NW, image=img_dx)
		canvas_dx.configure(bg="black")
		canvas_dx.image = img_dx  # evita garbage collection
		canvas_dx.place(x=330, y=150)



		slogan = tk.Label(text= "Biometric verification percentage is : "+str(face_distancess)+' %',
						bg="black",
						fg="white",
						font=("helvetica",15)) 
		slogan.pack(side=LEFT, ipadx=12, ipady=4, pady=0, padx=10)
		slogan.place(x=400, y=360)

	
		slogan = tk.Label(text= "The verification result is  : "+str(matches),
						bg="black",
						fg="white",
						font=("helvetica",15)) 
		slogan.pack(side=LEFT, ipadx=12, ipady=4, pady=0, padx=10)
		slogan.place(x=430, y=400)

###
		slogan = tk.Label(text= "This facial recognition system is based on the ",
						bg="black",
						fg="red",
						font=("helvetica",13)) 
		slogan.pack(side=LEFT, ipadx=12, ipady=4, pady=0, padx=10)
		slogan.place(x=10, y=420)
###
		slogan = tk.Label(text= "Python library face_recognition and the results",
						bg="black",
						fg="red",
						font=("helvetica",13)) 
		slogan.pack(side=LEFT, ipadx=12, ipady=4, pady=0, padx=10)
		slogan.place(x=10, y=440)
###
		slogan = tk.Label(text= "percentages must be interpreted in this way:   ",
						bg="black",
						fg="red",
						font=("helvetica",13)) 
		slogan.pack(side=LEFT, ipadx=12, ipady=4, pady=0, padx=10)
		slogan.place(x=10, y=460)
###
		slogan = tk.Label(text= "< 40% Insufficient",
						bg="black",
						fg="red",
						font=("helvetica",13)) 
		slogan.pack(side=LEFT, ipadx=12, ipady=4, pady=0, padx=10)
		slogan.place(x=10, y=500)
###
		slogan = tk.Label(text= "> 40% Minimum",
						bg="black",
						fg="red",
						font=("helvetica",13)) 
		slogan.pack(side=LEFT, ipadx=12, ipady=4, pady=0, padx=10)
		slogan.place(x=10, y=520)
###
		slogan = tk.Label(text= "> 50% Optimal",
						bg="black",
						fg="red",
						font=("helvetica",13)) 
		slogan.pack(side=LEFT, ipadx=12, ipady=4, pady=0, padx=10)
		slogan.place(x=10, y=540)
###
		slogan = tk.Label(text= "> 60% Maximum",
						bg="black",
						fg="red",
						font=("helvetica",13)) 
		slogan.pack(side=LEFT, ipadx=12, ipady=4, pady=0, padx=10)
		slogan.place(x=10, y=560)
###

#		show_image2()
		show_image()
		
		
def face_detect_landmarks():
	os.chdir(os.path.expanduser('~/02.computer_vision/'))

	global imagedxREC
	imagedxREC = 'knownRec.jpg'
	
	command = '/opt/computer_vision/recon68.py -i '+'\"'+imagedx+'\" -o '+'03.reports/reconknown/\"'+imagedxREC+'\"'
	subprocess.Popen(command, shell=True)
	time.sleep(2)
	
	global imagesxREC
	imagesxREC = 'unknownRec.jpg'
		
	command = '/opt/computer_vision/recon68.py -i '+'\"'+imagesx+'\" -o '+'03.reports/reconunknown/\"'+imagesxREC+'\"'
	subprocess.Popen(command, shell=True)


def change_bgcolor_white():
		root.configure(bg="white")
		frame.configure(bg="white")
		#os.execl(sys.executable, sys.executable, *sys.argv)

def change_image():		
		os.execl(sys.executable, sys.executable, *sys.argv)
		

def change_bgcolor_black():
		root.configure(bg="black")
		frame.configure(bg="black")
		#os.execl(sys.executable, sys.executable, *sys.argv)

def face_recognition_landmarks():

	os.chdir(os.path.expanduser('~/02.computer_vision/'))

	global imagedxREC
	imagedxREC = 'knownRec.jpg'
	
	command = '/opt/computer_vision/recon68.py -i '+'\"'+imagedx+'\" -o '+'03.reports/reconknown/\"'+imagedxREC+'\"'
	subprocess.Popen(command, shell=True)
	time.sleep(2)
	
	global imagesxREC
	imagesxREC = 'unknownRec.jpg'
		
	command = '/opt/computer_vision/recon68.py -i '+'\"'+imagesx+'\" -o '+'03.reports/reconunknown/\"'+imagesxREC+'\"'
	subprocess.Popen(command, shell=True)
	

##############
	global imagedxGIFrec
	global imagesxGIFrec


	imagedxGIFrec = imagedxREC+'.gif'
	print(imagedxGIFrec)

	imagesxGIFrec = imagesxREC+'.gif'
	print(imagesxGIFrec)


	command = ('convert  '+ 'jpeg:'+'03.reports/reconknown/'+ imagedxREC + ' -resize 300x200 gif:'+'03.reports/reconknown/'+imagedxGIFrec)
	subprocess.Popen(command, shell=True)
	print(imagedxGIFrec)
	
	command = ('file '+'03.reports/reconknown/'+ imagedxREC)
	subprocess.Popen(command, shell=True)
	
	command = ('file '+'03.reports/reconknown/'+ imagedxGIFrec)
	subprocess.Popen(command, shell=True)

		
	command = ('convert  '+ 'jpeg:'+'03.reports/reconunknown/'+ imagesxREC + ' -resize 300x200 gif:'+'03.reports/reconunknown/'+imagesxGIFrec)
	subprocess.Popen(command, shell=True)
	print(imagesxGIFrec)
	
	command = ('file '+'03.reports/reconunknown/'+ imagesxREC)
	subprocess.Popen(command, shell=True)
	
	command = ('file '+'03.reports/reconunknown/'+ imagesxGIFrec)
	subprocess.Popen(command, shell=True)

		
	# Load image sx
	global sximage
	sximage = face_recognition.load_image_file(imagesx)
	# Find all the faces and face encodings in the image sx
	face_locationssx = face_recognition.face_locations(sximage)
	face_encodingssx = face_recognition.face_encodings(sximage, face_locationssx)
		
	# Load  image dx
	dximage = face_recognition.load_image_file(imagedx)

	# Find all the faces and face encodings in the unknown image
	face_locationsdx = face_recognition.face_locations(dximage)
	face_encodingsdx = face_recognition.face_encodings(dximage, face_locationsdx)[0]
		
	face_distances = face_recognition.face_distance(face_encodingssx, face_encodingsdx)
	face_distancess =((1-face_distances)*100)
	
	matches = face_recognition.compare_faces(face_encodingssx, face_encodingsdx)
	print(face_distances)
	print(matches)
	print(str(face_distancess)+' %')
		
	os.chdir(os.path.expanduser('~/02.computer_vision/'))
	# Mostra immagine SX (unknown)
	canvas_sx = tk.Canvas(root, width=300, height=200)
	img_sx = PhotoImage(master=canvas_sx, file='03.reports/reconunknown/' + imagesxGIF)
	canvas_sx.create_image(0, 0, anchor=NW, image=img_sx)
	canvas_sx.configure(bg="black")
	canvas_sx.image = img_sx  # evita garbage collection
	canvas_sx.place(x=10, y=150)

	# Mostra immagine DX (known)
	canvas_dx = tk.Canvas(root, width=300, height=200)
	img_dx = PhotoImage(master=canvas_dx, file='03.reports/reconknown/' + imagedxGIF)
	canvas_dx.create_image(0, 0, anchor=NW, image=img_dx)
	canvas_dx.configure(bg="black")
	canvas_dx.image = img_dx  # evita garbage collection
	canvas_dx.place(x=330, y=150)


	slogan = tk.Label(text= "Biometric percentage of verify is : "+str(face_distancess)+' %',
					bg="black",
					fg="white",
					font=("helvetica",15)) 
	slogan.pack(side=LEFT, ipadx=12, ipady=4, pady=0, padx=10)
	slogan.place(x=400, y=360)

	slogan = tk.Label(text= "The result of verify is  : "+str(matches),
					bg="black",
					fg="white",
					font=("helvetica",15)) 
	slogan.pack(side=LEFT, ipadx=12, ipady=4, pady=0, padx=10)
	slogan.place(x=430, y=400)

	show_image2()
#	show_image()
	
	
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
frame.configure(bg="black")
root.wm_title("Facial Recognition IMAGE TO IMAGE")
root.geometry("1350x600")
root.configure(bg="black")

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="#ffffff",
                   bg="red",
                   command=quit)
button.pack(side=LEFT, ipadx=2, ipady=4, pady=0, padx=1)
#button.place(x=200, y=500)

slogan = tk.Button(frame,
                   text="OPEN IMAGE KNOWN",
                   fg="#ffffff",
                   bg="#550000",
                   command=openImagesx)
slogan.pack(side=LEFT, ipadx=2, ipady=4, pady=0, padx=1)
#slogan.place(x=60, y=50)

slogan = tk.Button(frame,
                   text="OPEN IMAGE UNKNOWN",
                   fg="#ffffff",
                   bg="#550000",
                   command=openImagedx)
slogan.pack(side=LEFT, ipadx=2, ipady=4, pady=0, padx=1)
#slogan.place(x=100, y=50)

slogan = tk.Button(frame,
                   text="FACE RECOGNITION",
                   fg="#ffffff",
                   bg="#550000",
                   command=facerecognition)
slogan.pack(side=LEFT, ipadx=2, ipady=4, pady=0, padx=1)
#slogan.place(x=140, y=50)

slogan = tk.Button(frame,
                   text="FACE DETECT LANDMARKS",
                   fg="#ffffff",
                   bg="#550000",
                   command=face_detect_landmarks)
slogan.pack(side=LEFT, ipadx=2, ipady=4, pady=0, padx=1)

slogan = tk.Button(frame,
                   text="FACE RECOGNITION LANDMARKS",
                   fg="#ffffff",
                   bg="#550000",
                   command=face_recognition_landmarks)
slogan.pack(side=LEFT, ipadx=2, ipady=4, pady=0, padx=1)

slogan = tk.Button(frame,
                   text="BGCOLOR WHITE",
                   fg="blue",
                   bg="white",
                   command=change_bgcolor_white)
slogan.pack(side=LEFT, ipadx=2, ipady=4, pady=0, padx=1)

slogan = tk.Button(frame,
                   text="BGCOLOR BLACK",
                   fg="white",
                   bg="black",
                   command=change_bgcolor_black)
slogan.pack(side=LEFT, ipadx=2, ipady=4, pady=0, padx=1)

slogan = tk.Button(frame,
                   text="RESET",
                   fg="white",
                   bg="red",
                   command=change_image)
slogan.pack(side=LEFT, ipadx=2, ipady=4, pady=0, padx=1)


slogan = tk.Canvas(root, width=80, height=80)
img = PhotoImage(master = slogan, file="/usr/share/icons/tsurugi/tsurugi.gif")
slogan.create_image(2, 2, anchor=NW, image=img)
slogan.configure(bg="black")
slogan.pack(side=LEFT, ipadx=2, ipady=3, pady=0, padx=5)
slogan.place(x=1110, y=480)

label = tk.Label(text="Visi@n",
				bg="black",
				fg="red",
				font=("helvetica",14),
				
					)
label.pack(side=LEFT, ipadx=10, ipady=4, pady=15, padx=5)
label.place(x=1110, y=570)

root.mainloop()
