def suma(*numeros):
    total = 0
    for n in numeros:
        total += n
    return total
message = suma(6, 4, 10, 20, 4, 6, 7)
print(message)