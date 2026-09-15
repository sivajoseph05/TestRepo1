'''
s="hello world"
print(s)
print(type(s))
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.count('l'))
print(s.endswith('ld'))
print(s.find('o'))
print(s.find('o',5))
print(s.replace('o','s'))

a="HELLO"
print(a.isupper())
print(a.islower())
print(a.isalnum())
print(a.isalpha())

s="he \n is \n good"
print(s)
print(s.splitlines())
print(s.splitlines(True))
print(s.split())
print(s.splitlines(","))

s="        siva    "
print(len(s))
print(len(s.strip()))
print(len(s.lstrip()))
print(len(s.rstrip()))

s=' 12-03-2020'
print(s.partition('-'))

s="helloworld"
print(s)
print(s[0:2])
print(s[:5])
print(s[1:])
print(s[-1])
print(s[-2:-1])
print(s[:-1])
print(s[::-1])


1. Reverse Only Letters

Given a string, reverse only the alphabet characters and keep special characters in the same position.

Input:
s = "a-bC-dEf-ghIj"

Output:
"j-Ih-gfE-dCba"


def reversed(s):
    k=s
    right=len(k)-1
    left=0
    
    ls=list(k)
    while left < right:
        if ls[left].isalpha() and ls[right].isalpha():
            ls[left],ls[right]=ls[right],ls[left]
            left+=1
            right-=1
        elif not s[left].isalpha():
            left += 1

        else:
            right -= 1
        
    r="".join(ls)
    return r

s="a-bc-def-ghij"
print(reversed(s))

2. First Non-Repeating Character

Find the first character that appears only once in the string.

Input:
s = "swiss"

Output:
"w"
def repeat(s):
    dict={}
    for i in s:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
            
    for i in s:
        if dict[i]==1:
            return i
    
    
    return None

s=input("enter the string:")
print(repeat(s))

3. Longest Word

Find the longest word in a sentence.

Input:
s = "Python coding challenges are fun"

Output:
"challenges"


def longest(s): 
    k=s.split()
    k.sort(key=len)
    
    return k[-1]

s = "Python coding challenges are fun"
print(longest(s))

4. Check Rotation

Check whether one string is a rotation of another.

Input:


Output:
True

def rotation(s1,s2):
    if len(s1)!=len(s2):
        return False
    
    c=s1+s1
    if s2 in c:
        return True
    
    return None

s1 = "waterbottle"
s2 = "erbottlewat"
print(rotation(s1,s2))

5. Compress String

Compress consecutive repeated characters.

Input:
s = "aaabbccccd"

Output:
"a3b2c4d1"


def compress(s):
    n=len(s)
    result=[]
    count=1
    for i in range(1,n):
        if s[i]==s[i-1]:
            count+=1
        else:
            result.append(s[i-1] + str(count))
            count=1
    result.append(s[-1]+str(count))

    return "".join(result)

s = "aaabbccccd"
print(compress(s))

7. Remove Duplicate Characters

Remove duplicate characters while keeping the first occurrence.

Input:
s = "programming"

Output:
"progamin"


def duplicate(s):
    seen=set()
    result=[]

    for i in s:
        if i not in seen:
            seen.add(i)
            result.append(i)
        
    
    return "".join(result)


s="programming"
print(duplicate(s))

8. Longest Substring Without Repeating Characters

Find the length of the longest substring without repeating characters.

Input:
s = "abcabcbb"

Output:
3


 9. Palindrome After Removing One Character

Check if a string can become a palindrome after removing at most one character.

Input:
s = "abca"

Output:
True
'''
def palindrome(s):
    left=0
    right=len(s)-1

    while left < right:
        if s[left]==s[right]:
            left+=1
            right-=1
        else:
            s[left].remove

    return

s = "abca"
print(palindrome(s))