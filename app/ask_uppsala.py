# Ada Lovelace Hackaton 
# ask_uppsala.py
# Created by Group #6 on 18 of November 2017.

def ask_uppsala(input):
    count = 0
    info = ""

    inputList = input.split(' ')
    print(inputList)
    keywords = ["Uppsala",
                "University",
                "found", "founded", "when", "who", "UU", "city", "Tell", "nation",
                "student nation", "courses", "programme", "what"]

    for inpWord in inputList:
        check = inpWord
        #print(check)
        for word in keywords:
            if check == word:
                count = count +1
                print(count)


    print (count)
    if count >= 3 :
        info = "UU was founded in 1447"

    ## algoritmh comes here
    return info


ques = "When was University founded?"
print (ask_uppsala(ques))
