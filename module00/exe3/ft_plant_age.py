def ft_plant_age():
    num_days = int(input("Enter plant age in days: "))
    if (num_days > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
