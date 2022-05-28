def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)


def serch_index(sorted_array, target_number):
    # ここから記述
    left = 0  # 探索するデータ範囲の左端，右端のindexを指定
    right = len(sorted_array) - 1

    while left <= right:  # 左端のindexが右端のindexを超えるまでループ
        middle = (left + right) // 2
        if sorted_array[middle] == target_number:  # 探索範囲の中央値に一致したらindexを返す
            return middle
        elif sorted_array[middle] < target_number:  # ターゲットが中央値よりも大きいときは次のループで後半を探索
            left = middle + 1
        else:  # ターゲットが中央値よりも小さいときは次のループで前半を探索
            right = middle - 1
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1


if __name__ == '__main__':
    main()
