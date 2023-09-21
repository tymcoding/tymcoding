import pandas as pd

# # 读取 CSV 文件
data = pd.read_csv('output.csv')
#
# # 打印数据的前几行
print(data.columns)
print(data.loc[:,:"制作数"])

# 首先，我们导入了 Pandas 库，并使用 pd 作为别名。
# read_csv() 是 Pandas 的一个函数，用于读取 CSV 格式的文件。在这个例子中，我们假设有一个名为 'data.csv' 的 CSV 文件需要被读取。你可以将文件路径替换成你实际的文件路径或文件名。
# data 是一个 Pandas 的 DataFrame 对象，它接收了从 CSV 文件中读取的数据。
# head() 是 DataFrame 对象的一个方法，它用于返回数据的前几行，默认返回前 5 行。你可以指定参数来返回更多或更少的行数。
# 最后，通过使用 print() 函数，我们打印出了 data.head() 的结果，即数据的前几行。


#####
# 读取 Excel 文件
# data = pd.read_excel('test.xlsx')
# print(data)
# # 将数据保存为 CSV 文件
# data.to_csv('output.csv', index=False)

#####






# DataFrame 是 Pandas 库中最重要的数据结构之一，它提供了许多方法来操作和处理数据。下面是一些常用的 DataFrame 方法：
#
# head(n)：返回数据的前 n 行，默认为前 5 行。
# tail(n)：返回数据的后 n 行，默认为后 5 行。
# info()：展示数据的基本信息，包括列名、非空值数量、每列的数据类型等。
# describe()：对数值列进行统计描述，包括计数、均值、标准差、最小值、最大值等。
# shape：返回数据框的维度（行数和列数）。
# columns：返回数据框的列名列表。
# index：返回数据框的索引列表。
# values：将数据框转换为一个 Numpy 数组（二维）。
# sort_values(by='column', ascending=True)：按照指定列的数值进行排序，默认升序。
# dropna()：删除包含缺失值的行或列。
# fillna(value)：将数据框中的缺失值填充为指定的值。
# groupby('column')：按照指定列的值进行分组。
# pivot_table(values, index, columns)：根据指定的列生成数据透视表。
# loc[row_indexer, col_indexer]：通过标签选择行和列。
# iloc[row_indexer, col_indexer]：通过索引选择行和列。