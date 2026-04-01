import numpy as np
import pandas as pd

# Создание генератора случайных чисел
rng = np.random.default_rng(1)
#*Создается современный генератор случайных чисел NumPy с фиксированным «зерном» 
# *(seed=1), чтобы результаты были воспроизводимы.
# *Создание первого MultiIndex (для строк)
mi1 = pd.MultiIndex.from_product([["A1", "A2"], [2025, 2026]], names=["property", "year"])
print(mi1)
# *ункция from_product создает декартово произведение списков. Получится 4 комбинации:
# *(A1, 2025), (A1, 2026), (A2, 2025), (A2, 2026).
# Создание второго MultiIndex (для столбцов)
mi2 = pd.MultiIndex.from_product([["B1", "B2", "B3"], ["jan", "feb"]], names=["shop", "month"])
print(mi2)

# Генерация массива случайных чисел 4x6
data = rng.random((4,6))
#* Создается массив случайных чисел размером 4 на 6, что в точности соответствует количеству 
#* элементов в ваших индексах mi1 (4 строки) и mi2 (6 столбцов).
df = pd.DataFrame(data, index=mi1, columns=mi2)
print(data)

#*по стоблцам
print(df["B2"])
print(df)

print("stopppp")
#* Срезы (сначала берем строчки)
print(df.iloc[1:,2:5]) #*с первой по последнюю

# A1       2026  0.549594  0.027559  0.753513
# A2       2025  0.303195  0.453498  0.134042
        #  2026  0.750365  0.280409  0.485191
ind1 = pd.IndexSlice[:, 2025]
ind2 = pd.IndexSlice[:, "jan"]
print('llllllllllllllllllllllll')
print(df.loc[ind1,ind2])
# shop                 B1        B2        B3
# month               jan       jan       jan
# property year
# A1       2025  0.511822  0.144160  0.311831
# A2       2025  0.329732  0.303195  0.134042

#*как можем в мультидексированному массиву обращаться
#* 1) поиск о нескольким индексам
data = {
    ("A1", 2025): 1,
    ("A1", 2026): 2,
    ("A1", 2027): 3,
    ("A2", 2025): 11,
    ("A2", 2026): 12,
    ("A2", 2027): 13,
    ("A3", 2025): 21,
    ("A3", 2026): 22,
    ("A3", 2027): 23,
}

sr = pd.Series(data)
sr.index.names = ["property", "year"]

print(sr)
# property  year
# A1        2025     1
        #   2026     2
        #   2027     3
# A2        2025    11
        #   2026    12
        #   2027    13
# A3        2025    21
        #   2026    22
        #   2027    23

index = pd.MultiIndex.from_product([["a", "b", "c"], [1, 2]])
data = pd.Series(rng.random(6), index=index)
print(data)

print(data["a":"b"])
# a  1    0.961657
#    2    0.724790
# b  1    0.541227
#    2    0.276891
# dtype: float64

#todo unstack 
#* Чаще всего unstack() применяется к данным с мультииндексом (иерархическим индексом): 
#* Kanaries Docs
#* Kanaries Docs
# *Действие: Метод «разворачивает» один из уровней строк и делает его уровнем столбцов.
# *Результат: Если применить его к объекту Series с мультииндексом, получится DataFrame.
# *По умолчанию: Разворачивается самый внутренний (последний) уровень индекса строк. 
# *Яндекс
# *Яндекс
# * +2


# 1. Создаем данные с мультииндексом (Год и Город)
index = pd.MultiIndex.from_tuples([
    (2023, 'Москва'), (2023, 'Питер'),
    (2024, 'Москва'), (2024, 'Питер')
], names=['Год', 'Город'])

data = pd.Series([20, 18, 22, 19], index=index, name='Температура')

print("--- Исходная Series (длинный формат) ---")
print(data)

# 2. Применяем unstack(), чтобы превратить города в столбцы
df_unstacked = data.unstack()

print("\n--- Результат unstack() (широкий формат) ---")
print(df_unstacked)

#** Выбор уровня: По умолчанию unstack() разворачивает последний уровень индекса (в примере — Город). 
# *Если вы хотите развернуть Год, используйте data.unstack(level=0).
# *Заполнение пустот: Если в одном из годов данных по какому-то городу не было, 
# **появится NaN. Чтобы вместо него стоял, например, 0, напишите data.unstack(fill_value=0)

# sr.index.names = ["product", "year", "count"]

# print(sr)
#todo df = sr.reset_index
#* Метод reset_index() — это функция в Pandas, которая сбрасывает 
#* текущий индекс строк и заменяет его стандартным числовым индексом (от 0 до N
#todo set_index() - индекс устанавливает

#*сводные таблицы - представление многомерных данных в виде двумерных таблиц
import zipfile
with zipfile.ZipFile('titanic.zip') as z:
    train = pd.read_csv(z.open('train.csv'))
    test = pd.read_csv(z.open('test.csv'))

print(train.head())


import seaborn as sns
titanic = sns.load_dataset('titanic')
print(type(titanic))
print(titanic.head)

print(titanic.groupby(["sex", "class"])["survived"].mean())
#todo Метод groupby() — это один из самых мощных инструментов в Pandas. Он нужен для группировки 
#* данных по какому-то признаку (например, по полу, классу каюты или году) и последующего 
#* вычисления статистики для этих групп.

births = pd.read

#todo head() - позволяет напечать первые 5 элементов


# 1. Настройка стиля графиков (раз ты установил seaborn)
sns.set_theme()

# ПРЕДПОЛОЖИМ, что у тебя уже загружен DataFrame 'births'
# Если нет, вот пример структуры данных:
# births = pd.read_csv('births.csv') 

# 2. Таблица рождаемости по десятилетиям и дням недели
births_dow = births.pivot_table("births", index="dayofweek", 
                                columns="decade", aggfunc="mean")

# 3. Таблица рождаемости по МЕСЯЦАМ и ДНЯМ (убираем привязку к конкретному году)
# Мы группируем все годы вместе, чтобы увидеть сезонность внутри года
births_dom = births.pivot_table("births", index=[births.month, births.day])

# 4. "МАГИЯ" ИНДЕКСА: Превращаем (месяц, день) в реальные даты 2012 года
# Используем 2012, так как он високосный (в нем есть 29 февраля)
try:
    births_dom.index = [datetime(2012, month, int(day)) 
                        for (month, day) in births_dom.index]
except ValueError as e:
    print(f"Ошибка в датах: {e}. Проверьте данные на наличие 31 июня или 31 сентября.")

# 5. ВИЗУАЛИЗАЦИЯ
plt.figure(figsize=(12, 4))

# Рисуем график среднего количества рождений по дням года
births_dom.plot()
plt.title('Среднее количество рождений по дням года (2012 как шаблон)')
plt.ylabel('Количество рождений')
plt.xlabel('Дата')

# ВАЖНО для VS Code: без этой строки график может не открыться в отдельном окне
plt.show()

# Если хочешь посмотреть по десятилетиям:
births_dow.plot()
plt.title('Рождаемость по дням недели и десятилетиям')
plt.show()
