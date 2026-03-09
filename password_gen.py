import random,string
def gen_pass(length,num=True,sepcial=True):
    letters=string.ascii_letters
    digit=string.digits
    spe=string.punctuation
    pool=letters
    if num:
        pool+=digit
    if sepcial:
        pool+=spe
    pwd=""
    for i in range(length):
        pwd+=random.choice(pool)
    return pwd
print(gen_pass(10))
