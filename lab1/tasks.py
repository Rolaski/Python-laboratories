import random


# ZADANIE 1
# Napisz program, który obliczy sumę wszystkich liczb parzystych od 1 do 100.
def zadanie1():
    suma = sum(x for x in range(1, 101) if x % 2 == 0)
    print(f"Suma liczb parzystych 1-100 : {suma}")


# ZADANIE 2
# Napisz funkcję czy_pierwsza(n), która sprawdzi, czy liczba n jest liczbą pierwszą.
def zadanie2():
    def czy_pierwsza(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    try:
        n = int(input("Podaj liczbe do sprawdzenia: "))
        wynik = "- Tak to liczba pierwsza" if czy_pierwsza(n) else "- Nie jest liczba pierwsza"
        print(f"{n} {wynik}")
    except ValueError:
        print("Miała być liczba!")


# ZADANIE 3
# Napisz funkcję, która odwróci podany ciąg znaków (string) bez użycia [::-1].
def zadanie3():
    def odwroc(ciag):
        wynik = ""
        for i in range(len(ciag) - 1, -1, -1):
            wynik += ciag[i]
        return wynik

    tekst = input("Podaj ciag do sprawdzenia: ")
    print(f"Odwrocony ciag: {odwroc(tekst)}")


# ZADANIE 4
# Napisz program, który zamienia temperaturę z Celsjusza na Fahrenheita i odwrotnie.
# Użytkownik podaje wartość i typ konwersji.
def zadanie4():
    def c_na_f(c):
        return c * 9 / 5 + 32

    def f_na_c(f):
        return (f - 32) * 5 / 9

    print("1 - Celsius -> Fahrenheit")
    print("2 - Fahrenheit -> Celsius")
    wybor = input("Wybierz typ konwersji (1 lub 2): ").strip()

    try:
        match wybor:
            case "1":
                val = float(input("Podaj temperature w °C: "))
                print(f"{val}°C = {c_na_f(val):.2f}°F")
            case "2":
                val = float(input("Podaj temperature w °F: "))
                print(f"{val}°F = {f_na_c(val):.2f}°C")
            case _:
                print("Podaj 1 lub 2!")
    except ValueError:
        print("Podaj poprawna wartosc liczbowa.")


# ZADANIE 5
# Napisz funkcję, która przyjmuje listę liczb i zwraca nową listę bez duplikatów.
def zadanie5():
    def usun_duplikaty(lista):
        seen = set()
        wynik = []
        for el in lista:
            if el not in seen:
                seen.add(el)
                wynik.append(el)
        return wynik

    przyklad = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(f"Oryginalna:        {przyklad}")
    print(f"Bez duplikatów:    {usun_duplikaty(przyklad)}")


# ZADANIE 6
# Napisz funkcję rekurencyjną, która oblicza silnię liczby n.
def zadanie6():
    def silnia(n):
        if n < 0:
            raise ValueError("Silnia nie jest zdefiniowana dla liczb ujemnych.")
        return 1 if n <= 1 else n * silnia(n - 1)

    try:
        n = int(input("Podaj liczbę do obliczenia silni: "))
        print(f"{n}! = {silnia(n)}")
    except ValueError as e:
        print(f"Błąd: {e}")


# ZADANIE 7
# Napisz program, który policzy, ile razy każdy znak występuje w podanym przez
# użytkownika tekście i zwróci to jako słownik.
def zadanie7():
    def policz_znaki(tekst):
        licznik = {}
        for znak in tekst:
            licznik[znak] = licznik.get(znak, 0) + 1
        return licznik

    tekst = input("Podaj tekst: ")
    wynik = policz_znaki(tekst)
    print("\nWystąpienia znaków:")
    for znak, ile in sorted(wynik.items()):
        print(f"  {repr(znak)}: {ile}")


# ZADANIE 8
# Napisz prostą grę, w której program losuje liczbę z zakresu od 1 do 20, a użytkownik
# zgaduje liczbę dopóki nie trafi. Po każdej próbie podaj, czy liczba jest za duża czy za mała.
def zadanie8():
    liczba = random.randint(1, 20)
    proby = 0
    print("Zgadnij liczbę z zakresu 1–20.\n")

    while True:
        try:
            prop = int(input("Twoja propozycja: "))
        except ValueError:
            print("Podaj poprawną liczbę całkowitą.")
            continue

        proby += 1
        match True:
            case _ if prop < liczba:
                print("Za mała! Spróbuj wyżej.")
            case _ if prop > liczba:
                print("Za duża! Spróbuj niżej.")
            case _:
                print(f"\nBrawo! Trafiłeś w {proby} {'próbie' if proby == 1 else 'próbach'}!")
                break


# ZADANIE 9
# Napisz program, który wyświetli tabliczkę mnożenia w formie tabeli (do 10x10).
def zadanie9():
    print("   ", end="")
    for i in range(1, 11):
        print(f"{i:4}", end="")
    print()
    print("   " + "-" * 40)
    for i in range(1, 11):
        print(f"{i:2}|", end="")
        for j in range(1, 11):
            print(f"{i * j:4}", end="")
        print()


# ZADANIE 10
# Napisz program, który odczyta plik tekstowy dane.txt i poda liczbę linii, słów i znaków w pliku
def zadanie10():
    nazwa = input("Podaj nazwę pliku (domyślnie: dane.txt): ").strip() or "dane.txt"
    try:
        with open(nazwa, encoding="utf-8") as f:
            zawartosc = f.read()
        linie = zawartosc.splitlines()
        slowa = zawartosc.split()
        print(f"\nPlik: {nazwa}")
        print(f"  Liczba linii: {len(linie)}")
        print(f"  Liczba słów:  {len(slowa)}")
        print(f"  Liczba znaków:{len(zawartosc)}")
    except FileNotFoundError:
        print(f"Błąd: Plik '{nazwa}' nie został znaleziony.")


ZADANIA = {
    "1": ("Suma liczb parzystych", zadanie1),
    "2": ("Liczby pierwsze", zadanie2),
    "3": ("Odwracanie ciągu", zadanie3),
    "4": ("Zamiana temperatur", zadanie4),
    "5": ("Lista bez duplikatów", zadanie5),
    "6": ("Silnia (rekurencja)", zadanie6),
    "7": ("Słownik liczników", zadanie7),
    "8": ("Gra w zgadywanie liczby", zadanie8),
    "9": ("Tabliczka mnożenia", zadanie9),
    "10": ("Odczyt pliku i analiza", zadanie10),
}


def menu():
    while True:
        print("\n" + "=" * 40)
        print("      MENU — wybierz zadanie")
        print("=" * 40)
        for nr, (nazwa, _) in ZADANIA.items():
            print(f"  {nr:>2}. {nazwa}")
        print("   0. Wyjście")
        print("=" * 40)

        wybor = input("Twój wybór: ").strip()

        match wybor:
            case "0":
                print("Do widzenia!")
                break
            case nr if nr in ZADANIA:
                print(f"\n--- Zadanie {nr}: {ZADANIA[nr][0]} ---")
                ZADANIA[nr][1]()
            case _:
                print("Nieprawidłowy wybór. Wpisz liczbę od 0 do 10.")


if __name__ == "__main__":
    menu()
