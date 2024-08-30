questions=[
      [
         "Current Railway Minister of India is","Mamta Banarjee","Ram Vilash","Ashwini Vaishnaw","Piyush Goyal",3
      ],
      [
          "Which god is also known as ‘Gauri Nandan’?","Agni","Indra","Hanuman","Ganesha",4
      ],
      [
          "What does not grow on tree according to a popular Hindi saying?","Money","Flowers","Leaves","Fruits",1
      ],
      [
          "Which city is known as the Pink City of India?","Banglore","Maysore","Jaipur","Kochi",3
      ],
      [
          "Who wrote India's National Anthem?","Rabindranath Tagore","Lal Bahadur Shastri","Chetan Bhagat","RK Narayan",1
      ],
      [
          "How many major religions are there in India?","6","7","8","9",1
      ],
      [
          "When is the National Hindi Diwas celebrated?","13 September","14 September","14 July","15 August",2
        
      ],
      [
          "How many states are there in India?","28","29","30","31",1
      ],
      [
          "Where is India Gate located?","Agra","Punjab","Mumbai","New Delhi",3
      ],
      [
          "Who wrote Vande Mataram?","Sarat Chandra Chattopadhyay","Rabindranath Tagore","Bankim Chandra Chatterjee","Ishwar Chandra Vidyasagar",3
      ],
      [
          "Which one of the following places is famous for the Great Vishnu Temple?","Bordubar, Indonesia","Bamiyan, Afghanistan","Panja Sahib, Pakistan","Ankorvat, Cambodia",4
      ],
      [
          "Where is the largest Buddhist Monastery in India located?","Sarnath, Uttar Pradesh","Tawang, Arunachal Pradesh","Tawang, Arunachal Pradesh","Gangtok, Sikkim",2
      ],
      [
          "Which Indian monument was originally built as a victory tower to commemorate the defeat of the Khan of Khambhat?","Qutub Minar","India Gate ","Charminar","Vijay Stambha",4
      ],
      [
        "Which ancient civilization is credited with the invention of the first known writing system, cuneiform?","Egyptians","Greeks","Sumerians","Romans",3
      ],
      [
          "Which of the following administrative innovations during the Mughal Empire had the most significant long-term impact on the empire's revenue collection system?","Introduction of the Mansabdari system","Establishment of the Jagirdari system","Implementation of Akbar's Dahsala system","Creation of the Diwan-i-Arz",3
      ]
    
]
level=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
money=0
for i in range(0,13):
    print(f"QUESTION FOR RS.{level[i]} \n \n")
    question=questions[i]
    print(question[0])
    print(f"A.{question[1]}                                  B.{question[2]}")
    print(f"C.{question[3]}                                  D.{question[4]}")
    choice=input("WANT TO QUIT OR ANSWER: ")
    choice=choice.lower()
    if(choice=="quit"):
        money=level[i-1]
        break
    else:
        ans=input("ENTER YOUR ANSWER: ")
        ans=ans.lower()
        answer=ord(ans)-ord('a')+1
        if(answer==question[-1]):
            print("CORRECT ANSWER")
            print(f"YOU WON RS.{level[i]}")
            if(i==4 or i==9):
                money=level[i]
        else:
            print("WRONG ANSWER")
            break
print(f"YOU ARE GOING HOME WITH RS.{money}")


