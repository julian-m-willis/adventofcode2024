def main():
    with open('input.txt', "r") as file:
        ans = 0
        for line in file:
            line = line.strip()
            ans += day3_part1(line)
            
    print(ans)
            
def day3_part1(line):
    n = len(line)
    ans = 0
    # Split by "mul(" to find potential multiplication instructions
    parts = line.split("mul(")
    
    for part in parts[1:]:  # Skip the first part as it's before any "mul("
        # Find the closing parenthesis
        if ")" not in part:
            continue
            
        # Split at the first closing parenthesis
        mul_content, rest = part.split(")", 1)
        
        # Check if the content is valid (contains only numbers and comma)
        if not all(c.isdigit() or c == ',' for c in mul_content):
            continue
            
        # Split the numbers
        try:
            num1, num2 = map(int, mul_content.split(","))
            # Check if numbers are 1-3 digits
            if 1 <= len(str(num1)) <= 3 and 1 <= len(str(num2)) <= 3:
                ans += num1 * num2
        except ValueError:
            continue
            
    return ans
                    
if __name__ == "__main__":
    main()
