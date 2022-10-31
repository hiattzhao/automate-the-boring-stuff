tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    
    colWidths = [0] * len(table)

    for i, row in enumerate(table):
        for col in row:
            if len(col) > colWidths[i]:
                colWidths[i] = len(col)

    # print (colWidths)

    for col in range(len(table[0])):
        for row in range(len(table)):
            print(table[row][col].rjust(colWidths[row]), end=' ')
        print()
    
printTable(tableData)