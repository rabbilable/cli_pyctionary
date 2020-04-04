import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data.keys():
        return data[w]
    elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
        user_response = input(
            f"Did you mean \"{get_close_matches(w, data.keys())[0]}\"?. type 'Y' for yes or 'N' for no: \n").lower()
        if user_response == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        else:
            return "Word doesn't exist please double check"
    else:
        return f"Sorry the \"{w}\" doesn't exist"


word = input("Enter a word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
