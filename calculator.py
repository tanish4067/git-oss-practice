def divide(numerator, denominator):
    if denominator == 0:
        return ValueError
    
    return numerator / denominator
print(divide(10, 0))