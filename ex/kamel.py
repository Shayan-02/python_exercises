# https://quera.org/problemset/282

def kamel(n: int) -> str:
    """
    
    """
    sums = sum(i for i in range(1, n//2+1) if n % i == 0)

    # if and else
    if sums == n:
        return "YES"
    else:
        return "NO"


print(kamel(int(input())))