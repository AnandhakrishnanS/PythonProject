from random import choice
lib=["Y","G","R","B","O","W"]
random_order=[choice(lib) for i in range(0,4) ]
print(random_order)
check_list=[]
for i in range(0,10):
    penalty=0
    right=0
    guess=input("your guess(space spearated)").split(" ")
    if len(check_list)>0:
        for J in check_list:
            if random_order[J]!=guess[J]:
                penalty+=1
    for i in range(0,4):
        if random_order[i] in guess:
            if random_order[i]==guess[i]:
                right+=1
                check_list.append(i)


    
        

    if guess==random_order:
        print(f"congratulations you got in {i} tries!!!")
        break
    else:
        print(f"right positions: {right}|wrong pos{penalty} ")
      
    