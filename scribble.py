import sys

if len(sys.argv) < 2:
    print('Please enter length as the first argument')
    sys.exit()

def get_words():
    res = []
    with open('words_alpha copy.txt', 'r') as f:
        for word in f.readlines():
            if len(word) == int(sys.argv[1]) + 1:
                res.append(word.strip())
    return res

list = get_words()
res = list[:]

while True:
    tmp = []
    prompt = input('Enter a letter and position, spacebar to list all words, 0 to restart or ! to quit: ')
    if prompt == '!':
        sys.exit()
    if prompt == '0':
        res = list
        continue
    if prompt == ' ':
        print(list)
        continue
    if not len(prompt) == 2:
        print('Wrong input')
        continue
    letter, position = [*prompt]
    if not isinstance(letter, str) or not position.isnumeric():
        print('Wrong input')
        continue
    position = int(position) - 1
    for word in res:
        if letter == word[position]:
            tmp.append(word)
    res = tmp
    print(res)
    
    