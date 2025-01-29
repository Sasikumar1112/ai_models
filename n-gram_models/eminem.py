reader = open('./dataset/eminem.txt', 'r')
#successor map creation
n = 4
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
        if len(window) == n:
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
# print(successor_map)
print("original lyrics:\n")
org_s = "made a living and a killing off it ever since bill clinton was still in office with monica lewinsky feeling on his nutsack i'm an mc still as honest but as rude and as indecent as all hell syllables skill-a-holic kill 'em all with)"
print(org_s)
print("\nn: {}\n".format(n))

import random
sentence = 'Made a living and a killing off it Ever since Bill Clinton was still in office'
sentence ='if he is as'
out = ""
ip_words = sentence.lower().split(" ")
keys = []
for i in range(50):
    #random.seed(3)
    #print(keys)
    if len(keys) == n:
        if tuple(keys) not in successor_map:
            print("\nword combo not found in trained set")
            break
        successor_word = random.choice(successor_map[tuple(keys)])
        out += keys.pop(0)
        out += " "
        keys.append(successor_word)
    else:
        keys.append(ip_words[i])
print(out)