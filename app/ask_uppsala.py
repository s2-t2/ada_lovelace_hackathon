# Ada Lovelace Hackaton
# ask_uppsala.py
# Created by Group #6 on 18 of November 2017.

def ask_uppsala (input):

    if (input[-1] == '?' or input[-1] == '!'):
        input = input[:-1]
    input = input.lower()
    question = input.split(' ')

    error_message = "Sorry, I didn't understand that! Try one more time! You can ask me about History of the University, Nations, Courses or Transportation. Or you can type '/help'"
    info = ""

    ##### CLUSTERS
    keywords_history = ["uppsala",
                        "university", "uni",
                        "history",
                        "faculties", "faculty"]
    matches_history = 0

    keywords_transport = ["train", "trains", "rtains",
                          "bus", "busses", "sub", "bbus",
                          "bicycle", "bike", "bycicle","stockholm",
                          "transport","arlanda","airport",
                          "polacksbacken","buses",
                          "student","discounts"]
    matches_transport = 0

    keywords_entertainment = ["bar", "bars", "rab",
                              "club", "clubs", "lcub",
                              "pubs","pub","bup",
                               "nation", "nations","ations",
                              "drink","drinking",
                              "beer","wine","alcohol",
                              "vodka","vkda","voldka"]
    matches_entertainment= 0

    for word in question:
        for key in keywords_history:
            if word == key:
                matches_history += 1
                #print ("found!")

        for key in keywords_transport:
            if word == key:
                matches_transport += 1
                #print ("found!")

        for key in keywords_entertainment:
            if word == key:
                matches_entertainment += 1
                #print ("found!")

    # COMPARE COUNTER AND SEND TO RIGHT CLUSTER
    if (matches_history >= 2):
        info = ask_history(question)
    elif (matches_transport >= 2):
        info = ask_transport(question)
    elif (matches_entertainment >= 2):
        info = ask_entertainment(question)
    else:
        return error_message

    return info

def ask_history(question):
    #info = "THIS QUESTION IS ABOUT HISTORY OF UPPSALA UNIVERSITY"

    ##### QUESTIONS
    # When/Who founded UU?
    keywords_q1 = ["who", "when", "how", "old", "founded", "foundation", "born"]
    matches_q1 = 0

    # How many students attend UU?
    keywords_q2 = ["how", "many", "attend","currently" "students", "alumni", "pupils"]
    matches_q2 = 0

    # Who is the Dean at UU?
    keywords_q3 = ["who", "dean", "at"]
    matches_q3 = 0

    # How many faculties does the university has?
    keywords_q4 = ["how", "many", "faculties", "faculty"]
    matches_q4 = 0

    # Who was the first female student at UU?
    keywords_q5 = ["who", "was", "first", "female", "student", "sweden"]
    matches_q5 = 0

    for word in question:
        for key in keywords_q1:
            if word == key:
                matches_q1 += 1

        for key in keywords_q2:
            if word == key:
                matches_q2 += 1

        for key in keywords_q3:
            if word == key:
                matches_q3 += 1

        for key in keywords_q4:
            if word == key:
                matches_q4 += 1

        for key in keywords_q5:
            if word == key:
                matches_q5 += 1

    # ANSWERS

    error_message = "Sorry, I didn't understand that! Try one more time! You can ask me about History of the University, Nations, Courses or Transportation. Or you can type '/help'"
    answer_1 = "Uppsala University was founded in 1477 by Jakob Ulvsson"
    answer_2 = "Currently there are "
    answer_3 = "Answer 3"
    answer_4 = "Answer 4"
    answer_5 = "Answer 5"

    # COMPARE COUNTER AND SEND TO RIGHT CLUSTER
    if (matches_q1 >= 2):
        info = answer_1
    elif (matches_q2 >= 2):
        info = answer_2
    elif (matches_q3 >= 2):
        info = answer_3
    elif (matches_q4 >= 2):
        info = answer_4
    elif (matches_q5 >= 2):
        info = answer_5
    else:
        return error_message

    return info

