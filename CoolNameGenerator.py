import random, string

letter_input_1 = input('Choose a letter..."v" for vowels, "c" for consonants "l" for any other letter')
letter_input_2 = input('Choose a letter..."v" for vowels, "c" for consonants "l" for any other letter')
letter_input_3 = input('Choose a letter..."v" for vowels, "c" for consonants "l" for any other letter')
letter_input_4 = input('Choose a letter..."v" for vowels, "c" for consonants "l" for any other letter')
letter_input_5 = input('Choose a letter..."v" for vowels, "c" for consonants "l" for any other letter')
letter_input_6 = input('Choose a letter..."v" for vowels, "c" for consonants "l" for any other letter')
letter_input_7 = input('Choose a letter..."v" for vowels, "c" for consonants "l" for any other letter')


vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'
letter = string.ascii_lowercase


def generator():
    if letter_input_1 == "v":
        letter1 =random.choice(vowels)
    elif letter_input_1 == "c":
        letter1 = random.choice(consonants)
    elif letter_input_1 == "l":
        letter1 = random.choice(letter)
    else:
        letter1 = letter_input_1 

    if letter_input_2 == "v":
        letter2 =random.choice(vowels)
    elif letter_input_2 == "c":
        letter2 = random.choice(consonants)
    elif letter_input_2 == "l":
        letter2 = random.choice(letter)
    else:
        letter2 = letter_input_2

    if letter_input_3 == "v":
        letter3 =random.choice(vowels)
    elif letter_input_3 == "c":
        letter3 = random.choice(consonants)
    elif letter_input_3 == "l":
        letter3 = random.choice(letter)
    else:
        letter3 = letter_input_3

    if letter_input_4 == "v":
        letter4 =random.choice(vowels)
    elif letter_input_4 == "c":
        letter4 = random.choice(consonants)
    elif letter_input_4 == "l":
        letter4 = random.choice(letter)
    else:
        letter4 = letter_input_4

    if letter_input_5 == "v":
        letter5 =random.choice(vowels)
    elif letter_input_5 == "c":
        letter5 = random.choice(consonants)
    elif letter_input_5 == "l":
        letter5 = random.choice(letter)
    else:
        letter5 = letter_input_5
    
    if letter_input_6 == "v":
        letter6 =random.choice(vowels)
    elif letter_input_6 == "c":
        letter5 = random.choice(consonants)
    elif letter_input_6 == "l":
        letter5 = random.choice(letter)
    else:
        letter6 = letter_input_6
    
    if letter_input_7 == "v":
        letter7 =random.choice(vowels)
    elif letter_input_7 == "c":
        letter7 = random.choice(consonants)
    elif letter_input_7 == "l":
        letter7 = random.choice(letter)
    else:
        letter7 = letter_input_7  
        
    name = letter1 + letter2 + letter3 + letter4 + letter5 + letter6 + letter7
    return(name)
    
for coolnames in range(20):
    print(generator())


