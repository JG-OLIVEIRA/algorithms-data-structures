def majority(vector, min, max):
    if(min == max):
        return vector[min]
    elif(max == min + 1):
        if(vector[min] == vector[max]):
            return vector[min]
    else:
        m = ((min + max)//2)
        left = majority(vector, min, m - 1)
        right = majority(vector, m + 1, max)
        return vector[left] if left == right else -1

vector1 = [1, 2, 1, 2, 1, 2, 1]

print(majority(vector1, 0, len(vector1) - 1))