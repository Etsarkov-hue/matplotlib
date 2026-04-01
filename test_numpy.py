import sys
import array
import numpy as np
# print(np.__version__)
# print("Hello NumPy!")
# print("EHFD==!")
#*динамическая типизация
x = 1
print(type(x))

l = [True, "2", 3.0, 4]
print([type(i) for i in l])

print(sys.getsizeof(l))
l1 = []
print(type(l1))
print(sys.getsizeof(l1))

a1 = array.array('i', []) #*создает массив
print(type(a1))
print(sys.getsizeof(a1))

a1 = array.array('i', [1])
print(sys.getsizeof(a1)) #*показывает сколько байт

#*рассмотрим как можно создавать массивы в Numpy\
#todo 1 - создание из списка
l = [1, 2, 3, 4, 5]
a = np.array(l)
print(a)
print(type(a))
#! <class 'numpy.ndarray'>
print("list(python)", sys.getsizeof(l))
ap = array.array('i', l) #* из l делаем массив типа Int ('i')
print("list(python)", sys.getsizeof(ap))
print("list(numpy)", sys.getsizeof(a))

#* повышающее приведение типов
a3 = np.array([1.01, 2, 3 ,4, 5])
print(type(a3), a3) #*превратились в действительные числа  [1.01 2.   3.   4.   5.  ]


#* явно задать тип
a3 = np.array([1.01, 2, 3 ,4, 5], dtype = int)
print(type(a3), a3) #* вывело [1 2 3 4 5]

#* одномерные массивы
a = np.array(range(2, 5))
print(a)

#*многомерные массивы
a = np.array([range(i, i+5) for i in (1, 2, 3)])
# 1 2 3 4 5
# 2 3 4 5 6
# 3 4 5 6 7
print(a)

#* можно создаавать  нуля по шаблона 
print(np.zeros(10)) #* [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#* из 1 построем многомерный массив
print(np.ones((3, 5), dtype= float))
# [[1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]
#*предопределнное значение
print(np.full((3,3), 3.1416))
# [[3.1416 3.1416 3.1416]
#  [3.1416 3.1416 3.1416]
#  [3.1416 3.1416 3.1416]]
#*линейная последовательность чисел
print(np.arange(0, 20, 2)) #*[ 0  2  4  6  8 10 12 14 16 18]

#*в интервале с одинаковыми промежутками между собой
print(np.linspace(0, 2, 5)) #* [0.  0.5 1.  1.5 2. ]

#* равномерное распределние от 0 до 1
print(np.random.random((2, 4)))
#* нормальное распредлелние
print(np.random.normal(0, 1, (2, 4)))

#* нормальное распредлелние от x до у
print(np.random.randint(0, 5, (2, 2)))

#* единичная матрица
print(np.eye(5, dtype = int))
# [[1 0 0 0 0]
#  [0 1 0 0 0]
#  [0 0 1 0 0]
#  [0 0 0 1 0]
#  [0 0 0 0 1]]

#*типы данных 
print(np.zeros(10, dtype = int)) #* питон
print(np.zeros(10, dtype = 'int16'))  #* нумпаевский

print(np.zeros(10, dtype = np.int16)) #* нумпаевский

#* Numerical Python = Numpy

#* -атрибуты массивов
#* индексация
#* срезы как получать и как заменять
#* измение формы масивов
#* обьединение и разбиение


#* -атрибуты массивов
#* Атрибуты: ndim - число размерностейб, shape - размер каждой размерности, size - общий размер массива
np.random.seed(1)

x1 = np.random.randint(10, size = 3) #[5 8 9]
print(x1.ndim, x1.shape, x1.size) #*1 (3,) 3

#* индексация
a = np.array([1, 2, 3, 4, 5])
print(a[0])

print(a[-2])
a[1] = 20
print(a)

#*двумерные массивы
a = np.array([[1, 2], [3, 4]])
print(a)
#*вставки
a = np.array([1, 2, 3, 4, 5])
print(a.dtype) #int64
a[0] = 3.14

print(a)
print(a.dtype)

#*срезы - подмассив массива [начало: конец: шаг] - [от 0 до конца:шаг = 1]

a = np.array([1,2 , 3, 4, 5])
print(a[:3])

print(a[3:])
print(a[1:4])

print(a[:2])

#*если шаг меньше нулоя [начало:конец:шаг] -> [конец:начало:шаг]

#*срезы в многомернрых массивах

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [19, 10, 11, 12]])

print(a[:2, :3]) 
# [[1 2 3]
#  [5 6 7]]
print(a[:, ::2])
# [ 1  3]
#  [ 5  7]
#  [19 11]]

print(a[:, 0])
print(a[0])
#*срезы в питоне - копии масиво или подмассивов, а в Numpy это представление (view)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [19, 10, 11, 12]])

print(a) 

a_2x2 = a[:2, :2]

print(a_2x2)
a_2x2[0,0] = 999
print(a)

a_2x2 = a[:2, :2].copy()

print(a_2x2)

a_2x2[0,0] =1001
print(a_2x2)
print(a)

#*изменение формы массвива

a = np.arange(1, 13)
print(a, a.shape, a.ndim)

print(a[3])
print(a[11])

a1 = a.reshape(1, 12)
print(a1, a1.shape, a1.ndim)

print(a1[0, 3])
print(a1[0, 11])

a2 = a.reshape(2, 6)
print(a2, a2.shape, a2.ndim)
a3 = a.reshape(2, 2, 3)
print(a3, a3.shape, a3.ndim)

print(a3[0, 1, 2])

a4 = a.reshape(1, 12, [1, 1])
print(a4, a4.shape, a4.ndim)
print(a4[0, 2, 0,0])

a5 = a.reshape(2, 6)
print(a5, a5.shape, a5.ndim)
print(a5[1,5])
a6 = a.reshape((2, 6), order = "F")
print(a6, a6.shape, a6.ndim)
print(a6[1, 4])

a = np.arange(1, 13)
print(a, a.shape, a.ndim)

print(a[3])
print(a[11])

a1 = a.reshape(1, 12)
print(a1, a1.shape, a1.ndim)

a2 = a[np.newaxis, :] #todo добавляет новую ось
print(a2, a2.shape, a2.ndim)
