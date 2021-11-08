#Write a Python program to calculate the length of a string
'''s = 'Python is simple'
print(len(s))

#Write a Python program to count the number of characters (character frequency) in a string
s = 'google.com'
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print (d)

from collections import Counter
res = Counter(s)
print (d)


#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string.
s = 'w3resource'
s1 = ""
l = list(s)
lsum = l[0:2]+l[-2:]
if len(s)>2:
    print(s1.join(lsum))
else:
    print(" ")

#4. Write a Python program to get a string from a given
#string where all occurrences of its first char have been changed to '$',
# except the first char itself.
s= 'restart'
l = s[0]
l1 = s[1:]
l2 = l1.replace(s[0],"$")
print(l + l2)


#5. Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.
s1 = 'abc'
s2 = 'xyz'
ns1 = s1[:2] + s2[2:]
ns2 = s2[:2] + s1[2:]
print(ns1," ",ns2)

#6.Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged.
s = input("Enter String")
if len(s)>2:
    if s.endswith('ing'):
        print(s,"ly",sep = "")
    else:
        print(s,'ing',sep = "")
else:
    print("length of given string is less than 2",s)


#7. Write a Python program to find the first appearance of
# the substring 'not' and 'poor' from a given string,
# if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.
s =  'The lyrics is not that poor!'
s1 = s.find("not")
s2 = s.find("poor!")
l = list(s.split())
print(l)
print(l.index("not"))
print(l.index("poor!"))
if s2 > s1 and s1 > 0 and s2 > 0:
    s = s.replace(s[s1:(s2 + 4)], 'good')
    print(s)
else:
    print(s)

#8. Write a Python function that takes a list of words and
# return the longest word and the length of the longest one.

n = int(input("Enter No. of words you want to give input:"))

def display():
    k = input("Enter Word ")

for k in range(n):
   display()
   d = len(k)
   l = []
   print(l.append(d))

s = "python is simple and interesting language"
for i in s.split():
    r = i[0].title() + i[1:-1] + i[-1].title()
    print(r,end=" ")
print()

#9. Write a Python program to remove the nth index character from a nonempty string
s = "python is simple and interesting language"
n = int(input("Enter the index"))
print(s.replace(s[n],""))


#10. Write a Python program to change a given string to a new string
# where the first and last chars have been exchanged
s = "python is simple and interesting language"
for i in s.split():
    r = i[-1] + i[1:-1] + i[0]
    print(r,end=" ")
print()#print(s.translate({i[0]:i[1],i[1]:i[0]}))