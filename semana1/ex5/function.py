def is_palindrome(a):
    n = len(a)
    for i in range(n//2):
        if a[i] != a[n-1-i]:
            return False
    return True
