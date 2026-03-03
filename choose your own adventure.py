namer=input("Name your character: ")
print("your a hero destined to kill the dragon \nbut how you choose to get their truly defines your destiny")
move=False
gate=False
chime=False
money=500
fish=False
user=input("ready to start your journey?(yes/no): ")
if user=="yes":
    print("'you left your cozy home,with only 500 runes in your pocket\nyour mother will await your return")
    print("......")
    print("your moving towards the city,Alleveria")
    print(".....")
    print("After you stumble your way through the busy market,you met an old guy\nHe senses something in you")
    print("Old guy: Oh great hero,i can sense you.\nHere take this chime i feel this could be a great use to you")
    print(namer,":but who are you")
    print("old guy:It doesn't matter my saviour ,i am just an old man in search of his duty")
    user=input("He seems suspicious, will you accept his offer?")
    if user=="yes":
        chime=True
        print("you added a chime bell to your inventory")
        print("The old man disappeared in to the crowd in the short moment you looked away")
    else:
        print("old man:it seems my time hasn't come to be use to you")
        print("he walks away with a sad face")
    print("you make your way towards the exit gate of the city,after you buy a sword and supplies from Alleveria's market")
    print("A guard stops you before yo cross the gates of the city")
    print("guard:nobody exits the city,before my approval")
    print(namer,":what should i do to get it:")
    print("guard,you need a permit")
    print(namer, "where can i apply?")
    print("old guy,you can go to the old mayors house to apply or you can slide me some 400 runes for it")
    user=input("go to mayors house or give rune(house/rune):")
    if user=="rune":
        money-=400
        print("you exited the city")
        gate=True
    else:
        print("you are on your way to the house but the guard sent some bandits your way\n and the robbed and killed you")
        print("game over")
    if gate:
        print("your on a crossway,on the left is the path towards forest\nto the right desert")
        option=input("what shall you choose(forest/dessert): ")
        if option=="forest":
            print("you have entered the forest..../nthe sound of the wind and animals surround you\nbut there is a n overwhelming sense that someone is watching you")
            print("you spot two eyes in the bushes")
            print("gathering all the courage left in you/n you decides to move the leaves hiding the eyes")
            print("it turns out to be a monkey")
            if chime:
                print("Monkey:hey can i have that chime,hanging of you backpack\n i will give you this big fish in return ")
                user=input("will you accept his offer(yes/no): ")
                if user=="yes":
                    print("you gave the monkey the chime and he gave you the big fish\nthe monkey happily ties the chime to tail and leaps to the nearby tree \nand the chime is audible all throught the forest")
                    fish=True
                else:
                    print("The monkey scratches your face and disappears into the thick forest")
            else:
                print("The monkey scratches your face and disappears into the thick forest")
            print("you continued you walk throught the forest but a angry bear jumps in front of you")










else:
    print("Game over")
