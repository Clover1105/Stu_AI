## （四）Pandas Series数据处理

### 1. Pandas库简介

#### Pandas

Pandas是一个开源的、用于数据处理和分析的Python库，特别适合处理表格类数据。它建立在NumPy 数组之上，提供了高效的数据结构和数据分析工具，使得数据操作变得更加简单、便捷和高效。

#### 核心

**数据结构**

`Series`：==一维数组==，可以存储任何数据类型（整数、字符串、浮点数等），每个元素都有一个与之对应的标签（索引）。 

`DataFrame`：==二维表格型数据结构==，可以视为<u>多个 `Series` 对象的集合</u>，每一列都是一个 `Series`。 每列可以有不同的数据类型，并且有行和列的标签。

**数据操作**

读取和保存数据：支持多种数据格式，如 CSV、Excel、SQL 数据库、JSON 等。 

数据选择和过滤：提供灵活的索引和条件筛选功能，方便数据的提取和过滤。 

数据清洗：提供了处理缺失数据、重复数据、异常值等数据清洗功能。 

数据转换：通过 `apply()` , `map()` , `replace()` 等方法进行数据转换。 

数据合并：使用 `concat()` , `merge()` , `join()` 等方法进行数据的横向和纵向合并。 

聚合和分组：使用 `groupby()` 结合 `agg()` , `transform()` 等方法进行数据的分组和聚合。

#### 主要特点

数据结构：Pandas提供了两种主要的数据结构：`Series`（一维数组）和`DataFrame`（二维表 格）。  

数据操作：支持数据的增、删、改、查等操作，以及复杂的数据转换和清洗。 

数据分析：提供丰富的数据分析方法，如聚合、分组、透视等。 

文件读取与写入：支持多种文件格式（如CSV、Excel、SQL等）的读取和写入。

与其他库集成良好：Pandas 与许多其他三方库（如 NumPy、Matplotlib、Scikit-learn等）无缝集成，形成了一个强大的数据科学生态系统。 

强大的社区支持：Pandas 拥有庞大的开发者社区，提供丰富的资源和学习材料。

### 2. Pandas的安装

Pandas是一个第三方库，并不属于Python的系统库，需要进行安装，可输入以下命令进行安装：

`pip install pandas`

### 3. 一维数组Series

一维数组可以理解为excel中的==一列==数据：

标签--可以是默认的，也可以是指定的

<img src="C:/Users/29202/AppData/Roaming/Typora/draftsRecover/4_线性代数与数据挖掘.assets/image-20260528171716542.png" alt="image-20260528171716542" style="zoom:50%;" />

#### Series的创建

在Pandas中，一维数组的创建离不开Pandas库中的Series类。

`class pandas.Series(data=None, index=None, dtype=None, name=None, copy=None,  fastpath=False)`

> `data`：可以是以下几种类型的数据： 
>
> - 标量值，如整数或字符串 
> - Python列表或元组 
> - Python字典 
> - 1d-Ndarray 
>
> `index`：数组或列表，用于定义Series的索引。如果未提供，则默认为从0开始的整数索引。 
>
> `dtype`：指定Series的数据类型。 
>
> `name`：给Series一个名字，用于后续的索引和操作。 
>
> `copy`：布尔值，默认为False【新版本的若指定索引了，会强制复制，即copy=True】。如果为True，则复制数据；如果为False，则尽可能避免复制数据， 仅影响`Ndarray`输入。 
>
> `fastpath`：布尔值，默认为False，通常不需要用户指定。它是Pandas库内部使用的一个优化标 志，当设置为 True 时，允许 Series 构造函数绕过一些检查和验证步骤，加快Series的创建速度。 但由于这个参数跳过了某些安全检查，因此在正常使用中，如果在创建Series时设置了 `fastpath`=True ，而传入的数据又不符合预期，则可能会导致不可预测的行为或错误。

**使用<u>标量</u>创建Series**

```python
import pandas as pd

# 定义一个变量data，并赋值为0
data = 0

# 使用pandas库的Series函数创建一个Series对象
# 第一个参数是要作为Series数据的值，这里是0
# 第二个参数是一个列表，用于指定Series的索引，这里指定了索引为['a', 'b', 'c']
series = pd.Series(data, index=['a', 'b', 'c'])

# 打印输出创建好的Series对象
print(series)
```

**使用<u>列表或元组</u>创建Series**

```python
import pandas as pd

# 定义一个列表data1，其中包含了整数1到5
data1 = [1, 2, 3, 4, 5]

# 定义一个元组data2，其中包含了整数5到1
data2 = (5, 4, 3, 2, 1)

# 使用pandas库的Series函数创建第一个Series对象series1
# 第一个参数data1是要作为Series1数据的值，即列表[1, 2, 3, 4, 5]
# 第二个参数是一个列表['a', 'b', 'c', 'd', 'e']，用于指定Series1的索引
series1 = pd.Series(data1, index=['a', 'b', 'c', 'd', 'e'])

# 使用pandas库的Series函数创建第二个Series对象series2
# 第一个参数data2是要作为Series2数据的值，即元组(5, 4, 3, 2, 1)
# 第二个参数是一个列表['a', 'b', 'c', 'd', 'e']，用于指定Series2的索引
series2 = pd.Series(data2, index=['a', 'b', 'c', 'd', 'e'])

# 打印输出创建好的第一个Series对象series1
print(series1)

# 打印输出创建好的第二个Series对象series2
print(series2)
```

**使用<u>字典</u>创建Series**

使用字典创建Series时，==字典的键就是索引，字典的值就是该索引对应的值==。如果使用字典创建 Series，并且指定了与字典的键不同的index参数，那么生成的Series数组中的数据就是以index参数的值为索引，但索引所对应的值是`NaN`。 ==在Pandas中， `NaN `（Not a Number）是一个特殊的浮点数，用于表示缺失数据或无效数据==。 `NaN `是  IEEE 浮点标准的一部分，Pandas 使用 `NaN `来表示数据集中缺失或未定义的值。

```python
import pandas as pd

# 定义一个字典data，其中包含了三个键值对，键分别为'a'、'b'、'c'，对应的值分别为1、2、3
data = {'a': 1, 'b': 2, 'c': 3}

# 使用pandas库的Series函数创建一个Series对象。
# 当传入一个字典作为参数时，字典的键会自动成为Series的索引，字典的值会成为对应索引下的数值。
series = pd.Series(data)

# 打印输出创建好的Series对象
print(series)
```

**使用`Ndarray`创建Series**

```python
import pandas as pd
import numpy as np

# 使用numpy的array函数创建一个一维数组data，数组中包含了整数1到5。
data = np.array([1, 2, 3, 4, 5])

# 使用pandas库的Series函数创建一个Series对象。
# 传入刚刚创建的一维numpy数组data作为参数，此时会将该数组的数据依次作为Series的数值，
# 并且会自动生成一个默认的整数索引（从0开始，依次递增，与数组元素的下标对应）。
# 自定义索引会强制复制，即copy=True
series = pd.Series(data,index=['a', 'b', 'c', 'd', 'e'],copy=False)

# 新版本的panda，使用series[0]会添加元素，而不会将series[0] 按位置索引工作
# series[0] = 100
series.iloc[0] = 100


# 打印输出创建好的Series对象，以便查看其具体内容，包括索引和对应的数据值等信息。
print(series)
print(data)
```

#### Series的属性（16）

