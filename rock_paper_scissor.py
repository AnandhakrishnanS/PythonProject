from random import choice
picker=["siss","rock","paper"]
user=''
points=0
com_points=0
while user!="end":
    ops=choice(picker)
    user=input(f"pick from (siss/rock/paper): ")
    if user=="siss":
        if ops=="paper":
            points+=1
            print(f"com:{ops}\nplayer:{user}\nyou got a point")
        elif ops=="rock":
            com_points += 1
            print(f"com:{ops}\nplayer:{user}\ncomputer got a point")
        elif ops=="siss":
            print(f"com:{ops}\nplayer:{user}\nno points")

    elif user=="rock":
        if ops=="paper":
            com_points += 1
            print(f"com:{ops}\nplayer:{user}\ncomputer got a point")
        elif ops=="rock":
            print(f"com:{ops}\nplayer:{user}\nno points")
        elif ops=="siss":
            points+=1
            print(f"com:{ops}\nplayer:{user}\nyou got a point")

    elif user=="paper":
        if ops=="paper":
            print(f"com:{ops}\nplayer:{user}\nno points")
        elif ops=="rock":
            points+=1
            print(f"com:{ops}\nplayer:{user}\nyou got a point")
        elif ops=="siss":
            com_points += 1
            print(f"com:{ops}\nplayer:{user}\ncomputer got a point")
    elif user=="end":
        print(f"current player points: {points}\ncomputer points: {com_points}")
        if com_points>points:
            print("computer won")
        else:
            print("player won")


