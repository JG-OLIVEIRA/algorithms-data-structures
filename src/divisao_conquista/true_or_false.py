def true_or_false(vector, q, max):
    if(vector[max] == 'F'):
        return true_or_false(vector, q + 1, max - 1)
    else:
        return q

vector1 = ["V", "V", "V", "V", "F", "F", "F"]
vector2 = ["V", "V", "V"]

print(true_or_false(vector1, 0, len(vector1) - 1))
print(true_or_false(vector2, 0, len(vector2) - 1))