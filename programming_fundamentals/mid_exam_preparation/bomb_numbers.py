number_sequence = input().split(" ")
number_sequence = list(map(int, number_sequence))
special_numbers = input().split(" ")
special_numbers = list(map(int, special_numbers))
bomb = special_numbers[0]
neighbors = special_numbers[1]

while True:
    # condition to break loop - bomb was detonated
    if bomb not in number_sequence:
        print(sum(number_sequence))
        break
    # bomb found in number sequence
    else:
        index = number_sequence.index(bomb)
        if 0 <= index - neighbors <= index + neighbors < len(number_sequence):
            number_sequence = number_sequence[0:index - neighbors] + number_sequence[index + neighbors+1::]
        # left numbers < remaining indices, start from 0 index
        elif index - neighbors < 0 and index + neighbors < len(number_sequence):
            number_sequence = number_sequence[index + neighbors + 1::]
        # right numbers < remaining indices, iterate until len -1 incl.
        elif 0 <= index - neighbors and index + neighbors > len(number_sequence) - 1:
            number_sequence = number_sequence[0:index - neighbors]
        elif index - neighbors < 0 and index + neighbors > len(number_sequence) - 1:
            number_sequence.clear()
