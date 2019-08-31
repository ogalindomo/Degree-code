#Project 4
#By: Oscar Galindo
import random

secretNum = random.randint(1,25)
guess = 0;
while guess != secretNum:
 guess = (int)(input("Guess the secret number."));
 if(guess == secretNum):
     print("Nice!");
 elif guess < secretNum:
     print("Too Low");
 else:
     print("Too High");
     
number=10
while(number > 0):
    print(number)
    number -= 1
print("blastoff!")