# GCD Calculator using Prime Factorization

A Python implementation of the Greatest Common Divisor (GCD) calculation using the prime factorization method.

## Features

- **Prime Factorization Method**: Calculates GCD by finding common prime factors between two numbers
- **Input Validation**: Ensures inputs are non-negative integers
- **Interactive Calculator**: Command-line interface for user input
- **Comprehensive Testing**: Includes test suite with 10 predefined number pairs
- **Educational Display**: Shows prime factorization of both numbers

## How It Works

The algorithm works by:

1. Finding all prime factors of both numbers
2. Identifying common prime factors
3. Multiplying the common factors to get the GCD

### Example

For numbers 18 and 24:
- 18 = 2 × 3 × 3
- 24 = 2 × 2 × 2 × 3
- Common factors: 2 × 3 = 6
- **GCD(18, 24) = 6**

## Usage

### Running the Program

```bash
python3 gcd_prime_factorization.py
```

The program will:
1. Run the test suite
2. Prompt you to enter two numbers
3. Calculate and display the GCD
4. Show the prime factorization of both numbers

### Using the Function Directly

```python
from gcd_prime_factorization import gcd_prime_factorization

result = gcd_prime_factorization(18, 24)
print(result)  # Output: 6
```

## Requirements

- Python 3.6+
- No external dependencies (uses only built-in modules)

## Error Handling

The function validates inputs and raises appropriate errors:

- `TypeError`: If inputs are not integers
- `ValueError`: If inputs are negative

## Algorithm Complexity

- **Time Complexity**: O(√n) for prime factorization
- **Space Complexity**: O(log n) for storing prime factors

## Files

- `gcd_prime_factorization.py`: Main implementation with interactive calculator
- `README.md`: This documentation file
- `.gitignore`: Git ignore file for Python projects

## Testing

The program includes a comprehensive test suite that verifies the GCD calculation against Python's built-in `math.gcd()` function using 10 predefined number pairs.
