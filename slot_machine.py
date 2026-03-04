from random import choice

from pycparser.c_ast import While

print("|||Wlcome to the slot machine|||\nBest place to ruin your life:>")
funds=int(input("How much money you got?: "))
print("||RULES||")
print("A|B|C\nA|A|A\nA|A|B")
print("just like above if you got one full line you will get the full bet money on the line or half for half lines")

def rng():
    list1=["A","B","C"]
    count=0
    mass=[]
    while count<3:
        list2=[]
        count+=1
        for j in range(3):
            list2.append(choice(list1))
        mass.append(list2)
    return mass
win_check=["AA","BB","CC","AAA","BBB","CCC"]
while True:
    times=int(input("Enter how many times you want to run the slot(0 to quit): "))
    bet=int(input("Enter the bet input: "))
    if times!=0:
        print("okay")
        for i in range(times):
            result=rng()
            win=False
            Half_win=False
            for k in result:
                if k[0]+k[1] not in win_check and k[0]+k[1]+k[2] not in win_check  :
                    funds-=bet
                elif k[0]+k[1]+k[2] in win_check:
                    funds+=bet
                    win=True
                elif k[0]+k[1] in win_check:
                    funds+=bet/2
                    Half_win=True

                ans = "|"
                letter=""
                for j in k:
                    letter+=j
                    ans+=f"{j}|"
                print(ans)
            if Half_win:
                print("Halfwin")
            if win:
                print("Fullwin")
            if Half_win==False and win==False:
                print("Lost money")
            print(f"Money:{funds}")
            win = False
            Half_win = False

            print("\n")













