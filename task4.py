def cyclic_shift(lst, n):
    if not lst:
        print("Список пустий.")
        return
    n = n % len(lst)
    for _ in range(n):
        shifted_element = lst.pop(-1)
        lst.insert(0, shifted_element)
        print(lst)

my_list = [1, 2, 3, 4, 5, 90, 0]
cyclic_shift(my_list, 3)

