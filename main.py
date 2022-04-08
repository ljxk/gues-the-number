import random
number = random.randint (1,10)
cheat = 1
if cheat == 1:
  print ("cheater "+str(number)+".")
print ("guess the number. 1 to 10")
guess = input()



if guess == str(number):
  print ("you win")
elif int(guess) > number:
  print ("lower")
elif int(guess) < number:
  print ("higher")
else:
  print ("how")