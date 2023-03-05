# Условие задачи: дается две строки needle и haystack,
# верните индекс первого появления иглы в стоге сена или -1, если игла не является частью стога сена.
# Пример:
# Ввод: haystack = "sadbutsad", needle = "sad"
# Вывод: 0
# Ввод: haystack = "leetcode", needle = "leeto"
# Вывод: -1

print('Введите стог сена')
haystack = input()
len_haystack = len(haystack)
print('Введите иглу')
needle = input()
len_needle = len(needle)
for i in range(len_haystack):
    if haystack[i] == needle[0]:
        index = i
        break
if needle == haystack[index:len_needle+index]:
    print(index)
else:
    print(-1)
