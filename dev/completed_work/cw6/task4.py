# Задание 4
nums = '2 23 23 23 23 32 32 32 4'


def sum_matrix(a):

    matrix_new = []
    lo = 0

    ln = a.split()
    for i in ln:
        ln[ln.index(i)] = int(i)

    matrix_size = ln[0]
    ln.pop(0)

    if matrix_size**2*2 != int(len(ln)) or matrix_size < 2:
        print('Error!')
        exit()

    m = 0
    h = matrix_size

    j = int(len(ln)/2)

    for i in range(int(len(ln)/2)):
        while j != int(len(ln)):
            matrix_new.append(ln[i]+ln[j])
            j += 1
            break

    while lo != matrix_size:
        for p in range(m, h):
            print(matrix_new[p], end=' ')
        print('')
        m += matrix_size
        h += matrix_size
        lo += 1


sum_matrix(nums)
