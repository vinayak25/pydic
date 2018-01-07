import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0: 
        yn = input("Did you mean %s instead? Enter Y if Yes , or N if No: " % get_close_matches(word,data.keys())[0])
        yn = yn.lower()
        if yn=="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn=="n":
            return "Word does not exist. Please double check it."
        else:
            return "We didn't understand your entry."

    else:
        return "Word does not exist. Please double check it."

word = input("Enter a word: ")
output_list = translate(word)
if type(output_list) == list:
    for item in output_list:
        print(item)
else:
    print(output_list)