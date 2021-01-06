with open("../files/example.txt", "r") as file:
    print(file.read())
    # No need to call close method

print("\n", 20 * "=", "\n")

with open("../files/example.txt", "r") as file:
    for line in file.readlines():
        # Break line fix end=""
        print(line)
