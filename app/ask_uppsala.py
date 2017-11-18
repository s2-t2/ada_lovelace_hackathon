# Ada Lovelace Hackaton 
# ask_uppsala.py
# Created by Group #6 on 18 of November 2017.

count = 0;


def ask_uppsala (input):
    inputList = input.split(',')
    print(inputList)
    keywords = ["Uppsala","University","found" ,"founded","when","who","UU","city","Tell","nation","student nation","courses","programme","what"]

    for inpWord in inputList :
        check = inpWord
        print(check)
        for word in keywords:
            if check == word :
                print (word)
    info = ""

    ## algoritmh comes here



    return ""

ques = "When was University founded?"
ask_uppsala(ques)
