import re
print("write the wildest shit you can")
with open("file.txt","w+") as f:
    f.write("Yesterday, I woke up feeling extremely <adjective1>.\n" \
"I decided it was the perfect day to visit <place>, a place famous for its <adjective2> atmosphere and <plural_noun1>.\n\n" \
"As I was walking down the street, I suddenly saw a <adjective3> <animal> wearing a <clothing_item> and carrying a <object1>.\n" \
"It looked at me and said, \"Do you know where I can find the <adjective4> <plural_noun2>?\"\n\n" \
"I was so <emotion1> that I accidentally dropped my <object2>.\n" \
"The <animal> quickly picked it up and handed it back to me while <verb_ing1> loudly.\n\n" \
"Without thinking, I shouted, \"Let’s go to <place2> and fix this problem with a <adjective5> <object3>!\"\n\n" \
"So we ran as fast as we could, <verb_ing2> past <plural_noun3> and jumping over <plural_noun4>.\n" \
"When we finally arrived, a mysterious <person_type> greeted us and whispered, \"Only the <adjective6> can unlock the secret of the <noun1>.\"\n\n" \
"In the end, everything turned out <adjective7>, and I learned that even the most <adjective8> days can lead to the best <plural_noun5>.\n\n" \
"And that is how I became known as the <adjective9> hero of <place3>.")

with open("file.txt","r")as f1:
    story=f1.read()
    start_char="<"
    end_char=">"
    start_no=-1
    word_dic={}

    for index,word in enumerate(story):
        if word==start_char:
            start_no=index
        if word==end_char and start_no!=-1:
            word_dic[story[start_no:index+1]]=""
    for i in list(word_dic.keys()):
        user=input(f"describe a {i} replacement: ")
        story=story.replace(i,user)
    print(story)










