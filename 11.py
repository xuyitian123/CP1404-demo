import random
def main():
  print("What is your name?")
  username = input()
  hole = 0#the number of round
  total = 0#total is the total number of shots
  Score=[]
  print("Welcome", (username))
  print("let's play golf,CP1401style.")
  menu=["i","p","q","I","P","Q"]
  while menu not in ["q","Q"]:
   print("Golf!")
   print("(I)nstructions")
   print("(P)lay")
   print("(Q)uit")
   menu = input()
   if menu == "p" or menu == "P" :#this program is play round
    print("The hole is a 230m par 5")
    print("you are 230m from the hole,after 0 shot/s.")
    goal = 230#the distance from hole to hole
    score = 0#score is the number of shots in each round
    while goal != 0:
      print("club selection:D is driver,I is iron,P is putter")
      club = input("Choose club:")
      if club == "d" or club == "D":
        distance = random.randint(80,120)#it is the distance that you went
      elif club == "i" or club == "I":
        distance = random.randint(24,36)#it is the distance that you went
      elif club == "p" or club =="P":
        distance = random.randint(8,12)#it is the distance that you went
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
        hole = hole + 1
        total = total + score
        print("Clunk... After",(score), "hits, the ball is in the hole!")
        print("Congratrulations!You are",(5-score),"under par in this hole")
        Score.append(score)
      elif goal == 0 and score == 5:
        hole = hole + 1
        total = total + score
        print("Clunk...After",(score),"hits,the ball is in the hole!")
        print("And that's par.")
        Score.append(score)
      elif goal == 0 and score > 5:
        hole = hole + 1
        total = total + score
        print("Clunk...After",(score),"hits,the ball is in the hole!")
        print("Disappointing!You are",(score-5),"over par in this hole")
        Score.append(score)
      if goal == 0 and total < 5*hole:
        print("You overall score is",(total),"and you are",(5*hole-total),"under par after",(hole),"hole(s)")
      if goal == 0 and total == 5*hole:
        print("You overall score is",(total),"and you are par after",(hole),"hole(s)")
      if goal == 0 and total > 5*hole:
        print("You overall score is",(total),"and you are",(total-5*hole),"over par after",(hole),"hole(s)")
   elif menu == "i" or menu == "I" :#this program is to read the instruction
     print("This is a simple golf game in which each hole is 230m game away with par 5. You are able to choose from 3 clubs, the Driver, Iron or Putter."
          "The Driver will hit around 100m, the Iron around 30m and the Putter around 10m. The putter is best used very close to the hole.")
     print("For each shot, you may use a driver, iron or a putter – each shot will vary in distance.")
     print("The average distance each club can hit is:")
     print("Driver=100m")
     print("Iron=30m")
     print("Putter=10m")
   elif menu == "q" or menu == "Q":#this program is to quit the game
      print("Fareware and thanks for playing,",(username))
      for hole,score in enumerate(Score):#this program is to cound the round each
        if score<5:
          print("Round",(hole+1),":",(score),"shots.",(5-score),"under par.")
        elif score==5:
          print("Round",(hole+1),":",(score),"shots.","on par.")
        elif score>5:
          print("Round",(hole+1),":",(score),"shots.",(score-5),"over par.")
   else:
     print("Invalid menu choice!")
main()