**index**

==返回Series中的索引==。

```python
import pandas as pd

# 创建Series数组
series = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

# 打印输出该Series对象的索引。
# Series对象的index属性可以获取到它的索引信息，这里会输出索引['a', 'b', 'c']。
print(series.index)

# 重新给Series对象的索引赋值。
# 将原来的索引['a', 'b', 'c']修改为新的索引['e', 'f', 'g']，
# 这会改变Series对象中每个数据元素对应的索引标识。
series.index = ['e', 'f', 'g']	# 数量必须一一对应，不能少，不能多

# 再次打印输出修改索引后的Series对象，
print(series)
```

**values**

用于==返回Series中的数据==，返回的数据将==以`Ndarray`数组的形式存在==。

```python
import pandas as pd

# 创建Series数组
series = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

# 打印输出该Series对象的数据。
print(series.values)
print(type(series.values))

# # values无法通过直接赋值的方式去修改
# series.values = ['e', 'f', 'g']
# print(series)
```

**name**

用于==返回Series的名称==，如果创建时指定了name参数，那么该属性的返回值就是name参数，如果没有指定则为None。

```python
import pandas as pd

# 创建Series数组
series = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

# 打印输出该Series对象的name属性值。
print(series.name)

# 给Series对象的name属性赋值为'test'。
# 这相当于给这个Series对象起了一个名字，方便在后续处理或展示数据时进行识别和区分。
series.name = 'test'

# 再次打印输出该Series对象的name属性值，
print(series.name)
```

**dtype和dtypes**

对于Series来说，`dtype`和`dtypes`的作用是一样的，都是用来==返回Series对象的数据类型==。 

需要注意的是：该属性是只读属性，不可以通过直接赋值的方式去修改数据类型。

```python
import pandas as pd

# 创建Series数组
series = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

# 打印输出该Series对象的数据类型。
# Series对象的dtype属性可以获取到其数据的类型，这里创建的Series数据是整数类型，所以会输出'int64'。
print(series.dtype)

# Series对象的dtype属性是只读属性，不可以直接通过赋值的方式来改变数据类型。
# 要改变Series对象的数据类型，需要使用astype等合适的方法来进行转换操作。

# series.dtype = 'float32'
#
# print(series.dtype)
```

**shape**

用于==描述Series的形状==，该返回值是一个==元组==。

```python
import pandas as pd
import numpy as np

# 创建Series数组
series = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
arr = np.array([1,2,3])

# 打印数组的形状
print(series.shape)
print(arr.shape)
```

**size**

用于==返回Series的元素数量==，该返回值是一个==整数==。

```python
import pandas as pd

# 创建Series数组
series = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

# 打印数组元素的元素数量
print(series.size)
```

**empty**

用来==表示Series数组是否为空==，返回值一个布尔值，如果数组里一个元素都没有就返回True，否则返回 False。

```python
import pandas as pd

# 创建Series数组
series = pd.Series()

# 判断数组是否为空
print(series.empty)
```

**hasnans**

用于==返回数组中是否包含NaN值==，如果数组中存在NaN，那么返回True，否则返回False。

```python
import pandas as pd
import numpy as np

# 创建Series数组
# 用numpy下的nan替代无效，缺失数据
series = pd.Series([1, 2, 3, np.nan], index=['a', 'b', 'c', 'd'])
series2 = pd.Series([np.nan])   # 是空值，但不代表数组为空

# 判断数组是否存在NaN值
print(series)
print(series.hasnans)
print(series2.empty)
```

**is_unique**

用于返回数组中的元素是否为独一无二的，如果所有的元素都是独一无二的，即数组中没有重复元素， 那么就返回True，否则返回False。

```python
import pandas as pd

# 创建Series数组
series = pd.Series(['a', 'b', 'c'])

# 判断数组中是否存在重复的元素
print(series.is_unique)
```

**nbytes**

用于返回该Series对象中所有数据占用的总字节数。

```python
import pandas as pd

# 创建Series数组
series = pd.Series([1, 2, 3, 4, 5], dtype='int64')

# 获取数组元素所占用的内存大小
print(series.nbytes)
```

**axes**

用于返回series对象行轴标签的列表。

和index差不多

```python
import pandas as pd

# 创建Series数组
series = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'], dtype='int64')

# 获取数组的行轴标签
print(series.axes)
```

**ndim**

返回Series数组的维度，对于Series数组来说，它的维度始终为1。

```python
import pandas as pd

# 创建Series数组
series = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'], dtype='int64')

# 获取数组的索引
print(series.ndim)
```

**array**

用于返回Series的底层数组，包括数组的元素、数组的长度及数组元素的数据类型。

```python
import pandas as pd
import numpy as np

# 创建一个NumPy数组
data = np.array([1, 2, 3, 4, 5])

# 使用NumPy数组创建一个Pandas Series
series = pd.Series(data)

# 打印Series的底层数据作为一个Pandas的Array对象
print(series.array)

# 打印上述Array对象的类型
print(type(series.array))
```

**attrs**

返回series的自定义属性，可以用来存储额外的说明性数据。

```python
import pandas as pd

# 创建一个包含整数1到5的Pandas Series
series = pd.Series([1, 2, 3, 4, 5])

# 打印额外的属性
print(series.attrs)

# 给Series添加额外的属性，这里添加了来源和时间信息
series.attrs = {'source': 'file1', 'time': '19:27:27'}

# 打印Series本身，将显示其数据和索引
print(series)

# 打印Series的额外属性
print('额外属性', series.attrs)
```

**is_monotonic_decreasing**

返回一个布尔值，表示Series是否按降序排列。

```python
import pandas as pd

# 创建一个Pandas Series，其值从5递减到1
series = pd.Series([5, 4, 3, 2, 1])

# 打印检查Series是否单调递减的结果
# 由于Series中的值是递减的，所以这个表达式将返回True
print(series.is_monotonic_decreasing)
```

**is_monotonic_increasing**

返回一个布尔值，表示Series 是否按升序排列。

```python
import pandas as pd

# 创建一个Pandas Series，其值从1递增到5
series = pd.Series([1, 2, 3, 4, 5])

# 打印检查Series是否单调递增的结果
# 由于Series中的值是递增的，所以这个表达式将返回True
print(series.is_monotonic_increasing)
```

#### Series中元素的索引与访问

**位置索引**

可以使用整数索引来访问Series中的元素，就像访问列表一样。

```python
import pandas as pd

# 创建一个Series
series = pd.Series([10, 20, 30, 40, 50])

# 通过位置索引获取元素
print(series[0])
print(series[2])
```

**标签索引** 

除了使用位置索引之外，还可以使用标签进行索引，与访问字典中的元素类似。

```python
import pandas as pd

# 创建一个带有标签的Series
series = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])

# 通过标签索引获取元素
print(series['a'])
print(series['c'])
```

**切片索引** 

Series对象的切片方式有两种，第一种是使用位置切片，其使用方法与列表的切片类似；第二种是使用标签切片，其语法与位置切片类似，都是 `start:stop` ，且开始值与终止值可以省略，但与位置切片不同的是，标签切片的范围是左右都闭合，即既包含start，又包含stop，而位置切片是左闭右开，只包含 start，不包含stop。

```python
import pandas as pd

# 创建一个带有标签的Series
series = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])

# 通过位置切片
print(series[:]) 

# 通过标签切片
print(series['b':'d'])
```

