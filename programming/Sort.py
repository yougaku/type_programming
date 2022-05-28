def main():
    # ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]


def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) <= 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    left = 0  # 左から検索していく値のインデックス
    right = len(array) - 1  # 右から検索していく値のインデックス

    while left < right:
        while array[left] < pivot:  # pivotより大きい値まで左から移動
            left += 1

        while array[right] > pivot:  # pivotより小さい値まで右から移動
            right -= 1

        if right < left:  # 左端と右端の位置が反転したら並べ替え終了
            break

        array[left], array[right] = array[right], array[left]  # 見つかった左の値と右の値を入替

    array[:left] = sort(array[:left])  # 分割した左部分を再帰的に処理を繰り返す
    array[left + 1:] = sort(array[left + 1:])  # 分割した右部分を再帰的に処理を繰り返す

    return array
    # ここまで記述


if __name__ == '__main__':
    main()
