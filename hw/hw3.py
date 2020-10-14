myWord = input ("Input your word: ")
backward_word = myWord[::-1]

if myWord == backward_word:
    print("correct")
else:
    print("try again")