**loc与iloc**

loc与iloc也是Series对象的属性，它们的作用就是用来访问Series中的元素，loc是基于标签的索引，iloc 是基于位置的索引。

```python
import pandas as pd

# 创建一个带有标签的Series
series = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])

# 使用.loc通过标签索引
print(series.loc['a'])

# 使用.iloc通过位置索引
print(series.iloc[0:2])
print(series.iloc[2])
```

**at与iat**

at与iat也是Series对象的属性，可以用来访问元素，at是基于标签的索引，iat是基于位置的索引。

```python
import pandas as pd

# 创建一个带有标签的Series
series = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])

# 使用.at通过标签索引
print(series.at['a'])

# 使用.iat通过位置索引
print(series.iat[0])
print(series.iat[2])
```

**head**

head是Series对象的方法，用于快速查看 Series 数据的开头部分内容。

`series.head(n=None)`

> `n` ：是可选参数，用于指定要返回的行数。如果不提供该参数，默认值为 5 。

```python
import pandas as pd

# 创建一个Series对象
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
series = pd.Series(data, index=index)

# 使用head函数查看前5行数据
print(series.head())
```

**tail**

tail的用法与head类似，但不同的是，它用于快速查看 Series 数据的末尾部分内容。

`series.tail(n=None)`

> `n` ：是可选参数，用于指定要返回的行数。若不提供该参数，默认值为 5 。

```python
import pandas as pd

# 创建一个Series对象
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
series = pd.Series(data, index=index)

# 使用tail函数查看后5行数据
print(series.tail())
```

**isin**

该函数用于判断 Series 中的每个元素是否在指定的一组值中，它会返回一个与原 Series 长度相同的布尔型 Series ，其中对应位置为 True 表示该位置的元素在指定的值集合中， False 则表示不在。

`series.isin(values)`

> `values` ：是一个可迭代对象（如列表、元组、集合等），用于指定要进行判断的一组值。

```python
import pandas as pd

# 创建一个Series对象
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

# 指定要判断的一组值
values_to_check = [20, 40]

# 使用isin函数进行判断
result = series.isin(values_to_check)
print(result)
```

**get**

`Series.get` 方法用于通过标签来获取Series中的元素。

`Series.get(key, default=None)`

> `key` : 你想要获取的元素的标签。 
>
> `default` : 可选参数，如果 key 不在标签中，返回这个默认值。如果没有指定，默认为 None 。

```python
import pandas as pd

# 创建一个示例Series
s = pd.Series(['apple', 'banana', 'cherry'], index=[1, 2, 3])

# 使用get方法获取元素
print(s.get(2)) 
print(s.get(4, 'Not Found')) 
```

#### 数据操作

**数据清洗**

数据清洗指对Series对象中的某些值进行删除、修改等操作，分别使用以下方法： 

==dropna()：删除包含NaN值的行。==

`series.dropna(axis=0, inplace=False)`

> `axis `：可选参数，用于指定按哪个轴删除缺失值。对于 Series 对象，因为它是一维数据结构， 只有一个轴，所以此参数默认值为 0 ，且一般不需要修改这个参数（在处理 `DataFrame` 时该参数 才有更多实际意义，如 axis = 0 表示按行删除， axis = 1 表示按列删除）。 
>
> `inplace `：可选参数，用于指定是否在原 Series 对象上进行操作。如果 `inplace = True` ，则会 直接在原 Series 上删除缺失值，原 Series 会被修改；如果 `inplace = False` （默认值），则会 返回一个删除了缺失值的新 Series ，原 Series 保持不变。

```python
import pandas as pd
import numpy as np

# 创建一个包含缺失值的Series对象
data = [1, np.nan, 3, 4, np.nan]
series = pd.Series(data)

# 使用dropna函数删除缺失值，返回新的Series
new_series = series.dropna()
print(new_series)
```

==fillna()：填充NaN值。==

`Series.fillna(value=None, method=None, axis=None, inplace=False, limit=None,  downcast=None)`

<u>pandas 的新版本（2.1+）中 fillna() 的 method 参数已被弃用。</u>

现在应该使用专门的方法：

- 前向填充: ffill() 或 fillna(method='ffill') → 改为 ffill()
- 后向填充: bfill() 或 fillna(method='bfill') → 改为 bfill()

> value ：用于填充缺失值的标量值或字典。如果传递的是字典，则字典的键应该是要填充的标签， 值是用于填充的值。 
>
> method ：字符串，表示填充的方法。可选值包括： 
>
> - pad / ffill ：用前一个非缺失值去填充缺失值。 
> - bfill / backfill ：用后一个非缺失值去填充缺失值。 
>
> axis ：填充的轴，对于 Series 对象来说，这个参数通常不需要指定，因为 Series 是一维的。 
>
> inplace ：布尔值，表示是否在原地修改数据。如果为 True ，则直接在原 Series 上修改，不 返回新的对象。 
>
> limit ：整数，表示最大填充量。如果指定，则只填充前 limit 个缺失值。 
>
> downcast ：字典，用于向下转换数据类型。例如，可以将 float64 转换为 float32 。

```python
import pandas as pd
import numpy as np

# 创建一个包含缺失值的 Series
s = pd.Series([1, np.nan, 3, np.nan, 5])

# 使用标量值填充
filled_with_scalar = s.fillna(0)
print(filled_with_scalar)

# 使用前向填充
filled_with_ffill = s.fillna(method='ffill')
print(filled_with_ffill)

# 使用后向填充
filled_with_bfill = s.fillna(method='bfill')
print(filled_with_bfill)

# 使用 limit 参数
filled_with_limit = s.fillna(value=0, limit=1)
print(filled_with_limit)
```

==isnull()：检测Series对象中的缺失值，它会返回一个布尔型Series，其中每个元素表示原Series对 应位置的值是否为缺失值（NaN）。==

`Series.isnull()`

```python
import pandas as pd
import numpy as np

# 创建一个包含缺失值的Series
s = pd.Series([1, 2, np.nan, 4, np.nan])

# 使用isnull()方法检测缺失值
missing_values = s.isnull()
print(missing_values)
```

==drop_duplicates()：用于去除Series对象中的重复项。==

`Series.drop_duplicates(keep='first', inplace=False, ignore_index=False)`

> keep：可选参数，决定了如何处理重复项。有三个选项： 
>
> - 'first' ：默认值，保留第一次出现的重复项。 
> - 'last' ：保留最后一次出现的重复项。 
> - False ：不保留任何重复项，即删除所有重复项。 
>
> inplace ：布尔值，默认为 False 。如果设置为 True ，则直接在原始Series上进行操作，返回值 为 None 。如果设置为 False ，则返回一个新的Series，不修改原始Series。 
>
> ignore_index ：布尔值，默认为 False 。如果设置为 True ，则结果的索引将被重新设置，以反 映删除重复项后的新顺序。如果设置为 False ，则保留原始索引。

```python
import pandas as pd

series = pd.Series(['a', 'b', 'b', 'c', 'c', 'c', 'd'])
series_unique = series.drop_duplicates(keep='first')
print(series_unique)
```

**数据转换**

==replace()：替换特定的值、一系列值或者使用字典映射进行替换。==

`Series.replace(to_replace=None, value=None, inplace=False, limit=None,  regex=False, method='pad')`

