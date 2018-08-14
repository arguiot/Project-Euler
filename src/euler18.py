import time

tri_num=[]

tri_num.append('75'.split(' '))
tri_num.append('95 64'.split(' '))
tri_num.append('17 47 82'.split(' '))
tri_num.append('18 35 87 10'.split(' '))
tri_num.append('20 04 82 47 65'.split(' '))
tri_num.append('19 01 23 75 03 34'.split(' '))
tri_num.append('88 02 77 73 07 63 67'.split(' '))
tri_num.append('99 65 04 28 06 16 70 92'.split(' '))
tri_num.append('41 41 26 56 83 40 80 70 33'.split(' '))
tri_num.append('41 48 72 33 47 32 37 16 94 29'.split(' '))
tri_num.append('53 71 44 65 25 43 91 52 97 51 14'.split(' '))
tri_num.append('70 11 33 28 77 73 17 78 39 68 17 57'.split(' '))
tri_num.append('91 71 52 38 17 14 91 43 58 50 27 29 48'.split(' '))
tri_num.append('63 66 04 68 89 53 67 30 73 16 69 87 40 31'.split(' '))
tri_num.append('04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'.split(' '))

x, y = 0, 0
for i in tri_num:
  y = 0
  for j in i:
    tri_num[x][y] = int(j)
    y += 1
  
  x+= 1
    
for i in range(len(tri_num)-1,-1,-1):
  for j in range(0,i):
    maximum = max(tri_num[i][j],tri_num[i][j+1])
    tri_num[i-1][j] += maximum

start = time.time()
answer = tri_num[0][0]
end = time.time()

total = end - start
print('Problem 18: ' + str(answer) + '\nDone in ' + str(total) + ' seconds.')

# Problem 18: 1074
# Done in 1.9073486328125e-06 seconds.
