import os
import numpy as np
import matplotlib.pyplot as plt

def DoubleSort(A, B):
    for i in range(0, len(A)):
      for j in range(i+1,len(A)):
        if (A[i]<A[j]):
          t = A[i]
          A[i] = A[j]
          A[j] = t
  
          t = B[i]
          B[i] = B[j]
          B[j] = t

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

file = r'D:\UITSe\HK5\Datasets\cifar-10-python\cifar-10-batches-py\data_batch_1'
data_batch_1 = unpickle(file)

# create figure
fig = plt.figure(figsize=(16, 12))
# setting values to rows and column variables
rows = 2
columns = 6


image = data_batch_1[b'data'][8]
unique = image.reshape(3,1024) #3 matrix 32x32
unique = unique.transpose(1,0) # 32 32x3

unique, count = np.unique(unique, return_counts=True, axis=1)
DoubleSort(count, unique)
for i in range(0, 5):
   print(unique[i])
image = image.reshape(3,32,32)
image = image.transpose(1, 2, 0)
plt.imshow(image)
plt.show()
plt.imshow([[unique[i] for i in range(0, 5)]])
plt.show()

# for index in range (0, 12):
#     image = data_batch_1[b'data'][index]
#     unique = image.reshape(1024, 3)
#     image = image.reshape(3,32,32) #3 matrix 32x32
#     aver = aveg = aveb = 0
#     for i in range (0, 32):
#         for j in range (0, 32):
#             aver += image[0][i][j]
#             aveg += image[1][i][j]
#             aveb += image[2][i][j]
#     aver /= 1024
#     aveg /= 1024
#     aveb /= 1024
#     print(index)
#     print(int(aver))
#     print(int(aveg))
#     print(int(aveb))
#     image = image.transpose(1, 2, 0)
#     fig.add_subplot(rows, columns, index + 1)
#     plt.imshow(image)
# plt.show()
# plt.imshow([[[int(aver), 0, 0], [0, int(aveg), 0], [0, 0, int(aveb)]]])

# temp = [image[0], [[0] * 32] * 32, [[0] * 32] * 32]
# temp = (np.array(temp)).transpose(1,2,0) 
# temp2 = [
#    [[0] * 32] * 32, image[1], [[0] * 32] * 32]
# temp2 = (np.array(temp2)).transpose(1,2,0) 
# temp3 = [
#    [[0] * 32] * 32, [[0] * 32] * 32, image[2]]
# temp3 = (np.array(temp3)).transpose(1,2,0) 
# image = image.transpose(1,2,0) #32 matrix 32x3
# plt.imshow(image)
# plt.show()
# fig.add_subplot(rows, columns, 1)
# plt.imshow(temp)
# fig.add_subplot(rows, columns, 2)
# plt.imshow(temp2)
# fig.add_subplot(rows, columns, 3)
# plt.imshow(temp3)
# plt.show()

# plt.imshow(unique)
# plt.show()

# Feats = AVEmethod(data_batch_1)
# fig.add_subplot(rows, columns, 1)
# # image = data_batch_1[b'data'][2]
# # image = image.reshape(3,32,32)[0] #3 matrix 32x32
# # image = image.transpose(1,2,0) #32 matrix 32x3
# plt.imshow(data_batch_1[3])
# print(len(data_batch_1[b'data']))


# fig.add_subplot(rows, columns, 2)
# # image1 = data_batch_1[b'data'][2]
# # image1 = image1.reshape(3,32,32)[1] #3 matrix 32x32
# # image1 = image1.transpose(1,2,0) #32 matrix 32x3
# plt.imshow(Feats[5], cmap='gray')
# plt.axis('off')


# fig.add_subplot(rows, columns, 3)
# # image1 = data_batch_1[b'data'][2]
# # image1 = image1.reshape(3,32,32)[2] #3 matrix 32x32
# # image1 = image1.transpose(1,2,0) #32 matrix 32x3
# plt.imshow(Feats[8], cmap='gray')
# plt.axis('off')

# def plot_10_by_10_images(images):

#     # figure size
#     fig = plt.figure(figsize=(10,10))

#     # plot image grid
#     for x in range(10):
#         for y in range(10):
#             ax = fig.add_subplot(10, 10, 10*y+x+1)
#             plt.imshow(images[10*y+x])
#             plt.xticks(np.array([]))
#             plt.yticks(np.array([]))
#     plt.show()

# images = data_batch_1[b'data']
# # plot_10_by_10_images(images)
# print(images.shape)