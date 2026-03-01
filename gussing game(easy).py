question_bank = {

    "What is the capital of France?": "Paris",

    "What is the largest planet in our solar system?": "Jupiter",

    "Who developed the theory of relativity?": "Albert Einstein",

    "What is the smallest prime number?": "2",

    "Which ocean is the largest?": "Pacific Ocean",

    "Who is known as the father of computers?": "Charles Babbage",

    "What is the chemical symbol for gold?": "Au",

    "Which country has the largest population?": "India",

    "What is the square root of 144?": "12",

    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",

    "What is the fastest land animal?": "Cheetah",

    "Which planet is known as the Red Planet?": "Mars",

    "What is the currency of Japan?": "Yen",

    "How many continents are there?": "7",

    "What gas do plants absorb from the atmosphere?": "Carbon dioxide",

    "Who discovered gravity?": "Isaac Newton",

    "What is the boiling point of water in Celsius?": "100",

    "Which is the longest river in the world?": "Nile",

    "What is the capital of India?": "New Delhi",

    "Which element has atomic number 1?": "Hydrogen",

    "What is the largest mammal?": "Blue whale",

    "Which language is used to create web pages?": "HTML",

    "What is the hardest natural substance?": "Diamond",

    "Who was the first man to walk on the Moon?": "Neil Armstrong",

    "Which country invented paper?": "China",

    "What is the national animal of India?": "Tiger",

    "What is the freezing point of water in Celsius?": "0",

    "Which organ pumps blood in the human body?": "Heart",

    "Which planet has rings?": "Saturn",

    "What is the tallest mountain in the world?": "Mount Everest",

    "What does CPU stand for?": "Central Processing Unit",

    "Which is the largest desert in the world?": "Sahara Desert",

    "What is the capital of the United Kingdom?": "London",

    "Who invented the telephone?": "Alexander Graham Bell",

    "Which vitamin is produced by sunlight?": "Vitamin D",

    "What is the national bird of India?": "Peacock",

    "How many days are there in a leap year?": "366",

    "Which blood cells fight infection?": "White blood cells",

    "What is the capital of Australia?": "Canberra",

    "Which instrument measures temperature?": "Thermometer",

    "What is the speed of light?": "299,792,458 meters per second",

    "Which is the smallest continent?": "Australia",

    "Who painted the Mona Lisa?": "Leonardo da Vinci",

    "What is the main gas in Earth's atmosphere?": "Nitrogen",

    "Which planet is closest to the Sun?": "Mercury",

    "What is the national sport of India?": "Hockey",

    "How many bones are in the human body?": "206",

    "Which is the largest organ in the human body?": "Skin",

    "What does RAM stand for?": "Random Access Memory",

    "Which country is famous for the Eiffel Tower?": "France"

}

from random import choice
user=''
counter=0
points=0
while user!="end":
    question=choice(list(question_bank.keys()))
    user=input(f"q{counter} . {question} ?")
    counter+=1
    if user==question_bank[question]:
        print("gained a point!!!")
        points+=1
    elif user=="end":
        print("Thankyou for playing")
    else:
        if points>0:
            points-=1
            print("lost a point :<")
print(points)

