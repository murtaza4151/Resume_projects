import random
computer = random.randint(1,100)
computer2 = random.randint(1,100)
computer3 = random.randint(1,100)
attempts = 0
max_attempts = 7
max_attempts2 = 5
max_attempts3 = 3
level = 1
status = True
choice = 0
while status:
    user = int(input("Enter a number="))
    attempts += 1
    if level == 1 :
      if user > computer:
        print(user,"Hint: Guess Lower number")
      elif user < computer:
        print(user,"Hint: Guess Upper number")
      elif user == computer:
        print(user,"You win Level 1 complete")
        level = 2
        attempts = 0
        continue
      if attempts >= max_attempts:
        print("Try only seven Time Game Over")
        choice = input("Do you want to continue the Game ??? write y for yes and n for No:")
        if choice == "y" or choice == "y":
          status = True
          level = 1
          attempts = 0
          continue
        else:
          status = False
          break
     
    elif level == 2:
      if user > computer2:
        print(user,"Hint: Guess Lower number")
      elif user < computer2:
        print(user,"Hint: Guess Upper number")
      elif user == computer2:
        print(user,"You win Level 2 complete")
        level = 3
        attempts = 0
        continue
      if attempts >= max_attempts2:
        print("Try only Five Time Game Over")
        choice = input("Do you want to continue the Game ??? write y for yes and n for No:")
        if choice == "y" or choice == "y":
          status = True
          level = 1
          attempts = 0
          continue
        else:
          status = False
          break
      
    elif level == 3:
      if user > computer3:
        print(user,"Hint: Guess Lower number")
      elif user < computer3:
        print(user,"Hint: Guess Upper number")
      elif user == computer3:
        print(user,"You win Level 3 complete")
        choice = input("Do you want to continue the Game ??? write y for yes and n for No:")
        if choice == "y" or choice == "y":
          status = True
          level = 1
          attempts = 0
          continue
        else:
          status = False
          break
      if attempts >= max_attempts3:
        print("Try only Three Time Game Over")
        choice = input("Do you want to continue the Game ??? write y for yes and n for No:")
        if choice == "y" or choice == "y":
          status = True
          level = 1 
          attempts = 0
          continue
        else:
          status = False
          break
      
print()
print("=====================================================")
print() 

