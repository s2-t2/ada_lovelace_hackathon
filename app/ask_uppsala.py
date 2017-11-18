# Ada Lovelace Hackaton
# ask_uppsala.py
# Created by Group #6 on 18 of November 2017.

def ask_uppsala (input):

   input.lower()

   question = input.split(' ')
   keywords = ["Uppsala", "University", "when", "founded", "was"]

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
       info = "Uppsala University was founded in 1447"

   ## algoritmh comes here

   return info

#question = "When was Uppsala University founded ?"

#print (ask_uppsala(question))