import re

text = input()

pairs_pattern = r"#[A-Za-z]{3}[A-Za-z]*##[A-Za-z]{3}[A-Za-z]*#|@[A-Za-z]{3}[A-Za-z]*@@[A-Za-z]{3}[A-Za-z]*@"
matches = re.findall(pairs_pattern, text)

valid_mirror_words = []
if matches:
    for match in matches:
        x = int(len(match) / 2)
        first_word = match[0:x]
        second_word = match[x:]
        if first_word == "".join(reversed(second_word)):
            valid_mirror_words.append(first_word)
            valid_mirror_words.append(second_word)

    print(f"{len(matches)} word pairs found!")

else:
    print(f"No word pairs found!")

if len(valid_mirror_words) > 0:
    output_pairs = []

    print("The mirror words are:")
    for i in range(0, len(valid_mirror_words), 2):
        valid_mirror_words[i] = valid_mirror_words[i].replace("@", "")
        valid_mirror_words[i] = valid_mirror_words[i].replace("#", "")
        valid_mirror_words[i+1] = valid_mirror_words[i+1].replace("#", "")
        valid_mirror_words[i+1] = valid_mirror_words[i+1].replace("@", "")
        output_pairs.append(f"{valid_mirror_words[i]} <=> {valid_mirror_words[i + 1]}")

    print(", ".join(output_pairs))
else:
    print("No mirror words!")
