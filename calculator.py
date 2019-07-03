def printInfo():
    print("----------------------")
    print("1. 더하기")
    print("2. 빼기")
    print("3. 곱하기")
    print("4. 나누기")
    print("5. 끝")

def selectOption():
    # while True:
    print("----------------------")
    choice = int(input("무엇? "))
    if choice > 0 and choice < 5:
        return choice
    elif choice == 5:
        return choice
            
    else:
        print("----------------------")
        print("잘못입력!!")
            # printInfo()
            # continue
        return "잘못입력"

def calculate(c):
    while True:
        print("----------------------")
        x = int(input("숫자1:"))
        y = int(input("숫자2:"))
        if c == 1:
            return x + y
        elif c == 2:
            return x - y
        elif c == 3:
            return x * y
        elif c == 4:
            if x == 0 or y == 0:
                print("----------------------")
                print("0으로 나눌수 없습니다")
                continue   
            else:
                return x / y

def printResult(r):
    print("----------------------")
    print("결과: ", r)

def run():
    while True:
        printInfo()
        choice = selectOption()
        if choice == 5:
            break
        elif choice == "잘못입력":
            continue
        result = calculate(choice)
        printResult(result)
        
run()
