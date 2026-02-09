n = 0
while n < 11:
    v = 0
    print(f"Table de {n}: ", end="")
    while v < 11:
        print(f"{n*v} ", end="")
        v+=1
    print()
    n+=1
