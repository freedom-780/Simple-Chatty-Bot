def greet(bot_name, birth_year):
    print(f'Hello! My name is {bot_name}.')
    print(f'I was created in {birth_year}.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print(f'What a great name you have {name}!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print(f"Your age is {age} that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    # write your code here
    print("What is the most popular programming language?")
    print("1. Python")
    print("2. C++")
    print("3. Fortran")
    print("4. Keras")
    answer = int(input())

    n = True
    while n:
        if answer == 1:
            n = False
        else:
            print("Pease, try again")
            answer = int(input())




def end():
    print('Congratulations, have a nice day!')


greet('Aid', '2020')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
