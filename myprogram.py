import sys

def main(*args):
    for fileName in args[0]:
        print(fileName)
        openTestFileByName(fileName)
    return


def openTestFileByName(fileName):
    try:
        f = open(f'./tests/{fileName}.txt')
    except OSError:
        print("Could not open/read file:", fileName)
        sys.exit()
    with f:
        rows, cols = [int(x) for x in next(f).split()]
        matrix = [[x for x in line.split()] for line in f]
        print('Longest adjacent sequence is: ', findLongestAdjSeq(rows, cols, matrix))
        print('\n')
        
        
def findLongestAdjSeq(rows, cols, matrix):
    maxSequence = 0
    hasVisited = fillMatrixWithSymbols(False, rows, cols)
    stack = []
    
    for row in range(rows):
        for col in range(cols):
            if hasVisited[row][col]:
                continue
            
            stack.append([row, col])
            seqLength = 0
            
            while stack:
                currentIndexes = stack.pop()
                currentRow = currentIndexes[0]
                currentCol = currentIndexes[1]

                if (hasVisited[currentRow][currentCol]):
                    continue
                
                current = matrix[currentRow][currentCol]
                hasVisited[currentRow][currentCol] = True
                seqLength += 1

                for dir in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    nextRow = currentRow + dir[0];
                    nextCol = currentCol + dir[1];

                    if nextRow < 0 or nextRow >= rows:
                        continue
                    if nextCol < 0 or nextCol >= cols:
                        continue
                    if hasVisited[nextRow][nextCol]:
                        continue
                    
                    adjacent = matrix[nextRow][nextCol]
                    
                    if current == adjacent:
                        stack.append([nextRow, nextCol])

            if seqLength > maxSequence:
                maxSequence = seqLength
            
    return maxSequence


def fillMatrixWithSymbols(symbol, rows, cols):
    return [[symbol] * rows for i in range(cols)]


if __name__ == "__main__":
    main(sys.argv[1:])

#main(['test1'])
#main(['test1', 'test2'])
#main(['test1', 'test2', 'test3'])
