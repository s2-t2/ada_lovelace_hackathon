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
                       "history"]
   matches_history = 0

   keywords_transport = ["train", "trains", "rtains",
                         "bus", "busses", "sub", "bbus",
                         "bicycle", "bike", "bycicle"]
   matches_transport = 0

   keywords_entertainment = ["bar", "bars", "rab",
                             "club", "clubs", "lcub",
                             "pubs","pub","bup",
                              "nation", "nations","ations"]
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

   if (matches_history > 3):
       info = ask_history(question)
   elif (matches_transport > 3):
       info = ask_transport(question)
   elif (matches_entertainment > 3):
       info = ask_entertainment(question)
   else:
       return error_message

   return info

def ask_history(input):
   info = "THIS QUESTION IS ABOUT HISTORY"

   # info = "Uppsala University was founded in 1447 by Swedish Swedishsson"

   return info

def ask_transport(input):
   info = "THIS QUESTION IS ABOUT TRANSPORT"

   return info

def ask_entertainment(input):
   info = "THIS QUESTION IS ABOUT ENTERTAINMENT"

   return info


#question = "When was Uppsala University founded ?"
#print (ask_uppsala(question))