> to_replace ：要替换的值，可以是以下类型： 
>
> - 标量：单个值。 
> - 列表：一系列值。 
> - 字典：键是要替换的值，值是替换后的新值。 
> - 正则表达式：如果 regex=True ，则可以使用正则表达式匹配要替换的值。 
>
> value ：替换后的新值，可以是标量或字典。如果 to_replace 是列表，则 value 也应该是相同 长度的列表。 
>
> inplace ：布尔值，表示是否在原地修改数据。如果为 True ，则直接在原 Series 上修改，不 返回新的对象。 
>
> limit ：整数，表示最大替换量。如果指定，则只替换前 limit 个匹配的值。 
>
> regex ：布尔值，表示是否将 to_replace 解释为正则表达式。 
>
> method ：字符串，表示填充的方法，在 to_replace 参数是一个标量、列表或元组，同时 value  参数设置为 None 时，可以使用 method 参数来指定填充缺失值（NaN）的方式。可选值包括： 
>
> - pad / ffill ：用前一个非缺失值去填充缺失值。 
> - bfill ：用后一个非缺失值去填充缺失值。

```python
import pandas as pd

# 创建一个 Series
s = pd.Series([1, 2, 3, 4, 5])

# 进行替换操作
replaced = s.replace(to_replace=2, value=20)
print(replaced)
```

==astype()：用于将 Series 的数据类型（dtype）转换或转换为另一种类型。==

`Series.astype(dtype, copy=True, errors='raise')`

> dtype：你希望将 Series 转换成的数据类型。 
>
> copy：布尔值，默认为 True 。如果为 False ，则转换数据类型时不会复制底层数据（如果可能 的话）。 
>
> errors：默认为 ‘raise’，控制当转换失败时的行为。如果设置为 ‘raise’，则在转换失败时会抛出异 常；如果设置为 ‘ignore’，转换失败后则返回原始 Series ，不做任何修改。

```python
import pandas as pd

s = pd.Series([1, 2, 3, 4, 5])

# 将整数转换为字符串
s_str = s.astype(float)
print(s_str)
```

==transform()：用于对Series中的数据进行转换操作，并返回与原始Series具有相同索引的新 Series。==

`Series.transform(func, axis=0, *args, **kwargs)`

> func : 应用于Series的函数。这个函数可以是内置函数，或者自定义的函数。 
>
> axis : 对于Series来说，这个参数不起作用，因为Series是一维的。在DataFrame上使用时， axis=0 （默认）表示按列应用函数， axis=1 表示按行应用函数。 
>
> *args, **kwargs : 这些参数会被传递给 func 函数。

```python
import pandas as pd

# 自定义一个函数，返回每个元素的平方
def square(x):
    return x ** 2
    
# 创建一个Series
s = pd.Series([1, 2, 3, 4, 5])

# 使用自定义函数对Series进行平方变换
transformed_series = s.transform(square)

print(transformed_series)
```

**数据排序**

==sort_values()：按照值对 Series 进行排序。==

`Series.sort_values(axis=0, ascending=True, inplace=False, kind='quicksort',  na_position='last', ignore_index=False, key=None)`

> axis：默认为 0。对于 Series，这个参数不起作用，因为 Series 是一维的，而 sort_values 总是 在 axis=0 上操作。 
>
> ascending：布尔值，默认为 True 。如果是 True ，则按照升序排列；如果是 False ，则按照降 序排列。 
>
> inplace：布尔值，默认为 False 。如果为 True ，则排序将直接在原始 Series 上进行，不返回新 的 Series。 
>
> kind：排序算法，{‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’}，默认为 ‘quicksort’。决定了使用 的排序算法。 
>
> na_position：{‘first’, ‘last’}，默认为 ‘last’。这决定了 NaN 值的放置位置。 
>
> ignore_index：布尔值，默认为 False 。如果为 True ，则排序后的 Series 将重置索引，使其成 为默认的整数索引。 
>
> key：函数，默认为 None 。如果指定，则这个函数将在排序之前应用于每个值，并且排序将基于 这些函数返回的值。

```python
import pandas as pd
import numpy as np

def square(x):
    return x**2

s = pd.Series([-3, 1, 4, 1, np.nan, 9],index=['a', 'b', 'c', 'd', 'e', 'f'])

# 排序并重置索引
sorted_s = s.sort_values()
print(sorted_s)
sorted_s = s.sort_values(ascending=False,na_position='first')   # first为字符串，要加引号
print(sorted_s)
sorted_s = s.sort_values(ignore_index=True,key=square)
print(sorted_s)
```

==sort_index()：按照索引的顺序对数据进行排序。==

`Series.sort_index(axis=0, level=None, ascending=True, inplace=False,  kind='quicksort', na_position='last', sort_remaining=True, ignore_index=False,  key=None)`

> axis : 默认为0，对于 Series，这个参数不起作用。 
>
> level : 默认为 None，如果索引是多级索引（也称为层次化索引或 MultiIndex），则可以指定要排序的级别。 
>
> ascending : 默认为 True，如果为 True，则按升序排序；如果为 False，则按降序排序。对于多级 索引，可以传递一个布尔值列表，以指定每个级别的排序顺序。 
>
> inplace : 默认为 False，如果为 True，则直接在原对象上进行修改，不会返回一个新的对象。 
>
> kind : {‘quicksort’, ‘mergesort’, ‘heapsort’}，默认为 ‘quicksort’，指定排序算法。‘quicksort’ 是最 快的通用排序算法，但不是稳定的；‘mergesort’ 是稳定的，但可能比 ‘quicksort’ 慢；‘heapsort’  是原地排序算法，但通常比其他两个选项慢。 
>
> na_position : {‘first’, ‘last’}, 默认为 ‘last’，指定 NaN 值应该排在排序结果的开头还是结尾。 
>
> sort_remaining : 默认为 True，对于多级索引，如果为 True，在该level排序后，在排序的基础上 对剩下的级别的元素还会排序。
>
> ignore_index : 默认为 False，如果为 True，则排序后的结果将不再保留原始索引，而是使用默认 的整数索引。 
>
> key：函数，默认为 None 。如果指定，则这个函数将在排序之前应用于每个值，并且排序将基于 这些函数返回的值。

```python
import numpy as np
import pandas as pd

arrays = [np.array(['qux', 'qux', 'foo', 'foo','baz', 'baz', 'bar', 'bar']),
          np.array(['two', 'one', 'two', 'one','two', 'one', 'two', 'one'])
         ]

s = pd.Series([1,2,3,4,5,6,7,8],index=arrays)
print(s)
print(s.shape)
res = s.sort_index(level=1,ascending=True,sort_remaining=True,ignore_index=False)
# res = s.sort_index()
print(res)
```

**数据筛选**

可以使用一个布尔数组来选择满足条件的元素。

```python
import pandas as pd

# 创建一个带有标签的Series
series = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])

# 选择大于30的元素
print(series[series > 30])
```

**数据拼接**

==concat()：用于将多个Pandas对象（如Series或DataFrame）沿着一个轴连接起来的函数。==

`pandas.concat(objs, *, axis=0, join='outer', ignore_index=False, keys=None,  levels=None, names=None, verify_integrity=False, sort=False, copy=None)`

