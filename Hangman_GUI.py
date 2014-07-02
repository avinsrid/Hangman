#!/usr/bin/env python
#  blitzavi89
# ----------------------------------------------------------------
# HANGMAN GUI MODULE (Python 3.x)
# ----------------------------------------------------------------
import urllib
import json
import random
import tkinter
from tkinter import *
import tkinter.messagebox

class Hangman_GUI(tkinter.Tk) :
	def __init__(self, parent) :
		tkinter.Tk.__init__(self, parent)
		self.parent = parent
		self.Initialize_Hanger()

# Create 100x100 array of buttons to display the Hangman Graphic
	hangman_button = []
	alpha_tiles = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	tiles_button = []
	display_message = "SELECT TITLES ONE AT A TIME TO GUESS COUNTRY"
	blank_buttons = []
	display_buttons = []
	question = None
	play_again_button1 = None
	play_again_button2 = None
	callback_CheckGameStatus = None
	chance = 0
	replay = True
	number_of_games = 0
	number_won_games = 0
	def Initialize_Hanger(self) :
		self.grid()
		for i in range(20) :
			self.hangman_button.append([])
			for j in range(25) :
				self.hangman_button[i].append(tkinter.Button(self))
				self.hangman_button[i][j].configure(width = 1, height = 1)
				self.hangman_button[i][j].grid(column = i, row = j)

# Design the hanger in "Black"
		for i in range(0,3) :
			self.hangman_button[7][i].configure(bg = "Black")
		for i in range(7,15) :
			self.hangman_button[i][0].configure(bg = "Black")
		for i in range(0,25) :
			self.hangman_button[15][i].configure(bg = "Black")
		for i in range(11,20) :
			self.hangman_button[i][24].configure(bg = "Black")

# Colour all others buttons except the hanger to "Yellow"		
		for every_list in self.hangman_button :
			for every_sqr in every_list :
				if every_sqr["bg"] != "Black" :
					every_sqr.configure(bg = "Yellow")

# Make the man's face
	def Make_Face(self) :
		for i in range(4,11) :
			self.hangman_button[i][3].configure(bg = "Red")
		for i in range(3,10) :
			self.hangman_button[4][i].configure(bg = "Red")
		for i in range(3,10) :
			self.hangman_button[10][i].configure(bg = "Red")
		for i in range(4,11) :
			self.hangman_button[i][9].configure(bg = "Red")
		self.hangman_button[6][4].configure(bg = "Blue")
		self.hangman_button[8][4].configure(bg = "Blue")
		self.hangman_button[7][6].configure(bg = "Blue")
		self.hangman_button[6][8].configure(bg = "Blue")
		self.hangman_button[7][8].configure(bg = "Blue")
		self.hangman_button[8][8].configure(bg = "Blue")

# Make the man's body
	def Make_Body(self) :
		for i in range(9,19) :
			self.hangman_button[7][i].configure(bg = "Red")

# Make the man's left leg
	def Make_Left_Leg(self) :
		self.hangman_button[6][19].configure(bg = "Red")
		self.hangman_button[5][20].configure(bg = "Red")
		self.hangman_button[5][21].configure(bg = "Red")
		self.hangman_button[5][22].configure(bg = "Red")
		self.hangman_button[5][23].configure(bg = "Red")

# Make the man's right leg
	def Make_Right_Leg(self) :
		self.hangman_button[8][19].configure(bg = "Red")
		self.hangman_button[9][20].configure(bg = "Red")
		self.hangman_button[9][21].configure(bg = "Red")
		self.hangman_button[9][22].configure(bg = "Red")
		self.hangman_button[9][23].configure(bg = "Red")

# Make the man's left hand
	def Make_Left_Hand(self) :
		self.hangman_button[6][13].configure(bg = "Red")
		self.hangman_button[5][14].configure(bg = "Red")
		self.hangman_button[4][15].configure(bg = "Red")

# Make the man's right hand
	def Make_Right_Hand(self) :
		self.hangman_button[8][13].configure(bg = "Red")
		self.hangman_button[9][14].configure(bg = "Red")
		self.hangman_button[10][15].configure(bg = "Red")

# Create tiles from A-Z for user selection
	def Tile_Create(self) :
		self.grid()
		alpha_index = 0
		for i in range(0,13) :
			self.tiles_button.append([])
			for j in range(0,2) :
				self.tiles_button[i].append(tkinter.Button(self, activebackground = "Green", text = self.alpha_tiles[alpha_index], bg = "White", command = lambda x = i, y = j : self.OnClickTile(x,y)))
				self.tiles_button[i][j].configure(width = 1, height = 1)
				self.tiles_button[i][j].grid(column = 20 + i, row = j +6)
				alpha_index += 1

# Display the message that tells what user needs to do through text in buttons
	def Main_Display(self) :
		self.grid()
		line_counter = 0
		row_counter = 0
		for i in range(len(self.display_message)) :
			self.display_buttons = tkinter.Button(self, fg = "Yellow", text = self.display_message[i], bg = "Black", activebackground = "Black", activeforeground = "Yellow")
			self.display_buttons.grid(column = 20 + line_counter, row = row_counter)
			self.display_buttons.configure(width = 1, height = 1)
			if line_counter >= 13 :
				line_counter = 0
				row_counter +=1
			else :
				line_counter +=1

