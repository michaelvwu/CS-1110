# Michael Wu (mvw5mf)

def load_spelling_file(filename):
    correct_spelling = {}
    misspelling = {}

    datafile = open(filename, "r")
    for line in datafile:
        line = line.split(",")
        correct_spelling[line[1].strip()] = line[0]
        misspelling[line[0]] = line[1].strip()

    return correct_spelling, misspelling

correct_spelling, misspelling = load_spelling_file("misspellings.csv")
done = False
while not done:
    word = input("Please enter a word (END to quit): ")
    if word == "END":
        done = True
        break
    if word in correct_spelling:
        print("The word '", word, "' is spelled correctly!")
    elif word in misspelling:
        print("I think that '", word, "' is spelled", misspelling[word])
    else:
        print("I don't know that word.  Sorry!")