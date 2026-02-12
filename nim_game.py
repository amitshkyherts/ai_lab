total_sticks = 13


def nim(current_sticks):
    num = current_sticks % 4
    if num == 0:
        num = 3

    return num


while (total_sticks):
    print(f"remaining sticks: {total_sticks}")
    num_sticks = int(input("pick either 1, 2, or 3 sticks: "))
    if num_sticks < 0 or num_sticks > 3:
        print("invalid num of sticks picked, try again")
        continue

    total_sticks -= num_sticks
    if total_sticks == 0:
        print("you win!")

    computer = nim(total_sticks)
    print(f"the computer picked: {computer}")
    total_sticks -= computer
    if total_sticks == 0:
        print("computer wins!")

