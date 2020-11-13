Row1 = ['1', '2', '3']
Row2 = ['4', '5', '6']
Row3 = ['7', '8', '9']

b = 0
a = 0
XPlaced = False
OPlaced = False


def drawgame():
    print(f"     |     |")
    print(f"  {Row1[0]}  |  {Row1[1]}  |  {Row1[2]}  ")
    print(f"     |     |")
    print(f"- - - - - - - - -")
    print(f"     |     |")
    print(f"  {Row2[0]}  |  {Row2[1]}  |  {Row2[2]}  ")
    print(f"     |     |")
    print(f"- - - - - - - - -")
    print(f"     |     |")
    print(f"  {Row3[0]}  |  {Row3[1]}  |  {Row3[2]}  ")
    print(f"     |     |")
    print()


drawgame()


def win(winner):
    print(winner, 'has won')
    print()
    print('Congrats')
    exit()


def wincheck(who):
    # horizontal Check
    if Row1[0] == who and Row1[1] == who and Row1[2] == who:
        win(who)
    if Row2[0] == who and Row2[1] == who and Row2[2] == who:
        win(who)
    if Row3[0] == who and Row3[1] == who and Row3[2] == who:
        win(who)
    # horizontal Check

    # Vertical Check
    if Row1[0] == who and Row2[0] == who and Row3[0] == who:
        win(who)
    if Row1[1] == who and Row2[1] == who and Row3[1] == who:
        win(who)
    if Row1[2] == who and Row2[2] == who and Row3[2] == who:
        win(who)
    # Vertical Check

    # Diagonal Check
    if Row1[0] == who and Row2[1] == who and Row3[2] == who:
        win(who)
    if Row1[2] == who and Row2[1] == who and Row3[0] == who:
        win(who)
    # Diagonal Check

    # Tie
    Detect = True
    for i in Row1:
        if i in '123456789':
            Detect = False
    for i in Row2:
        if i in '123456789':
            Detect = False
    for i in Row3:
        if i in '123456789':
            Detect = False

    if Detect == True:
        print('How sad it\'s a tie')
        print()
        print('Try to win next time ok?')
        exit()
    # Tie


while True:
    XPlaced = False
    while XPlaced == False:
        while a < 1 or a > 9:
            a = int(input('Player X: where to place? '))
        Row = ((a - 1) // 3)
        Column = ((a - 1) % 3)

        if a >= 1 and a <= 3 and Row == 0 and Row1[Column] != 'X' and Row1[Column] != 'O':
            Row1[Column] = 'X'
            XPlaced = True

        if a >= 4 and a <= 6 and Row == 1 and Row2[Column] != 'X' and Row2[Column] != 'O':
            Row2[Column] = 'X'
            XPlaced = True

        if a >= 7 and a <= 9 and Row == 2 and Row3[Column] != 'X' and Row3[Column] != 'O':
            Row3[Column] = 'X'
            XPlaced = True
        a = 0

    drawgame()
    wincheck('X')

    OPlaced = False
    while OPlaced == False:
        while b < 1 or b > 9:
            b = int(input('Player O: where to place? '))
        Row = ((b - 1) // 3)
        Column = ((b - 1) % 3)

        if b >= 1 and b <= 3 and Row == 0 and Row1[Column] != 'X' and Row1[Column] != 'O':
            Row1[Column] = 'O'
            OPlaced = True

        if b >= 4 and b <= 6 and Row == 1 and Row2[Column] != 'X' and Row2[Column] != 'O':
            Row2[Column] = 'O'
            OPlaced = True

        if b >= 7 and b <= 9 and Row == 2 and Row3[Column] != 'X' and Row3[Column] != 'O':
            Row3[Column] = 'O'
            OPlaced = True
        b = 0

    drawgame()
    wincheck('O')
