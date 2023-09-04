
def find_word_horizontal(crossword, word):
    out_lst = []
    for i in range(len(crossword)):
        for j in range(len(crossword[i])):
            for k in range(len(word)):
                if word[k] == crossword[i][j]:
                    if k == len(word)-1:
                        out_lst.append(j-1)
                        out_lst.append(i-1)
                    else:
                        j += 1
                else:
                    break
    print(out_lst)
def find_word_vertical(crossword, word):
    out_lst = []
    for i in range(len(crossword)):
        for j in range(len(crossword[i])):
            for k in range(len(word)):
                if word[k] == crossword[i][j]:
                    if k == len(word)-1:
                        out_lst.append(j)
                        out_lst.append(i)
                    else:
                        i += 1
                else:
                    break
    print(out_lst)


crossword = [['s','d','o','g']
            ,['c','u','c','m']
            ,['a','c','a','t']
            ,['t','e','t','k']]

word = 'cat'
find_word_horizontal(crossword, word)
find_word_vertical(crossword, word)