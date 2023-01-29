from getpass import getpass as input
print ("Welcome To The Epic 🪨  📄 ✂️  Battle Simulator")
print ()
print ("Now both players should select your move (pick between R-Rock, P-Paper or S-Scissors)")
print ()
player_1_score = 0
player_2_score = 0
while True:
    player_1 = input()
    player_2 = input()
    print ()
    print ("Player 1 picked", player_1)
    print ("Player 2 picked", player_2)
    print()
    if player_1 == "r" or player_1 == "R":
      if player_2 == "r" or player_2 == "R":
        print ("Both players went for a rock fest. It's a tie")
      elif player_2 == "p" or player_2 == "P":
        print ("Paper covers rock in defeat. Player 2 wins")
        player_2_score += 1
      elif player_2 == "s" or player_2 == "S":
        print ("Rock crushes scissors to smithereens. Player 1 wins")
        player_1_score += 1
      else:
        print ("Pick right option")
        continue
    elif player_1 == "p" or player_1 == "P":
      if player_2 == "r" or player_2 == "R":
        print ("Paper covers rock in defeat. Player 1 wins")
        player_1_score += 1
      elif player_2 == "p" or player_2 == "P":
        print ("Both players got a paper cut. It's a tie")
      elif player_2 == "s" or player_2 == "S":
        print ("Scissors tears paper to shreds. Player 2 wins")
        player_2_score += 1
      else:
        print ("Pick right option")
        continue
    elif player_1 == "s" or player_1 == "S":
      if player_2 == "r" or player_2 == "R":
        print ("Rock crushes scissors to smithereens. Player 2 wins")
        player_2_score += 1
      elif player_2 == "p" or player_2 == "P":
        print ("Paper covers rock in defeat. Player 2 wins")
        player_2_score += 1
      elif player_2 == "s" or player_2 == "S":
        print ("The scissors fight got bloody for both players. It's a tie")
      else:
        print ("Pick right option")
        continue
    else:
      print ("Pick right option")
      continue

    if player_1_score == 3:
      print("Player 1 wins the game!!!! 🥳🥳🥳")
      print ("Game Over")
      break
    elif player_2_score == 3:
      print("Player 2 wins the game!!!! 🥳🥳🥳")
      print ("Game Over")
      break
