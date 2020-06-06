def collatz(number):
    # 偶数
    if number % 2 == 0:
        return number / 2
    elif number % 2 == 1:
        return 3 * number + 1


print('整数を入力してください。:')
while True:
    try:
        input_number = int(input())
    except ValueError as identifier:
        print('入力された文字は整数ではありません。整数を入力してください。')
        continue

    print(collatz(input_number))
