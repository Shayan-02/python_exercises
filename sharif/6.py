def is_valid(s, t):
    """
  Checks if a code `s` is valid given a valid code `t`.

  Args:
    s: The code to be checked.
    t: The valid code.

  Returns:
    True if `s` is valid, False otherwise.

  Examples:
    >>> is_valid("a", "a")
    True
    >>> is_valid("a", "b")
    False
    >>> is_valid("ab", "a")
    False
    >>> is_valid("ab", "b")
    True
    """
    alphabet_s = set(s)
    alphabet_t = set(t)
    return alphabet_s == alphabet_t

n, t = map(str, input().split())
for i in range(int(n)):
  s = input()
  if is_valid(s, t):
    print("Yes")
  else:
    print("No")
