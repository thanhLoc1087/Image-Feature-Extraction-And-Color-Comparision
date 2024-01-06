import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def ReadFile():
    dirpath = os.getcwd()
    train = pd.read_csv(dirpath + '\\mnist_train.csv')
    test = pd.read_csv(dirpath + '\\mnist_test.csv')

    X_test = test.drop(['label'], axis=1)
    y_test = test[['label']]

    X_train = train.sort_index().drop(['label'], axis=1)
    y_train = train.sort_index()[['label']]

    X_train = np.array(X_train)
    X_test = np.array(X_test)

    X_train = X_train.reshape(X_train.shape[0], 28, 28)
    X_test = X_test.reshape(X_test.shape[0], 28, 28)
    print(X_test.shape)
    print(y_test.shape)
    return X_train, X_test, y_train, y_test

def TrainingSet(X_train):
  NumberOfClass = 10 #Number of Classes: 0-->9
  Training = []
  for k in range(0,NumberOfClass):
    Training.append([])

  #Phân loại ảnh vào đúng label
  for k in range(0, len(X_train)):
    d = y_train.iloc[k, 0]
    Imag = X_train[k]
    P = []
    for i in range(0, 28):
      p = []
      for j in range(0, 28):
        x = int(Imag[i][j])
        p.append(x)
      P.append(p)
    Training[d].append(P)
  return Training

def ChangeToPredicate(Imag, value):
  P = []
  for i in range(0, 28):
    p = []
    for j in range(0, 28):
      x = int(Imag[i][j]/64)+value
      p.append(x)
    P.append(p)
  
  return P

def TrainingSet_GENmethod(X_train):
  NumberOfClass = 10 #Number of Classes: 0-->9
  Training = []
  for k in range(0, NumberOfClass):
    Training.append([])

  for k in range(0, len(X_train)):
    d = y_train.iloc[k, 0]
    Imag = X_train[k]
    TransImag = ChangeToPredicate(Imag, 1)
    Training[d].append(TransImag)

  return Training

def ComputeLG(Image1, Image2):
  for i in range(0,28):
    for j in range(0,28):
      if Image1[i][j] < 64:
        Image1[i][j] = int((Image1[i][j]+Image2[i][j])/2)
  return Image1

def GENmethod(Training):
  Result = []
  for lop in range(0, NumberOfClass):
    T = Training[lop]
    ElementOfClass = len(T)
    Feat = T[0]
    for k in range(1, ElementOfClass):
      Imag = T[k]
      ComputeLG(Feat, Imag)
        
    Result.append(Feat)
  
  return Result

def ComputeGen(Training): 
  ElementOfClass = len(Training)
  Feat = Training[0]
  for k in range(1, ElementOfClass):
    Imag = Training[k]
    ComputeLG(Feat, Imag)
  return Feat

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

def FRQmethod(Training):
  Result = []
  for lop in range(0, NumberOfClass):
    T = Training[lop]
    ElementOfClass = len(T)
    Feat = T[0] 
    for i in range(0,28):
      for j in range(0,28): 
        a = np.array([T[k][i][j] for k in range(0, ElementOfClass)])
        unique, counts = np.unique(a, return_counts=True)
        unique = unique.tolist()
        counts = counts.tolist()

        DoubleSort(counts, unique)
        pos = 0
        Feat[i][j] = int(unique[pos])
    Result.append(Feat)
  return Result

  
def ComputeFRQ(Training):
  T = Training
  ElementOfClass = len(T)
  Feat = T[0] 
  for i in range(0,28):
    for j in range(0,28): 
      a = np.array([T[k][i][j] for k in range(0, ElementOfClass)])
      unique, counts = np.unique(a, return_counts=True)
      unique = unique.tolist()
      counts = counts.tolist()
      DoubleSort(counts, unique)
      pos = 0
      Feat[i][j] = int(unique[pos])
  return Feat

def AVEmethod(Training):
    Result = []
    for lop in range(0, NumberOfClass):
      T = Training[lop]
      ElementOfClass = len(T)
      Feat = T[0]
      for k in range(1,ElementOfClass):
          Imag = T[k]
          for i in range(0,28):
            for j in range(0,28): 
              Feat[i][j] = float((Feat[i][j]*k + Imag[i][j]))/(k+1)
    
      for i in range(0,28):
        for j in range(0,28):
          Feat[i][j] = int(Feat[i][j])
      
      Result.append(Feat)

    return Result

def TestSet_GENmethod(X_test):
    Test = []
    for k in range(0, len(X_test)):
      Imag = X_test[k]

      TransImag = ChangeToPredicate(Imag,0)
      Test.append(TransImag)

    return Test

def TestSet(X_test):
    Test = []
    for k in range(0, len(X_test)):
      Imag = X_test[k]
      P = []
      for i in range(0, 28):
          p = []
          for j in range(0, 28):
            x = int(Imag[i][j])
            p.append(x)
          P.append(p)
      Test.append(P)

    return Test

