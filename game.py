import random

while True:
    secret_num=random.randint(1,10)
    i=0
    while True:
      guess=int(input("guess num between(1,10):"))
      i+=1
      if guess < 1 or guess > 10:
        print("⚠️  please entre num between 1 to 10")
        continue
    
      if guess==secret_num:
        print("you win 🏆")
        print("you guessing toal:",i,"times")
        break
      else:
        print("try again")

    again=input("play again?(y/n):").lower()
    if again !="y" :
     print("thanks for playing")
     