text = "я люблю море и завтра иду на море море"
words_counter = {}
for word in text.split():
    try:
        words_counter[word] += 1
    except KeyError:
        words_counter[word] = 1
print(words_counter)
top_wods = []
max = 0
for word, count in words_counter.items():
    if count > max:
        max = count
        max_word = word
print(max_word)

