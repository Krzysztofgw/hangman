import random, string


word_list = ['python', 'java', 'kotlin', 'javascript']
guess_word = str(random.choice(word_list))
word = (len(guess_word)) * "-"
letter = ""
word_set = set()
counter = 0
choice = ""

def check_letter(letter):
    global word, counter, word_set
    word_ = []
    iteration = 0
    if letter in guess_word and letter not in word_set:
        word_set.add(letter)
        for x in range(len(guess_word)):
            if guess_word[x] == letter:
                word_.append(letter)
            elif word[x] != "-":
                word_.append(word[x])
            else:
                word_.append("-")
        word = "".join(word_)
    elif letter in word_set:
        print("No improvements")
        counter += 1
    else:
        word_set.add(letter)
        print("No such letter in the word")
        counter += 1


def print_word():
    print()
    print(word)
    print("Input a letter:", end=" ")


def check_if_correct(letter):
    if letter.__len__() != 1:
        print("You should input a single letter")
        return True
    elif letter not in string.ascii_lowercase:
        print("It is not an ASCII lowercase letter")
        return True
    elif letter in word_set:
        print("You already typed this letter")
        return True
    else:
        return False


def menu():
    print('Type "play" to play the game, "exit" to quit:',end=" ")


print("H A N G M A N")
while choice != "exit":
    menu()
    choice = input()
    if choice == "play":
        while counter < 8 and word != guess_word:
            print_word()
            letter = input()
            if check_if_correct(letter):
                pass
            else:
                check_letter(letter)
        if word == guess_word:
            print(word)
            print("You guessed the word!")
            print("You survived!\n")
        else:
            print("You are hanged!")
    elif choice == "exit":
        break
