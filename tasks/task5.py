# tasks/task5.py

def solve():
# Ниже пишите решение задачи
    symbols = input()
    char1, char2, char3 = symbols.split()s

    code1 = ord(char1)
    code2 = ord(char2)
    code3 = ord(char3)

    print("Код символа", char1, "равен", code1)
    print("Код символа", char2, "равен", code2)
    print("Код символа", char3, "равен", code3)
   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()