from milly_pkg import questions
from milly_pkg import operations

operations.start_menu()
#0-Earnings,1-Phone_Life_Line,2-50/50_Life_Line,3-gameplay_status,4-walk_away
options = [0,False,False,True,False]
question_index = [0,100,200,300,500,1000,2000,4000,8000,16000,32000,64000,125000,250000,500000,1000000]
worth = 1




question_list = { "question1": "In 1768 Captain James Cook set out to explore which ocean?",
           "question2": "Who was elected President of the United States in 2016",
           "question3": "Which city is the home of Batman?",
           "question4": "Which of the following ingredients is not normally used to brew beer?",
           "question5": "Substances that have a definite size and shape, and vibrating particles that are close together are?",
           "question6": "What is the most densely populated U.S. state?",
           "question7": "Albert Einstein was a scientist famous for his work on physics. Where was he born?",
           "question8": "How fast can an ostrich run?",
           "question9": "Balanced forces act on objects that are?",
           "question10": "Which Caribbean island has the greatest area?",
           "question11": "Zulia is a province of which country?",
           "question12": "Which state of the U.S. has recorded the fastest surface wind?",
           "question13": "How much of your vision do you lose if you go blind in one eye?",
           "question14": "Goulash is a beef soup associated with this nation?",
           "question15": "The jelly-like substance that makes up most of a cell is the?",
           }

class Question:
    def __init__(self, mainQuest, optiona, optionb,optionc,optiond,right,phone):
        self.mainQuest = mainQuest
        self.option1 = optiona
        self.option2 = optionb
        self.option3 = optionc
        self.option4 = optiond
        self.right = right
        self.phone = phone


Question_1 = Question(question_list['question1'],'Pacific Ocean  ','Atlantic Ocean ','Indian Ocean   ','Arctic Ocean   ','a','a')
Question_2 = Question(question_list['question2'],'Barack Obama   ','George Bush    ','Donald Trump   ','Bill Clinton   ','c','c')
Question_3 = Question(question_list['question3'],'Las Vegas      ','Los Angelos    ','Califonia      ','Gotham City    ','d','d')
Question_4 = Question(question_list['question4'],'Hops           ','Yeast          ','Malt           ','Vinegar        ','d','d')
Question_5 = Question(question_list['question5'],'Liquids        ','Gases          ','Solids         ','None           ','c','c')
Question_6 = Question(question_list['question6'],'Connecticut    ','New Jersey     ','Rhode Island   ','Maryland       ','b','b')
Question_7 = Question(question_list['question7'],'Germany        ','United States  ','France         ','Canada         ','a','a')
Question_8 = Question(question_list['question8'],'25 km/hr       ','50 km/hr       ','65 km/hr       ','165 km/hr      ','c','c')
Question_9 = Question(question_list['question9'],'Stationary     ','In motion      ','Rising         ','falling        ','c','d')
Question_10= Question(question_list['question10'],'Jamaica       ','Cuba           ','Puerto Rico    ','Hispanola      ','b','b')
Question_11= Question(question_list['question11'],'Colombia      ','Brazil         ','Venezuela      ','Ecuador        ','c','a')
Question_12= Question(question_list['question12'],'Illinois      ','New Hampshire  ','Montana        ','Alaska         ','b','b')
Question_13= Question(question_list['question13'],'10 percent    ','20 percent     ','35 percent     ','50 percent     ','b','a')
Question_14= Question(question_list['question14'],'Morocco       ','Greece         ','Israel         ','Hungary        ','d','d')
Question_15= Question(question_list['question15'],'Cytoplasm     ','Nucleus        ','Chloroplast    ','None           ','a','d')
#player2 = Question('Aaron,1200',1300)

while True:
    option_to_validate = input('Enter Option: ')
    if option_to_validate == '1':
        print('Loading Game')
        break
    else:
        print('Invalid option!')

