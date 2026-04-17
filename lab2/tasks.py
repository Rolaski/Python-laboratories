"""
Biblioteka NumPy - Rozwiązania ćwiczeń
=======================================
Źródło: Wektor__macierz__tablica_zadania_dla_Studentów
"""

import numpy as np
from sklearn.model_selection import train_test_split

print("=" * 60)
print(f"NumPy version: {np.__version__}")
print("=" * 60)


# ===========================================================
# ĆWICZENIE 1
# Sprawdź czy wszystkie elementy tablic zwracają True
# ===========================================================
print("\n--- ĆWICZENIE 1: np.all() ---")

A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])

B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])

C = np.array([[True, False, False],
              [True, True, True]])

D = np.array([0.1, 0.3])

print(f"A.all() = {A.all()}")   # True  - wszystkie niezerowe
print(f"B.all() = {B.all()}")   # False - jest 0
print(f"C.all() = {C.all()}")   # False - jest False
print(f"D.all() = {D.all()}")   # True  - wszystkie niezerowe


# ===========================================================
# ĆWICZENIE 2
# Operacje na tablicach: tworzenie, reshape, indeksowanie
# ===========================================================
print("\n--- ĆWICZENIE 2: Tworzenie i operacje na tablicach ---")

# Jednowymiarowa tablica 0..19
matrix = np.arange(20)
print(f"matrix = {matrix}")
print(f"Kształt (shape): {matrix.shape}")

# Zerowy i piąty element (index 0 i 4)
print(f"Element o indeksie 0: {matrix[0]}")
print(f"Element o indeksie 4: {matrix[4]}")

# Reshape do 2x10
new_matrix = matrix.reshape(2, 10)
print(f"\nnew_matrix (2x10):\n{new_matrix}")
print(f"Nowy kształt: {new_matrix.shape}")

# Czwarty element w zerowym wierszu (indeks [0][3])
print(f"new_matrix[0][3] = {new_matrix[0][3]}")

# Lista potęg 2 i konwersja na numpy array
a_python_list = [2**x for x in range(10)]
special_matrix = np.array(a_python_list)
print(f"\nspecial_matrix (potęgi 2): {special_matrix}")

# Tablice zer, jedynek, pusta, pełna, diagonalna, losowa
zero_array = np.zeros(10)
print(f"\nzero_array:   {zero_array}")

one_array = np.ones((2, 5))
print(f"one_array (2x5):\n{one_array}")

empty_array = np.empty(100)
print(f"empty_array (pierwsze 5): {empty_array[:5]} ...")

lucky_array = np.full((5, 5), 13)
print(f"\nlucky_array (5x5, same 13):\n{lucky_array}")

diagonal_array = np.eye(5)
print(f"\ndiagonal_array (5x5, jedynki na przekątnej):\n{diagonal_array}")

random_array = np.random.random(10)
print(f"\nrandom_array (10 losowych): {random_array}")


# ===========================================================
# ĆWICZENIE 3
# Tablica nieparzysta, filtrowanie booleanem i warunkami
# ===========================================================
print("\n--- ĆWICZENIE 3: Filtrowanie tablic ---")

# Nieparzyste liczby od 5 do 29
matrix = np.arange(5, 30, 2)
print(f"matrix (nieparzyste 5-29): {matrix}")

# Maska boolowska: True gdy element < 10
boolMatrix = matrix < 10
print(f"boolMatrix (< 10):         {boolMatrix}")

# Elementy spełniające boolMatrix (< 10)
print(f"Elementy < 10:             {matrix[boolMatrix]}")

# Elementy < 20
print(f"Elementy < 20:             {matrix[matrix < 20]}")

# Elementy podzielne przez 3
print(f"Elementy podzielne przez 3: {matrix[matrix % 3 == 0]}")


# ===========================================================
# ĆWICZENIE 4
# Ręczny podział danych na train/test (80%/20%)
# ===========================================================
print("\n--- ĆWICZENIE 4: Podział train/test ---")

matrix = np.arange(50).reshape(10, 5)
print(f"Kształt matrix: {matrix.shape}")

# Podział 20% / 80%
split_level = 0.2
num_rows = matrix.shape[0]
split_border = split_level * num_rows