def Compare(Imag,Feat):
  d = 0
  for i in range(0,28):
    for j in range(0,28):
      d = d + abs(Imag[i][j] - Feat[i][j])
    
  return d

def Predict(Test):
  Pred_Test = []
  Result_Test = []
  for i in range(0,len(Test)):
    Result_Test.append(y_test.iloc[i, 0])

    Imag = Test[i]
    min_test = 255*28*28*2
    value = -1
    for k in range(0,10):
      test = Compare(Imag,Result[k])
      if min_test > test:
        min_test = test
        value = k
    Pred_Test.append(value)

  return Pred_Test, Result_Test

def ComputeAccuracy(Predict_Test, Result_Test):
    Measure = []
    for i in range(0,10):
      Measure.append([0,0,0,0])

    for i in range(0,len(Predict_Test)):    
      lop = Predict_Test[i]
      if (lop == Result_Test[i]):
        Measure[lop][0] = Measure[lop][0] + 1   #TP
        for k in range(0,NumberOfClass):
          if (k!=lop):
            Measure[k][3] = Measure[k][3] + 1   #TN
      else:
        Measure[lop][2] = Measure[lop][2] + 1   #FN
        Measure[Result_Test[i]][1] = Measure[Result_Test[i]][1] + 1 #FP
        for k in range(0,NumberOfClass):
          if (k!=lop) and (k != Result_Test[i]):
            Measure[k][3] = Measure[k][3] + 1   #TN


    for i in range(0,10):
      a = Measure[i][0] #TP
      b = Measure[i][1] #FP
      c = Measure[i][2] #FN
      d = Measure[i][3] #TN
      print(a+b+c+d)
      if ((a+b) != 0) and ((a+c)!=0):
        print("Class ",i,a,b,c,d,str(a/(a+b)),str(a/(a+c)),str((a+d)/(a+b+c+d)))
      elif ((a+b) != 0):
        print("Class ",i,a,b,c,d,str(a/(a+b)),0.0,str((a+d)/(a+b+c+d)))
      elif ((a+c) != 0):
        print("Class ",i,a,b,c,d,0.000,str(a/(a+c)),str((a+d)/(a+b+c+d)))
      else:
        print("Class ",i,a,b,c,d,str((a+d)/(a+b+c+d)))


if __name__== '__main__':
    # create figure
    fig = plt.figure(figsize=(10, 7))
    # setting values to rows and column variables
    rows = 2
    columns = 5
    NumberOfClass = 10
    X_train,X_test, y_train, y_test = ReadFile()

# # GEN method
    Training = TrainingSet_GENmethod(X_train)
    Result = GENmethod(Training)
    Test = TestSet_GENmethod(X_test)
    Predict_Test, Result_Test = Predict(Test)
    ComputeAccuracy(Predict_Test, Result_Test)
    print("---------GEN-----------")
    for i in range(0, 10):
      fig.add_subplot(rows, columns, i + 1)
      plt.imshow(Result[i], cmap='gray')
    plt.show()

# # # FRQ method
    # Training = TrainingSet(X_train)
    # Result = FRQmethod(Training)
    # Test = TestSet(X_test)
    # Predict_Test, Result_Test = Predict(Test)
    # ComputeAccuracy(Predict_Test, Result_Test)
    # print("---------FRQ-----------")
    # for i in range(0, 10):
    #   fig.add_subplot(rows, columns, i + 1)
    #   plt.imshow(Result[i], cmap='gray')
    # plt.show()

# # # AVE method
    # Training = TrainingSet(X_train)
    # Result = AVEmethod(Training)
    # Test = TestSet(X_test)
    # Predict_Test, Result_Test = Predict(Test)
    # ComputeAccuracy(Predict_Test, Result_Test)
    # print("---------AVE-----------")
    # for i in range(0, 10):
    #   fig.add_subplot(rows, columns, i + 1)
    #   plt.imshow(Result[i], cmap='gray')
    # plt.show()

# # # LL method
    # Training = TrainingSet(X_train)
    # Result = np.array([Training[k][0] for k in range(0, 10)])

    # Test = TestSet(X_test)
    # Predict_Test, Result_Test = Predict(Test)
    # print("---------LL-1-----------")
    # ComputeAccuracy(Predict_Test, Result_Test)
    # Result = np.array([Training[k][1] for k in range(0, 10)])

    # Test = TestSet(X_test)
    # Predict_Test, Result_Test = Predict(Test)
    # print("---------LL-2=----------")
    # ComputeAccuracy(Predict_Test, Result_Test)
    # Result = np.array([Training[k][2] for k in range(0, 10)])

    # Test = TestSet(X_test)
    # Predict_Test, Result_Test = Predict(Test)
    # print("---------LL-3-----------")
    # ComputeAccuracy(Predict_Test, Result_Test)
    # for i in range(0, 10):
    #   fig.add_subplot(rows, columns, i + 1)
    #   plt.imshow(Result[i], cmap='gray')
    # plt.show()