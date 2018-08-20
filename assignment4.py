#1. Reverse the list

a=[1,2,3,4]
print(a[::-1])
a.reverse()
print(a)

#2. Print all the uppercase letters from a string.

s = input("Enter a string: ")
for ch in s :
   if ch.isupper():
       print(ch)
  

#3. Split the user input on comma's and store the values in a list as integers.

a=input("enter a string containing commas")
print(a.split(','))

#4. Check whether a string is palindromic or not.

a=input("enter a string to check palindrome")
if a==a[::-1]:
    print("%s is a palindrome"%(a))
else:
    print("%s is not a palindrome"%(a))
    
#5. Make a deepcopy of a list and write the difference between shallow copy and deep copy.
'''
A shallow copy means constructing a new collection object and then populating it with references to the child objects found in the original. In essence, a shallow copy is only one level deep. The copying process does not recurse and therefore won’t create copies of the child objects themselves.

A deep copy makes the copying process recursive. It means first constructing a new collection object and then recursively populating it with copies of the child objects found in the original. Copying an object this way walks the whole object tree to create a fully independent clone of the original object and all of its children.
'''
   #example of deep copy
import copy
 
li1 = [1, 2, [3,5], 4]
li2 = copy.deepcopy(li1)
li2[2][0] = 7
print(li2)
print(li1)
    



