# In this we will make a program that is capable of showing questions like KBC to the users

print('''Welcome to
      KON BANEGA CROREPATI''')
print("Let's see the First Question!!")

questions = [ 
                [
                    "What is the capital of France?","Germany", "Italy", "Paris", "Laos", 3
                    ],
                [
                    "Who wrote the play \"Romeo and Juliet\"?", "James Chadvick", "William Shakespeare", "Williamson", "Jonty Rhodes", 2
                    ],
                [
                    "What is the largest planet in our solar system?", "Jupiter", " Neptune", "Uranus", "Saturn", 1
                    ],
                [
                    "Which country is known as the Land of the Rising Sun?", "China", "Japan", "Nepal", "India", 2
                    ],
                [
                    "In which year did the Titanic sink?", 1909, 1910, 1911, 1912, 4
                    ],
                ["What is the capital of Italy?","Madrid", "Rome", "Paris", "Berlin", 2
                ],
                ["Which gas do plants primarily absorb during photosynthesis?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen", 2
                ],

                ["What is the largest ocean on Earth?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", 4
                ],
                ["Who discovered penicillin?", "Marie Curie", "Alexander Fleming", "Louis Pasteur", "Thomas Edison", 2
                ],
                ["What is the hardest natural substance on Earth?", "Gold", "Diamond", "Iron", "Quartz", 2
                ],
                ["In which continent is the Sahara Desert located?", "Asia", "North America", "Africa", "Australia", 3
                ],
                ["Which planet is known as the Red Planet?", "Venus", "Mars", "Jupiter", "Mercury", 2
                ],
                ["What is the primary ingredient in guacamole?", "Tomato", "Avocado", "Pepper", "Onion", 2
                ],
                ["Which Shakespeare play features the characters Oberon and Titania?", "Hamlet", "Macbeth", "A Midsummer Night's Dream", "Othello",3
                ],
                ["Which country is known for the Great Wall?", "India", "China", "Japan", "Mongolia", 2
                ],
                ]
levels = [10000, 20000, 40000, 60000, 80000, 100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
money = 0

for i in range(0, len(questions)):
    question= questions[i]
    print(f"\n\nThe question for Rs. {levels[i]}")
    
    print(f" {question[0]}    1. {question[1]}        2. {question[2]}")
    print(f" 3. {question[3]}          4. {question[4]}")
    
    answer = int(input("Enter the answer: "))
    if answer == question[-1]:
        print(f"Correct Answer!! You won Rs. {levels[i]} ")
        
        if i == 4:     #it means after 4th level Rs. 40000 will be given if user gets out 
            money=40000
        
        elif i==9:    #it means after 9th level Rs. 300000 if he gets out after 9 th question
            money = 300000
        
        elif i==14:
            money = 1000000
    else:
        print("Wrong Answer!!")
        break
    
print(f"You will take {money} into your home..")


  


     