> objs : 参与连接的Pandas对象的列表或元组。例如，可以是多个Series或DataFrame。 
>
> axis : {0或’index’, 1或’columns’}，表示连接的轴，默认为0。0表示沿着行方向连接（索引轴）， 1表示沿着列方向连接（列轴）。 
>
> join : {‘inner’, ‘outer’}，默认为’outer’。如何处理其他轴上的索引。'outer’表示并集，保留所有索 引；'inner’表示交集，只保留所有对象共有的索引。 
>
> ignore_index : 布尔值，默认为False。如果为True，则不保留原索引，而是创建一个新索引，可 以避免重复的索引。 
>
> keys : 序列，默认为None。用于创建分层索引的键。如果提供了keys，则生成的DataFrame或 Series将具有分层索引。 
>
> levels : 序列列表，默认为None。用于构造分层索引的特定级别，如果设置了keys，则默认为 keys。 
>
> names : 列表，默认为None。生成的分层索引中的级别名称。如果提供了keys，表示使用keys作 为索引名称。
>
> verify_integrity : 布尔值，默认为False。如果为True，则检查新连接的轴是否包含重复的索 引，如果发现重复，则引发ValueError。这在确保数据没有重复时很有用。 
>
> sort : 布尔值，默认为False。在连接之前是否对非连接轴上的索引进行排序。这在连接多个 DataFrame时很有用，可以确保索引是有序的。 
>
> copy : 布尔值，默认为None。如果为True，则不管是否需要，都会复制数据。如果为False，则尽 量避免复制数据，除非必要。None表示自动选择。

```python
import pandas as pd

# 创建三个Series
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([4, 5, 6], index=['c', 'd', 'f'])
s3 = pd.Series([7, 8, 9], index=['e', 'f', 'g'])

# 使用concat连接Series
result = pd.concat([s1, s2, s3])
print(result)
```

#### 统计计算

**count**

用于计算 Series 中非NaN（非空）值的数量

```python
import pandas as pd

# 创建一个包含空值的Series
s = pd.Series([1, 2, None, 4, None])

# 使用count()函数计算非空值的数量
count_non_na = s.count()
print(count_non_na)
```

**sum**

`sum()` 函数会计算所有值的总和

`Series.sum(axis=None, skipna=True, numeric_only=None, min_count=0)`

> axis : 对于 Series 对象来说，这个参数通常不起作用，因为 Series 是一维的。它主要在 DataFrame 对象中用于指定操作的轴（0表示按列求和，1表示按行求和）。 
>
> skipna : 布尔值，默认为 True 。如果为 True ，则在计算总和时会忽略 NaN 值，如果为False，则 返回NaN。 
>
> numeric_only : 布尔值，默认为 None 。如果为 True ，则只对数字类型的数据进行计算，只针对 DataFrame。 
>
> min_count : int值，默认为0。表示在计算总和之前，至少需要多少个非 NaN 值。如果非 NaN 值的 数量小于 min_count ，则结果为 NaN 。

```python
import pandas as pd

s = pd.Series([1, 2, None, 4, 5])
total = s.sum(min_count=5)
print(total)  
```

**mean**

`mean() `函数会计算所有值的平均值

`Series.mean(axis=None, skipna=True, numeric_only=None)`

> axis : 对于 Series 对象来说，这个参数通常不起作用，因为 Series 是一维的。它主要在 DataFrame 对象中用于指定操作的轴（0表示按列计算平均值，1表示按行计算平均值）。 
>
> skipna : 布尔值，默认为 True 。如果为 True ，则在计算平均值时会忽略 NaN 值，如果为False， 则返回NaN。 
>
> numeric_only : 布尔值，默认为 None 。如果为 True ，则只对数字类型的数据进行计算，只针对 DataFrame。

```python
import pandas as pd

s = pd.Series([1, 2, 3, 4, 5])
average = s.mean()
print(average)
```

**median**

`median()` 函数用于计算DataFrame或Series中的中位数

`Series.median(axis=0, skipna=True, numeric_only=False)`

> axis : 对于 Series 对象来说，这个参数通常不起作用，因为 Series 是一维的。它主要在 DataFrame 对象中用于指定操作的轴（0表示按列计算中位数，1表示按行计算中位数）。 
>
> skipna : 布尔值，默认为True。如果为True，则在计算中位数之前会排除NaN值，如果为False， 则返回NaN。 
>
> numeric_only : 布尔值，默认为 None 。如果为 True ，则只对数字类型的数据进行计算，只针对 DataFrame。

```python
import pandas as pd

s = pd.Series([1, 2, 3, 4, 5])
median_value = s.median()
print(median_value)
```

**min和max**

`Series.min()` 函数用于计算Series对象中的最小值， `Series.max()` 函数用于计算Series对象中的最大 值。

`Series.min(axis=0, skipna=True, numeric_only=False)`

`Series.max(axis=0, skipna=True, numeric_only=False)`

> axis : 对于 Series 对象来说，这个参数通常不起作用，因为 Series 是一维的。它主要在 DataFrame 对象中用于指定操作的轴（0表示按列计算最小值或最大值，1表示按行计算最小值或 最大值）。 
>
> skipna : 布尔值，默认为True。如果为True，则在计算最值之前会排除NaN值，如果为False，则返回NaN。 
>
> numeric_only : 布尔值，默认为 None 。如果为 True ，则只对数字类型的数据进行计算，只针对 DataFrame。

```python
import pandas as pd

s = pd.Series([1, 2, 3, 4, 5])
min_value = s.min()
max_value = s.max()
print('最小值是：', min_value)
print('最大值是：', max_value)
```

**var**

`Series.var()` 函数用于计算Series对象的方差。

> axis : 对于 Series 对象，这个参数不会产生任何效果，因为 Series 是一维的。在 DataFrame 中， axis 用于指定沿着哪个轴计算方差。 
>
> skipna : 布尔值，默认为 True 。如果为 True ，则在计算方差之前会忽略 NaN 值。如果设置为 False ，计算方差时会包括 NaN 值，通常会导致结果也是 NaN 。 
>
> ddof : 整数，默认为 1 。Delta Degrees of Freedom，用于贝塞尔校正，以得到样本方差的估 计。对于无偏估计（样本方差）， ddof 通常设置为 1 。如果计算总体方差，应该将 ddof 设置为 0 。 
>
> numeric_only : 布尔值，默认为 False 。如果为 True ，则只对数字类型的数据进行方差计算，忽 略非数字类型的数据。

```python
import pandas as pd
import numpy as np

s = pd.Series([1, 2, np.nan, 4, 5])
variance = s.var()
print('方差是：', variance)
```

**std**

`Series.std()` 函数用于计算Series对象的标准差。

`Series.std(axis=None, skipna=True, ddof=1, numeric_only=False, **kwargs)`

> axis : 对于Series来说，这个参数不会产生任何效果，因为Series是一维的。它主要用于 DataFrame，以指定沿着哪个轴计算标准差。 
>
> skipna : 布尔值，默认为True。如果为True，则在计算标准差之前会忽略NaN值，如果为False， 则返回NaN。
>
> ddof : 整数，默认为1。Delta Degrees of Freedom，是贝塞尔校正的参数。对于无偏估计（样本 标准差），ddof通常设置为1。 
>
> numeric_only : 布尔值，默认为False。如果为True，则只对数字类型的数据进行计算，只针对 DataFrame。 
>
> **kwargs : 其他关键字参数。

```python
import pandas as pd
import numpy as np

s = pd.Series([1, 2, np.nan, 4, 5])
std_dev = s.std()
print('标准差是：', std_dev)
```

**quantile**

