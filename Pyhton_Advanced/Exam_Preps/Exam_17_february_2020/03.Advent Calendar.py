

def fix_calendar(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            current = numbers[i]
            next = numbers[j]
            if current < next:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


# Test Code:
numbers = [3, 2, 1]
fixed = fix_calendar(numbers)
print(fixed)