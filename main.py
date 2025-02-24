import random


def generate(start,stop):
    generated = random.randint(start,stop)
    return generated

def level():
    return level_value

def guessing():
    global level_value
    level_value = 1
    start = 0
    stop = 10
    score = 0

    while level_value <= 5:
        generated_number = generate(start, stop)
        number = input(f"Guess a number within range {start} and {stop}: ")


        try:
            num = int(number)

        except  ValueError:
                print("Please enter a valid number")
                continue
        print(f"Level: {level_value}")
        if level_value == 6:
            break
        if num == generated_number:
            print(f"Correct:Level {level_value} completed")
            level_value +=1

            start += 10
            stop += 10
            score +=1



        else:
            print("Wrong!,Try again")
            continue

    return score


if __name__ == "__main__":
    print(f"Total scores: {guessing()}")