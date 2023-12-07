def countDigitOne(n):
    count = 0
    factor = 1
    i = 1

    while i <= n:
        divider = i * 10
        count += (n // divider) * i + min(max(n % divider - i + 1, 0), i)
        i *= 10

    return count

n = int(input("Enter the value of n: "))

result = countDigitOne(n)
print(f"The total number of digit 1 in numbers up to {n} is: {result}")
