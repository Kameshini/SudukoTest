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
peers={box: set() for box in boxes}
for unit in unitlist:
    for box in unit:
        peers[box].update(unit)

def grid_values(grid):
    values = []
    all_digits = '123456789'
    for c in grid:
        if c == '.':
            values.append(all_digits)
        elif c in all_digits:
            values.append(c)
    assert len(values) == 81
    result = dict(zip(boxes, values))
    return result

def eliminate(values):
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit,'')
    return values

#only choice
#if there is only one box which would allow a certain digit then that box must be assigned that digit
def only_choice(values):
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        # Use the Eliminate Strategy
        values = eliminate(values)
        # Use the Only Choice Strategy
        values = only_choice(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values