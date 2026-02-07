def sayName(name: str) -> str :
    """
    This function takes a string as input and returns a string that says "Haji", "Karbalayee", "Mashti", or "Agha" depending on the input string.

    Args:
        name (str): A string that contains either "Y", "y", "N", or "n"

    Returns:
        str: A string that says "Haji", "Karbalayee", "Mashti", or "Agha" depending on the input string
    """
    valid = ["Y", "y", "N", "n"]
    if name[0] in valid and name[1] in valid and name[2] in valid:
        if name[0].lower() == "y":
            return "Haji"
        elif name[1].lower() == "y":
            return "Karbalayee"
        elif name[2].lower() == "y":
            return "Mashti"
        else:
            return "Agha"
    else:
        return "Invalid input"


print(sayName(input()))