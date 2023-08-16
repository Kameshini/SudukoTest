rows="ABCDEFGHI"
cols="123456789"

def cross (a, b):
    return[s+t for s in a for t in b]
boxes = cross (rows, cols)

#labels of boxes a1 - a9 is the top first row
boxes =['A1','A2','A3','A4','A5', 'A6','A7','A8','A9'
        'B1','B2','B3','B4','B5', 'B6','B7','B8','B9'
        'C1','C2','C3','C4','C5', 'C6','C7','C8','C9'
        'D1','D2','D3','D4','D5', 'D6','D7','D8','D9'
        'E1','E2','E3','E4','E5', 'E6','E7','E8','E9'
        'F1','F2','F3','F4','F5', 'F6','F7','F8','F9'
        'G1','G2','G3','G4','G5', 'G6','G7','G8','G9'
        'H1','H2','H3','H4','H5', 'H6','H7','H8','H9'
        'I1','I2','I3','I4','I5', 'I6','I7','I8','I9']

#for units
row_units=[cross (r, cols) for r in rows]
#row_units [0] = ['A1, A2', 'A3' ...]
#will display top most row

col_units=[cross(rows, c)for c in cols]
#col_units[0] = ['A1', 'B1', 'C1' ...]
#will display left most column

square_units=[cross (rs, cs)for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
#this will display a square of 9 blocks
#square units [0]=['A1','A2','A3,'B1','B2','B3','C1','C2','C3']
#calling [0] will display the top left square

unitlist=row_units+col_units+square_units

def GridValues(puzzle_string):
    grid={}#initialise the grid dictionary

    #loop through each box and set initial values
    for box, value in zip (boxes, puzzle_string):
        if value.isdigit(): #stating if statement on if the value are digits
            grid[box]=value #then set box value to a digit
        else:
            grid[box] = '.' #if not a digit then add a .
    return grid #show my grid


#example of the grid in use
puzzle_string="..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3.."
grid=GridValues(puzzle_string)
print(grid)