import os

def main():
    while True:
        wynik = int(getFromFile()) + 1
        saveToFile(str(wynik))


def saveToFile(wynik):
    with open('wyniki.txt', 'w') as file:
        file.write(wynik + "\n")
        file.close()

def getFromFile():
    while not os.path.exists('dane.txt'):
        pass
    with open('dane.txt', 'r') as file:
        liczba = file.readline()
        file.close()
        os.remove('dane.txt')
        return liczba

if __name__ == '__main__':
    main()

