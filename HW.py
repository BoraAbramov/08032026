import random

def get_lucky_numbers(amount: int) -> tuple[int]:
    """
    :param amount: number of lucky numbers
    :return: tuple with lucky numbers
    """
    numbers = [random.randint(1, 100) for _ in range(amount)]
    return tuple(numbers)

print(get_lucky_numbers(7)) #for this one I used AI for help

#The function receives the tuple of lucky numbers
#Ask the user to input numbers
#Continue asking until the user guesses one of the lucky numbers
#When the user guesses correctly, stop the loop
#Return the number of attempts the user needed

def input_until_lucky(lucky_numbers: tuple) -> int:
    """
    :param lucky_numbers: receives the tuple of lucky numbers
    user need to guess one of the lucky numbers
    :return:number of attempts
    """
    amount = int(input("Enter amount of lucky numbers to generate: "))
    lucky_numbers = get_lucky_numbers(amount)
    guess_count = 0
    while True:
        try:
            user = int(input("please enter your guess: "))
        except ValueError:
            print("something went wrong, please try again")
            continue
        guess_count += 1
        if user in lucky_numbers:
            return print(f"the of your guess is {guess_count} times")
        else:
            continue



guess_the_number = input_until_lucky(get_lucky_numbers)