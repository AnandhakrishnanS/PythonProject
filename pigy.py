from random import choice

players={}

while True:
    player_name=input("enter the name of player: ")
    if player_name!="quite":
        players[player_name] = 0
    else:
        break
rng=[1,20,50,30,3,5,6,8,2]
winner=""
cont="c"
while cont=="c":
    lucky=choice(list(players.keys()))
    times=int(input(f"how many times{lucky} wanna role: "))
    for i in range(0,times):
        point=choice(rng)
        print(point)
        print(f"{lucky} points: {players[lucky]}")
        if point==1:
            if players[lucky]!=0:
                players[lucky]=0
        else:
            players[lucky]+=point
    for player,score in players.items():
        if score>=100:
            winner=player
            cont="f"
print(f"{winner} won with a score of {players[winner]}")






