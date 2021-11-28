stones_array1 = [1, 3, 5, 7, 8, 9, 12, 14, 17, 21]

all_sum = sum(stones_array1)
sum_two = 0
j = 0  # с помощью этой переменной можно узнать, какие камни во второй куче, разряд 1 -- взяли в кучу камень с
# соответствующей разряду позиции в массиве
for i in range(0, 1 << len(stones_array1), 1):
    current_sum = 0
    position = 0  # на каком разряде находимся
    k = i  # мы сохраняем i в к, чтобы не потерять i
    while k > 0:
        if k % 2 == 1:
            current_sum += stones_array1[position]
        k = k // 2
        position += 1
    if abs((all_sum - sum_two) - sum_two) > abs((all_sum - current_sum) - current_sum):
        sum_two, j = current_sum, i

print(f'Сумма первой кучи: {all_sum-sum_two}, второй: {sum_two}, их разность: {abs((all_sum-sum_two) - sum_two)}.')

# далее просто красивый вывод, показывающий, какие камни в какой куче лежат

heap_1 = []
heap_2 = []
position = 0
k = j
for i in range(0, len(stones_array1), 1):  # для того, чтобы наполнить другую кучу, пробегаем ВСЕ БИТЫ, даже если
    # страшие разряды нули.
    if (k % 2) == 1:
        heap_2.append(stones_array1[position])
    else:
        heap_1.append(stones_array1[position])
    k = k // 2
    position += 1

print(f"Первая куча: {heap_1}, её сумма: {sum(heap_1)}. Вторая куча: {heap_2}, её сумма: {sum(heap_2)}.\n"
      f"Разность: {abs(sum(heap_1) - sum(heap_2))}.")
