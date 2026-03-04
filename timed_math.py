import random
oper=["+","-","*"]
minor=2
us=int(input("what difficulty you wnat this to be (10,20,40,60,80,100,1000): "))
max_prob=int(input("How many problems you want: "))
maxer=us

def gen_prob():
    left=random.randint(minor,maxer)
    right=random.randint(minor,maxer)
    opor=random.choice(oper)
    return f"{left} {opor} {right}"
for i in range(max_prob):
    prob=gen_prob()
    true_ans=eval(prob)
    while True:
        ans = int(input(f"what's the answer {prob}: "))
        if ans==true_ans:
            break
        elif ans=="giveup":
            print(true_ans)
            break
        else:
            print("wrong try again")

