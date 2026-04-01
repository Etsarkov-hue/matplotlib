import numpy as np
#*правила трансливрования (broadcasting)
#* 1. правило сравниваются размерности двух массив, если размерности отличаются то форма массива с меньшейй
#* 1. правило размерностью дополняется единицами с левой стороны
a = np.ones((2,3)) #*массив из единичек 2 на 3
b = np.arange(3) #*массив 012
# c = np.ones((1,3))

print(a)
print(b)

# print(a.shape) #* показывает две строки и три столбца (2, 3)
# print(b.shape) #* (3,)  
# print(c.shape)
c = a+b
print(c) #[1 2 3]
         #[1 2 3]
#*1 a ->(2, 3) , b -> (3,) => a ->(2, 3) , b -> (1,3)(размерности)

#* 2. Правило Если формы двух массивов не совпадают в каком то измерении то массив с формой 
#* 2. Праивло равной единице, растягивается до соответствия формы другого массива
#* 3. Правило Если в каком либо измерении размеры массивов различаются и не один не равен единике
#* 3 Правило  то генерируется ошибка
a = np.arange(3).reshape((3,1))
b = np.arange(3)

print(a)
print(b)
print(a.shape) #*(3, 1)
print(b.shape)

[0]
[1]
[2]
print(a + b)
print(a*b)


a = np.ones((3, 2))
b = np.arange(3)
print("/??????")
print(a)
print(b)
print(a.shape) #*(3, 1)
print(b.shape)

a = np.array(
    [
        
        [1, 2, 3, 4, 5 ,6, 7, 8, 9],
        [9,8,7,6,5,4,3,2,1]
        
    ]
    
)
print(a)
aMean = a.mean() #*считаем средняя значение
print(aMean) #* считаем среднее значение

aMean = a.mean(0) #* берем в качестве среднего 0
print(aMean) #*[5. 5. 5. 5. 5. 5. 5. 5. 5.]

print(a.shape)
print(aMean.shape)

aCentr = a - aMean
print(aCentr) #*[[-4. -3. -2. -1.  0.  1.  2.  3.  4.]
#*[ 4.  3.  2.  1.  0. -1. -2. -3. -4.]]

print(aCentr.mean(0)) #* центрирование


a = np.array(
    [
        
        [1, 2, 3, 4, 5 ,6, 7, 8, 9],
        [9,8,7,6,5,4,3,2,1]
        
    ]
    
)
aMean = a.mean(1) 
print(aMean) 
print(a.shape)
print(aMean.shape)

print('???')
# aMean = a.Mean[:, np.newaxis] #! Добавление новой оси
# print(aMean)
print(aMean.shape)

# aCentr = a - aMean
print(aCentr)
print(aCentr.mean(1))

# import matplotlib.pyplot as plt


# [5. 5. 5. 5. 5. 5. 5. 5. 5.]
# (2, 9)
# (9,)
# [[-4. -3. -2. -1.  0.  1.  2.  3.  4.]
#  [ 4.  3.  2.  1.  0. -1. -2. -3. -4.]]
# [0. 0. 0. 0. 0. 0. 0. 0. 0.]

a = np.array(
    [
        
        [1, 2, 3, 4, 5 ,6, 7, 8, 9],
        [9,8,7,6,5,4,3,2,1]
        
    ]
    
)
x = np.linspace(0, 10 , 100)
# Функция np.linspace(0, 10, 100): Эта команда генерирует массив из 100 равномерно распределенных
# чисел в интервале от 0 до 10 включительно. Вы создали шесть таких идентичных массивов для переменных x, y, z, p, h, n
y = np.linspace(0, 10 , 100)
z = np.linspace(0, 10 , 100)
p = np.linspace(0, 10 , 100)
h = np.linspace(0, 10 , 100)
n = np.linspace(0, 10 , 100)
print(x)
print(x.shape)
print(y.shape)
z = np.sin(x)*y
print(z)

# plt.imshow
# plt.colobar
# plt.show

#*маскирование
print("//////")
x = np.arange(1, 6)
print(x)
a= x < 3
print(a)
b= x < 3
print(b)
#todo [ True  True False False False]
#todo [ True  True False False False]

rng1 = np.random.default_rng(seed =1) #* генератор
rng2 = np.random.default_rng(seed = 10)
rng1 = np.random.default_rng(seed =1)
rng1 = np.random.default_rng(seed =1)
rng1 = np.random.default_rng(seed =1)
x = rng1.integers(10, size=(3, 4)) #*делаем размер 

print(x)

print(x < 6 )
#*  Сколько элементов имеют значение меньше 6

print(np.count_nonzero(x < 6))
print(np.sum(x < 6))

print(np.sum(x < 6, axis = 0))
print(np.sum(x < 6, axis = 1))
#* проверям условия то что равно или неравно
print(np.any(x > 8))
print(np.any(x > 8))
print(np.any(x > 8))
print(np.any(x > 8))

print(np.all(x != 8))


print('????')

#*Наложение маски (вынмиаем элементы)
print(x < 5)
a = x[x < 5]
print(a)
print(a.shape)




#* and pr &
#* булева алгебра
print(bool(42), bool(0))
print(bool(42 and 0))


print(bool(42 or 0))

print("///")
print(bin(42))
print(bin(59))


print(bin(42 and 49 ))
print(bin(42 or 49 ))

print(bin(42 & 49 ))
print(bin(42 | 49 ))

a = np.array([1, 0 , 1, 0, 1], dtype = bool)
b = np.array([1, 1,1,1,1,0], dtype= bool)
print(a&b)

#*Способы доступа к элементам массива
print("////")
a = np.arange(10)
print(a)
print(a[3])
print(a[3:4])
print(a[a == 3])

#векторизация/ прихотливая (fancy) индексация

a = np.arange(10)

ind = [3, 5, 0]
print(a[ind])

# row = np.array
# # col= np.array
# row = np.array
# col = np.array

# print(row.shape)
# print(col.shape)

# print(a[row[:, np.newaxis], col])
