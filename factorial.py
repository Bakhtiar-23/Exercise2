def factorials(n: int) -> dict:
    factorial_dict = {}

    for number in range(1, n + 1):
        factorial_value = 1
        for i in range(1, number + 1):
            factorial_value *= i
        factorial_dict[number] = factorial_value

    return factorial_dict

# Example usage
n = int(input("Enter a number: "))
result_dict = factorials(n)

for num, factorial in result_dict.items():
    print(f"Factorial of {num}: {factorial}")
