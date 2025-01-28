reader = open('./dataset/eminem.txt', 'r')
#successor map creation
successor_map = {}
window = []
punctuation = '.;,-“’”:?—‘!()_[]'
for lines in reader:
    if lines == "\n" or "chorus" in lines.lower():
        continue
    for word in lines.split(" "):
        clean_word = word.strip(punctuation).lower()
        if "\n" in clean_word:
            clean_word = clean_word.replace("\n","")
        if len(window) == 2:
            key = tuple(window)
            value = clean_word
            if key not in successor_map:
                successor_map[key] = [clean_word]
            else:
                successor_map[key].append(value)
            window.append(clean_word)
            window.pop(0)
        else:
            window.append(clean_word)

#print(successor_map)
import random
word = "fuck"
word1 = "you"
for i in range(50):
    #random.seed(3)
    print(word,end=" ")
    key_tuple = (word, word1)
    if key_tuple not in successor_map:
        print("word combo not found in trained set")
        break
    successor_word = random.choice(successor_map[key_tuple])
    word,word1 = word1,successor_word
    