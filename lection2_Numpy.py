import numpy as np
import timeit
#*Слияние и разбиение
x = np.array([1,2,3])
y = np.array([4, 5, 7])
z = np.array([6])

xyz = np.concatenate([x, y, z]) #* объединение
print(xyz)

x = np.array([[1,2,3], [4, 5, 7]])
y = np.array([[4, 5, 7], [8, 9, 1]])
xy1 = np.concatenate([x, y]) #вывод в столбик
print(xy1)

xy2 = np.concatenate([x, y], axis=1) #склейка подставляем просто рядом (горизонтальная)
print(xy2)

xy3 = np.concatenate([x, y], axis=0) #cклейка по ветикали в стобик
print(xy3)

x = np.array([[1,2,3], [4, 5, 6]])
y = np.array([[7, 8, 9], [10, 11, 12]])
print("////")
print(np.vstack([x ,y]))  #cклейка по ветикали в стобик

print(np.hstack([x ,y]))  #склейка подставляем просто рядом (горизонтальная)
print(np.dstack([x ,y])) #todo склейка правый массив переноситься вверх

print(f"//////")
#* Разбиение массивов
xy = np.vstack([x ,y])
print(xy)
#! Метод .split() разбивает строку на части и возвращает их в виде списка. 
print(np.split(xy, [1], axis = 0))

print(np.vsplit(xy, [2]))

#*Универсальные функции

xp = np.arange(1, 10)
print(x)


"""
def f(x):
    out = np.empty(len(x))
    for i in range(len(x)):
        out[i] = 1.0 / x[i]
    return out
print(f(x))
"""
#print(1.0/x)
#print(timeit.timeit(stmt="f(x)", globals = globals()))
#print(timeit.timeit(stmt="1.0/x", globals = globals()))
print("/////")
#* УФ арифметические операции
x = np.arange(5)
print(x)

print(x+1)
print(x-1)
print(x*2)
print(x/2)
print(x//2)

print(x**2)
print(x%2)

print(x*2-2)

print(".....")
print (x+1)
print(np.add(x, 1)) #*прибавляет единицу к каждому элементу массива делается без цикла for

x = np.arange(-5, 5)
print(x)

print(abs(x)) #*абсолютное значение
print(np.abs(x))
print(np.absolute(x))


print("....")
x = np.array([3 + 4j, 4 - 3j])
print(abs(x))
print(np.abs(x))

#*Уф



#* синусы косинусы

#* показательные i логарифмы


#* exp, power log, log2, log10

x = [0, 0.0001, 0.001, 0.01, 0.1]

print("exp = ", np.exp(x))
print("exp - 1 = ", np.exp(x))

# print('log(x) =', np.log(x))

# print('log(1+x) =', np.loglp(x))

#*Универсал фунеции

x = np.arange(5)
print(x)

y = x*10
print(y)
#*multiply() - это умножение
y = np.multiply(x, 10)
print(y)


print("////")
z = np.empty(len(x))
y = np.multiply(x, 10, out=z) #* out куда я хочу получить результат
print(z)


z = np.zeros(10)
x = np.arange(5)
print(x)
print(z)
# a = np.(10)
z[::2] = x*10 #*на каждое четное поставили 10 

#0 0 10 0 20 0 30 0 40 0
print(z)

print("////")

z = np.zeros(10)
np.multiply(x, 10, out = z[::2])
print(z) #* [ 0.  0. 10.  0. 20.  0. 30.  0. 40.  0.]



#* фукнции свертки которые показывают сводные показатели

x = np.arange(1, 5)
print(x)
print(np.add.reduce(x)) #*многократно прибавляем элементы  - это про функцию reduce
print(np.add.accumulate(x)) #* аккумуляция результата

print(np.subtract.reduce(x))
print(np.subtract.accumulate(x))

print(np.sum(x))
print(np.cumsum(x)) #* сумма с накплением
print(np.prod(x))
print(np.cumprod(x))

x = np.arange(1, 10)
print(np.add(x, x))
print(np.add.outer(x, x))
#todo Метод .outer создает таблицу сложения. Он берет каждый элемент
#todo из первого массива и прибавляет
#todo к нему каждый элемент из второго. В итоге получается матрица \(9\times 9\): 
print(np.multiply.outer(x,x)) #*таблца уумножения

#*Агрегирование
np.random.seed(1) #* зафиксировали генератор случ чисел

s = np.random.random(100)
print(sum(s)) #питон
print(np.sum(s)) #нумпай
a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(np.sum(a))
print(np.sum(a))
print(np.sum(a, axis = 1))
print(np.sum(a, axis = 0))
print(type(a))
print(a.sum(a, 2))
print(a.sum(0))
print(a.sum(1))
#*минимумы и максимумы
np.random.seed(1)
s = np.random.random(100)

print(min(s))
print(np.min(s))

print(max(s))
print(np.max(s))

#*транслиование и броадкастикнг

a = np.array([1, 2, 3])
b = np.array9([5, 5, 5])

print(a+b)
print(np.sum(a+b))
print(a+5)
