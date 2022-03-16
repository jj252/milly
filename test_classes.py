import pytest
'''
class Person:
    def __init__(self, name):
        self.name = name

def test_classes_compare():
    p1 = Person("Mindy")
    p2 = Person("Mindy")
    assert p1 == p2'''

question_list = { "question1": "In 1768 Captain James Cook set out to explore which ocean?",
           "question2": "Who was elected President of the United States in 2016"
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

def test_classes_compare():
    Question_1 = Question(question_list['question1'],'Pacific Ocean  ','Atlantic Ocean ','Indian Ocean   ','Arctic Ocean   ','a','a')
    Question_2 = Question(question_list['question2'],'Barack Obama   ','George Bush    ','Donald Trump   ','Bill Clinton   ','c','c')

    assert Question_1 != Question_2

def test_classes_compare2():
    Question_1 = Question(question_list['question1'],'Pacific Ocean  ','Atlantic Ocean ','Indian Ocean   ','Arctic Ocean   ','a','a')
    Question_2 = Question(question_list['question2'],'Barack Obama   ','George Bush    ','Donald Trump   ','Bill Clinton   ','c','c')

    assert Question_1 == Question_2