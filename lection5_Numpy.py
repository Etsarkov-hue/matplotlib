#todo Pandas
#* Series
#* DataFrame (матрица в качестве строк)
import numpy as np
import pandas as pd

data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(data)
#* бибилотека pandas это грубо говоря excel в коде во много раз лучше
# 0    0.25
# 1    0.50
# 2    0.75
# 3    1.00
# dtype: float64
print(data.values)
# [0.25 0.5  0.75 1.  ]
print(type(data.values))

print(data.index)
# RangeIndex(start=0, stop=4, step=1)
print(data[1])
print(data[1:3])
#* обращаемся к индексам

data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
print(data)
print(data["a"]) #*0.25
print(data["b":"d"])

print('????/??????')

data = pd.Series([0.25, 0.5, 0.75, 1.0], index=[1, 10, 7, 'd'])
print(data)
print(data[10:"d"]) #*срез

dict = {
    "A": 10,
    "B": 20,
    "C": 30,
    "D": 40,
    "E": 50, 
}
data_dict = pd.Series(dict)
print(data_dict)
print(data_dict["B"])
# dtype: int64
# 20

#*cписки
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
data = pd.Series(5, index=[10, 20 , 30])
print(data)
# 10    5
# 20    5
# 30    5
#*словари
dict = {
    "A": 10,
    "B": 20,
    "C": 30,
    "D": 40,
    "E": 50, 
}
data_dict = pd.Series(dict, index = ["A", "D"])
print(data_dict)

#todo Series одномерный массив
#todo data двумерный массив

dict1 = {
    "A": 10,
    "B": 20,
    "C": 30,
    "D": 40,
    "E": 50, 
}
data_dict1 = pd.Series(dict1)
dict2 = {
    "A": 11,
    "B": 21,
    "C": 31,
    "D": 41,
    "E": 51, 
}
data_dict2 = pd.Series(dict2)

df = pd.DataFrame({"dict_01": data_dict1, "dict_02": data_dict2})
print(df) #cклеили два массива
# A       10       11
# B       20       21
# C       30       31
# D       40       41
# E       50       51
print(df.values)
print(type(df.values))

print(df.columns) #* Это быстрый способ узнать названия всех столбцов в твоей таблице
print(type(df.values))

print(df.index) #*метки строк
print(type(df.index)) #*метки строк

print(df["dict_01"])
print(df["dict_02"])

df = pd.DataFrame(data_dict1, columns=["rrr"])
print(df)

# print(pd.DataFrame([{"a": i, "b": 2*i}i for i in range (4)]))

#Nan - Not a Number

print(pd.DataFrame(np.zeros(3)))

print("//////////////////////")

#* Index  - способо сослатбся (reference) на данные в series или в data frame

index = pd.Index([2, 5, 3 ,5 ,71])
print(index)
print(type(index))

print(index[1])
print(index[::2])

index1 = pd.Index([2, 5, 3 ,5 ,71])
index2 = pd.Index([1, 2, 51 ,71 ,4])
print(index1.intersection(index2))
print(index1.union(index2))
print(index1.symmetric_difference(index2))
# Index([2, 71], dtype='int64')
# Index([1, 2, 3, 4, 5, 5, 51, 71], dtype='int64')
# Index([1, 3, 4, 5, 51], dtype='int64')

#* Numpy
#* arr[1,2]
#* индексация\
#* срезы arr[:, 1:4]
#* маскирование arr[arr > 5]
#* arr[0m [1, 5] arr[:, [1,5]]]

data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
print(data["a"])
print("a" in data)
# 0.25
# True

data["a1"]= 990
print(data)


data["a2"]= 990
print(data)


data["a3"]= 990
print(data)


data["a4"]= 990
print(data)


print(data[2:4])

print(data> 0.3) #* можно добваить  еще условия




#****атрибуты - индексаторы

print("TOooooooooooooooooooooooooooooooooooooooop")
dict1 = {
    "A": 10,
    "B": 20,
    "C": 30,
    "D": 40,
    "E": 50, 
}
data_dict1 = pd.Series(dict1)
dict2 = {
    "A": 11,
    "B": 21,
    "C": 31,
    "D": 41,
    "E": 51, 
}
data_dict2 = pd.Series(dict2)

df = pd.DataFrame({"dict_01": data_dict1, "dict_02" : data_dict2})

print(df["dict_01"])

df["new"] = df["dict_01"]
print(df)

df["new"] = df["dict_01"] /  df["dict_02"]
print(df)
#    dict_01  dict_02  new
# A       10       11   10
# B       20       21   20
# C       30       31   30
# D       40       41   40
# E       50       51   50
#    dict_01  dict_02       new
# A       10       11  0.909091
# B       20       21  0.952381
# C       30       31  0.967742
# D       40       41  0.975610
# E       50       51  0.980392

#* чтобы получить внутренности нужно взять values

print(df.values)

print(df["dict_01"]) #* столбец
print(df.values[0]) #* строка
# [10.         11.          0.90909091]

print("Stoooooooooooooooooooop")

print(df)

print(df.loc[:"dict_02"], )
print(df)

print(".........")

#* срезы с помощью iloc и loc
#* глянуть


rng = np.random.default_rng(1) #*установили рандом
s = pd.Series(rng.integers(0, 10, 6))

print(np.exp(s))

# df = pd.DataFrame(rng.inegers(0, 10, (3,4)), columns = ["A", "B", "C", "D"])
# print(df)
# 
# print(np.sin(df * 4))


rng = np.random.default_rng(1) #*установили рандом
s = pd.Series(rng.integers(0, 10, 6))

print(np.exp(s))

# df = pd.DataFrame(rng.inegers(0, 10, (3,4)), columns = ["A", "B", "C", "D"])
# print(df)
# 
# print(np.sin(df * 4))

print("TOooooooooooooooooooooooooooooooooooooooop")
dict1 = {
    "A": 10,
    "B": 20,
    "C": 30,
    "D": 40,
    "E": 50, 
}
data_dict1 = pd.Series(dict1)
dict2 = {
    "A": 11,
    "B": 21,
    "C": 31,
    "D": 41,
    "E": 51, 
}
data_dict2 = pd.Series(dict2)

df = pd.DataFrame({"dict_01": data_dict1, "dict_02" : data_dict2})

print(df["dict_01"])
# print()
print(A - A[0])
df = pd.DataFrame(A, columns = ["A", "B", "C", "D"])
print(df)
# print(df - "")

# iloc изучить 
# substract изучить