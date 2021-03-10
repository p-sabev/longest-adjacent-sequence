def longestColorsAdjSequence():
    with open('./tests/test4.txt') as f:
        rows, columns = [int(x) for x in next(f).split()]
        matrix = [[x for x in line.split()] for line in f]
    
    print(rows)
    print(columns)
    print(matrix)
    
    return;

longestColorsAdjSequence();
