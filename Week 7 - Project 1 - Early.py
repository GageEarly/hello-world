def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        return 0
    numbers = sorted(numbers)
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    return numbers[mid]

def mode(numbers):
    if not numbers:
        return 0
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    return max(counts, key=counts.get)

def main():
    numbers = [10, 20, 30]
    print("Mean:", mean(numbers))
    print("Median:", median(numbers))
    print("Mode:", mode(numbers))

if __name__ == "__main__":
    main()
