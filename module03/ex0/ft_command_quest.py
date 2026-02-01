import sys

print("=== Command Quest ===")
if len(sys.argv) == 1:
    print("No arguments provided!")
print("Program name:", sys.argv[0])
if len(sys.argv) > 1:
    print("Arguments received:", len(sys.argv) - 1)
    num = 0
    for current in sys.argv:
        if num > 0:
            print(f"Argument {num}:", current)
        num += 1
print("Total arguments:", len(sys.argv))
