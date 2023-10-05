import os

def main():
    while True:
        liczba = input("Podaj liczbe: ")
        saveToFile(liczba)
        wynik = getFromFile()
        print("Wynik: " + wynik)


def saveToFile(liczba):
    with open('dane.txt', 'w') as file:
        file.write(liczba + "\n")
        file.close()

def getFromFile():
    while not os.path.exists('wyniki.txt'):
        pass
    with open('wyniki.txt', 'r') as file:
        wynik = file.readline()
        file.close()
        os.remove('wyniki.txt')
        return wynik
    
if __name__ == '__main__':
    main()