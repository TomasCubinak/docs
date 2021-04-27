list1 = [1, 2, 3, 4, 5]
list2 = ['one', 'two', 'three', 'four', 'five']



zipped = list(zip(list1, list2))

print(zipped)

unzipped = list( zip(*zipped))

print(unzipped)

# for i in range(5):
#     list1[i]
#     list2[2]

# for (l1, l2), in zip(list1, list2):
#     print(l1)
#     print(l2)

item = ['Apple', 'Banama', 'Orange']
count = [3, 6, 4]
prices = [0.99, 0.25, 0.50]

sentences = []
for (item, count, price) in zip(item, count, prices):
    item, count, prices = str(item), str(count), str(prices)
    sentence = 'I bought ' + count + ' ' + item + 's at' + prices + '.'
    sentences.append(sentence)
print(sentence)