`Series.quantile()` 方法用于计算Series中数值的分位数。

`Series.quantile(q=0.5, interpolation='linear')`

> q ：这个参数是必需的，它表示要计算的分位数值。可以是单一的数值，也可以是一个数值列表。 例如， q=0.5 表示计算中位数（50%分位数）。 
>
> interpolation ：这个参数决定了当所需的分位数位于两个数据点之间时，应该如何插值。默认 值是 'linear' ，表示线性插值。其他选项包括 'nearest' （最近的值）、 'lower' （选择较小 的值）、 'higher' （选择较大的值）、 'midpoint' （两个值的中间点）。

其计算过程为:

- 首先将Series中的所有非NaN元素按升序排序。

- 假设Series的长度为 `n`, 我们需要计算第 `q` 个分位数的位置下标 `index`:

$$
\text{index} = q \times (n - 1)
$$

- 如果 `index` 是一个整数, 则直接取该位置上的值; 如果 `index` 不是整数, 则需要进行插值计算。

- 根据不同的插值方法, 确定最终的分位数值:

    - `linear` (默认): 线性插值。假设 `index = i + f`, 其中 `i` 是整数部分, `f` 是小数部分。那么分位数为: $Q = x_{i} + f \times (x_{i+1} - x_{i})$, 其中 $x_{i}$ 和 $x_{i+1}$ 是排序后的数据中第 `i` 和 `i+1` 个元素。

    - `lower`: 选择较小的那个值。即取 $x_{i}$。

    - `higher`: 选择较大的那个值。即取 $x_{i+1}$。

    - `nearest`: 选择最近的那个值。如果 `f <= 0.5`, 取 $x_{i}$, 否则取 $x_{i+1}$。

    - `midpoint`: 取这两个值的平均数, 即: $Q = \frac{x_{i} + x_{i+1}}{2}$。


```python
import pandas as pd

# 创建一个示例Series
s = pd.Series([1, 2, 3, 4, 5])

# 计算0.5分位数
median_value = s.quantile(q=0.5, interpolation='linear')

print(median_value)
```

**cummax**

该方法用于计算Series中元素的累积最大值，返回一个相同长度的Series，其中每个位置上的值表示从Series开始到当前位置（包括当前位置）的最大值。

`Series.cummax(axis=None, skipna=True, *args, **kwargs)`

> `axis`: 对于Series来说，这个参数不起作用，因为Series是一维的。在DataFrame上使用时，`axis=0`（默认）表示按列计算，`axis=1`表示按行计算。
>
> `skipna`: 布尔值，默认为`True`。如果为`True`，则在计算累积最大值时会忽略`NaN`值；如果为`False`，则任何`NaN`值都会传播，并且会导致结果在该位置及之后的值都为`NaN`。
>
> `*args`, `**kwargs`: 这些参数用于兼容性，通常不需要使用。

```python
import pandas as pd

# 创建一个Series
s = pd.Series([2, 1, 3, 5, 4, 6])

# 计算累积最大值
cummax_series = s.cummax()

print(cummax_series)
```

**cummin**

该方法用于计算Series中元素的累积最小值，返回一个相同长度的Series，其中每个位置上的值表示从Series开始到当前位置（包括当前位置）的最小值。

`Series.cummin(axis=None, skipna=True, *args, **kwargs)`

> `axis`: 对于Series来说，这个参数不起作用，因为Series是一维的。在DataFrame上使用时，`axis=0`（默认）表示按列计算，`axis=1`表示按行计算。
>
> `skipna`: 布尔值，默认为`True`。如果为`True`，则在计算累积最小值时会忽略`NaN`值；如果为`False`，则任何`NaN`值都会传播，并且会导致结果在该位置及之后的值都为`NaN`。
>
> `*args`, `**kwargs`: 这些参数用于兼容性，通常不需要使用。

```python
import pandas as pd

# 创建一个Series
s = pd.Series([2, 1, 3, 5, 4, 6])

# 计算累积最小值
cummin_series = s.cummin()

print(cummin_series)
```

**cumsum**

用于计算Series中元素的累积和。该方法返回一个相同长度的Series，其中每个位置上的值表示从Series开始到当前位置（包括当前位置）的所有元素的累加和。

`Series.cumsum(axis=None, skipna=True, *args, **kwargs)`

> `axis`: 对于Series来说，这个参数不起作用，因为Series是一维的。在DataFrame上使用时，`axis=0`（默认）表示按列计算，`axis=1`表示按行计算。
>
> `skipna`: 布尔值，默认为`True`。如果为`True`，则在计算累积和时会忽略`NaN`值；如果为`False`，则任何`NaN`值都会传播，并且会导致结果在该位置及之后的值都为`NaN`。
>
> `*args`, `**kwargs`: 这些参数用于兼容性，通常不需要使用。

```python
import pandas as pd

# 创建一个Series
s = pd.Series([1, 2, np.nan, 4, 5])

# 计算累积和
cumsum_series = s.cumsum()

print(cumsum_series)
```

**cumprod**

用于计算Series中元素的累积乘积。该方法返回一个相同长度的Series，其中每个位置上的值表示从Series开始到当前位置（包括当前位置）的所有元素的累积乘积。

`Series.cumprod(axis=None, skipna=True, *args, **kwargs)`

> `axis`: 对于Series来说，这个参数不起作用，因为Series是一维的。在DataFrame上使用时，`axis=0`（默认）表示按列计算，`axis=1`表示按行计算。
>
> `skipna`: 布尔值，默认为`True`。如果为`True`，则在计算累积乘积时会忽略`NaN`值；如果为`False`，则任何`NaN`值都会导致结果在该位置及之后的值都为`NaN`。
>
> `*args`, `**kwargs`: 这些参数用于兼容性，通常不需要使用。

```python
import pandas as pd

# 创建一个Series
s = pd.Series([1, 2, np.nan, 4, 5])

# 计算累积乘积
cumprod_series = s.cumprod()

print(cumprod_series)
```

#### 分组和聚合

**groupby**

用于将Series中的数据分组，并允许你对这些分组进行操作，比如计算每个组的总和、平均值、最大值、最小值等。

`Series.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, observed=False, dropna=True)`

> `by`：确定分组依据，如果`by`是一个函数，它会在对象索引的每个值上调用。如果传递了字典或Series，将使用这些对象的值来确定组。如果传递了长度等于所选轴的列表或ndarray，则直接使用这些值来确定组。
>
> `axis`：用于分组的轴。对于Series，这个参数通常设置为0（默认值），因为Series是一维数据结构。
>
> `level`：如果索引是多级索引（MultiIndex），则此参数用于指定分组所依据的级别，`by`和`level`同时只能存在一个，且必须存在一个。
>
> `as_index`：是否将分组键作为结果的索引，默认值为`True`。仅与DataFrame输入相关。
>
> `sort`：是否对结果进行排序。默认值为`True`。
>
> `group_keys`：是否在结果中包含分组键。默认值为`True`。
>
> `observed`：是否仅包含实际观察到的分类值。默认值为`False`。
>
> `dropna`：是否从结果中排除包含NaN的组。默认值为`True`。

```python
import pandas as pd

# 创建一个Series对象
data = [10, 20, 10, 30, 20, 10]
series = pd.Series(data)

# 根据Series的值进行分组，并计算每组的计数
grouped = series.groupby(series).count()

print(grouped)
```

