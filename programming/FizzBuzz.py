for num in range(1, 101):
    string = ''

    # ここから記述
    if num % 3 == 0:
        string += 'Fizz'    #3で割り切れる数なら"Fizz"を追加
    if num % 5 == 0:
        string += 'Buzz'    #5で割り切れる数なら"Buzz"を追加
    if string == '':
        string = str(num)   #ここまでで何も"string"に単語が入っていなければ，数字を文字として代入
    # ここまで記述

    print(string)
