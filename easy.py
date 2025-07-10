# Write a Python program to check if a number is even or odd.
num=int(input("enter the number: "))
def even_or_odd(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
print(even_or_odd(num))
    
# Write a Python program to find the largest of three numbers.
def largest():
    num1=int(input("enter the number: "))
    num2=int(input("enter the second number: "))
    num3=int(input("enter the third number: "))
    if num1 >=num2 and num1 >= num3:
        return num1
    elif num2 >=num1 and num2 >=num3:
        return num2
    else:
        return num3
print(largest())


# Write a Python program to check if a string is a palindrome.
def string_palindrome():
    string=input("enter the string: ")
    rev=""
    for i in range(len(string)-1,-1,-1):
        rev+=string[i]
    if rev==string:
        return "palindrome"
    else:
        return "not palindrome"
print(string_palindrome())

# Write a Python program to calculate the factorial of a number.
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
print(factorial(5))

# Write a Python program to generate the Fibonacci sequence up to n terms.
def fibanacci(n):
    a=0
    b=1
    list=[]
    for i in range(n):
        list.append(a)
        c=a
        a=b
        b=c+b
    return list
print(fibanacci(10))
        



# Write a Python program to count the number of vowels in a string.
def vowel(s):
    # string="udayasree"
    vowels="aeiou"
    vowel_c=0
    vowels_list=[]
    for i in s:
        if i in vowels:
            vowel_c+=1
            vowels_list.append(i)
    return vowel_c
print(vowel("udayasree"))


# Write a Python program to find the sum of all elements in a list.
lst=[1,2,3,4,5,6,7,8,9]
def sum_of_list(list):
    sum=0
    for i in range(len(list)):
        sum+=list[i]
    return sum
print(sum_of_list(lst))



# Write a Python program to reverse a given string.
def reverse(string):
    rev=""
    for i in range(len(string)-1,-1,-1):
        rev+=string[i]
    return rev
print(reverse("udayasree"))


# Write a Python program to check if a number is prime.
def is_prime(n):
    fact=0
    for i in range(2,n):
        if n%i==0:
            return "not prime"
    return "prime"
print(is_prime(63))


# Write a Python program to find the GCD of two numbers.
def gcd(num1,num2):
    m=min(num1,num2)
    gcd_num=1
    for i in range(1,m+1):
        if num1%i==0 and num2%i==0:
             gcd_num=i
            
    return gcd_num
print(gcd(16,10))


# Write a Python program to print the multiplication table of a given number.
def table(n):
    for i in range(1,11):
        print(f"{n} X {i}={n*i}")
print(table(5))


# Write a Python program to find the second largest number in a list.
def second_max(list):
    max=list[0]
    max2=list[1]
    for i in range(len(list)):
        if max < list[i] :
            max2=max
            max=list[i]
        elif max > list[i]  > max2:
            max2=list[i]
    return max2
print(second_max([1,2,3,4,4,5,6,8,7,22]))


# Write a Python program to remove duplicates from a list.
def remove_duplicates(n):
    unique=[]
    for i in n:
        if i not in unique:
            unique.append(i)
    return unique
print(remove_duplicates([1,2,3,4,5,3,2,7]))

# Write a Python program to sort a list in ascending order.
def sort_list(list):
    for i in range(len(list)):
        for j in range(i,len(list)-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]= list[j+1],list[j]
              
    return list
print(sort_list([1,3,2,3,5,7,9,5,8]))