```python
import pandas as pd

# 创建一个Series对象
data = [10, 20, 30, 40, 50, 60]
index = ['a', 'b', 'a', 'b', 'c', 'c']
series = pd.Series(data, index=index)

# 根据Series的索引进行分组，并计算每组的和
grouped = series.groupby(series.index).sum()

print(grouped)
```

```python
import pandas as pd
import numpy as np

arrays = [np.array(['qux', 'qux', 'foo', 'foo', 'baz', 'baz', 'bar', 'bar']),
          np.array(['two', 'one', 'two', 'one', 'two', 'one', 'two', 'one'])]

s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8], index=arrays)
res = s.groupby(level=0).count()
print(res)
```

**agg**

`Series.agg()`方法用于对Series中的数据进行聚合操作

`Series.agg(func=None, axis=0, *args, **kwargs)`

> `func`: 聚合函数或函数列表/字典。可以是一个函数名称（字符串），也可以是实际的函数对象，或者是这些的列表或字典。如果是字典，则键将是输出列的名称，值应该是应用于Series的函数。
>
> `axis`: 整数或字符串，默认为0。由于Series是一维数据结构，这个参数实际上在Series的上下文中不起作用。在DataFrame的上下文中，`axis=0`表示按列进行聚合，`axis=1`表示按行进行聚合。
>
> `*args`: 位置参数，可以传递给`func`。
>
> `**kwargs`: 关键字参数，可以传递给`func`。

```python
import pandas as pd

s = pd.Series([1, 2, 3, 4, 5])

# 计算平均值
result = s.agg('mean')
print(result)

# 计算最大值和最小值
result = s.agg(['max', 'min'])
print(result)

# 使用字典为聚合函数命名
result = s.agg({'Maximum': 'max', 'Minimum': 'min'})
print(result)

# 使用自定义函数并传递额外的参数
def custom_agg(x, power):
    return (x ** power).sum()

result = s.agg(custom_agg, power=2)
print(result)
```

#### 数据可视化

**plot**

`Series.plot` 方法是用来绘制Series数据的可视化图表的，该方法提供了灵活的接口，允许用户通过不同的参数来定制图表的类型、样式、布局等，其用法与Matplotlib中的plot相同。

`Series.plot(*args, **kwargs)`

主要参数：

> `kind`: 图表类型，可以是以下之一：
>
> - `'line'`: 折线图（默认）
> - `'bar'`: 柱状图
> - `'barh'`: 水平柱状图
> - `'hist'`: 直方图
> - `'box'`: 箱线图
> - `'kde'`: 核密度估计图
> - `'area'`: 面积图
> - `'pie'`: 饼图
> - `'scatter'`: 散点图
> - `'hexbin'`: 六边形箱图
>
> `ax`: Matplotlib 轴对象，用于在指定的轴上绘制图表。如果不提供，则创建新的轴对象。
>
> `figsize`: 图表的尺寸，格式为 `(width, height)`，单位为英寸。
>
> `use_index`: 是否使用 Series 的索引作为 x 轴标签。默认为 `True`。
>
> `title`: 图表的标题。
>
> `grid`: 是否显示网格线。默认为 `False`。
>
> `legend`: 是否显示图例。默认为 `False`。
>
> `xticks`: x 轴的刻度位置。
>
> `yticks`: y 轴的刻度位置。
>
> `xlim`: x 轴的范围，格式为 `(min, max)`。
>
> `ylim`: y 轴的范围，格式为 `(min, max)`。
>
> `color`: 绘制颜色，可以是单个颜色或颜色列表。
>
> `label`: 图例标签。

```python
import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series([1, 3, 2, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
s.plot(kind='line', title='Line Plot', grid=True, figsize=(8, 4), style='r--', linewidth=2)
plt.show()
```

**hist**

用于绘制Series数据直方图的方法。这个方法提供了多种参数来定制直方图的外观和样式。

`Series.hist(by=None, ax=None, grid=True, xlabelsize=None, xrot=None, ylabelsize=None, yrot=None, figsize=None, bins=10, backend=None, legend=False, **kwargs)`

> `by`: 如果不是`None`，则将数据分组并分别绘制每个组的直方图。
>
> `ax`: matplotlib的Axes对象，如果指定了，则直方图将绘制在该Axes上。
>
> `grid`: 布尔值，默认为`True`，表示是否在直方图上显示网格线。
>
> `xlabelsize`: int或str，用于设置x轴标签的字体大小。
>
> `xrot`: int或float，用于设置x轴标签的旋转角度。
>
> `ylabelsize`: int或str，用于设置y轴标签的字体大小。
>
> `yrot`: int或float，用于设置y轴标签的旋转角度。
>
> `figsize`: 元组，用于设置直方图的大小，格式为 `(width, height)`。
>
> `bins`: int或序列，用于设置直方图的柱子数量或具体的边界。
>
> `backend`: 用于指定绘图后端，通常Pandas会使用matplotlib。
>
> `legend`: 布尔值，默认为`False`，表示是否在直方图上显示图例。
>
> `**kwargs`: 其他关键字参数，将被传递给matplotlib的`hist`函数。

```python
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 创建一个包含随机数据的Series
s = pd.Series(np.random.randn(1000))

# 绘制直方图
s.hist(bins=30, figsize=(8, 6), color='blue', edgecolor='black')

# 设置标题和轴标签
plt.title('Histogram of a Random Sample')
plt.xlabel('Value')
plt.ylabel('Frequency')

# 显示图表
plt.show()
```

#### 其他常用方法

**unique**

该函数用于返回Series中的唯一值。这个方法返回一个数组，其中包含了Series中所有唯一的值。数组中的值是按照它们在原始Series中首次出现的顺序排列的。

`Series.unique()`

```python
import pandas as pd

# 创建一个Series
s = pd.Series(['apple', 'banana', 'apple', 'orange', 'banana', 'banana'])

# 获取唯一值
unique_values = s.unique()

# 输出唯一值
print(unique_values)
```

**nunique**

该函数用于计算Series中唯一值的数量。这个方法返回一个整数，表示Series中唯一值的数量。

`Series.nunique(dropna=True)`



`dropna`: 布尔值，默认为`True`。如果为`True`，则在计算唯一值数量之前，会先从Series中排除NaN值。



```python
import pandas as pd

# 创建一个Series
s = pd.Series(['apple', 'banana', 'apple', 'orange', 'banana', 'banana'])

# 计算唯一值的数量（排除NaN）
unique_count = s.nunique(dropna=True)

# 输出唯一值的数量
print(unique_count)
```



##### 3.8.3 value_counts

该方法用于计算Series中每个值的出现次数。这个方法返回一个包含每个唯一值及其对应出现次数的Series。

python

```
Series.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)
```



- `normalize`: 布尔值或 `'all'`，默认为 `False`。如果为 `True`，返回每个值的相对频率；如果为 `'all'`，则返回所有值的相对频率之和为 1。
- `sort`: 布尔值，默认为 `True`。如果为 `True`，结果将按计数值降序排序。
- `ascending`: 布尔值，默认为 `False`。如果为 `True`，结果将按计数值升序排序。
- `bins`: 用于离散化连续数据，可以是整数或分位数数组。如果指定了 `bins`，则结果将是每个 `bin` 的计数。
- `dropna`: 布尔值，默认为 `True`。如果为 `True`，则排除 NaN 值。

python

