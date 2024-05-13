def isPalindrome(s):
    ''' check if a number is a Palindrome '''
    s = str(s)
    return s == s[::-1]

def generate_palindrome(minx,maxx):
    ''' return a list of Palindrome number in a given range '''
    temproaryList = [] # taking null set for later addition of elements
    for i in range(minx,maxx+1):
        if isPalindrome(i):
            temproaryList.append(i)

    return temproaryList
generate_palindrome(1,120)


num = input('Enter any number : ')
try:
   val = int(num)
   if num == str(num)[::-1]:
      print('The given number is PALINDROME')
   else:
      print('The given number is NOT a palindrome')
except ValueError:
   print("That's not a valid number, Try Again !")