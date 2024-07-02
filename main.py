def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """

    number = None
    while number is None:
        user_input = input("Enter a numeric value: ")
        try:
            number = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        else:
            print(number)

    ########################################
    # Do not delete the return statement
    ########################################
    return number


if __name__ == '__main__':
    main()
