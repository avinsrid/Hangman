#!/usr/bin/env python
#  blitzavi89
# ----------------------------------------------------------------
# SIMPLE HANGMAN GAME WITH GUI (Python 3.x)
# ----------------------------------------------------------------
from Hangman_GUI import *
import random
import json
import tkinter
 

# Begin the Game Here
def Begin_Game() :
	global hangman
	hangman.Tile_Create()
	hangman.Main_Display()
	Show_Puzzle()

# Main game logic, that includes reading from JSON file
def Show_Puzzle() :
	global hangman
	country_file = open("countries.json" , "r+")
	json_Obj = json.loads(country_file.read())
	country_file.close()
	country_list = []

	for country in json_Obj :
		country_list.append(country["name"])

	country_question = random.choice(country_list)
	print ("Show_Puzzle(): Random Generated Country is " + country_question)
	testfunc = Check_Game_Status
	hangman.Generate_Puzzle_Blank(country_question, testfunc)
	hangman.Quit_Button()

# Check if we need to continue the game or not based on 'replay' value
def Check_Game_Status() :
	global hangman
	if hangman.replay == True :
		Game_Replay()
	else :
		Destroy_Game()

# Destroy game. I think this never gets called. However :P just to be safe
def Destroy_Game() :
	global hangman
	hangman.destroy()

# If 'replay' from Check_Game_Status = True, we will reset game environment variables and proceed to play game again
def Game_Replay() :
	global hangman
	for every_element in hangman.blank_buttons :
		if every_element != " " :
			every_element.destroy()
		else :
			every_element = None
	hangman.tiles_button = []
	hangman.blank_buttons = []
	hangman.display_buttons = []
	hangman.question = None
	hangman.callbackfunc = None
	hangman.chance = 0
	hangman.Initialize_Hanger()
	hangman.play_again_button1 = None
	hangman.play_again_button2 = None
	Begin_Game()

# Initiate the game process here
hangman = Hangman_GUI(None)
Begin_Game()
hangman.mainloop()