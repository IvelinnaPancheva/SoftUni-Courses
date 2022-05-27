number_of_words = int(input())
synonyms = dict()

for x in range(number_of_words):
    word = input()
    synonym_word = input()
    if word not in synonyms:
        synonyms[word] = []
        synonyms[word].append(synonym_word)
    else: # word exists as key in dictionary and already has list of values
        synonyms[word].append(synonym_word)

for key, value in synonyms.items():
    print(f"{key} - {', '.join(value)}")