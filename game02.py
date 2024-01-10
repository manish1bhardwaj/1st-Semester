def display(x):
   print('''
{0}| {1} |{2}
___| ___ |___
{3}| {4} |{5}
___| ___ |___
{6}| {7} |{8}
   |     |
'''.format(*x))
   
#main code
move = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
display(move)
turn = 'X'
while 1:
    input1 = int(input(f'{turn} Turn index location 0-8:'))
    if move[input1]!=' ':
        print('location already used \n try amother location')
        continue
    else:
        move[input1] = turn
    display(move)
    if move[0] == move[4] == move[8]   !=' ':
        print(f'(move[0]) win')
        break
    if move[0] == move[3] == move[6]   !=' ': 
        print(f'(move[0]) win')
        break
    if move[0] == move[1] == move[2]   !=' ': 
        print(f'(move[0]) win')
        break
    if move[3] == move[4] == move[6]   !=' ': 
        print(f'(move[3]) win')
        break
    if move[6] == move[7] == move[8]   !=' ': 
        print(f'(move[6]) win')
        break
    if move[1] == move[4] == move[7]   !=' ': 
        print(f'(move[1]) win')
        break
    if move[2] == move[5] == move[8]   !=' ': 
        print(f'(move[2]) win')
        break
    if move[2] == move[4] == move[6]   !=' ': 
        print(f'(move[2]) win')
        break
   
    if ' ' not in move:
        print("tie")
        break
    turn = '0' if turn == 'X' else 'X'