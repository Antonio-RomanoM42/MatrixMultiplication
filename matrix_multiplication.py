def inputMatrix(row,col):
    mat = []
    for k in range(row):
        mat.append([])
        for j in range(col):
            while True:
                value = input("Insert value: ")
                if not value.isdigit():
                    print("Invalid value, try again.")
                    continue
                else:
                    break
            value = int(value)
            mat[k].append(value)
    return mat


def getMatrixProduct(a,b):
    num = []
    for k in range(len(a)):
        num.append([])
        for j in range(len(b[0])):
            num[k].append(sum([a[k][i]*b[i][j] for i in range(len(a[0]))]))
    return num
  

def check_row_col():
    while True:
        row = input("Insert number of rows: ")
        if not row.isdigit() or int(row) <= 0:
            print("Invalid. Please try again.")
            continue
        else:
            break
    row = int(row)
    while True:
        col = input("Inser number of columns: ")
        if not col.isdigit() or int(col) <= 0:
            print("Invalid. Please try again.")
            continue
        else:
            break
    col = int(col)
    return row,col


def graphics(mat):
    for row in mat:
        print('|',end = ' ')
        for col in row:
            print(col,end = ' ')
        print('|',end = '\n')


if __name__ == "__main__":
    while True:
        print("First matrix.")
        (row1,col1) = check_row_col()
        print("Second matrix.")
        (row2,col2) = check_row_col()
        if col1 != row2:
            print("Invalid dimensions: columns of 1st matrix must be equal to row of 2nd matrix.")
            continue
        else:
            break

    print("First matrix values")
    a = inputMatrix(row1,col1)
    graphics(a)
    print("Second matrix values")
    b = inputMatrix(row2,col2)
    graphics(b)
    result = getMatrixProduct(a,b)
    print("\nResult:")
    graphics(result)
