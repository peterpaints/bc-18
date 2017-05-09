def gen_primes(n):
    # We require input n to be an int. Positive and greater than 1.
    if not isinstance(n, int):
        return ValueError('Only integers are allowed as input')
    elif n < 2:
        return ValueError('The integer should be greater than 1')
    else:
        """Generate prime numbers from 1 up to the specified number n."""
        # Modified this function to implement a sieve of erastothenes.
        # 1 is not a prime number. Initializing the list of primes with 2
        # allows us to skip even numbers in the outer loop. This means
        # less numbers to iterate on, thus less operations for the function.
        prime_numbers = [2]
        sieve = [True] * (n + 1)
        for i in range(3, n + 1, 2):
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
                    sieve[j] = False
        return prime_numbers


# print gen_primes(100)

# Asymptotic analysis:
# The function does the following operations
# 0. Initializing a list with a single number 2 in it = O(1)
# 1. Creating list of n+1 True values = O(N)
# 2. Looping over half the items in the list (odd numbers) = O(N/2)
# 3. Checking if each item in N/2 is a prime = O(1)
# 4. Appending each prime number to the list = O(1)
# 5. Looping over N/i items to set them to False = O(N/i)
# 6. Setting numbers in step 5 to false = 0(N/i)

# O(1) + O(N) + (O(N/2) * (O(1) + O(1) + (O(N/i) * O(N/i))))
# In step 3 onwards, as i increases, O(N/i) changes to O(N log N)

# We will now have O(1) + O(N) + O(N log N)
# Since in Big O Notation we usually simplify to the largest operation,
# this function can be said to have a time complexity of O(N log N)
