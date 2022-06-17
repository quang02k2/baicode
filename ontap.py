import numpy as np
import os
import shutil


# bai4.5

#
# def doc(x):
#     with open(x,mode='r') as f:
#         n,m = map(int,f.readline().split())
#         print(n,' ',m)
#         for i in range(n):
#             print(f.readline().split(),end='')
#
#
# def gan_bien(x):
#     with open(x,mode='r') as f:
#         n,m  = map(int,f.readline().split())
#         a = []
#         for i in range(n):
#             x = f.readline().split()
#             for j in range(m):
#                 x[j] = float(x[j])
#                 a.append(x)
#         a = np.array(a)
#     return n,m, a
#
#
# def sum_0(n,m,a):
#     dem = 0
#     for i in range(n):
#         for j in range(m):
#             if a[i][j] == 0:
#                 dem +=1
#     return dem
#
#
# def tbc(a,col):
#     k = 0.0
#     for i in range(len(a)):
#         k += a[i][col]
#     return k/len(a[0])
#
#
# def thay_the(n,m,a):
#     for i in range(m):
#         h = tbc(a,i)
#         for j in range(n):
#             if a[j][i] == 0:
#                 a[j][i] = h
#     return a
#
#
# def file(d,a):
#     with open(d,mode='w') as f:
#         f.write(str(len(a)) + ' ')
#         f.write(str(len(a[0])) + '\n')
#         for i in range(len(a)):
#             for j in range(len(a[0])):
#                 f.write(str(a[i][j]) + ' ')
#             f.write('\n')
#
#
#
# def saves(file1, file2,a):
#     with open(file1,mode='w') as f:
#         f.write(str(100) + ' ')
#         f.write(str(len(a[0])) + '\n')
#         for i in range(100):
#             for j in range(len(a[0])):
#                 f.write(str(a[i][j]) + ' ')
#             f.write('\n')
#     with open(file2,mode='w') as f:
#         f.write(str(len(a)-100) + ' ')
#         f.write(str(len(a[0])) + '\n')
#         for i in range(len(a)-100):
#             for j in range(len(a[0])):
#                 f.write(str(a[i][j]) + ' ')
#             f.write('\n')
#
#
# def main():
#     x = 'D:/DATA45.data'
#     n,m,a = gan_bien(x)
#     aa = thay_the(n,m,a)
#     d = 'D:/image2.txt'
#     file(d,a)
#     file1 = 'D:/file1.txt'
#     file2 = 'D:/file2.txt'
#     saves(file1,file2,a)
#     os.mkdir('D:/THUMUC1')
#     shutil.copy('D:/image2.txt','D:/THUMUC1')
#     os.remove('D:/image2.txt')
#
#
# main()





# bai 5.4


def












