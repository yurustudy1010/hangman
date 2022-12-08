def hangman(word):
    wrong = 0
    stages = ["",
            "1____________________",
            "2|                   ",
            "3|         |         ",
            "4|         O        D",
            "5|        /|\       E",
            "6|        / \       A",
            "7|                  T",
            "8|                  H"
            ]
    print("ハングマン行数＝" + str(len(stages)))
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print('ハングマンへようこそ！')
    while wrong < len(stages) - 1:
        print("\n")
        msg = '1文字を予想してね'
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong +=1
            print(' Ha Zu Re')
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print('You Win !')
            print("The answer was " + " ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You ROSE! The answer was {}".format(word))

Answer = 'cat'
print(type(Answer))

hangman(Answer)


