# A programme that takes two user int inputs and adds them

def main():
    while True:
        first_input = input("First number: ")
        second_input = input("Second number: ")
        if add_input(first_input, second_input):
            break

def add_input(first_input, second_input):
    """Converts to int and adds to user provided input"""
    try:
        first_input = int(first_input)
        second_input = int(second_input)
    except ValueError:
        print("Accepted input: Int \nTry Again ...")
        return False
    else:
        print(first_input + second_input)
        return True


if __name__ == '__main__':
    main()