# Generate the Blanks for Country Puzzle Guess
	def Generate_Puzzle_Blank(self, question, callback_CheckGameStatus) :
		self.grid()
		self.question = question.upper()
		self.callback_CheckGameStatus = callback_CheckGameStatus
		for i in range(0,len(self.question)) :
			self.blank_buttons.append(tkinter.Button(self, text = "_"))
			self.blank_buttons[i].configure(width = 1, height = 1)
			self.blank_buttons[i].grid(column = 20 + i, row = 10)
			if self.question[i] == " " :
				self.blank_buttons[i].destroy()
				self.blank_buttons[i] = " "

# Logic during clicking of a letter for guessing the country
	def OnClickTile(self, xCor, yCor) :
		if self.question != None :
			if self.tiles_button[xCor][yCor]["text"] in self.question and self.tiles_button[xCor][yCor]["bg"] == "White" :
				show_text = self.tiles_button[xCor][yCor]["text"]
				self.tiles_button[xCor][yCor].configure(bg = "Black")
				for i in range(len(self.question)) :
					if self.question[i] == show_text :
						self.blank_buttons[i].configure(text = self.tiles_button[xCor][yCor]["text"])
					else :
						pass
				if self.Check_Win() == True :
					self.number_won_games += 1
					tkinter.messagebox.showinfo("Hangman Popup", "You Win!")
					self.Exit_GUI()
				else :
					pass

			elif self.tiles_button[xCor][yCor]["text"] in self.question and self.tiles_button[xCor][yCor]["bg"] == "Black" :
				pass
			elif self.tiles_button[xCor][yCor]["text"] not in self.question and self.tiles_button[xCor][yCor]["bg"] == "Black" :
				pass
			else :
				if self.chance == 0 :
					self.Make_Face()
					self.chance +=1
					self.tiles_button[xCor][yCor].configure(bg = "Black")
					if self.Check_Win() == True :
						self.number_won_games += 1
						tkinter.messagebox.showinfo("Hangman Popup", "You Win!")
						self.Exit_GUI()
					else :
						pass
				elif self.chance == 1 :
					self.Make_Body()
					self.chance +=1
					self.tiles_button[xCor][yCor].configure(bg = "Black")
					if self.Check_Win() == True :
						self.number_won_games += 1
						tkinter.messagebox.showinfo("Hangman Popup", "You Win!")
						self.Exit_GUI()
					else :
						pass
				elif self.chance == 2 :
					self.Make_Right_Hand()
					self.chance +=1
					self.tiles_button[xCor][yCor].configure(bg = "Black")
					if self.Check_Win() == True :
						self.number_won_games += 1
						tkinter.messagebox.showinfo("Hangman Popup", "You Win!")
						self.Exit_GUI()
					else :
						pass
				elif self.chance == 3 :
					self.Make_Left_Hand()
					self.chance +=1
					self.tiles_button[xCor][yCor].configure(bg = "Black")
					if self.Check_Win() == True :
						self.number_won_games += 1
						tkinter.messagebox.showinfo("Hangman Popup", "You Win!")
						self.Exit_GUI()
					else :
						pass
				elif self.chance == 4 :
					self.Make_Right_Leg()
					self.chance +=1
					self.tiles_button[xCor][yCor].configure(bg = "Black")
					if self.Check_Win() == True :
						self.number_won_games += 1
						tkinter.messagebox.showinfo("Hangman Popup", "You Win!")
						self.Exit_GUI()
					else :
						pass
				elif self.chance >= 5 :
					self.Make_Left_Leg()
					self.tiles_button[xCor][yCor].configure(bg = "Black")
					self.Exit_GUI()
				else :
					self.Exit_GUI()

# Exit Prompt after each round
	def Exit_GUI(self) :
		if self.replay == False:
			self.number_of_games += 1
			tkinter.messagebox.showinfo("Hangman Popup", "THANKS FOR PLAYING! \n Number of Games Played = " + str(self.number_of_games) + "\n Number of Games Won = " + str(self.number_won_games))
			self.callback_CheckGameStatus()
		else:
			self.number_of_games +=1
			tkinter.messagebox.showinfo("Hangman Popup","LET US PLAY AGAIN! HIT QUIT IF YOU WISH TO EXIT GAME :)")
			self.callback_CheckGameStatus()

# What 'Quit Button' does
	def Quit_Button(self) :
		self.grid()
		self.quit_button = tkinter.Button(self, bg = "Yellow", fg = "Red", text = "Quit", activebackground = "Green", command = self.OnClickQuit)
		self.quit_button.configure(width = 1, height = 1)
		self.quit_button.grid(column = 27, row = 14)

# Quit Hangman based on Quit click
	def OnClickQuit(self) :
		self.replay = False
		self.Exit_GUI()

# Function to check if we have a win situation based on made guesses
	def Check_Win(self) :
		check = True
		for element in self.blank_buttons :
			if element == " " or element["text"] != "_" :
				check = check and True
			else :
				check = check and False
		return check





