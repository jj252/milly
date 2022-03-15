from milly_pkg import operations

def question_1(options,Question_,question_index,worth):
    print("  === Who Wants to be a Millionaire ===   ")
    print('$' + str(float(question_index[worth])) + ' Question')
    print(Question_.mainQuest)
    print("------------------------------------------")
    print("| A-"+ Question_.option1 +"   | B-"+Question_.option2+"|")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| C-"+ Question_.option3 +"   | D-"+Question_.option4+"|")
    print("------------------------------------------")
    print("|           E-Phone A Friend             |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("|           F-    50/50                  |")
    print("------------------------------------------")
    print("|           G-  Walk Away                |")
    print("------------------------------------------")
    while True:
        validate_question = input('Enter Your Choice: ')
        if validate_question.lower() == Question_.right:
            print('Correct!')
            
            options[0] += 1
            #print(question_index[options[0]])
            return options
        elif validate_question.lower() == 'e' and options[1] == False:
            print('The Answer is',Question_.phone)
            options[1] = True
        elif validate_question.lower() == 'e' and options[1] == True:
            print('Phone A Friend has been Used Already')
        elif validate_question.lower() == 'f' and options[2] == False:
            options[2] = True
            if Question_.right == 'a':
                Question_.option2 = '               '
                Question_.option4 = '               '
            elif Question_.right == 'b':
                Question_.option1 = '               '
                Question_.option4 = '               '
            elif Question_.right == 'c':
                Question_.option1 = '               '
                Question_.option2 = '               '
            elif Question_.right == 'd':
                Question_.option2 = '               '
                Question_.option3 = '               '

            operations.question_1(Question_)
        elif validate_question.lower() == 'f' and options[2] == True:
            print('50/50 has been Used Already')

        elif validate_question.lower() == 'g':
            options[3] = False
            options[4] = True
            return options

        elif validate_question.isdigit():
            print('You cannot enter a number')

        elif not(validate_question.lower() == 'a' or validate_question.lower() == 'b' or validate_question.lower() == 'c' or validate_question.lower() == 'd' or validate_question.lower() == 'e' or validate_question.lower() == 'f'or validate_question.lower() == 'g'):
            print('You must enter a character from A-G')
            
        else:
            print('Incorrect!')
            options[3] = False
            
            return options

