for i in range (2,21):
    with open(f"tables/Multiplication_of_{i}.txt", "w") as k:
        for j in range(1,11):
            k.write(f"{i}x{j}={i*j}")
            if j!=10:
                k.write('\n')
