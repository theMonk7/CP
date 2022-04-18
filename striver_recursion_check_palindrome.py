def rec_check_palindrome(s,n,i):
    if i > n//2:
        return True
    return s[i] == s[n-i-1] and rec_check_palindrome(s,n,i+1)

s = "abbaabb"
n = len(s)
print(rec_check_palindrome(s,n,0))