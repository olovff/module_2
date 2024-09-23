numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for num in numbers:
    if num == 1:
        continue

    is_prime = True


    del_ = 1

    for del_ in range(1, num):
         if del_ == num:
             is_prime = True

         if del_ != num and del_ != 1:

             is_prime = num % del_ > 0
             if not is_prime:
                 break



    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

print(primes)
print(not_primes)