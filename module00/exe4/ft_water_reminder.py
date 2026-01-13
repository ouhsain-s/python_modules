def ft_water_reminder():
    last_day = int(input("Days since last watering: "))
    if (last_day > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")