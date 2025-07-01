def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

digits = set()

for num in range(10, 100):
    if is_prime(num):
        for digit in str(num):
            digits.add(int(digit))

print("Digits used in 2-digit prime numbers:")
print(sorted(digits))
