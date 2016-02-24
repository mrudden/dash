# dash.py
# Dungeon Adventure Shell
# Michael Rudden, 2016

import sys
from bash import bash

running = True

def welcome():
  print """You find yourself somewhere in the middle of a dark dungeon.
Perhaps you should explore your environment, or type \"check guide\"
to consult the Explorer's Guide you always carry in your pocket."""

def run():
  while running:
    input = raw_input("\nWhat would you like to do? >")
    print ""
    if input == "check guide":
      check_guide()
    elif input == "look":
      print "You quickly look at your surroundings. On first glance you see:"
      print bash('ls')
    elif input == "look up":
      print "You look up above you and see:"
      print bash('ls ..')
    elif input == "look around":
      print "You take a good look around you, stopping to make note of what you see:"
      print bash('ls -a')
    elif input == "bash":
      bash_input = True
      while bash_input:
        bash_command = raw_input("$")
        if bash_command == "exit":
          bash_input = False
        else:
	  print bash(bash_command)
    elif input == "exit":
      print "there is no escape"
      sys.exit()
    else:
      print "Please enter a valid command"

def check_guide():
  print """You open the worn book in your pocket and see the following:
look = ls
look around = ls -a
look up = ls ..
"""

welcome()
run()
