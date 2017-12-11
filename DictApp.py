"""difflib is a library to compare text
Methods of difflib:
    > sequencematcher
    > get_close_matches
Assignment: read a json file and make a dictionary using python
Features:
1) Python ask user to enter a word
2) If word is available in dictionary (json file) python will show meaning of word
3) If you type something closer to the word available in dictionary, it will give you closest match to the word
and will show the meaning of the word
4) capitalize the noun/pronoun entered by user.
  """
import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
data = json.load(open("data.json","r")) #returns a dictionary in the form of key and value
def dictionary(word):
    word = word.lower() #since all data in json present in lower case. We convert all user input into lower case
    if word in data: #check key in dictionary. If this is true
        return data[word]
    elif word.title() in data: #capitalize the word. example "california" to "California"
        return data[word.title()]
    elif word.Upper() in data:
        return data[word.Upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        yn = input("Did you mean %s instead? Enter Y for yes and N for no: "% get_close_matches(word,data.keys())[0])
        if yn is "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn is "N":
            return "%s doesn't exit in dictionary"% word
        else:
            return "You were asked to enter Y or N"
    else:
        return "%s is not present in dictionary"%word
word = input("Enter a word to check the meaning: ")
#print(dictionary(word))  this will print a List
output = dictionary(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print (output)
