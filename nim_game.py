total_sticks = 13


def nim(num_sticks):
    # player's turn
    global total_sticks
    total_sticks -= num_sticks

    # computer's turn
    num = total_sticks % 4
    if num == 0:
        num = 1

    total_sticks = total_sticks - num
    return num


while (total_sticks):
    print(f"remaining sticks: {total_sticks}")
    n = int(input("pick: "))

    if n < 0 or n > 3:
        print("invalid num of sticks picked, try again")
        continue

    print(f"the computer picked: {nim(n)}")
