import random


def num_gen(last_num):
    list_num = [*range(1, last_num + 1, 1)]
    rand_num = random.choice(list_num)
    return rand_num


last_raceno = int(input("What is the number of the last race "))
raceno = num_gen(last_raceno)
print(raceno)


def race_list():
    horse_list = []

    horses = int(input(f"Enter last horse number in {raceno}: "))
    horse_list = [*range(1, horses + 1, 1)]

    # print(horse_list)

    scratch_str = input("Enter horse numbers scratched seperated by a space: ")
    scratch_list = scratch_str.split()
    scratch_list = [int(i) for i in scratch_list]
    x = 0
    # print(scratch_list)

    while x < len(scratch_list):
        # print(x)
        horse_list.remove(scratch_list[x])
        x += 1
    return horse_list


horses_list = race_list()
trifecta = random.sample(horses_list, 5)
print(f"The box trifecta today is in Race {raceno} and the numbers are {trifecta}\n")

quinella = random.choice(horses_list)
print(f"Roughie to take with second favourite for the Quinella: {quinella}")


def horse_gen(leg_horses):
    horse = random.choice(leg_horses)
    return horse


print("Now let's put the Quaddie on \n")
raceno = int(input("Enter the First Leg Race No: \n"))
first_leg_horses = race_list()
first_leg = horse_gen(first_leg_horses)
raceno = int(input("Enter the Second Leg Race No: \n"))
second_leg_horses = race_list()
second_leg = horse_gen(second_leg_horses)
raceno = int(input("Enter the Third Leg Race No: \n"))
third_leg_horses = race_list()
third_leg = horse_gen(third_leg_horses)
raceno = int(input("Enter the Fourth Leg Race No: \n"))
fourth_leg_horses = race_list()
fourth_leg = horse_gen(fourth_leg_horses)

print(f"Today's quadrella is {first_leg}, {second_leg}, {third_leg}, {fourth_leg}")
