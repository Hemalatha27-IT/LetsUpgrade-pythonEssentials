def checkprime(number):
    if number > 1:
          for i in range(2,number):
                if (number % i) == 0:
                    return False
                else:
                    return True

# if the entered number is less than or equal to 1
# then it is not prime number
    else:
          return False
lst = list(range(2500))
lst_prime = filter(checkprime,lst)
print(list(lst_prime))
