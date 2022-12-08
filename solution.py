"""
author: Jorge Armando Salas Martinez
modified: 12/8/2022
"""
def main():
    filename = input("enter the filename: ")
    A = getData(filename)
    
    if filename == None:
        print("filename not found or has bad data")
        return
    
    value = solution(A)
    print(value)


def solution(A, i=0, j=0, current_sum = 0):
    if i > len(A) - 1:
        return current_sum
    
    value = A[i][j]

    if len(A) == 1:
        return value
    
    a = solution(A, i + 1, j, value + current_sum)
    b = solution(A, i + 1, j + 1, value + current_sum)

    if a > b:
        return a
    return b


def getData(filename):
    with open(filename, "r") as file:
        data = []
        expected_length = 1
        for line in file:
            line = line.strip()
            line = line.split(" ")
            if len(line) != expected_length:
                return None
            line = list(map(lambda x: int(x), line))
            data.append(line)
            expected_length = expected_length + 1
        return data
    return None

main()
