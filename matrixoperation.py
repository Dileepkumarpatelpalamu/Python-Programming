rows = int(input("Enter no of rows :"))
cols = int(input("Enter no of cols :"))
matrix = []
for i in range(rows):
    l =[]
    for j in range(cols):
        x=int(input("Enter "+str(i+1)+" rows "+str(j+1)+" Element : "))
        l.append(x)
    matrix.append(l)
print(matrix)

# Write a program for sum of matrix
add = 0
for i in range(rows):
    for j in range(cols):
        add = add + matrix[i][j]
print("Sum of matrix :",add)

# Write a program for sum of each rows
for i in range(rows):
    add = 0
    for j in range(cols):
        add = add+matrix[i][j]
    print("Sum of "+str(i+1)+" rows = "+str(add))
# Writ a program for pdig of matrix
add = 0 
for i in range(rows):
    for j in range(cols):
        if i == j:
            add = add + matrix[i][j]
print("Sum of PDIG of matrix : ",add)
# Write a program for rev PDIG of Matrix
add = 0
for i in range(rows):
    for j in range(cols):
        if i+j == cols-1:
            add = add + matrix[i][j]
print("Sum of rev PDIG :", add)
# Write a program to sum each colomns of matrix
"""
00 01 02
10 11 12
20 21 22
"""
for i in range(rows):
    add = 0
    for j in range(cols):
        add = add + matrix[j][i]
    print("Sum of "+str(i+1)+" columns "+str(add))
# Write a program to print transpose of matrix
print("Transpose Before of Matrix :")
print(matrix)
print("Transpose After of Matrix :")
trans = []
for i in range(rows):
    l =[]
    for j in range(cols):
        x = matrix[j][i]
        l.append(x)
    trans.append(l)
print(trans)



