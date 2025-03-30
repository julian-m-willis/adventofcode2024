from collections import Counter

def read_input_file(filename):
    left_list = []
    right_list = []
    with open(filename, "r") as file:
        for line in file:
            # Split the line by whitespace and convert each part to an integer
            numbers = list(map(int, line.split()))
            if len(numbers) == 2:
                left_list.append(numbers[0])
                right_list.append(numbers[1])
    return left_list, right_list

def compute_total_distance(left_list, right_list):
    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    # Compute the sum of absolute differences of corresponding pairs
    total_distance = sum(abs(a - b) for a, b in zip(left_sorted, right_sorted))
    return total_distance

def compute_similarity_score(left_list, right_list):
    # Count the occurrences of each number in the right list
    right_counts = Counter(right_list)
    # For each number in left_list, multiply by its count in right_list (if any)
    similarity_score = sum(number * right_counts.get(number, 0) for number in left_list)
    return similarity_score

def save_output_file(filename, content):
    with open(filename, "w") as file:
        file.write(str(content))

if __name__ == "__main__":
    # Read input from file
    left, right = read_input_file("./input.txt")
    
    # Compute the total distance
    distance = compute_total_distance(left, right)
    
    # Print the result (optional)
    print("The total distance is:", distance)
    
    # Compute the similarity score
    score = compute_similarity_score(left, right)
    print("The similarity score is:", score)
    
    # Save the result to an output file
    save_output_file("output.txt", score)
