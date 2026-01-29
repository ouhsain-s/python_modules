def garden_operations(err_type: str):

    if err_type == "ValueError":
        try:
            num = int("invalid input")
        except ValueError:
            return "Caught ValueError: invalid literal for int()"
    elif err_type == "ZeroDivisionError":
        try:
            num = 21 / 0
        except ZeroDivisionError:
            return "Caught ZeroDivisionError: division by zero"
    elif err_type == "FileNotFoundError":
        try:
            file = open("missing.txt", "r")
            file.close()
        except FileNotFoundError:
            return ("Caught FileNotFoundError: No such file 'missing.txt'")
    elif err_type == "KeyError":
        try:
            dec = {"flower": "orkeda", "three": "Oka"}
            p = dec["plant"]
            print(p, end="")
        except KeyError:
            return ("Caught KeyError: 'missing\\_plant'")
    elif err_type == "multiple":
        try:
            dec = {"t": "t"}
            num = int(dec["abc"])
            num / 0
        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
            return ("Caught an error, but program continues!")


def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    print("Testing ValueError...")
    print(garden_operations("ValueError"))
    print(end="\n")
    print("Testing ZeroDivisionError...")
    print(garden_operations("ZeroDivisionError"))
    print(end="\n")
    print("Testing FileNotFoundError...")
    print(garden_operations("FileNotFoundError"))
    print(end="\n")
    print("Testing KeyError...")
    print(garden_operations("KeyError"))
    print(end="\n")
    print("Testing multiple errors together...")
    print(garden_operations("multiple"))
    print(end="\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