```
import pandas as pd

# 创建一个Series
s = pd.Series(['apple', 'banana', 'apple', 'orange', 'banana', 'banana'])

# 计算每个值的出现次数
value_counts = s.value_counts()

# 输出每个值的出现次数
print(value_counts)
```



##### 3.8.4 describe

该方法用于生成描述性统计信息。这个方法返回一个包含计数、均值、标准差、最小值、25%25% 分位数、中位数、75%75% 分位数和最大值的 Series。

python

```
Series.describe(percentiles=None, include=None, exclude=None)
```



- `percentiles`: 数值列表或数值元组，默认为 `[.25, .5, .75]`，表示要包含在输出中的分位数。
- `include`: 字符串或类型列表，用于指定要包括在结果中的数据类型。默认为 `None`，即包括所有数字类型。
- `exclude`: 字符串或类型列表，用于指定要从结果中排除的数据类型。默认为 `None`。

python

```
import pandas as pd

# 创建一个Series
s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 生成描述性统计信息
description = s.describe()

# 输出描述性统计信息
print(description)
```



##### 3.8.5 copy

该函数用于创建Series对象的一个副本。

python

```
Series.copy(deep=True)
```



- `deep`: 布尔值，默认为`True`。当`deep=True`时，会进行深拷贝，即复制数据和索引的副本，而不是仅仅复制引用。当`deep=False`时，会进行浅拷贝，即只复制数据或索引的引用。

python

```
import pandas as pd

# 创建一个Series
original_series = pd.Series([1, 2, 3, 4, 5])

# 创建一个深拷贝
deep_copied_series = original_series.copy()

# 创建一个浅拷贝
shallow_copied_series = original_series.copy(deep=False)

# 修改深拷贝中的数据
deep_copied_series[0] = 999

# 输出原始Series和深拷贝后的Series
print("Original Series:\n", original_series)
print("Deep Copied Series:\n", deep_copied_series)

# 修改浅拷贝中的数据
shallow_copied_series[1] = 888

# 输出原始Series和浅拷贝后的Series
print("Original Series after shallow_copied_series):\n", original_series)
print("Shallow Copied Series:\n", shallow_copied_series)
```



##### 3.8.6 reset_index

该函数用于重置Series的索引，将原来的索引转换为一个列，并将一个新的默认整数索引赋给Series。

python

```
Series.reset_index(level=None, *, drop=False, name=no_default, inplace=False, allow_duplicates=False)
```



- `level`: int 或 level 名，可选。如果 Series 是多级索引 (MultiIndex)，则只移除指定的级别。默认为 `None`，移除所有级别。
- `drop`: 布尔值，默认为`False`。如果为`True`，则不将旧索引添加为新列，直接丢弃。
- `name`: 字符串，可选。用于新列的名称，默认为 `no_default`。如果未指定，并且索引有名字，则使用索引的名字。
- `inplace`: 布尔值，默认为`False`。如果为`True`，则在原地修改 Series，不返回新的对象。
- `allow_duplicates`: 布尔值，默认为`False`。如果为`True`，则允许在重置索引后出现重复的索引值。默认情况下，如果出现重复的索引值，Pandas 会抛出错误，对 Series 无用。

python

```
import pandas as pd
import numpy as np

# 创建一个简单的Series对象
data = pd.Series(np.random.randint(1, 100, 5), index=['c', 'a', 'e', 'b', 'd'])

# 对Series进行排序
sorted_series = data.sort_values()

# 重置索引
reset_indexed_series = sorted_series.reset_index(drop=True)
print("排序后的Series: ")
print(sorted_series)
print("重置索引后的Series: ")
print(reset_indexed_series)
```



##### 3.8.7 info

用于显示Series的概要信息的方法。这个方法提供了关于Series的元数据，包括数据类型、非空值的数量、内存使用情况等。

python

```
Series.info(verbose=None, buf=None, max_cols=None, memory_usage=None, show_counts=True)
```



- `verbose`: 布尔值或`None`，默认为`None`。如果为`True`，则输出更详细的信息。
- `buf`: 一个文件-like对象，如果提供，则将输出写入这个对象而不是标准输出。
- `max_cols`: int，用于显示的最大列数。如果列数超过这个值，则显示。
- `memory_usage`: 布尔值或str，默认为`None`。如果为`True`，则显示内存使用情况。如果设置为`deep`，则会计算列的内存使用情况，这可能非常慢。
- `show_counts`: 布尔值，默认为`True`。如果为`True`，则显示非空值的数量。

python

```
import numpy as np
import pandas as pd

# 创建一个示例Series
s = pd.Series([1, 2, np.nan, 4, 5], name='example_series', index=['a', 'b', 'c', 'd', 'e'])

# 显示Series的概要信息
s.info()
```



##### 3.8.8 apply

对Series中的每个元素应用一个函数，并返回一个结果Series。

python

```
Series.apply(func, convert_dtype=True, args=(), **kwargs)
```



- `func`: 一个函数，它将被应用到Series的每一个元素上。这个函数可以是Python的内置函数，也可以是用户自定义的函数。
- `convert_dtype`: 布尔值，默认为`True`。如果为`True`，则在可能的情况下，Pandas会尝试将结果转换为适合的数据类型。
- `args`: 一个元组，包含传递给`func`的位置参数。
- `**kwargs`: 一个字典，包含传递给`func`的关键字参数。

python

```
import pandas as pd

# 创建一个series
series = pd.Series([1, 2, 3, 4, 5])

# 使用apply方法结合lambda函数，对series中的每个元素执行平方操作
res = series.apply(lambda x: x * 2)

# 打印结果，输出每个元素的平方值
print(res)
```



##### 3.8.9 map

对series中的每个元素应用一个映射，它允许你将一个函数应用到series的每个元素上，或者将一个字典或series映射到series的值上。

python

```
Series.map(arg, na_action=None)
```



- `arg`: 这可以是以下几种类型：
    - **函数**：将此函数应用于series的每个元素。
    - **字典**：将series中的值映射到字典的键上，返回对应的值。
    - **Series**：使用另一个series的索引来映射当前series的值。
- `na_action`: 默认为 `None`。如果设置为 `'ignore'`，并且 `arg` 是一个函数，那么将忽略 NaN 值，并保留它们不变。

python

```
import pandas as pd

# 创建一个series
s = pd.Series([1, 2, 3, 4, 5])

# 定义一个函数，用于将值翻倍
def double(x):
    return x * 2

# 使用map方法应用这个函数
s_doubled = s.map(double)
print(s_doubled)
```



python

```
import pandas as pd

# 创建一个映射字典
grade_mapping = {
    90: 'A',
    80: 'B',
    70: 'C',
    60: 'D',
    0: 'F'
}

# 创建一个成绩的Series
grades = pd.Series([80, 92, 77, 59, 100])

# 使用map方法应用这个字典
grades_mapped = grades.map(grade_mapping)
print(grades_mapped)
```



python

```
import pandas as pd

# 创建一个名为series1的Series对象
series1 = pd.Series([50, 60, 70, 80, 90], index=['a', 'b', 'c', 'd', 'e'])

# 创建一个名为grades的Series对象，代表成绩数据
grades = pd.Series([80, 92, 77, 59, 100], index=[0, 1, 2, 3, 4])

# 使用grades的map方法，将grades中的每个值作为键，去series1中查找对应的键值并返回
res = grades.map(series1)

# 打印输出新生成的Series对象res
print(res)
```







