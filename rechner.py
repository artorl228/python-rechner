"""Einfacher Taschenrechner für die Konsole."""


def rechnen(a, operator, b):
    """Berechnet a (operator) b und gibt das Ergebnis zurück."""
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        if b == 0:
            raise ZeroDivisionError("Durch 0 kann man nicht teilen.")
        return a / b
    raise ValueError("Unbekannter Operator. Erlaubt: + - * /")


def zahl_eingeben(text):
    """Fragt so lange nach, bis eine gültige Zahl eingegeben wird."""
    while True:
        eingabe = input(text).replace(",", ".")
        try:
            return float(eingabe)
        except ValueError:
            print("Das ist keine Zahl. Bitte noch einmal.")


def main():
    print("Taschenrechner (zum Beenden: q)")
    while True:
        operator = input("Operator (+ - * /) oder q: ").strip()
        if operator == "q":
            print("Tschüss!")
            break
        if operator not in ("+", "-", "*", "/"):
            print("Bitte einen der Operatoren + - * / eingeben.")
            continue

        a = zahl_eingeben("Erste Zahl: ")
        b = zahl_eingeben("Zweite Zahl: ")

        try:
            ergebnis = rechnen(a, operator, b)
            print(f"{a} {operator} {b} = {ergebnis}")
        except ZeroDivisionError as fehler:
            print(f"Fehler: {fehler}")


if __name__ == "__main__":
    main()
