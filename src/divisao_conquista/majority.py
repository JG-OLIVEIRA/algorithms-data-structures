def majority(vector, min, max):
    q = 0
    for i in range(max):
        if(vector[i] == vector[min]):
            q = q + 1
    if(q > ((max)//2)):
        return vector[min]
    else:
        return majority(vector, min + 1, max)