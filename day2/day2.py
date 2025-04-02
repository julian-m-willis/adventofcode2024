###part 1
def day2_part1(numbers):
    # Convert strings to integers
    numbers = [int(x) for x in numbers]
    
    # Check if sequence is increasing or decreasing
    increasing = numbers[0] < numbers[1]
    
    # Check each adjacent pair
    for i in range(len(numbers) - 1):
        # Check if direction changes
        if increasing and numbers[i] >= numbers[i + 1]:
            return False
        if not increasing and numbers[i] <= numbers[i + 1]:
            return False
            
        # Check if difference is between 1 and 3
        diff = abs(numbers[i] - numbers[i + 1])
        if diff < 1 or diff > 3:
            return False
            
    return True

#part 2
def day2_part2(numbers):
    # First try without removing any number
    if day2_part1(numbers):
        return True
        
    # Try removing each number one at a time
    for i in range(len(numbers)):
        # Create a new list without the current number
        test_numbers = numbers[:i] + numbers[i+1:]
        if day2_part1(test_numbers):
            return True
            
    return False

answer = 0
with open('./input.txt', "r") as file:
    for line in file:
        numbers = line.split()
        numbers = [int(x) for x in numbers]
        if day2_part2(numbers):
            answer += 1

print(answer)
            
            
