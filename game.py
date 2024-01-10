move = ['','','','','','','','','']
format_display = '''

{0}| {1} |{2}
___| ___ |___
{3}| {4} |{5}
___| ___ |___
{6}| {7} |{8}
   |     |
'''.format(*move)
print(format_display)

for i in range(4):
    turn = 'X'
    input1 = int(input(f'{turn})Turn index location:'))
    move[input1]=turn

    format_display = '''

{0}| {1} |{2}
___| ___ |___
{3}| {4} |{5}
___| ___ |___
{6}| {7} |{8}
   |     |
'''.format(*move)
    print(format_display)
    turn = 'O'
    input1 = int(input(f'{turn})Turn index location:'))
    move[input1]=turn
    format_display = '''

    {0}| {1} |{2}
    ___| ___ |___
    {3}| {4} |{5}
    ___| ___ |___
    {6}| {7} |{8}
       |     |

      '''
    format_display = '''

    {0}| {1} |{2}
    ___| ___ |___
    {3}| {4} |{5}
    ___| ___ |___
    {6}| {7} |{8}
      |     |
    '''.format(*move)
    print(format_display)

