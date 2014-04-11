import random
f=open("highScore.txt","r+")
high=f.read()
highScore=int(high)
print "Coin Guessing Game.    All time high score:", highScore, "corrects"
myScore=0
while True:
    coin=random.randint(0,1)
    guess=raw_input("Predict heads or tails")
    if guess=="Heads" and coin==0:
        myScore=myScore+1
        print "It is heads.  Your score is:", myScore
    if guess=="Heads" and coin==1:
        print "It is tails.  Game Over"
        break
    if guess=="Tails" and coin==0:
        print "It is tails.  Game Over"
        break
    if guess=="Tails" and coin==1:
        myScore=myScore+1
        print "It is tails.  Your score is:", myScore
if highScore<myScore:
    highScore=myScore
print "Your Score:", myScore, "   High Score:", highScore
f.seek(0)
f.truncate()
f.write(str(highScore))
