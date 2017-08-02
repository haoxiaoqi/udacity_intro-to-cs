# udacity_intro-to-cs
###Lesson 22 how to have infinitely power###
##############################################################################
###quiz 10###
def is_palindrome(s):
    if s == '':
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
###############################################################################
