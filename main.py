'''Напишите программу, которой на вход подается последовательность чисел через пробел, а также запрашивается у пользователя любое число.
В качестве задания повышенного уровня сложности можете выполнить проверку соответствия указанному в условии ввода данных.
Далее программа работает по следующему алгоритму:
Преобразование введённой последовательности в список
Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.
При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска, который был рассмотрен в этом модуле. Реализуйте его также отдельной функцией.
 
Подсказка
Помните, что у вас есть числа, которые могут не соответствовать заданному условию. В этом случае необходимо вывести соответствующее сообщение

'''

# Bubble sort array
def sorting(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

# Return previous input number index
def check_index(array, element, left, right):
    if left > right: 
        return False 
    middle = (right+left) // 2 
    if array[middle-1] < element and array[middle] >= element:
        return middle - 1
    elif element < array[middle]:
        return check_index(array, element, left, middle-1)
    else: 
        return check_index(array, element, middle+1, right)


# Checking input: spaces and integers
while True: 
    try:
        text = input('Enter numbers separeted by space: ')   
        if ' ' not in text:
            raise ValueError('Wrong input!')
        lst = list(map(int, text.split()))
        break
    except ValueError:
        print('Wrong input! Missing the spaces or enter integers!')

sorting_lst = sorting(lst)

# Checking num = integer
while True:
    try:
        num = input('Enter integer: ')
        num = int(num)
        if num > max(sorting_lst) or num <= min(sorting_lst):
            raise ValueError('Wrong input!')
        break
    except ValueError:
        print('Wrong input! Enter the integer or out of scope!')

# Output sorting list
print('Sorting list: ', sorting_lst)

# Output index
index = check_index(lst, num, 0, len(sorting_lst)-1)
print('Index: ', index)