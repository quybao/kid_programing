
# coding: utf-8

# In[ ]:


import csv
import random

words = []
already_tested_words = [] 
with open('insteadofvery.csv') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',')
    words = [row for row in datareader]    


# now pick a word to test
def do_test(words, already_tested_words):
    while True:
        test_word = words[random.randint(0,len(words) - 1)]
        if test_word not in already_tested_words:
            already_tested_words.append(test_word)
            break

    # now pick another 3 words used for multiple choices
    multiple_choices = []
    multiple_choices.append(test_word)
    while(len(multiple_choices) < 4):
        choice_word = words[random.randint(0,len(words) - 1)]
        if choice_word not in multiple_choices:
            multiple_choices.append(choice_word)

    shuffle_choices = random.sample(multiple_choices, len(multiple_choices))

    correct = False
    while(correct != True):
        print('\nWhat can be used instead of "{}"? (type the number corresponding to correct answer)'.format(test_word[0]))
        for i,choice in enumerate(shuffle_choices):
            print("{}: {}".format(i + 1, choice[1].strip()))
        print('', flush=True)

        answer = input('Your answer: ')
        try:
            if (shuffle_choices[int(answer) - 1][1] == test_word[1]):
                print("You are correct. Good job!")
                correct = True
            else:
                print("Sorry, that's not correct. Let's try again.\n")
        except:
            print("Please enter the number from 1 to 4.")
            

round_text = input("Welcome. How many words do you want to test today? ")
rounds = int(round_text)
for i in range(0,rounds):
    do_test(words, already_tested_words)
    if i < rounds - 1:
        print("\nLet's do another one")
    else:
        print('\nCongratulation! You master {} ways of not using "very" today.'.format(rounds))

