# This will be a TRPG, Text-Based adventure game with
# lots of rooms, friend, enemies, hidden treasures, secrets,
# collectibles and more. Gain XP, save HP, have FUN! =D
# (listening to GameOfThrones music)...make them LIE! xD
# The player can not trust anyone! (after enough interactions)
# 'You can only ask 1 question'-type of characters.
# Moody characters, if (s)he's happy, will help you more.
# Lie-detector / Truth serum. (you know how it works)
# Give items (presents) to characters, make them happy.
# Give them alcohol? - makes happy, more likely to say dumb shit.
# Likelyhood: random choice out of 10(0), (7xYes + 3xNo = 70% chance.)
#   make a likelyhood situation where there is no option where we get to win. small help/big help, but no solution.
# Variables: Happy = 1 Helpful = 1 ---> =2. If sum >=2, big help comes.
# Stats print loop: print stats, run a function, stats, then another function.
#   Make a variable: storyline. add +1 to proceed to next one? (bad idea?)
#       or just include stats_print in all functions.

##########################################################################################################

# Variables:

# Basic stats:
HP = 100
XP = 0
MONEY = 100

money_given = 0
PoorJohnMoney = 0

import time #this is needed for the time.sleep function to work!

##########################################################################################################

def wait1():
  time.sleep(1)

def wait2():
  time.sleep(2)
  
def start_game():
  Quasimodo()

def Quasimodo():
    stats_print()
    print "Hi, I'm Quasimodo. Do you want to go inside? (yes/no)"
    Quasimodo_answer = raw_input()
    if Quasimodo_answer == "yes":
      print "You are in! :D"
      PoorJohn() # here comes the PoorJohn part
    elif Quasimodo_answer == "no":
      print "Hm..."
      wait2()
      print "Then why are you here?"
      end_game()  
    else:
      print "Ermm...what?"
      wait2()
      Quasimodo()

#Let's make PoorJohn aggressive :D
def PoorJohn():
    global HP
    global MONEY
    global PoorJohnMoney
    money_given = 0
    while MONEY > 0:
          print "Hi, I am PoorJohn. Please give me money! I have %r money now." % PoorJohnMoney
          print "How much would you give? :)"
          money_given = int(raw_input())
          if money_given >= 10 and money_given <= MONEY:
            MONEY = MONEY - money_given
            PoorJohnMoney = PoorJohnMoney + money_given
            print "HAHAHAH! I have %r money now!" % PoorJohnMoney
            stats_print()
            PoorJohn()
          elif money_given < 20 and money_given >= 10 and money_given <= MONEY:
            print "That's not enough! You fokkin CONT! *Punch in da face*"
            HP = HP - 5
            MONEY = MONEY - money_given
            PoorJohnMoney = PoorJohnMoney + money_given
            stats_print()
            PoorJohn()
          elif money_given < 10 and money_given > 0 and money_given <= MONEY:
            print "What the fuck man?! *Shoots you in the leg*"
            HP = HP - 30
            MONEY = MONEY - money_given
            PoorJohnMoney = PoorJohnMoney + money_given
            stats_print()
            PoorJohn()
          else:
            print "I have no more money! Goodbye"
            end_game()
    else:
      print "What am I doing? I do not even have that much money."
      wait2()
      print "Should I give him all the money I have?"
      give_all_money = raw_input()
      if give_all_money == "yes":
        PoorJohnMoney = MONEY + PoorJohnMoney
        MONEY = 0
        end_game()
      elif give_all_money == "no":
        print "Ok, I have some money left."
        stats_print()
        end_game
      
      money_given = MONEY #this should make sure that the money_given is not more than the MONEY the player has.
    
##########################################################################################################
        
def end_game():
    stats_print()
    print "Press Enter to close window."
    end_game = raw_input()

def stats_print():
    print "HP:      %r" %HP
    print "XP:      %r" %XP
    print "MONEY:   %r" %MONEY
    print "PoorJohnMoney:   %r" %PoorJohnMoney
    
def just_a_list_of_stages():
    print "---------------"
    print "THE END...roll credits"
    wait1()
    print "just_a_list_of_stages"
    wait1()
    print "give_me_money"
    wait1()
    print "Quasimodo"
    wait1()
    print "end_game"
    wait1()
    print "stats_print"
    wait1()
    print "---------------"
    
##########################################################################################################

start_game()
just_a_list_of_stages()
