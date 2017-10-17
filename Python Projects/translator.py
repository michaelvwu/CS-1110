# Michael Wu (mvw5mf)
#working with dictionaries

dictionary = {'hello': 'ahoy','help': 'argh'}

phrase = input("what do you want to translate?: ")
phrase_list = phrase.split(' ')

translated_phrase = ""

for word in phrase_list:
    translated_phrase += dictionary[word] + " "

print(translated_phrase)

# print(dictionary.get(phrase, "I don't know that word"))