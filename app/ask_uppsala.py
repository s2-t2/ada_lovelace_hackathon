# Ada Lovelace Hackaton
# ask_uppsala.py
# Created by Group #6 on 18 of November 2017.

def ask_uppsala (input):


   if (input[-1] == '?' or input[-1] == '!'):
       input = input[:-1]

   input = input.lower()

   question = input.split(' ')
   keywords = ["uppsala", "university", "when", "founded", "was","who","history"]

   matches = 0
   info = ""

   for word in question:
       a = word
       for key in keywords:
           b = key
           if a == b:
               matches += 1
               #print ("found!")

   if (matches > 2):
       info = "Uppsala University was founded in 1447 by Swedish Swedishsson"
   else:
       info = "I don't understand try one more time"

   ## algoritmh comes here

   return info

#question = "When was Uppsala University founded ?"
#print (ask_uppsala(question))