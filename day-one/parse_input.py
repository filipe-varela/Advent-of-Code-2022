from pprint import pprint


def main():
    with open("day-one\\input.txt", "r") as input_txt:
        data = input_txt.read()
    data = data.split("\n")
    elfs = []
    elf = []
    for i in data:
        if not i:
            elfs.append(elf.copy())
            elf.clear()
        else:
            elf.append(int(i))
    calories_per_elf = [sum(i) for i in elfs]
    first_max_elf = calories_per_elf.pop(calories_per_elf.index(max(calories_per_elf)))
    second_max_elf = calories_per_elf.pop(calories_per_elf.index(max(calories_per_elf)))
    third_max_elf = calories_per_elf.pop(calories_per_elf.index(max(calories_per_elf)))
    print(sum([first_max_elf, second_max_elf, third_max_elf]))


if __name__ == "__main__":
    main()
