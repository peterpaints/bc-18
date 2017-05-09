def gen_primes(n):
    # We require input n to be an int. Positive and greater than 0.
    if not isinstance(n, int):
        raise ValueError("Only integers are allowed as input")
    elif n < 1:
        raise ValueError("The integer should be greater than 0")
    else:
        """Generate prime numbers from 1 up to the specified number n."""
        # Modified this function to implement a sieve of erastothenes.
        # 1 is not a prime number. Initializing the list of primes with 2
        # allows us to skip even numbers in the outer loop. This means
        # less numbers to iterate on, thus less operations for the function.
        prime_numbers = [2]
        sieve = [True] * (n + 1)
        # Using xrange means each number is operated on lazily, i.e without
        # placing the entire list of numbers in memory at the same time
        for i in xrange(3, n + 1, 2):
            if sieve[i]:
                # The above if statement will evaluate the first number, that
                # is 3, as a prime number.
                prime_numbers.append(i)
                # Once the first number has been appended to prime_numbers
                # as a prime, we now want to cross out all the multiples of
                # that number since they are not primes and we need not iterate
                # over them. Again, this means less operations for the function
                # This is why there is an i at the end of range() below, to
                # skip them. Also, we start at squares of i since anything
                # below that has already been eliminated by smaller i's.
                for j in range(i**2, n + 1, i):
                    # for some reason, xrange here returns a StackOverflow
                    # error with large ints like 1000000
                    sieve[j] = False
        return prime_numbers


print gen_primes(100)

# import time
# start_time = time.time()
# # main()
# print("--- %s seconds ---" % (time.time() - start_time))

# gen_primes(39) now logs 0.00000190734863281 seconds.
# gen_primes(10000) now logs 0.000000953674316406 seconds.
# gen_primes(1000000) now logs 0.00000286102294922 seconds.