first_part_of_data = matrix[:round(split_border), :]
second_part_of_data = matrix[round(split_border):, :]
print(f"Pierwsza część (20%) - kształt: {first_part_of_data.shape}")
print(f"Druga część   (80%) - kształt: {second_part_of_data.shape}")

# Przetasuj wiersze
np.random.shuffle(matrix)
print(f"\nPo shuffle - pierwsza część:\n{matrix[:round(split_border), :]}")
print(f"Po shuffle - druga część:\n{matrix[round(split_border):, :]}")


# ===========================================================
# ĆWICZENIE 5
# Podział na X_train, X_test, y_train, y_test
# ===========================================================
print("\n--- ĆWICZENIE 5: X_train / X_test / y_train / y_test ---")

data = np.arange(500).reshape(100, 5)
np.random.shuffle(data)

split_level = 0.8
num_rows = data.shape[0]
split_border = split_level * num_rows

X_train = data[:round(split_border), :-1]
X_test  = data[round(split_border):, :-1]
y_train = data[:round(split_border), -1:]
y_test  = data[round(split_border):, -1:]

print(f"X_train kształt: {X_train.shape}")   # (80, 4)
print(f"X_test  kształt: {X_test.shape}")    # (20, 4)
print(f"y_train kształt: {y_train.shape}")   # (80, 1)
print(f"y_test  kształt: {y_test.shape}")    # (20, 1)

# Weryfikacja przez sklearn
X_train_sk, X_test_sk, y_train_sk, y_test_sk = train_test_split(
    data[:, :-1], data[:, -1], test_size=0.2, shuffle=True
)
print(f"\n[sklearn] X_train: {X_train_sk.shape}, X_test: {X_test_sk.shape}")
print(f"[sklearn] y_train: {y_train_sk.shape}, y_test: {y_test_sk.shape}")


# ===========================================================
# ĆWICZENIE 6
# Mnożenie macierzy, np.where, append
# ===========================================================
print("\n--- ĆWICZENIE 6: Macierze, where, append ---")

# Tablica 5x5 z liczbami 1..25
X = np.arange(1, 26).reshape(5, 5)
print(f"X:\n{X}")

# Macierz jedynek o tym samym kształcie co X
Ones = np.ones_like(X)
print(f"\nOnes:\n{Ones}")

# Mnożenie macierzowe X * Ones
result = np.dot(X, Ones)
print(f"\nX dot Ones:\n{result}")

# Macierz jednostkowa (element neutralny mnożenia macierzowego)
diag = np.zeros_like(X, dtype=float)
np.fill_diagonal(diag, 1)
print(f"\nMacierz jednostkowa diag:\n{diag}")

result_identity = np.dot(X, diag)
print(f"\nX dot diag (powinno być X):\n{result_identity}")
print(f"Czy X dot diag == X? {np.allclose(result_identity, X)}")

# np.where: jedynki gdzie X > 10, zera w pozostałych przypadkach
where_gt10 = np.where(X > 10, 1, 0)
print(f"\nJedynki gdzie X > 10:\n{where_gt10}")

# np.where: jedynki gdzie X parzyste, zera gdzie nieparzyste
where_even = np.where(X % 2 == 0, 1, 0)
print(f"\nJedynki gdzie X parzyste:\n{where_even}")

# X_bis: 2*wartość gdzie X > 10, 0 w pozostałych
X_bis = np.where(X > 10, X * 2, 0)
print(f"\nX_bis (2x gdzie >10, else 0):\n{X_bis}")
print(f"Liczba elementów niezerowych: {np.count_nonzero(X_bis)}")

# Append - doklejanie tablic
x = np.array([[10, 20, 30],
              [40, 50, 60]])
y = np.array([[100],
              [200]])

# Nowa kolumna (axis=1)
x_new_col = np.append(x, y, axis=1)
print(f"\nPo doklejeniu y jako kolumny (axis=1):\n{x_new_col}")

# Nowy wiersz (axis=0) - y musi mieć 3 kolumny
y_row = np.array([[100, 200, 300]])
x_new_row = np.append(x, y_row, axis=0)
print(f"\nPo doklejeniu wiersza (axis=0):\n{x_new_row}")

print("\n" + "=" * 60)
print("Wszystkie ćwiczenia zakończone!")
print("=" * 60)