for x in range(1, 17):
    #area_func = globals()[question_index + str(x)]
    #area_func = globals()[question_index + str(x)]
    #area_func()
    if x == 1 and options[0] == 0:
        options = questions.question_1(options,Question_1,question_index,worth)
        if options[3] == True:
            print('Your have earned: $' + str(float(question_index[worth])))
            worth +=1
        
    elif x == 2 and question_index[options[0]] == 100:
        options = questions.question_1(options,Question_2,question_index,worth)
        
        if options[3] == True:
            print('Your have earned: $' + str(float(question_index[worth])))
            worth +=1
    elif x == 3 and question_index[options[0]] == 200:
        options = questions.question_1(options,Question_3,question_index,worth)
        
        if options[3] == True:
            print('Your have earned: $' + str(float(question_index[worth])))
            worth +=1
    elif x == 4 and question_index[options[0]] == 300:
        options = questions.question_1(options,Question_4,question_index,worth)
        
        if options[3] == True:
            print('Your have earned: $' + str(float(question_index[worth])))
            worth +=1
    elif x == 5 and question_index[options[0]] == 500:
        options = questions.question_1(options,Question_5,question_index,worth)
        
        if options[3] == True:
            print('Your have earned: $' + str(float(question_index[worth])))
            worth +=1
    elif x == 6 and question_index[options[0]] == 1000:
        options = questions.question_1(options,Question_6,question_index,worth)
        
        if options[3] == True:
            print('Your have earned: $' + str(float(question_index[worth])))
            worth +=1
    elif x == 7 and question_index[options[0]] == 2000:
        options = questions.question_1(options,Question_7,question_index,worth)
        
        if options[3] == True:
            print('Your have earned: $' + str(float(question_index[worth])))
            worth +=1
    elif x == 8 and question_index[options[0]] == 4000:
        options = questions.question_1(options,Question_8,question_index,worth)
        
        if options[3] == True:
            print('Your have earned: $' + str(float(question_index[worth])))
            worth +=1
    elif x == 9 and question_index[options[0]] == 8000:
        options = questions.question_1(options,Question_9,question_index,worth)
        
        if options[3] == True:
            print('Your have earned: $' + str(float(question_index[worth])))
            worth +=1
    elif x == 10 and question_index[options[0]] == 16000:
        options = questions.question_1(options,Question_10,question_index,worth)
        
        if options[3] == True:
            print('Your have earned: $' + str(float(question_index[worth])))
            worth +=1
    elif x == 11 and question_index[options[0]] == 32000:
        options = questions.question_1(options,Question_11,question_index,worth)
        
        if options[3] == True:
            print('Your have earned: $' + str(float(question_index[worth])))
            worth +=1
    elif x == 12 and question_index[options[0]] == 64000:
        options = questions.question_1(options,Question_12,question_index,worth)
        
        if options[3] == True:
            print('Your have earned: $' + str(float(question_index[worth])))
            worth +=1
    elif x == 13 and question_index[options[0]] == 125000:
        options = questions.question_1(options,Question_13,question_index,worth)
        
        if options[3] == True:
            print('Your have earned: $' + str(float(question_index[worth])))
            worth +=1
    elif x == 14 and question_index[options[0]] == 250000:
        options = questions.question_1(options,Question_14,question_index,worth)
        
        if options[3] == True:
            print('Your have earned: $' + str(float(question_index[worth])))
            worth +=1
    elif x == 15 and question_index[options[0]] == 500000:
        options = questions.question_1(options,Question_15,question_index,worth)

        if options[3] == True:
            print('Your have earned: $' + str(float(question_index[worth])))
            worth +=1
    elif x == 16 and question_index[options[0]] == 1000000:
        operations.winner()
        break
    else:
        if question_index[options[0]] < 1000 and options[4] == False:
            print('Your have earned: $0.0')

        elif question_index[options[0]] >= 1000 and question_index[options[0]] < 32000 and options[4] == False:
            print('Your have earned: $1000.0')

        elif question_index[options[0]] >= 32000 and question_index[options[0]] < 1000000 and options[4] == False:
            print('Your have earned: $32000.0')

        elif options[4] == True:
            print('Your have earned $' + str(float(question_index[options[0]])))

        print('Thank You for Playing!')
        break
      