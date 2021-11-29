import random
print("H A N G M A N")
while True:
    input_ = input('Type "play" to play the game, "exit" to quit: ')
    if input_ == "exit":
        break
    if input_ != "play":
        continue
    word_list = ["python", "java", "kotlin", "javascript"]
    random_output = random.choice(word_list)
    guess_set = set()
    counter = 8
    allinput = []
    lower =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',''
                'q','r','w','t','s','x','z','v','y','u']
    guessed = ["-" for letter in random_output]# this line print guess every letter in an index in  set 
    while counter > 0:
        print()
        print("".join(guessed))# this line print word like this ----
        guess = input("Input a letter: ")
        lengthofinput = len(guess)

        if  lengthofinput != 1:
            print("You should input a single letter")
        elif guess not in lower:
            print("It is not an ASCII lowercase letter")
        elif guess in allinput:
            print(guess_set)
            print("You already typed this letter")
        elif guess not in set(random_output):
            if guess in allinput:
               print(guess_set)
               print("You already typed this letter")
            else:
                print("No such letter in the word")
                counter -= 1
        elif guess in set(random_output) and guess not in guess_set:
            guess_set.add(guess)
            guessed = [letter if letter in guess_set else "-" for letter in random_output]
            print(allinput)

        allinput.append(guess)



    if guess_set == set(random_output):
        print("You guessed the word!\nYou survived!")

    else:
            print("You are hanged!")#print(guess_set)

