
def get_int(prompt, check_positive = False):
    '''Will gets the integer input and validate positive based on argument'''
    while True:
        num = input(prompt)

        try:
            num = int(num)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if check_positive:
            if num <= 0:
                print("Enter a positive number.")
                continue
            else:
                return num
        else:
            return num