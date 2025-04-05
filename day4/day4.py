def main():
    with open('input.txt', "r") as file:
        matrix = []
        for line in file:
            matrix.append(line.strip())
            
        ans1 = day4_part1(matrix)
        
    print(f"Part 1: {ans1}")
    # print(f"Part 2: {ans2}")

def day4_part1(matrix):
    #go left to right and right to left
    ans = 0
    for row in matrix:
        for i in range(len(row)-3):
            if row[i:i+4] == "XMAS" or row[i:i+4] == "XMAS"[::-1]:
                ans += 1
                
    #go top to bottom and bottom to top
    for i in range(len(matrix[0])):
        for j in range(len(matrix)-3):
            if matrix[j][i] == "X" and matrix[j+1][i] == "M" and matrix[j+2][i] == "A" and matrix[j+3][i] == "S":
                ans += 1
            if matrix[j][i] == "S" and matrix[j+1][i] == "A" and matrix[j+2][i] == "M" and matrix[j+3][i] == "X":
                ans += 1
                
    #go top left to bottom right and top right to bottom left
    for i in range(len(matrix)-3):
        for j in range(len(matrix[0])-3):
            if matrix[i][j] == "X" and matrix[i+1][j+1] == "M" and matrix[i+2][j+2] == "A" and matrix[i+3][j+3] == "S":
                ans += 1
            if matrix[i][j] == "S" and matrix[i+1][j+1] == "A" and matrix[i+2][j+2] == "M" and matrix[i+3][j+3] == "X":
                ans += 1
                
    #go bottom left to top right and bottom right to top left
    for i in range(len(matrix)-3):
        for j in range(3, len(matrix[0])):
            if matrix[i][j] == "X" and matrix[i+1][j-1] == "M" and matrix[i+2][j-2] == "A" and matrix[i+3][j-3] == "S":
                ans += 1
            if matrix[i][j] == "S" and matrix[i+1][j-1] == "A" and matrix[i+2][j-2] == "M" and matrix[i+3][j-3] == "X":
                ans += 1
    
    return ans
    
if __name__ == "__main__":
    main()