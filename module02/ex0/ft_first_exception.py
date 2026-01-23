def check_temperature(temp_str: str):
    try:
        temp = int(temp_str)
        if (0 <= temp <= 40):
            return (f"Temperature {temp}°C is perfect for plants!")
        elif (temp > 40):
            return (f"Error: {temp}°C is too hot for plants (max 40°C)")
        else:
            return (f"Error: {temp}°C is too cold for plants (min 0°C)")
    except ValueError:
        return (f"Error: '{temp_str}' is not a valid number")


def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    print(end="\n")

    print("Testing temperature: 25")
    print(check_temperature("25"))
    print(end="\n")
    print("Testing temperature: abc")
    print(check_temperature("abc"))
    print(end="\n")
    print("Testing temperature: 100")
    print(check_temperature("100"))
    print(end="\n")
    print("Testing temperature: -50")
    print(check_temperature("-50"))
    print(end="\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
