# function stub
# When referring to cell address, the subscripts must be in the correct
# format.  Because of how the arrays are defined, the index order
# is [row][col], not [col][row]
#     print(m1[2][1])   # Correct way to refer to a matrix element
#     print(m2[2,1])    # Incorrect -- will result in a syntax error

def mmult(a, b):
    print("Multiplying two matrices:")
    print(a)
    print(b)
    c = []
    numMults = 0
    # insert matrix multiplication code here
    for i in range(len(a)):
        for j in range(len(b)):
            add=a[i][0]*b[0][j]+a[i][1]*b[1][j]
            numMults += 2
            c.append(add)
    # print results and return answer 
    print("Result:")
    print(c)
    print("# multiplications:",numMults)
    return c


# Matrix Multiplication function test 1
m1 = [# c0 c1
       [ 1, 2],   # r0
       [ 3, 4]    # r1
     ]
m2 = [# c0 c1
       [ 4, 1],   # r0
       [ 6, 8],   # r1
     ]
m1x2 = mmult(m1, m2)

# Matrix Multiplication function test 2
m3 = [# c0 c1 c2
       [ 1, 2, 3],   # r0
       [ 4, 5, 6],   # r1
       [ 7, 8, 9]    # r2
     ]
m4 = [# c0 c1 c2
       [ 3, 4, 5],   # r0
       [ 8, 6, 4],   # r1
       [ 7, 6, 2]    # r2
     ]
#m3x4 = mmult(m3, m4)

# Matrix Multiplication function test 3
m5 = [# c0 c1 c2 c3
       [ 1, 2, 3, 4],   # r0
       [ 5, 6, 7, 8],   # r1
       [ 9, 0, 1, 2],   # r2
       [ 3, 1, 4, 5]    # r3
     ]
m6 = [# c0 c1 c2 c3
       [ 3, 4, 5, 2],   # r0
       [ 8, 6, 4, 9],   # r1
       [ 7, 6, 2, 1],   # r2
       [ 5, 9, 2, 0]    # r3
     ]
#m5x6 = mmult(m5, m6)

