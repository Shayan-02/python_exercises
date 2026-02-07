def adad_chap_kon(num: int) -> str:
    """
    Prints the given number such that each digit is repeated as many times as its value.

    Args:
        num (int): The input number.

    Returns:
        str: The modified string.
    """
    for i in str(num):  # iterate over each digit in the number
        print(f"{i}: ", end="")  # print the digit and a space
        for j in range(int(i)):  # repeat the digit as many times as its value
            print(i, end="")  # print the digit
        print()  # print a newline after each iteration

adad_chap_kon(input())