def ask_transport(question):
    info = "THIS QUESTION IS ABOUT TRANSPORT"

    ##### QUESTIONS
    # How much is the train to stockholm
    keywords_q1 = ["how", "much", "train","trains", "stockholm","to"]
    matches_q1 = 0

    # How much is monthly subscription for UL card
    keywords_q2 = ["ul", "card" "how", "monthly","subscription"]
    matches_q2 = 0

    # how far is arlanda airport
    keywords_q3 = ["how","far","arlanda","airport"]
    matches_q3 = 0

    # buses to polacksbacken
    keywords_q4 = ["bus", "buses", "polacksbacken", "to"]
    matches_q4 = 0

    # are there student discounts for transportation
    keywords_q5 = ["student", "discounts", "transportation", "are"]
    matches_q5 = 0

    for word in question:
        for key in keywords_q1:
            if word == key:
                matches_q1 += 1

        for key in keywords_q2:
            if word == key:
                matches_q2 += 1

        for key in keywords_q3:
            if word == key:
                matches_q3 += 1

        for key in keywords_q4:
            if word == key:
                matches_q4 += 1

        for key in keywords_q5:
            if word == key:
                matches_q5 += 1

    # ANSWERS

    error_message = "Sorry, I didn't understand that! Try one more time! You can ask me about History of the University, Nations, Courses or Transportation. Or you can type '/help'"
    answer_1 = "Ticket to Stockholm is 120 SEK"
    answer_2 = "The monthly subscription for UL card is 550 SEK."
    answer_3 = "Arlanda airport is 27.21 kilometers"
    answer_4 = "Bus no. 4 and Bus no. 21 comes from Uppsala Central Station to Polacksbacken"
    answer_5 = "There are student discounts available for Transportation cards."

    # COMPARE COUNTER AND SEND TO RIGHT CLUSTER
    if (matches_q1 >= 2):
        info = answer_1
    elif (matches_q2 >= 2):
        info = answer_2
    elif (matches_q3 >= 2):
        info = answer_3
    elif (matches_q4 >= 2):
        info = answer_4
    elif (matches_q5 >= 2):
        info = answer_5
    else:
        return error_message

    return info

def ask_entertainment(question):
    info = "THIS QUESTION IS ABOUT ENTERTAINMENT"

    ##### QUESTIONS
    # When/Who founded UU?
    keywords_q1 = ["who", "when", "how", "old", "founded", "foundation", "born"]
    matches_q1 = 0

    # How many students attend UU?
    keywords_q2 = ["how", "many", "attend", "currently" "students", "alumni", "pupils"]
    matches_q2 = 0

    # Who is the Dean at UU?
    keywords_q3 = ["who", "dean", "at"]
    matches_q3 = 0

    # How many faculties does the university has?
    keywords_q4 = ["how", "many", "faculties", "faculty"]
    matches_q4 = 0

    # Who was the first female student at UU?
    keywords_q5 = ["who", "was", "first", "female", "student", "sweden"]
    matches_q5 = 0

    for word in question:
        for key in keywords_q1:
            if word == key:
                matches_q1 += 1

        for key in keywords_q2:
            if word == key:
                matches_q2 += 1

        for key in keywords_q3:
            if word == key:
                matches_q3 += 1

        for key in keywords_q4:
            if word == key:
                matches_q4 += 1

        for key in keywords_q5:
            if word == key:
                matches_q5 += 1

    # ANSWERS

    error_message = "Sorry, I didn't understand that! Try one more time! You can ask me about History of the University, Nations, Courses or Transportation. Or you can type '/help'"
    answer_1 = "Uppsala University was founded in 1477 by Jakob Ulvsson"
    answer_2 = "Currently there are "
    answer_3 = "Answer 3"
    answer_4 = "Answer 4"
    answer_5 = "Answer 5"

    # COMPARE COUNTER AND SEND TO RIGHT CLUSTER
    if (matches_q1 >= 2):
        info = answer_1
    elif (matches_q2 >= 2):
        info = answer_2
    elif (matches_q3 >= 2):
        info = answer_3
    elif (matches_q4 >= 2):
        info = answer_4
    elif (matches_q5 >= 2):
        info = answer_5
    else:
        return error_message

    return info


question = "Are there student discounts on transportation?"
print (ask_uppsala(question))