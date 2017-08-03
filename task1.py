import random
def main():
  print("What is your name?")
  username = input()
  print("Hello", (username),"let's play golf,CP1401style.")
  for menu in range(0,100):
   print("(I)nstructions (P)lay (Q)uit")
   menu = input()
   if menu == "p" :
    print("The hole is a 230m par 5,you are 230m from the hole,after 0 shot/s.club selection:D is driver,I is iron,P is putter")
    goal = 230
    score = 0
    while goal != 0:
      club = input()
      if club == "d" or club == "D":
        distance = random.randint(80,120)
      elif club == "i" or club == "I":
        distance = random.randint(24,36)
      elif club == "p" or club =="P":
        distance = random.randint(8,12)
        if goal <= 10:
          special = random.randint(0,11)
          if special <= 8:
            goal = distance
      else:
        distance = 0
        print("air score")
      goal = abs(goal-distance)
      score = score + 1
      print("Your shot went",(distance),"m")
      print("You are ",(goal),"from the hole, after",(score),"shot/s")
      if goal == 0 and score < 5:
        print("Clunk... After",(score), "hits, the ball is in the hole! And that’s  under par.")
      elif goal == 0 and score == 5:
        print("Clunk...After",(score),"hits,the ball is in the hole!And that's par.")
      elif goal == 0 and score > 5:
        print("Clunk...After",(score),"hits,the ball is in the hole!And that's over par.")
   elif menu == "i" :
     print("This is a simple golf game in which each hole is 230m game away with par 5. You are able to choose from 3 clubs, the Driver, Iron or Putter."
          "The Driver will hit around 100m, the Iron around 30m and the Putter around 10m. The putter is best used very close to the hole.")
   elif menu == "q" :
     print("Fareware and thanks for playing,",(username))
main()

