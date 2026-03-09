import random
print("in this game youi will have to guess a number the computer has randomily picked\n from your chosen range.\nThe system will give you a hint if the number id closest your highest or lowest values.")
final_ranges= int(input("the range starts from 10 to(20/50/100)"))
penalty=0
rando=random.randrange(10,final_ranges+1)
user=''
while user!='end':
    cold=rando-10
    hot=final_ranges-rando
    if  cold<hot:
        print(f"closer to 10")
    else:
        print(f"closer to {final_ranges}")

    user=input("whats your giuess??: ")
    if user=="give up":
        print(f"random number=={rando}")
        break
    elif int(user)==rando:
        print("yeah you got it")
        break
    else:
        penalty+=1
        print("wrong guess")
