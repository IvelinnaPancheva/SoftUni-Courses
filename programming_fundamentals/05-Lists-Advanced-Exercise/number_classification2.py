def positive_seq(number_sequence):
    positive = [str(x) for x in number_sequence if x >= 0]
    return f"Positive: {', '.join(positive)}"


def negative_seq(number_sequence):
    negative = [str(x) for x in number_sequence if x < 0]
    return f"Negative: {', '.join(negative)}"


def even_seq(number_sequence):
    even = [str(x) for x in number_sequence if x % 2 == 0]
    return f"Even: {', '.join(even)}"


def odd_seq(number_sequence):
    odd = [str(x) for x in number_sequence if x % 2 != 0]
    return f"Odd: {', '.join(odd)}"


number_seq = input().split(", ")
number_seq = [int(x) for x in number_seq]
print(f"{positive_seq(number_seq)}")
print(f"{negative_seq(number_seq)}")
print(f"{even_seq(number_seq)}")
print(f"{odd_seq(number_seq)}")

