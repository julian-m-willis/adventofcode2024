def main():
    with open('input.txt', "r") as file:
        # Concatenate all lines into one string
        full_text = "".join(line.strip() for line in file)
        
        # Process the entire text at once
        ans1 = day3_part1(full_text)
        ans2 = day3_part2(full_text)
            
    print(f"Part 1: {ans1}")
    print(f"Part 2: {ans2}")
            
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

def day3_part2(line):
    ans = 0
    enabled = True  # Multiplications are enabled by default
    
    # Split by do() and don't() to get sections
    parts = []
    current = line
    
    while current:
        # Find the next do() or don't()
        do_pos = current.find("do()")
        dont_pos = current.find("don't()")
        
        # If neither is found, add the rest and break
        if do_pos == -1 and dont_pos == -1:
            parts.append(current)
            break
            
        # Find which comes first
        if do_pos == -1:
            pos = dont_pos
            marker = "don't()"
        elif dont_pos == -1:
            pos = do_pos
            marker = "do()"
        else:
            pos = min(do_pos, dont_pos)
            marker = "do()" if pos == do_pos else "don't()"
            
        # Add the section before the marker and the marker itself
        parts.append(current[:pos])
        parts.append(marker)
        current = current[pos + len(marker):]
    
    # Process each section
    for part in parts:
        if part == "do()":
            enabled = True
        elif part == "don't()":
            enabled = False
        elif enabled:
            # Process this section with part1 logic
            ans += day3_part1(part)
            
    return ans
                    
if __name__ == "__main__":
    main()
