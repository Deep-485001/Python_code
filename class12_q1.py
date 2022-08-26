def factorial(n, m):
    fact = 1
    for i in range(1, n):
        fact = fact * i
 
    for i in range(n, m + 1):
        fact = fact * i
        print(f"The Factorial of {i} is : {fact}")
 
if __name__ == '__main__':
 
    n =int(input("Enter stating of factorial series no. : "))
    m = int(input("Enter number of steps : "))
 
    factorial(n, m)

