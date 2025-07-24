import random

#TOSS
c=0#for determining who won
d=0#for adressing that only numbers between 1 and 10 are entered
e=0#for adressing only odd and even are chosen
#making sure no error
while d==0:
    try:
        pc1=int(input("Enter your number for toss here: "))
    except:
        pc1=random.randint(1,10)
        print("Since the input provided by the player was invalid, the computer has chosen the value for you: ", pc1)
    if pc1<11 and pc1>0:
        while e==0:
            pc2_1=input("Choose whteher the sum of the numbers chosen by me and you will be odd or even:\n")
            pc2=pc2_1.lower()
            if pc2=="odd" or pc2=="even":
                cc1=random.randint(1,10)
                ds1=pc1+cc1
                #decision wheter player wins or not
                if ds1%2==0 and pc2=="even":
                    print("Congrats! You won.")
                    print("I chose", cc1)
                    c=1
                elif ds1%2!=0 and pc2=="even":
                    print("Yay! I won.")
                    print("I chose", cc1)
                elif ds1%2!=0 and pc2=="odd":
                    print("Congrats! You won.")
                    print("I chose", cc1)
                    c=1
                elif ds1%2==0 and pc2=="odd":
                    print("Yay! I won.")
                    print("I chose", cc1)
                e=1
            else:
                print("You could only between odd or even.")
                e=0
        d=1 
    else:
        print("The number can only be between 1 and 10(both of them included).")
        d=0

#Decison for balling and batting
if c==1:
    a1=0
    while a1==0:
        pc3_1=input("Batting or Balling:")
        pc3=pc3_1.lower()
        if pc3=="batting":
            cc3="balling"
            a1+=1
        elif pc3=="balling":
            cc3="batting"
            a1+=1
else:
    cc2=random.randint(1,2)
    if cc2==1:
        cc3="batting"
    else:
        cc3="balling"

print("So I'll do ", cc3) # type: ignore

#Function for battting/balling
def bat_ball(player, score):
    out=False
    try:
        pc4=int(input("Enter your number here: "))
    except:
        pc4=random.randint(1,10)
        print("Since the input provided by the player was invalid, the computer has chosen the value for you: ", pc4)
    cc4=random.randint(1,10)
    if pc4<1 or pc4>10:
        print("The number can only be between 1 and 10(both included).")
    else:
        if pc4!=cc4:
            if player=="The player":
                score+=pc4
                print(f"{player} made {str(score)}.")
                print("I chose ", cc4)
            else:
                score+=cc4
                print(f"{player} made {str(score)}.")
                print("I chose ", cc4)
        else:
            print(f"{player} is out with a score of {str(score)}.")
            print("I chose ", cc4)
            out=True
    return score, out

#THE GAME
score_player=0
score_computer=0

#if player bats first
if cc3=="balling": #type: ignore
    out1=False
    while out1==False:
        score_player, out1= bat_ball("The player", score_player)
    print(f"You made a score of {score_player}. So the computer has to make a score of {score_player+1}")

    out2=False
    while score_computer<score_player and out2==False:
        score_computer, out2 = bat_ball("The computer", score_computer)

    if out2==True:
        print(f"The computer lost by {score_player-score_computer} runs.")
    else:
        print("The player(You) lost.")

#if player balls first
elif cc3=="batting": #type: ignore
    out1=False
    while out1==False:
        score_computer, out1= bat_ball("The computer", score_computer)
    print(f"The computer made a score of {score_computer}. So you have to make a score of {score_computer+1}")

    out2=False
    while score_player<score_computer and out2==False:
        score_player, out2 = bat_ball("The player", score_player)

    if out2==True:
        print(f"You lost by {score_computer-score_player} runs.")
    else:
        print("The computer lost.")
    

#makes sure the window stays open even after the game is finished
a=0
while a==0: 
    exit=input("The game has ended. Press any key to close the program.\n")
    a+=1