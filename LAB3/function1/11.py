"""Write a Python function that checks whether a word or 
phrase is palindrome or not.
 Note: A palindrome is word, phrase, or sequence that reads
the same backward as forward, e.g., madam"""
def palindr(s = str(input())):
    s1 = s[::-1]
    if s1 == s:
        print('it is palindrome')
    else:
        print('it is not palindrome')
palindr()