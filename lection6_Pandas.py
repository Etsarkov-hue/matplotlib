import numpy as np
import pandas as pd
#*отсутствующие данные
a = np.nan
a = -999999

#*Pandas 
#* два способа хранения данных 
#* 1) NaN, None 
#* 2)pd.NA
a = None
print(type(a))

a = np.array([1,2,3])
b = np.array([1, None, 3])
print(a.sum())
#*print(a.sum()) #так не получиться

c = np.array([1, np.nan, 3])
print(c.sum()) #* сумма будет nan

print(c)
print(1+ np.nan)

print(np.nansum(c)) #*игноирурем эти значения

x = pd.Series([1, 2,3 ,4, 5], dtype = int)
print(x)
x[0] = None
x[1]= np.nan
print(x)
# 0    NaN
# 1    NaN
# 2    3.0
# 3    4.0
# 4    5.0

x = pd.Series([" 1", "2", "3", "4", "5"])
print(x) #*dtype: str
x[0] = None
x[1]= np.nan
print(x)
# 0    NaN
# 1    NaN
# 2      3
# 3      4
# 4      5
# dtype: str

x = pd.Series([1, np.nan, None, 5])
print(x) #*dtype: float64

x = pd.Series([1, np.nan, None, pd.NA])
print(x) #*dtype: object

#*int, uint, float
x = pd.Series([1, np.nan, None, pd.NA], dtype = "Int32")
print(x) #* dtype: Int32
# 0       1
# 1    <NA>
# 2    <NA>
# 3    <NA>
# dtype: Int32

x = pd.Series([1, np.nan, None, 5, "hello"])
print(x)
#*находим пустые значения

print(x.isnull())
print(x.notnull())
print(x[x.notnull()])


x = pd.DataFrame([[1, np.nan, None], [1,2,3], [2, np.nan, 3]])
print(x)

print(x.dropna())
#    0    1    2
# 0  1  NaN  NaN
# 1  1  2.0  3.0
# # 2  2  NaN  3.0
#    0    1    2
# 1  1  2.0  3.0

#*выделение ненулевых столбцов
print(x.dropna(axis=1))
print(x.dropna(axis=0, how="any")) #*отбрасывание строк
print(x.dropna(axis=0, how="all")) #* отбрасывание всего

print("//////////")
print(x)
print(x.dropna(axis=0, thresh=1)) #*должно быть минимум N непустых значений
#* можем фильтровать в массивах данных

#*how = all - убрать, если ВСЕ значения отсутсвтуют
#*how = any - убрать, если хотф бы ОДНО значения отсутсвтуют

x = pd.DataFrame([None, 4, np.nan, None, 1,2,3], dtype = "Int32")
print(x)
print(x.fillna(4)) #*заменили пустые значение на 4
# 0  4
# 1  4
# 2  4
# 3  1
# 4  2
# 5  3

print(x.ffill()) #*заполнение предыдущим
# 0  <NA>
# 1  <NA>
# 2  <NA>
# 3     1
# 4     2
# 5     3
print(x.bfill()) #*заполнение следующим

print(x.ffill(axis = 1)) #*заполнение предыдущим + оси
print(x.bfill(axis = 0)) #*заполнение следующим + оси

#*существуе спец клас мультииндекс
index = [
    ("A1",2025),
    ("A1", 2026),
    ("A2", 2025),
    ("A2", 2026),
    ("A3", 2025),
    ("A3", 2026)
    
    
]
data = [1, 2, 3, 4, 5, 6]
s = pd.Series(data, index = index)
print(s)
mi = pd.MultiIndex.from_tuples(index)
print(mi)

s = s.reindex(mi)
print(s)

s1 = pd.Series(data, index=mi)
print(s1)

# print(s[:, 2025])

#*очень удобно для нахождения
index = [
    ("A1",2025, 1),
    ("A1", 2026, 2),
    ("A2", 2025, 1),
    ("A2", 2026), 2,
    ("A3", 2025, 1),
    ("A3", 2026, 2),
    ("A1",2025, 1),
    ("A1", 2026, 2),
    ("A2", 2025, 1),
    ("A2", 2026), 2,
    ("A3", 2025, 1),
    ("A3", 2026, 2)
    
    
]

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


#*очень удобно для нахождения
index = [
    ("A1",2025, 1),
    ("A1", 2026, 2),
    ("A2", 2025, 1),
    ("A2", 2026), 2,
    ("A3", 2025, 1),
    ("A3", 2026, 2),
    ("A1",2025, 1),
    ("A1", 2026, 2),
    ("A2", 2025, 1),
    ("A2", 2026), 2,
    ("A3", 2025, 1),
    ("A3", 2026, 2)
    
    
]


# print(df)


s = pd.Seris(index)
# print(s)
