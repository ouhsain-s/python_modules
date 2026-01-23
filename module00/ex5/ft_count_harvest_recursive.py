def ft_count_harvest_recursive(numdays: int = -1):
    is_last_print = -1
    if (numdays < 0):
        numdays = int(input("Days until harvest: "))
        is_last_print = 1
    if (numdays > 1):
        ft_count_harvest_recursive(numdays - 1)
    if (numdays > 0):
        print(f"Day {numdays}")
    if (is_last_print != -1):
        print("Harvest time!")
