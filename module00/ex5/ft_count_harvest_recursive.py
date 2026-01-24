def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    count = 1

    def rep(days, count):
        if count <= days:
            print("Day", count)
            count += 1
            rep(days, count)
    rep(days, count)
    print("Harvest time!")
