# Import the math module
import math
from collections import Counter

# Define the function to get the prime factors of a number
# The function name is get_prime_factors
# The argument is n
def get_prime_factors(n):
    """
    Find all prime factors of a number n.
    
    Args:
        n (int): The number to factorize
        
    Returns:
        list: List of prime factors (including duplicates)
    """
    if n <= 0:
        return []
    if n == 1:
        return [1]
    
    factors = []
    # Handle even numbers
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # Check odd numbers from 3 to sqrt(n)
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n = n // i
        i += 2
    
    # If n is still greater than 1, it's a prime factor
    if n > 1:
        factors.append(n)
    
    return factors


def gcd_prime_factorization(a, b):
    """
    Calculate GCD of two numbers using prime factorization method.
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: Greatest Common Divisor of a and b
        
    Raises:
        TypeError: If inputs are not integers
        ValueError: If inputs are negative
    """
    # Validate input types
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers")
    
    # Validate input values
    if a < 0 or b < 0:
        raise ValueError("Both inputs must be non-negative integers")
    
    # Handle edge cases
    if a == 0 and b == 0:
        return 0
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Get prime factors for both numbers
    # Example: a=18, b=24
    factors_a = get_prime_factors(abs(a))  # [2, 3, 3] for 18
    factors_b = get_prime_factors(abs(b))  # [2, 2, 2, 3] for 24
    
    # Find common prime factors using Counter intersection
    # Convert lists to counters to count occurrences
    counter_a = Counter(factors_a)  # {2: 1, 3: 2} for 18
    counter_b = Counter(factors_b)  # {2: 3, 3: 1} for 24
    common_counter = counter_a & counter_b  # {2: 1, 3: 1} - min of each count
    
    # Convert back to list of factors
    # Take the minimum count for each common factor
    common_factors = []
    for factor, count in common_counter.items():
        common_factors.extend([factor] * count)  # [2, 3] for our example
    
    # Calculate GCD by multiplying common factors
    # 2 × 3 = 6, which is the GCD of 18 and 24
    gcd = 1
    for factor in common_factors:
        gcd *= factor
    
    return gcd


def test_gcd_function():
    """
    Test the GCD function with 10 specific number pairs.
    Also includes the example from the problem (18, 24).
    """
    print("Testing GCD function using prime factorization method:")
    print("=" * 60)
    
    # Test with the provided example
    print(f"Example: GCD(18, 24) = {gcd_prime_factorization(18, 24)}")
    print("Expected: 6")
    print()
    
    # Test with 10 specific number pairs chosen to give interesting GCD results
    test_pairs = [
        (12, 18),    # GCD = 6
        (24, 36),    # GCD = 12
        (48, 64),    # GCD = 16
        (15, 25),    # GCD = 5
        (30, 45),    # GCD = 15
        (56, 84),    # GCD = 28
        (72, 96),    # GCD = 24
        (100, 150),  # GCD = 50
        (42, 63),    # GCD = 21
        (80, 120)    # GCD = 40
    ]
    
    print("Testing with 10 specific number pairs:")
    print("-" * 40)
    
    for i, (a, b) in enumerate(test_pairs):
        # Calculate GCD using our method
        our_gcd = gcd_prime_factorization(a, b)
        
        # Calculate GCD using Python's built-in method for verification
        builtin_gcd = math.gcd(a, b)
        
        # Check if our result matches the built-in result
        is_correct = our_gcd == builtin_gcd
        
        print(f"Test {i+1:2d}: GCD({a:3d}, {b:3d}) = {our_gcd:3d} {'✓' if is_correct else '✗'}")
        
        if not is_correct:
            print(f"         Expected: {builtin_gcd}, Got: {our_gcd}")
    
    print()
    print("All tests completed!")


if __name__ == "__main__":
    # Run the test function
    test_gcd_function()
    
    # Interactive input section
    print("\n" + "=" * 60)
    print("Interactive GCD Calculator:")
    print("-" * 30)
    
    try:
        # Get input from user
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        # Calculate and display GCD
        result = gcd_prime_factorization(num1, num2)
        print(f"\nGCD({num1}, {num2}) = {result}")
        
        # Show prime factorization for educational purposes
        print(f"\nPrime factorization:")
        factors1 = get_prime_factors(abs(num1))
        factors2 = get_prime_factors(abs(num2))
        print(f"{num1} = {' × '.join(map(str, factors1)) if factors1 else '1'}")
        print(f"{num2} = {' × '.join(map(str, factors2)) if factors2 else '1'}")
        
    except ValueError as e:
        if "invalid literal for int()" in str(e):
            print("Error: Please enter valid integers.")
        else:
            print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nGoodbye!")
