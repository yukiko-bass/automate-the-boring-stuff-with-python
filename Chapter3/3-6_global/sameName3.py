def spam():
    global eggs
    eggs = 'spam'     # グローバル変数になる


def bacon():
    eggs = 'bacon'  # ローカル変数になる
    print('inner bacon() ' + eggs)


def ham():
    print(eggs)  # グローバル変数になる


eggs = 42  # グローバル変数になる
spam()
print(eggs)

bacon()
print(eggs)
