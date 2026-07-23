# 四、python基础知识

## （一） 行与缩进

在Python编程语言中，行与缩进扮演着非常关键的角色。

### 1. 行

Python的每行代码通常代表一条语句的结束，且不需要任何的符号作为每行的结束符。如果一条语句太长可以使用反斜杠作为续航符来换行。

### 2. 缩进

在Python中，通过缩进来组织代码块，例如函数体、循环体、类等。缩进必须一直，通常使用空格来实现（推荐使用4个空格），也可以使用一个制表符。同一级别的代码块应该具有相同的缩进量，下一级别的代码块应比上级别的代码块应比上级别的代码块增加一个缩进层级。

==注意==：Python不依赖于花括号{}或其他符号来标识代码块的开始和结束，而是完全依赖于缩进来确定代码块的范围。因此，正确的缩进对于python程序的正确解析至关重要。

```python
print("123")
 print("123")
# 代码会报错（缩进错误）
```

```python
print("123")
print("123")
a = 1
b=2	# 可以，但不美观
if a < b:
    print("a<b")
print(123+123+123+123+123+123+123+123+123+123+123+\
     123+123+123+123+123+123+)	# '\'：换行符
```

## （二）注释、变量、标识符与关键字

```python
# print("123")
print("456")	# 这是一个单行注释，只会输出456
```

```python
# 这是一个多行注释的例子
print("Hello World1")
"""
print("Hello World2")
print("Hello World3")
print("Hello World4")
print("Hello World5")
"""
print("Hello World6")
```

### 1. 变量

变量是 python 中最重要，也是最难的知识点

程序运行过程中，用来存储数据的容器，且可以参与数据之间的运算

变量的定义格式：**变量名 = 数据**

变量的基本类型：*数字、字符串、列表、元组、集合、字典*

==注意==：Python是动态类型语言，变量无需预先声明类型，直接赋值调用即可。

（1）python中的变量是一种代数思想，写代码的时候变量非常简洁，称之为标识符，变量表示的是一种数据

```python
x=10	# x是一个标识符（变量的名字）它的数据是数字10
print(x)

y="hello"	# y是一个标识符（变量的名字）它的数据是字符串"hello"
print(y)

print("hello,python")
```

（2）变量的取值和存值

```python
a = 10  # 存值：给一个变量a赋值（存值）如果这个变量不存在，就会在当前作用域创建一个变量，然后给这个变量第一次赋值（初始化）
print(a)    # 取值：取出变量最近一次存的值
a = 20  # 存值：给一个变量a赋值（存值）这个变量已经存在了，就会重新给这个变量赋值（更新）
print(a)    # 取值：取出变量最近一次存的值

# 总结：变量存值，有就更新，没有就创建；变量取值，没有就报错，有就取出变量最近一次存的值
# print(b) -- 程序崩溃（报错）

print(123)  # 前面报错，这里正确的语句也不会运行，因为python语言是一个脚本语言
```

（3）变量是一种不加引号的标识符、单词

变量名设计公约，见名知意

变量的名字规则：字母、数字、下划线的组合，数字不能打头

大小驼峰：agent_name、agentName、AgentName

```python
x = 10
_ = 127
print(x)
print(_)
x1 = 10
x2 = 20
train_test_split = 0.8

# 1y = 10 -- 报错
# get name = "zhang"	# 报错

# 面试可以说是正确的，根据实际情况来说
华清远见 = 2024 # 符合Unicode编码的都可以作为变量名
print(华清远见)
```

（4）变量保存的数据，有哪些类型的数据？

数字、布尔数据、字符串、None、列表、元组、字典、集合、函数、类、对象

```python
x = 10
y = "张三"
z = True
```

（5）变量的三个基本属性：

- **id号**：反映的是变量值的内存地址使用id()函数查看
- **类型**：每一个变量都有自己的类型。
- **值**：存储的数据。

使用 ==is 或 is not== 可查看两个变量的id号是否相同。

```python
a = 1
print(id(a))	# 140737162942112

b = 2
print(a is b)
print(a is not b)

c = 1
print(a is c)
```

变量的赋值与地址变化：

```python
a = 10
b = a
```

答：`a`在创建时，被绑定到整数对象`10`（对于小整数，指向全局缓存池）。
		创建`b`时，Python将`b`绑定到`a`所绑定的**同一个对象**上。
		此时`a`和`b`是两个独立的变量标签，但它们**指向同一块内存地址**。

### 2.  注释

是程序员为了解释代码的工作原理、逻辑或意图而添加的内容，并且解释器不会翻译这些内容。这些注释对于阅读代码的人来说是重要的参考信息，尤其是当代码变得复杂或涉及多个文件和模块时，它有助于提高代码的可读性和可维护性。

程序在运行的时候，这个代码不会对程序产生任何影响

注释常常是对我们的代码进行一个解释作用

注释的作用：

- *提高代码的可读性和可维护性。*
- *提高团队的合作效率。*
- *可以用作调试代码。*

在Python里，注释分为单行注释与多行注释。

- **单行注释**以**井号（#）**开头，井号（#）所在位置的右边都会被当作注释。

    编辑器内部可以直接使用快捷键 Ctrl + / 把选择的内容进行注释
- ==注意==：#号和注释的内容之间一般用一个空格分开。
- **多行注释**使用**三引号**，三对单引号或者三对双引号，引号之间的内容就是注释的内容，但是**单引号与双引号**之间**不能混合使用**，否则会报错。
- **单行注释**多用于对一行或一小部分代码进行解释。
    **多行注释**多用于函数或类的介绍。

```python
# 注释：就是程序在运行的时候，这个代码不会对程序产生任何影响
# 注释常常是对我们的代码进行一个解释的作用

# 单行注释：“#”后面的内容就是注释
# 多行注释：三个单引号 -- '''注释内容'''、三个双引号 -- """注释内容"""

# 编辑器内部可以直接使用快捷键 Ctrl+/ 把选择的内容进行单行注释
```

```python
# print("123")
print("456")	# 这是一个单行注释，只会输出456
```

```python
# 这是一个多行注释的例子
print("Hello World1")
"""
print("Hello World2")
print("Hello World3")
print("Hello World4")
print("Hello World5")
"""
print("Hello World6")
```

### 3. 标识符

程序员用来给代码中的不同对象指定的不同名字，比如变量的名字。

标识符的命名规范：

- 只能包含<u>字母、数字、下划线</u>，但**不能以数字开头**。
- 不能包含空格，但是可以使用下划线来分割名称。
- 不能使用Python的关键字作为标识符的名称。

==注意==：Python中的标识符的命名是区分大小写的。

**驼峰命名法**：是一种编程和书写标识符时采用的命名约定，分为小驼峰命名法和大驼峰命名法。

- **小驼峰命名法**：第一个单词的首字母以小写字母开始，之后的单词的首字母以大写字母开始，例如myName。
- **大驼峰命名法**：所有单词的首字母都是大写，通常用于类名，如MyName。

### 4. 关键字

也是一种标识符，只不过是Python解释器提前占用了的标识符，每一个关键字都有自己的特殊功能，比如常用的if、for、while、import、def等等。

可以通过调用Python的**keyWord**库来查看Python中的关键字都有哪些。

```python
import keyword

print(keyword.kwlist)
```

## （三）数字

### 1. 数字的类型

```python
x = 10
print(x)	# 整数

x2 = 3.14
print(x2)	# 小数

x3 = (2+3j)
print(x3)	# 复数

x4 = True	# 1
x5 = False	# 0
print(x4,x5)	# 布尔
```

### 2. 进制

是一种数的表示方法，在计算机中常用的进制为二进制、八进制、十进制以及十六进制，各进制之间都是可以通过计算进行相互转换的。

计算机的世界是二进制，也就是0和1，逢二进一。
我们日常生活所用的进制是十进制，表示逢十进一。

> 二进制：逢二进一，以0b或0B开头，只有0和1两个数，计算机的世界就是由0和1组成的，通常8位为一组，比如0b11011001。
>
> 八进制：逢八进一，以0o或0O开头，有0-7共8个数。
>
> 十进制：逢十进一，有0-9共10个数。
>
> 十六进制：逢十六进一，以0x或0X开头，包含0-9共10个数字以及A、B、C、D、E、F六个字母（字母大小写均可），通常为2位一组，比如0x1a
>
> 开头全是数字0

二进制与十进制的相互转换：

| 进制             | 方法                                                         |
| ---------------- | ------------------------------------------------------------ |
| 二进制转十进制   | 每一个数位上的数字乘以其对应的位置权重（即该位置离原点的距离，单位是基数的幂次），然后将所有数位的结果相加即可得到该数字在十进制下的值。<br/>比如二进制数字1011101转为十进制可表示为：<br/>1×2<sup>0</sup>+0×2<sup>1</sup>+1×2<sup>2</sup>+1×2<sup>3</sup>+1×2<sup>4</sup>+0×2<sup>5</sup>+1×2<sup>6</sup> = 1+0+4+8+16+0+64 = 93 |
| 十进制转二进制   | 使用除2取余法（整数部分）和乘2取整法（小数部分）进行转换<br />**除二取余法**：将十进制的整数除以二，不断收集余数，直到商为0为止，然后将余数按照反方向排序就是整数的二进制数值。<br />**乘2取整法**：将十进制的小数乘以二，不断收集乘以二之后的整数部分，然后用小数部分接着乘以2，直到小数部分为0为止，得到的整数部分就是小数的二进制数值。 |
| 二进制转十六进制 | 将二进制数从右向左按照每四位一组进行分组（不足四位的高位补0），每一组的四个二进制数都对应不同的十进制数值，然后将其相加得到十六进制数。<br/>比如二进制数0b1111，第一个1就对应十进制的8，第二个1对应十进制的4，第三个1对应十进制的2，第四个1对应十进制的1，可以按照从左到右的顺序简记为8421，也就是每个位数对应的十进制数值。如果该位数上的值为0，就代表0。 |
| 十六进制转二进制 | 将每个十六进制数先转化为十进制的数值，然后根据8421的规则来转化为二进制<br />比如0x1a，1就是十进制的1，对应8421规则里的0001，a对应十进制的10，对应8421规则里的1010，因此0x1a转化为二进制就是11010（高位的0可以省略不写）。 |

```python
# 数字更长用的划分：int8 int16 int32 int64 uint8 float32 float64
# 未来会学习大模型的量化压缩

# 了解的知识点
n1 = 0xA0F	# 十六进制
print(n1)	# 2575

n2=0o37	# 八进制
print(n2)	# 31

n3=9	# 10进制
print(n3)	# 9

n5=0b10	# 2进制
print(n5)	# 2

print(int(20.5))	# 20
print(float(20))	# 20.0
print(bin(3))	# 0b11
print(oct(20))	# 0o24
print(hex(29))	# 0x1d
print(complex(29))	# (29+0j)
print(complex(10,3))	# (10+3j)
```

### 3. 源码、反码、补码

数据在存储的时候，涉及到原码、反码、补码转换的问题。

> 原码：给人看的
> 反码：用来作原码和补码之间的转换的
> 补码：给计算机看的，数据存储在计算机中都是以数据的补码进行存储的

原码、反码、补码都是针对二进制数，所以先将数据转化为二进制，<u>二进制的第一位叫做符号位</u>，表示数据的正负，0表示正数，1表示负数。

比如1，其二进制为0000 0001，-1的二进制为：1000 0001

> 对于正数：
> 	原码 = 反码 = 补码 = 二进制数
>
> 对于负数：
> 	原码 = 二进制数
> 	反码 = 原码符号位不变，其他位按位取反（0变1，1变0)
> 	补码 = 反码 + 1

```python
# 二进制	3
print(0b11)
print(0B11)

# 八进制	9
print(0o11)
print(0O11)

# 十六进制	17
print(0x11)
print(0X11)
```

```python
# 二进制转十进制	45
print(0b101101)
# 十进制转二进制	0b1010
print(bin(10))
# 二进制转十六进制	0xb5
print(hex(0b10110101))
# 十六进制转二进制	0b1010
print(bin(OxA))
```

### 4. 运算符

在Python中，常用的运算符分为以下几类：

**算术运算符**

- +：加法运算符，返回两个对象的和
- -：减法运算符，返回两个对象的差
- *：乘法运算符，返回两个对象的积
- /：除法运算符，返回两个对象的商
- //：整除运算符，返回两个对象的商的整数部分
- %：取余运算符，返回两个对象的商的余数部分
- **：幂运算符：返回两个对象的幂运算的结果

```python
# 算术运算
x = 10
y = 20
z = x + y
z = x - y
z = x * y
z = x / y
z = x ** y
z = x % y
z = x // y
print(z)
```

**比较运算符**

- ==：等于，比较两个对象是否相等，返回布尔值
- !=：不等于，比较两个对象是否不相等，返回布尔值
- \>：大于，比较两个对象的大小关系，返回布尔值
- <：小于，比较两个对象的大小关系，返回布尔值
- \>=：大于等于，比较两个对象的大小关系，返回布尔值
- <=：小于等于，比较两个对象的大小关系，返回布尔值

```python
# 比较运算
z = x > y
z = x < y
z = x >= y
z = x <= y
z = x is y
z = x is not y
```

**逻辑运算符**

- and：布尔与，and两边都为True时，才会返回True，只要有一个False就会返回False
- or：布尔或，or两边都为False时，才会返回False，只要有一个True就会返回True
- not：布尔非，将True改为False，将False改为True
- **小口诀**：对于and，全True为True，有False就False；
                   对于or，全False为False，有True就True。

```python
# 逻辑运算
z = 10 and 0
print(z)	# 0
x = 95
y = 99
z = x > 90 and y > 90	# true and true
print(z)	# True
z = 100 or 200	# 左边为真，不看右边，直接返回左边
print(z)	# 100
'''
总结：x = A and B
A运行的结果转化为布尔值 -->
如果为真，B运行，x的结果就是B运行的结果
如果为假，B不运行，x的结果就是A运行的结果
'''
```

**赋值运算符**

- =：赋值运算符，把=右边的对象赋值给 = 左边的对象
- +=：加法赋值运算符
- -=：减法赋值运算符
- *=：乘法赋值运算符
- /=：除法赋值运算符
- //=：整除赋值运算符
- %=：取余赋值运算符
- **=：平方赋值运算符

```python
# 赋值运算
x = 10
x += 10	# x = x + 10
# += -= *= /= %= //= **=
```

**位运算符**

操作对象都是**二进制数**，对**补码**进行运算

- &：按位与，对两个数据的补码进行位与位之间的与运算，全1为1，有0则0

- |：按位或，对两个数据的补码进行位与位之间的或运算，全0为0，有1则1

- ^：按位异或，对两个数据的补码进行位与位之间的异或运算，相同为0，不同为1

- ~：按位取反，对一个数据的补码进行按位取反，0变1，1变0

- <<：按位左移，将一个数据的补码全部左移若干位，由符号右边的数决定左移的位数。

- \>>：按位右移，将一个数据的补码全部右移若干位，由符号右边的数决定右移的位数。

```python
# 位运算符
print(3 & -3)	# 1
print(3 | -3)	# -1
print(~(-3))	# 2
print(3 ^ (-3))	# -2
print(3 << 1)	# 6
print(3 >> 1)	# 1
print(-3 >> 1)	# -2
```

### 5. 运算符的优先级

运算符的优先级（从上向下排列，上面的优先级最高）

> 圆括号()：圆括号内的表达式拥有最高优先级
>
> **：乘方运算
>
> *、/、%、//：算术运算符，先乘除
>
> +、-：算数运算符，后加减
>
> <<、>>：位运算符的左移与右移
>
> &：位运算符的按位与
>
> ^：位运算符的按位异或
>
> |：位运算符的按位或
>
> \>、<、>=、<=、==、！=：比较运算符
>
> not、and、or：逻辑运算符
>
> =、+=等赋值运算符优先级最低

当多个相同优先级的运算符连续出现时，它们遵循从左至右原则，也就是说，如果没有优先级更高的运算符插入，将按照代码自左向右的顺序依次计算。

如果需要改变运算的自然优先级顺序，可以使用括号来强制优先计算某些部分，这个方法也是很常用的一个方法。

### 6. 数学函数

部分函数是python环境自带的 部分是math模块带的部分是公共的

先引入math模块:    **import math**

| 函数            | 返回值 ( 描述 )                                              |
| --------------- | ------------------------------------------------------------ |
| abs(x)          | 返回数字的绝对值，如abs(-10) 返回 10                         |
| math.ceil(x)    | 返回数字的上入整数，如math.ceil(4.1) 返回 5                  |
| cmp(x, y)       | 如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 **Python 3 已废弃，使用 (x>y)-(x<y) 替换**。 |
| math.exp(x)     | 返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045         |
| math.fabs(x)    | 以浮点数形式返回数字的绝对值，如math.fabs(-10) 返回10.0      |
| math.floor(x)   | 返回数字的下舍整数，如math.floor(4.9)返回 4                  |
| math.log(x)     | **默认以 e\*e\*（自然常数，约等于 2.71828）为底**，计算的是**自然对数**（即 ln⁡(x)ln(*x*)）<br />如math.log(math.e)返回1.0,math.log(100,10)返回2.0 |
| math.log10(x)   | 返回以10为基数的x的对数，如math.log10(100)返回 2.0           |
| max(x1, x2,...) | 返回给定参数的最大值，参数可以为序列。                       |
| min(x1, x2,...) | 返回给定参数的最小值，参数可以为序列。                       |
| math.modf(x)    | 返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。 |
| math.pow(x, y)  | x**y 运算后的值。                                            |
| round(x ,n)     | 返回浮点数 x 的四舍六入值，如给出 n 值，则代表舍入到小数点后的位数。**其实准确的说是保留值将保留到离上一位更近的一端。**  <br />1.保留整数只有一个小数时:4舍6入5看齐,奇进偶不进  <br />2.保留整数或小数超过一个小数时:看保留位的下下位是否存在 |
| math.sqrt(x)    | 返回数字x的平方根。                                          |

```python
import math
x = abs(-10)
x = math.ceil(3.14)
x = math.floor(3.94)
x = round(3.5)	# 四舍六入 5看齐 奇进偶不进
x = max(100,200,3)
x = min(100,3,5)
x = math.log(100)
x = math.e
x = math.pi	# 约等于Π
print(x)
```

### 7. 随机数

先引入random库基础库:    `import random`

| 函数                                | 描述                                                         |
| ----------------------------------- | ------------------------------------------------------------ |
| random.choice(seq)                  | 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。 |
| random.randrange (start, stop,step) | 从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1 |
| random.random()                     | 随机生成下一个实数，它在[0,1)范围内。                        |
| random.shuffle(list)                | 将序列的所有元素随机排序,修改原list                          |
| uniform(x, y)                       | 随机生成实数，它在[x,y]范围内.                               |

### 8. 三角函数

先引入math库基础库:    `import math`

| 函数             | 描述                                              |
| ---------------- | ------------------------------------------------- |
| math.acos(x)     | 返回x的反余弦弧度值。                             |
| math.asin(x)     | 返回x的反正弦弧度值。                             |
| math.atan(x)     | 返回x的反正切弧度值。                             |
| math.atan2(y, x) | 返回给定的 X 及 Y 坐标值的反正切值。              |
| math.cos(x)      | 返回x的弧度的余弦值。                             |
| math.sin(x)      | 返回的x弧度的正弦值。                             |
| math.tan(x)      | 返回x弧度的正切值。                               |
| math.degrees(x)  | 将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0 |
| math.radians(x)  | 将角度转换为弧度                                  |

```python
# 三角函数
import math
x = math.sin(3.14159265)
print(x)
deg = math.pi/180	# 角度转弧度：1度等于多少弧度
x = math.cos(30*deg)
x = math.sin(0*deg)
x = math.tan(90*deg)
x = math.degrees(math.pi/2)	# degrees--弧度转角度
x = math.radians(180)	# radians--角度转弧度
x = math.asin(0.5)
print(x)
```

### 9. 数学常量

先引入math库基础库:    **import math**

| 常量    | 描述                                  |
| ------- | ------------------------------------- |
| math.pi | 数学常量 pi（圆周率，一般以π来表示）  |
| math.e  | 数学常量 e，e即自然常数（自然常数）。 |

==思考题==：如果已知一个三角形的三个顶点（2，3）（2，8）（8，5），求每一个角是几度？

```python
"""
a向量 = (x2-x1,y2-y1)
cos = (a向量*b向量)/(a向量的模*b向量的模)
边长：d = sqrt((x2-x1)**2+(y2-t1)**2)
余弦值：cosa = (b^2+c^2-a^2)/2bc
      cosb = (a^2+c^2-b^2)/2ac
      cosc = (a^2+b^2-c^2)/2ab
先将坐标明确定义出来，
"""
import math # 导入math库

# 定义三个顶点坐标
x1,y1 = 2,3
x2,y2 = 2,8
x3,y3 = 8,5

# 计算边长  math.sqrt(x)：返回数字x的平方根。
a = math.sqrt((x2-x1)**2+(y2-y1)**2)
b = math.sqrt((x3-x2)**2+(y3-y2)**2)
c = math.sqrt((x1-x3)**2+(y1-y3)**2)

# 计算余弦值
cos_a = (b**2+c**2-a**2)/(2*b*c)
cos_b = (a**2+c**2-b**2)/(2*a*c)
cos_c = (a**2+b**2-c**2)/(2*a*b)
print(cos_a,cos_b,cos_c)

# 计算角度  math.degrees(x)：将弧度转换为角度
j_a = math.degrees(math.acos(cos_a))
j_b = math.degrees(math.acos(cos_b))
j_c = math.degrees(math.acos(cos_c))

# 输出结果
print(f'三角形的角是：{j_a:.2f}\t{j_b:.2f}\t{j_c:.2f}')
print(f"内角和为：{j_a+j_b+j_c:.2f}度")
```

```python
import math # 导入math库

# 定义三个顶点坐标
x1,y1 = 2,3
x2,y2 = 2,8
x3,y3 = 8,5

# a向量(a1,a2)
a1 = x2-x1
a2 = y2-y1
# b向量(b1,b2)
b1 = x3-x1
b2 = y3-y1
# cos(a,b)=
cos_theta = (a1*b1+a2*b2)/((a1**2+a2**2)**0.5 * (b1**2+b2**2)**0.5) # 夹角公式，求夹角余弦（弧度）
cos_theta = math.acos(cos_theta)    # 反余弦
theta1 = math.degrees(cos_theta) # 弧度转角度
print(theta1)

# c向量(a1,a2)
c1 = x3-x2
c2 = y3-y2
# d向量(d1,d2)
d1 = x1-x2
d2 = y1-y2
# cos(c,d)=
cos_theta = (c1*d1+c2*d2)/((c1**2+c2**2)**0.5 * (d1**2+d2**2)**0.5) # 夹角公式，求夹角余弦（弧度）
cos_theta = math.acos(cos_theta)    # 反余弦
theta2 = math.degrees(cos_theta) # 弧度转角度
print(theta2)

# e向量(b1,b2)
e1 = x1-x3
e2 = y1-y3
# f向量(f1,f2)
f1 = x2-x3
f2 = y2-y3
# cos(e,f)=
cos_theta = (e1*f1+e2*f2)/((e1**2+e2**2)**0.5 * (f1**2+f2**2)**0.5) # 夹角公式，求夹角余弦（弧度）
cos_theta = math.acos(cos_theta)    # 反余弦
theta3 = math.degrees(cos_theta) # 弧度转角度
print(theta3)

# theta3 = 180 - (theta1 + theta2)

print(theta1+theta2+theta3)	# 180
```



## （四）字符串

### 1. 字符串表达式

引号引起来的单引号、双引号、三引号（三个三引号或双引号）；

```python
x = '华清远见'
print(x)

x = "华清"
print(x)

x = """远见"""
print(x)

x = """字符串
	华清远见
	"""
print(x)
```

### 2.  类型检测

字符串用type函数检测的结果为str

```python
x = "hello"
res = type(x)
print(res)
print(type(100))
```

### 3. 转义字符

使用反斜杠\对字符进行转义，如`\r` 回车    `\n` 换行    `\t` 缩进     `\\ ` 表示 \

字符串前加`r`表示原始字符串：所见即所得，不转义；

```
x = "hello\nhqyj\thao"
print(x)
x = "c:\\hqyj\\name"
x = r"c:\hqyj\name"
print(x)
```

### 4. 运算

- 字符串连接：+

- 相邻的两个或多个 *字符串字面值* （引号标注的字符）会自动合并

- 字符串多次重复

```python
x = "hello"
y = x + "hqyj"
print(y)	# hellohqyj
z = x * 3
print(z)	# hellohellohello
```

### 5. f-string：格式化字符串

f-string 是 python3.6 之后版本添加的，称之为字面量格式化字符串，是新的格式化字符串的语法(旧的字符串格式化自行了解)。

之前我们习惯用百分号 (%)

**f-string** 格式化字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去

用了这种方式明显更简单了，不用再去判断使用 %s，还是 %d。

```python
r = 120
g = 130
b = 255
# color = "rgb(120,130,255)"
color = "rgb("+str(r)+","+str(g)+","+str(b)+")"
color = f"rgb({r},{g},{b})"
print(color)

lr = 0.5
print(f"学习率是：{lr}")

# 补充
print(10)
a = 20
print(a)

lr = 0.5
print(f"学习率是：{lr}")

lr = 0.5
res = f"学习率是：{lr}"
print(res)

x = 3.14159
print(f"{x:.2f}")	# x插入到字符串的时候，保留2位小数
```

### 6. 字符串可以索引

可以把字符串看成数组，通过下标访问字符，支持负数

支持通过下标截取子字符串,第一个参数省略表示0，第二个参数省略表示到最后

```python
x = "hello"
res = x[1]
res = x[0:3]
print(res)
```

### 7. 常用的API

Python 的字符串常用内建函数如下：

| 序号   | 方法及描述                                                   |
| ------ | ------------------------------------------------------------ |
| ==1==  | `capitalize()`将字符串的第一个字符转换为大写                 |
| ==2==  | `center(width, fillchar)`返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。 |
| ==3==  | `count(str, beg= 0,end=len(string))`返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数 |
| ==4==  | `endswith(suffix, beg=0, end=len(string))`检查字符串是否以 suffix 结束，如果 beg 或者 end 指定则检查指定的范围内是否以 suffix 结束，如果是，返回 True,否则返回 False。 |
| 5      | `expandtabs(tabsize=8)`把字符串 string 中的 \t 符号转为空格，tab 符号默认的空格数是 8 。 |
| ==6==  | `find(str, beg=0, end=len(string))`检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1 |
| ==7==  | `index(str, beg=0, end=len(string))`跟find()方法一样，只不过如果str不在字符串中会报一个异常。 |
| 8      | **isalnum**()非空字符串 中没有符号 就返回True                |
| 9      | **isalpha**()非空字符串 中没有符号和数字 就返回True          |
| 10     | **isdigit**()如果字符串只包含数字则返回 True 否则返回 False.. |
| 11     | **islower**() 用于检测字符串中的所有字符是否都是小写字母,字符都是小写，则返回 True，否则返回 False |
| 12     | **isnumeric**()如果字符串中只包含数字字符，则返回 True，否则返回 False |
| 13     | **isspace**()如果字符串中只包含空白，则返回 True，否则返回 False. |
| 14     | **istitle**()如果字符串是标题化的(见 title())则返回 True，否则返回 False |
| 15     | **isupper**()用于检测字符串中的所有字符是否都是大写字母,并且都是大写，则返回 True，否则返回 False |
| ==16== | `join(seq)`以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串 |
| ==17== | `len(string)`返回字符串长度                                  |
| 18     | **ljust**(width, fillchar\])返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。 |
| ==19== | `lower()`转换字符串中所有大写字符为小写.                     |
| ==20== | **lstrip**()截掉字符串左边的空格,\t,\r,\n或指定字符。        |
| 21     | **maketrans**()创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。 |
| 22     | **max**(str)返回字符串 str 中最大的字母。                    |
| 23     | **min**(str)返回字符串 str 中最小的字母。                    |
| ==24== | `replace(old, new , max)`将字符串中的 old 替换成 new,如果 max 指定，则替换不超过 max 次。 |
| 25     | **rfind**(str, beg=0,end=len(string))类似于 find()函数，不过是从右边开始查找. |
| 26     | **rindex**( str, beg=0, end=len(string))类似于 index()，不过是从右边开始. |
| 27     | **rjust**(width, fillchar)返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串 |
| ==38== | **rstrip**()删除字符串末尾的空格\t,\r,\n或指定字符。         |
| ==29== | `split(sep="", maxsplit=string.count(str))`以 sep为分隔符截取字符串，如果 maxsplit有指定值，则仅截取 maxsplit+1 个子字符串 |
| 30     | **splitlines**(keepends)按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。 |
| 31     | **startswith**(substr, beg=0,end=len(string))检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。 |
| ==32== | `strip(chars)`在字符串上执行 lstrip()和 rstrip()             |
| ==33== | `swapcase()`将字符串中大写转换为小写，小写转换为大写         |
| ==34== | `title()`返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写 |
| ==35== | `upper()`转换字符串中的小写字母为大写                        |
| 36     | **zfill** (width) 在字符串左侧填充指定数量的零，确保整个字符串达到指定长度 |

```python
# 分割
x = "http://www.hhh.com/home?name=karen&page=20&cout=2"
res = x.split("?")	# 分割
print(res)
x = 'name=karen&page=20&cout=2'
res = x.split("&")	# 分割

x = 'name=karen'
res = x.split("=")
print(res)

# 大小写转化
x = " hello hQyj "
res = x.upper()
res = x.lower()
res = x.capitalize()
res = x.title()
print(res)

# 去掉空格
x = "hello hQyj"
res = x.strip()
res = x.lstrip()
res = x.rstrip()
print(res)

# 查找
x = "华清远见是一家培训机构,华清远见"
res = x.index("华清远见",1)	# 没有报错
print(res)
x = "华清远见是一家培训机构,华清远见"
res = x.find("华清远见",1)	# 没有报错
print(res)

# 连接
x = "-"
# res = x.join("华清远见")
res = x.join(["nihao","hello","华清"])
print(res)

# 替换
x = "abc"
res = x.replace("ab","hello")
print(res)
```

## （五）输入和输出

### 1. 输出

在Python中，使用内置的print()函数进行输出，并且有几种不同的输出方式如下所示：

- 基本输出：直接打印数据或变量
- 格式化输出：使用百分号（%)操作符(现在不推荐使用，但是旧版本的代码中很常见)
- **formatl方法**：使用花括号作为占位符来指定要格式化的数据类型和格式，然后通过将数据插入到占位符中来生成最后的输出结果。
- **f-string**：在字符串前加一个f或F，然后在输出的内容中加上花括号{}，花括号{}里面是要输出的表达式，是一种新的字符串格式方法，在python3.6版本之后引入的输出方法。
- “=={:\[填充]\[对齐]\[符号]\[宽度]\[,]\[.精度]\[类型]}==”

```python
# 直接输出（也是用于开发阶段）
print("hello")
print("hello", 100, True)

x = 100
y = "hello"
z = True
print(x, y, z, sep="-")

print(100, end="\n")    # 默认换行
print(200, end="")
print(99)

print("hello", end = "",flush = True)   # flush：渲染
print("python", end = "",flush = True)
```

```python
# 格式化输出
name = 'zhangsan'
age = 18

# 直接输出的方法
print("My name is",name,"and i am",age,"years old.")

# 格式化输出的方法
print("My name is %s and i am %d years old." %(name, age))

weight = 70.123456789
print("My name is %s and my weight is %f" %(name, age))

# m.n
# m是用来控制输出数据的所占长度
# n是用来控制输出数据的精度问题
print("My name is %s and my weight is %5f" %(name, weight))
print("My name is %s and my weight is %10f" %(name, weight))
print("My name is %s and my weight is %.2f" %(name, weight))
print("My name is %s and my weight is %.5f" %(name, weight))
```

```python
# format方法，使用{}来占位
name = 'zhangsan'
age = 18
print("My name is {} and i am {} years old" .format(name, age))
print("My name is {} and i am {} years old" .format(age, name))

weight = 70.123456789012324567890
print("My name is {} and my weight is {:.2f}" .format(name, weight))
```

```python
# f-string，使用{}占位，并直接插入表达式
name = 'zhangsan'
age = 18
print(f"My name is {name} and i am {age + 1} years old")

weight = 70.12345678
print(f"My name is {name} and my weight is {weight:.2f}")
```

### 2. 输入

在Python中，使用内置的input()函数来获取用户输入的数据，其用法为：

> 变量 = input(“要输入的提示词，可以没有”)

需要注意的是，使用 input() 函数获取到的数据都会被转化为字符串存储在变量中。

```python
# 输入（也是用于开发阶段）
res = input()   # 会让程序暂停在这里，等待程序员在控制台输入
print(res,"99999874562")
print(666)
print(res,type(res))
if int(res%2) == 0:
    print("偶数")
else:
    print("奇数")
```

## （六）列表

Python 支持多种复合数据类型，可将不同值组合在一起。最常用的**列表** ，是用方括号标注，逗号分隔的一组值。列表可以包含不同类型的元素，但一般情况下，各个元素的类型相同

```python
# 总结：python中用的最多的数据类型是 -- 数字、字符串、列表、函数、对象
x = [10,203,"hello",100.1,True]    # 列表是一个装数据的容器，任何数据都可以放进去
print(x)
```

### 1. 索引

与字符串的索引一样，列表索引从 0 开始，第二个索引是 1，依此类推。

索引也可以从尾部开始，最后一个元素的索引为 -1，往前一位为 -2，以此类推。

使用下标索引来访问列表中的值，同样你也可以使用方括号 [] 的形式截取字符

**注意:==切片是浅拷贝操作==**

```python
# 取出数据（重难点）

# 1. 每个元素有了两个索引（正数和负数）
res = x[2]
print(res)
print(x[3])
print(x[-3])
print(x[2])
# 如果列表的索引不存在，去取数据，就会报错
# print(x[100])   # 报错
# print(x[-100])  # 报错

# 2. 切片
res = x[1:5]    # 切片的结果是一个列表，左闭右开
res = x[1:10]   # 切片可以越界
res = x[2:]     # 省略右边就默认取到结束
res = x[:4]     # 省略左边就默认从0开始
res = x[:]      # 默认取从开始到结束
x = [10,20,30,40,50,60]
res = x[2:5:2]
res = x[:5:2]
res = x[2::2]
res = x[1:2:]
res = x[-4:4:1]     # 如果左和右符号不一样，先换算成一样的符号
res = x[-4:4:-1]    # 空列表
# 总结 步长为正数就是从start开始往右取 步长为负数就是从start开始往左取
print(res)
```

```python
# 如果下面代码没问题，能取到数据，那么y列表应该是什么样的
# res = y[-8:10:2] -- 小标10必须在下标-8的右边

x = [1,2,3,4,5,6]
print(x[::1])   # [0:-1:1]
print(x[::-1])  # [-1:0:-1]
# 总结 步长不写默认1 步长写了，但是start和end不写，默认是看步长为负数还是正数然保证能取完
```

### 2. 更新列表

对列表的数据项进行修改或更新,也可以使用 **append()** 方法来添加列表项

```python
x = [10,20,30,40,50]
x[0] = 100
a = 2
x[a] = 200
print(x)

x = [10,20,30,40,50]
# x[5] = 50   # 赋值时，下标不允许越界
x.append(100)
print(x)
```

### 3. 删除列表元素

可以使用 del 语句来删除列表的的元素

```python
list = ['openAI', 'hqyj', 1997, 2004]
print (list)
del list[2]
print (list)
```

### 4. 列表操作符

| Python 表达式                | 结果                         | 描述                 |
| ---------------------------- | ---------------------------- | -------------------- |
| len([1, 2, 3])               | 3                            | 长度                 |
| [1, 2, 3] + [4, 5, 6]        | [1, 2, 3, 4, 5, 6]           | 组合                 |
| ['Hi!'] * 4                  | ['Hi!', 'Hi!', 'Hi!', 'Hi!'] | 重复                 |
| 3 in [1, 2, 3]               | True                         | 元素是否存在于列表中 |
| for x in [1, 2, 3]: print(x) | 1 2 3                        | 迭代                 |

```python
x = [10,20]
y = 100
res = y in x
print(res)

x = [10,20]
y = x*2     # 把列表的元素重复2遍
print(y)

x = [10,20]
a = [100,200]
# y = x+10    # 列表可以和列表相加，但是不能和数字相加
y = x+a # 把两个的元素装在一个新列表中
print(y)

x = [10,20,30,40,50]
y = len(x)
print(y)

```

### 5. 嵌套列表

```python
x = [[10,20,30],[40,50,60,[70,80,90]]]
print(x[0])
print(x[1][1])
print(x[1][3][1])

a = [10,20,30]
b = [100,200,300]
c = [a, b]
print(c[1][2])
```

### 6.列表常用API

操作列表的函数

| 序号 | 函数                        |
| ---- | --------------------------- |
| 1    | len(list)列表元素个数       |
| 2    | max(list)返回列表元素最大值 |
| 3    | min(list)返回列表元素最小值 |
| 4    | list(seq)将元组转换为列表   |

```python
x = [10,20,30]	# 语法糖
res = max(x)
res = min(x)
res = len(x)
print(res)

# x = list(可迭代对象) -- 提了一下，后面的课会讲
x = list((102,103,104,20))
x = list("hello")
print(x)
```

列表的方法

| 序号 | 方法                                                         |
| ---- | ------------------------------------------------------------ |
| 1    | list.append(obj)在列表末尾添加新的对象                       |
| 2    | list.count(obj)统计某个元素在列表中出现的次数                |
| 3    | list.extend(seq)在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表） |
| 4    | list.index(obj)从列表中找出某个值第一个匹配项的索引位置      |
| 5    | list.insert(index, obj)将对象插入列表                        |
| 6    | list.pop(index=-1)移除列表中的一个元素（默认最后一个元素），并且返回该元素的值 |
| 7    | list.remove(obj)移除列表中某个值的第一个匹配项               |
| 8    | list.reverse()反向列表中元素                                 |
| 9    | list.sort( key=None, reverse=False)对原列表进行排序: x.sort(key=lambda a:abs(a-3), reverse=False) |
| 10   | list.clear()清空列表                                         |
| 11   | list.copy()复制列表                                          |

```python
x = [10,20,30,40,50,60]
x.append(100)
print(x)

x = [10,20,30,40,50,60]
res = x.pop()   # 移除指定下标的元素，并返回该元素
print(res,x)

x = [10,20,30,40,50,60]
res = x.pop(1)
print(res,x)

x = [10,20,30,40,50,60]
x.remove(40)  # 移除指定元素，并返回None
print(x)

x = [10,20,30,40,50,60]
x.insert(3,100)     # 把100插入到缩影为3的位置 以前的3后面的元素都向后移动一位
print(x)

# del关键字
x = 100
del x # 删除变量
print(x)

x = [10,20,30,40,10]
res = x.count(10)
print(res)

x = [10,20,30]
y = [100,200]
x.extend(y) # 这个函数会操作x列表，把y列表的元素添加到x列表中
print(x)

x = [10,20,10,10]
res = x.index(10)
print(res)

x = [10,20,30,40]
y = x.reverse()
print(x)

x = [10,20,30,40]
x.clear()
print(x)

"""
引用数据的思想：
列表是一个引用数据：它会创建列表对象，占用内存空间
x = [10,20,30,40] -- 创建了一个列表对象，占用了一个内存空间
y = x -- 不会重新创建一个列表对象，也就是说不会新开辟内存空间
y[1] = 666
print(x) -- [10,666,30,40]
"""
x = [10,20,30,40]
y = x.copy()
y[1] = 666
print(x,y)

x = [10,20,30,40]
y = x
print(y)

x = [1,40,20,10,15,102,30,2]
x.sort(key=lambda x:abs(x-10))
print(x)
```

## （七）条件语句

### 1. 布尔值

```python
# 布尔值
x = 10 > 20
x = 100 == 200
x = 10 is 10
x = 10 is not 10
x = 10 != 10
print(x)

x = 10
x = 0   # False
x = "hello"
x = ""    # False
x = " "
x = [10,20]
x = [0]
x = []    # False
x = None  # False 表示没有值
y = bool(x)   # 任何数据都可以转化为布尔值
print(y)
# 空（None）和0-->False   其余值-->True
```

### 2. if条件语句

**if condition:**

  **# 当条件为真时执行这里的代码,否则不执行这里**

```python
"""
if 表达式:
    缩进逻辑运行代码
    缩进逻辑运行代码
"""
if 10 < 20:
    print("10小于20")
    c = 10 + 20
    print(c)

age = 16
if age > 18:
    print("成年了")

x = 10
if x:   # 10转化为布尔值
    print("执行了")
```

### 3. if-else条件语句

**if condition:**

  **# 当条件为真时执行这里的代码**

**else:**

  **# 如果前面的条件都为假，执行这里的代码**

```python
x = 19
if x > 18:
    print("成年了")
else:
    print("未成年")
```

### 4. if-elif-else条件语句

**if condition:**

  **# 当条件为真时执行这里的代码**

**elif another_condition:**

  **# 当上面条件为假，而这个条件为真时执行这里的代码**

**else:**

  **# 如果前面的条件都为假，执行这里的代码**

```python
age = 19
if age > 18:
    print("成年了")
    age = 12
if age < 16:
    print("不允许上班")
if age > 22:
    print("可以结婚")
else:
    print("前面都没成立")

age = 19
if age > 18:
    print("成年了")
    age = 12
elif age < 16:
    print("不允许上班")
elif age > 22:
    print("可以结婚")
else:
    print("前面都没成立")
```

### 5. and or 逻辑运算符

```python
def fn():
    print("执行了fn")
    return 0
def fm():
    print("执行了fm")
    return 200
res = fn() or fm()
print(res)
```

### 6. 练习题

有一个果园，装苹果21323个苹果，一个篮子装17个苹果，如果都刚好装满了，就打印"篮子刚好够用,剩下的篮子退货"，如果是有一个篮子没装满，就打印"有一篮没装满，送福利"

```python
x = 21323
if x % 17 == 0:
    print("篮子刚好够用,剩下的篮子退货")
else:
    print(f"有一篮没装满,只装了{x%17}个 送福利")
```

## （八）循环语句

### 1. for-in 循环

**for 循环** 用于迭代遍历可迭代对象（如列表、字符串、字典等）：

```python
x = [10,20,30,40]
print(x[0])
print(x[1])
print(x[2])
print(x[3])
for i in x:
    print(i)

x = [10,20,30,40]
for el in x:
    print(el)

"""
相当于
el = x[0]
print(el)

el = x[1]
print(el)

el = x[2]
print(el)

el = x[3]
print(el)

"""

x = [10,21,30,41]
for el in x:
    if el % 2 == 0:
        print(el)

x = [[10,20,30,40],[100,200]]
for el in x:
    # print(el)
    for el2 in el:
        print(el2)
```

### 2. for-in else

for后面的 else 是指 -- 当for执行完毕（不管是否成立）以后就执行 else 代码块

```python
x = [11,21,30,41]
for el in x:
    if el % 2 == 0:
        print(el)
else:
    print("没有偶数")
```

### 3. range函数

用于生成一个整数序列，序列中的每个元素按照指定的步长递增（默认步长为1）。这个函数并不会真正创建一个列表，而是返回一个可迭代的对象——`range`对象。当你在循环中使用它时可以遍历内部的元素

**range(stop)**
**range(start, stop)**
**range(start, stop, step)**

参数说明：

- `start`（可选）：序列的起始值，默认是0。
- `stop`：序列的停止值，序列不会包含此值。
- `step`（可选）：每次迭代增加的步长，默认是1。

```python
# range(start,end,step)函数
# 返回一个可迭代对象
res = range(2,50,2) # [2,3,4]
# print(res)
for i in res:
    print(i)

for i in range(10):
    print(i)
```

> 总结: for循环 是循环的已知数据容器内部有多少的数据

### 4. while循环

**while 循环** 在条件为真时重复执行代码块

```python
"""
while 停止循环的条件代码:
   print(6666)#反复执行的业务代码
   #想办法在某一次循环中 把停止循环的条件代码 设置为False
"""

# 如果你的账户余额超过或者等于10000刀: 过一次霍尔木兹海峡,给5%的手续费
# 如果小于10000刀: 过一次霍尔木兹海峡,给200刀
# 不能欠账
# 请问我有2342334刀 能过几次
money=2342334
count=0
while money>=200:
    if money>=10000:
        money=money-money*0.05
    else:
        money=money-200
    count+=1
print(count,money)
```

### 5. break 和 continue

- **break**：用于跳出当前循环。
- **continue**：用于跳过当前迭代，继续下一次迭代。

```python
# break -- 停止当前循环语句(1.break后面的代码不执行 2.for也不循环,不执行了)
# continue -- 停止当前循环语句的当次循环(1.continue后面的代码不执行 2.for继续下次循环)

# 案例:
data = [10,20,30,40]
for i in data:  # 遍历data列表
    print(i)
    break
    # print("我不会执行")    # 不会执行
print("执行这个打印,说明for代码已经全部执行完毕")

#案例:
data = [10,20,30,40]
for i in range(5):
    for el in data:
        if el == 30:
            break   # 停止当前循环（for el in data）
        print(i,el)
print("执行这个打印,说明for代码已经全部执行完毕")
# 案例:
data=[10,20,30,40]
for i in data:
    print(i)
    continue
    # print("我不会执行")    #
print("执行这个打印,说明for代码已经全部执行完毕")
#案例:
for i in range(5):
    for el in range(5):
        if el==3:
            continue
        print(i,el)
print("执行这个打印,说明for代码已经全部执行完毕")
```

### 6. pass语句

pass是空语句，占位符，是为了保持程序结构的完整性。

pass 不做任何事情，一般用做占位语句

```python
# pass -- 是一个占位符,什么都不执行
if 100:
    pass    # 占位符
print(666)
```

### 7. 条件表达式

```python
# 条件表达式
# x = A if B else C
# B是一个表达式 它的结果转化为布尔值
# 是True x就为 A
# 是False x就为 C
x="cuda:1" if 1 else "cpu"    # cuda,显卡的驱动；1，外接显卡
print(x)
```

## （九）元组

Python 的元组与列表类似，不同之处在于元组的元素不能修改。

元组使用小括号 ( )，列表使用方括号 [ ]。

> 元组：
>
> ​    跟列表一样,也是一个存放任何类型数据的容器
>
> 区别在于 --
>
> 1. 元组定义[创建]后,就不能修改了
>
> 2. API不一样
>
> 语法：()

###  1. 创建元组

元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

元组中只包含一个元素时，需要在元素后面添加逗号 ，否则括号会被当作运算符使用

```python
# 创建元组(多个元素之间用逗号隔开)
# 存放相同类型的数据
x = (10,20,30,40)
print(x)
# 存放不同类型的数据
x = ("hello",True,3.14,[10,20,30])
print(x)

# 创建元组(1个元素,必须加逗号)
x = (30)  # (10+20)*30 --> (30)*30  所以(30)就是30
print(x,type(x))	# int
x = (30,)
print(x,type(x))	# tuple

# 创建元组(0个元素)
x=()
print(x,type(x))

# 不需要括号也可以
tup3 = "a", "b", "c", "d"

# 多元素元组可以省略括号(重点)
x = 10,20 #相当于(10,20)
x = "hello", True, 3.14
print(x,type(x))
```

### 2. 索引和切片

元组与字符串类似，下标索引从 0 开始，可以进行截取，组合等。

```python
# 取出元组中的元素 -- 索引、切片
x = (10,20,30,40)
print(x[0])
print(x[-1])
print(x[1:3])
print(x[1:3:2])     # (20,)
```

### 3. 修改元组

元组中的元素值是不允许修改的，但我们可以对元组进行连接组合

```python
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz') 

# 创建一个新的元组
tup3 = tup1 + tup2
print (tup3)

# 以下修改元组元素操作是非法的。
# tup1[0] = 100 

# 修改元组中的数据(不支持)
x = (10,20,30,40)
x[0] = 100     # 报错不允许修改元组中的数据（'tuple' object does not support item assignment）
print(x)

x = ("hello",True,3.14,[10,20,30])
print(x[3])
print(x[3][0])
x[3][0]=100     # 不允许修改元组中的数据,但是可以修改元组中的元素的内部的数据
print(x)
```

### 4. 元组不可变

所谓元组的不可变指的是元组所指向的内存中的内容不可变。

```python
tup = (1, 2, 3, 4, 5, 6, 7)
tup[1] = 100
print(tup)#报错'tuple' object does not support item assignment
```

### 5. 删除元组

元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组

```python
tup = ('openAI', 'hqyj', 100, 200) 
print (tup)
del tup
print (tup)#name 'tup' is not defined
```

### 6. 元组运算符

与字符串一样，元组之间可以使用 +、+=和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。

| Python 表达式                 | 结果                         | 描述                 |
| ----------------------------- | ---------------------------- | -------------------- |
| len((1, 2, 3))                | 3                            | 计算元素个数         |
| (1, 2, 3)+(4, 5, 6)           | (1, 2, 3, 4, 5, 6)           | 连接得到一个新的元组 |
| ('Hi!',) * 4                  | ('Hi!', 'Hi!', 'Hi!', 'Hi!') | 复制                 |
| 3 in (1, 2, 3)                | True                         | 元素是否存在         |
| for x in (1, 2, 3): print (x) | 1 2 3                        | 迭代                 |

### 7. 元组常用API

Python元组包含了以下内置函数

| 序号 | 方法        | 描述                   |
| ---- | ----------- | ---------------------- |
| 1    | len(tuple)  | 返回元组中元素个数。   |
| 2    | max(tuple)  | 返回元组中元素最大值。 |
| 3    | min(tuple)  | 返回元组中元素最小值。 |
| 4    | tuple(list) | 将列表转换为元组。     |

```python
# 1.len
x = (10,20,30)
res = len(x)
print(res)

# 2.in
res = 100 in x
print(res)

# 3.for
for el in x:
    print(el)
    
# 4.index
x = (10,203,10,2)
print(x.index(10))#元组中第一个10的索引

# 5.count
count = x.count(10)
print(count)

# 6.max
print(max(x))

# 7.min
print(min(x))
```

### 8. 解构赋值

解构赋值:
    把等号赋值语句右边的数据容器(能迭代的数据容器)
    按照索引顺序 依次赋值给等号左边的变量(一次多个变量的语法)

```python
a = [10,20]
a = (100,200)
a = "你好"
# 将等号赋值语句右边的数据容器（可迭代的数据容器） 按照索引顺序 依次赋值给 等号左边的 变量（一次多个变量的语法）
x,y = a # 相当于 x=a[0]  y=a[1]
print(x,y)
```

### 9. 案例

```python
# 案例:
x = 10
y = 20
x,y = y,x
# 这个代码怎么运行的 越细节越好(面试了很多很多研究生 没有一个能解释清楚的)
# 1.先取出y变量的值 然后取出x变量的值
# 2.创建一个内存对象(元组类型的) 假设叫a --> (20,10)
# 3.把等号右边的数据容器(元组) 解构了 按照索引的顺序赋值给等号左边的变量
# x=a[0]  y=a[1]
print(x,y)

# 为什么不是:把y赋值给x , 把x赋值给y
# 原因:脚本程序的执行 是一个任务一个任务的完成的 所以才有那句话:变量取值一定取的是最近一次的存的值

"""
伪代码:我们假装是python.exe 我来一个任务一个任务的执行代码
x=10
y=20
x=y # 取出y的值是20 赋值给x --> x=20
y=x # 取出x的值是20[最近一次存的值] 赋值给y==> y=20
"""

# _,img = fn()
```

## （十）字典

字典:
    也是一个数据容器
    只不过 它不是通过下标按照顺序存储数据
    它是按照键值对的方式来保存数据:
    {key:value, key2:value2,....}
    数据可以是任何类型 键名 必须是不可变的数据类型

### 1. 可变数据和不可变数据

```python
# 可变数据和不可变数据
x = 10
x2 = 10
print(id(x),id(x2))
print(id(x) == id(x2))  # 在内存中10是一个数据 x和x2都是那个10 数据的id表示的是它的内存地址

x = 10
x = 20   # 10并没有变 x重新指向新的数据20

x = [10,20,30]
print(x,id(x))  # [10, 20, 30] 2257163824448
x[0] = 100
print(x,id(x))  # [100, 20, 30] 2257163824448
# x列表的id没有变,说明列表还是那个列表  x中的数据发生了变化 说明列表可以被改变

# 总结:
# 数字 字符串 布尔值 None 元组 都是不可变数据
# 列表 字典 集合 函数  类 函数对象 都是可变数据
```

### 2. 创建字典

dict 作为 Python 的关键字和内置函数，变量名不建议命名为 **dict**。

键必须是唯一的，但值则不必。

值可以取任何数据类型，但键必须是不可变的，如字符串，数字。

```python
# 创建字典
x = {
    "name":"张三",
    "age":18,
    1:"三好学生",
    2:"程序员",
    ("华清远见","成都"):[800,1200,30],
    None:100,
    "son":{"name":"李四"}
}
print(x) # 打印字典
print(len(x))	# 查看字典的数量
print(type(x))	# 查看类型
```

### 3. 访问字典的值(取)

把相应的键放入到方括号中

如果用字典里没有的键访问数据，会输出错误

```python
# 取出字典中的数据
print(x)
print(x["name"])
print(x[1])
print(x["son"])
print(x["son"]["name"])
# print(x["1"])     # 字典中没有这个键名时 取值会报错
print(x[("华清远见","成都")])
```

### 4. 修改字典(存)

向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对

```python
# 存值
x[3] = 666  # 没有键名就是添加
x[1] = 666  # 有键名就是更新
print(x)
```

### 5. 变量的代数思想

```python
a = "name"
x = {"a":"张三"}
print(x)

a = "name"
x = {a:"张三"}    # 键名为："name"
print(x)


a = "name"
x = {a:"张三","age":a}    # 1
name = "age"
print(x[name])  # 2

# 总结:未来
# 上面代码1写内部写a的地方 可以写任何表达式,只要运行出来是一个数据就行了
# 上面代码2写内部写name的地方 可以写任何表达式,只要运行出来是一个数据就行了,而是这个数据是字典的已经存在的键名就行了

# x={(fn()+a):xxx[]()[1]}   # 词典
# x[fm()+b]
```

### 6. 删除字典元素

能删单一的元素也能清空字典，清空只需一项操作

显式删除一个字典用del命令

```python
mydic = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
del mydic['Name'] # 删除键 'Name'
mydic.clear()     # 清空字典

 
print (mydic['Age'])
print (mydic['School'])

del mydic         # 删除字典
```

### 7. 字典键的特性

字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。

1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住

```python
mydic = {'Name': 'jack', 'Age': 27, 'Name': 'karen'}
print (mydic['Name'])
```

2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行

```python
mydic1 = {97:"a",98:"b"}
mydic2 = {"name":"karen","age":27}
mydic3 = {['Name']: 'karen', 'Age': 27}
print(mydic3[['Name']])#报错unhashable type: 'list'
```

### 8. 笔试题

提取网址中的用户信息
{"wd":"你好","count":20,"page":2,"user":"karen"}

```python
"""
笔试题：
    提取网址中的用户信息
    {"wd":"你好","count":20,"page":2,"user":"karen"}
"""
# 案例：直接添加
x = {}
x["wd"] = "你好"
print(x)

# 案例：变量添加
x = {}
a = "wd"
b = "你好"
x[a] = b
print(x)

# 案例：字典添加
x = {}
res = ["wd","你好"]
x[res[0]] = res[1]
print(x)

# 题目代码
url = "http://www.baidu.com/s?wd=你好&count=20&page=2&user=karen"
# url = "https://www.h.com/zhuanti/2025nzpd/index.html?plan=%E5%B5%8C%E5%85%A5%E5%BC%8F-%E4%BD%8E&unit=%E8%A1%8C%E4%B8%9A&k=%E5%8D%8E%E9%9D%92%E8%BF%9C%E8%A7%81&s=hq1&sdclkid=AL2D152iA6D6AL-pAo&bd_vid=10635573657764966776"

x = {}
# print(url.split("?")[1].split("&")) -- 先用？分割字符串为列表，提取下标为1的元素，再用&分割为列表
for sub_str in url.split("?")[1].split("&"):    # 遍历列表，用=分割为列表
    # print(sub_str.split("="))
    key,value = sub_str.split("=")  # 将列表的元素作为键值对
    x[key] = value  # 添加到字典中
print(x)    # {"wd":"你好","count":20,"page":2,"user":"karen"}
```

### 9. 字典常用API

操作字典的函数：

| 序号 | 函数           | 描述                                               |
| ---- | -------------- | -------------------------------------------------- |
| 1    | len(dict)      | 计算字典元素个数，即键的总数。                     |
| 2    | str(dict)      | 输出字典，可以打印的字符串表示。                   |
| 3    | type(variable) | 返回输入的变量类型，如果变量是字典就返回字典类型。 |

字典的方法：

| 序号  | 函数及描述                                                   |
| ----- | ------------------------------------------------------------ |
| 1     | `dict.clear()`删除字典内所有元素                             |
| 2     | `dict.copy()`返回一个字典的浅复制                            |
| 3     | `dict.fromkeys(seq)`创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值 |
| ==4== | `dict.get(key, default=None)`返回指定键的值，如果键不在字典中返回 default 设置的默认值 |
| 5     | `key in dict`如果键在字典dict里返回true，否则返回false       |
| 6     | `dict.items()`以列表返回一个视图对象                         |
| 7     | `dict.keys()`返回一个视图对象                                |
| 8     | `dict.setdefault(key, default=None)`和`get()`类似, 但如果键不存在于字典中，将会添加键并将值设为default |
| 9     | `dict.update(dict2)`把字典dict2的键/值对更新到dict里         |
| 10    | `dict.values()`返回一个视图对象                              |
| 11    | `pop(key,default)`删除字典 key（键）所对应的值，返回被删除的值。 |
| 12    | `popitem()`返回并删除字典中的最后一对键和值。                |

```python
# get()重点
# dict.get(key, default=None)返回指定键的值，
# 如果键不在字典中返回 default 设置的默认值
x = {"name":"张三","age":18,"sex":"男"}
# res = x["rank"]   # 键不存在会报错
res = x.get("rank") # 键不存在返回None（或自定义默认值），不会报错
print(res)
res = x.get("rank1",100)
print(res)
print(x.get("rank2",1000))

# for重点
x = {"name":"张三","age":18,"sex":"男"}
for el in x:    # el是字典的键
    print(f"el:{el},el的类型:{type(el)}, x[el]:{x[el]}")

x = {"name":"张三","age":18,"sex":"男"}
for el in x.keys(): # el是字典的键
    print(f"el:{el},el的类型:{type(el)}, x[el]:{x[el]}")

x = {"name":"张三","age":18,"sex":"男"}
for el in x.values():   # el是字典的值
    print(f"el:{el}")

x = {"name": "张三", "age": 18, "sex": "男"}
for el in x.items():    # el是字典的键值对
    print(el)

x = {"name": "张三", "age": 18, "sex": "男"}
for k,v in x.items():   # 将键值对的键和值分别赋值给k,v; k是字典的键 v是字典的值
    print(k,v)

# 删除
x = {"name":"张三","age":18,"sex":"男"}
x.clear()
x = {}  # 重新定义一个x字典，之前的会被删除，释放空间
# del x   # 删除x变量，变量名不存在会报错
# del x["name"]   # 删除x字典的name键值对

# 拷贝
x = {"name":"张三","age":18,"sex":"男"}
y = x.copy()    # 浅拷贝，改变y字典，x字典不会改变
# y = x   # 赋值，x字典会改变
y["name"] = "李四"
print(x,y,id(x),id(y))
res = "sex" in x
print(res)

# 键值对 -- dict.items()以列表返回一个视图对象
x = {"name":"张三","age":18,"sex":"男"}
y = x.items()   # 可迭代对象 里面是键值对 for可以循环取出每一对
print(x,y,id(x),id(y))

# dict.setdefault(key, default=None)和get()类似,
# 但如果键不存在于字典中，将会添加键并将值设为default
x = {"name":"张三","age":18,"sex":"男"}
x.setdefault("rank",100)    # 字典中没有"rank"就设置
x.setdefault("age",100)     # 字典中有"age"就不设置
print(x)


x = {"name":"张三","age":18,"sex":"男"}
x2 = {"name":"李四","age":20,"sex":"女"}
x2 = {"age":20,"sex":"女"}
x2 = {"age":20,"sex":"女","it":"python"}
# dict.update(dict2)把字典dict2的键/值对更新到dict里
x.update(x2)#把x2的键值对全部复制粘贴进x中
# pop(key,default)删除字典 key（键）所对应的值，返回被删除的值
x.pop("name")   # 删除x中的"name"
print(x)
```

## （十一）集合

集合（set）:
    也是一个数据容器
    主要是用来存放不重复数据的
    没有顺序,没有索引 如果添加了重复元素 只会保留一个
    可以进行交集、并集、差集等常见的集合操作

### 1. 创建集合

可以使用大括号 { } 创建集合，元素之间用逗号 , 分隔， 或者也可以使用 set() 函数创建集合。

**注意：**创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

**parame = {value01,value02,...}**

**set(value)**

```python
x = set()  # 集合只能用set()创建，{}会被解释为字典
print(x, type(x))
```

### 2. 添加元素

将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作。

**s.add( x ) 添加元素到集合** 

**s.update( x ) 添加元素到集合，且参数可以是列表，元组，字典等** ，x 可以有多个，用逗号分开

```python
x = {10, 20, 30, 10}
x.add(100)
x.add(100)
x.update([10, 20, 304, ])
x.update((100, 200))
x.update({100, 200, 300})
x.update([90, 80, 70], (88, 99))
print(x)
```

### 3. 移除元素

**s.remove( x ):将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误。**

**s.discard( x ):将元素 x 从集合 s 中移除，如果元素不存在，不会发生错误。**

**s.pop():对集合进行无序的排列，然后将这个无序排列集合的左面第一个元素进行删除。（随机删除）** 

```python
# s.remove(x):将元素 x从集合 s中移除，如果元素不存在，则会发生错误。
x = {10, 20, 30, 40}
x.remove(10)
print(x)
# x.remove(10)  # 移除没有的元素 会报错

# s.discard( x ):将元素 x从集合 s中移除，如果元素不存在，不会发生错误。
x = {10, 20, 30, 40}
x.discard(10)
print(x)
x.discard(10)

# s.pop():对集合进行无序的排列，然后将这个无序排列集合的左面第一个元素进行删除。
x.pop()  # 随机删除一个元素
print(x)
```

### 4. 计算集合元素个数

**len(s):计算集合元素个数**

```python
x = {10, 20, 30, 40}
print(len(x))
```

### 5. 清空集合

**s.clear():清空集合**

```
s1 = {10, 20, 30}
s1.clear()
print(s1)
```

### 6. 判断元素是否在集合中存在

**x in s  判断元素 x 是否在集合 s 中，存在返回 True，不存在返回 False。**

```python
s1 = {10, 20, 30}
print(20 in s1)
```

### 7. 其他操作

```python
print(str(x))  # 集合转为字符串，打印出来像集合（实际不是集合），只是没有打印引号
for el in x:  # 遍历集合
    print(el)
```

### 8. 数学运算

```python
# 数学运算
x = {10, 20, 30, 40}
y = {20, 30, 40, 50}
# 交集
print(x & y)
print(x.intersection(y))
# 并集
print(x | y)
print(x.union(y))
# 差集
print(x - y)
print(x.difference(y))
# 对称差集 -- (a-b) | (b-a)
print(x ^ y)
print(x.symmetric_difference(y))
```

### 9. 集合内置方法完整API

集合的方法

| 方法                          | 描述                                                         |
| ----------------------------- | ------------------------------------------------------------ |
| add()                         | 为集合添加元素                                               |
| clear()                       | 移除集合中的所有元素                                         |
| copy()                        | 拷贝一个集合                                                 |
| difference()                  | 返回多个集合的差集                                           |
| difference_update()           | 移除集合中的元素，该元素在指定的集合也存在。                 |
| discard()                     | 删除集合中指定的元素                                         |
| intersection()                | 返回集合的交集                                               |
| intersection_update()         | 返回集合的交集。                                             |
| isdisjoint()                  | 判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。 |
| issubset()                    | 判断指定集合是否为该方法参数集合的子集。                     |
| issuperset()                  | 判断该方法的参数集合是否为指定集合的子集                     |
| pop()                         | 随机移除元素                                                 |
| remove()                      | 移除指定元素                                                 |
| symmetric_difference()        | 返回两个集合中不重复的元素集合。                             |
| symmetric_difference_update() | 移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。 |
| union()                       | 返回两个集合的并集                                           |
| update()                      | 给集合添加元素                                               |
| len()                         | 计算集合元素个数                                             |

## （十二）数据类型转换

### 1.  数据类型

六大基本数据类型：

> 数字 —— num = 1
>
> 字符串 —— str = ‘Hello’
>
> 列表 —— list = [1,2,3,4,5]
>
> 元组 —— tuple = (1,2,3,4,5)
>
> 集合 —— set = {1,2,3,4,5}
>
> 字典 —— dict = {“key1”:”value1”,”key2”:”value1”}

type()函数：用来查看存储数据的变量的变量类型，换句话说就是查看数据类型的。

```python
# type()函数的用法
my_int = 1
my_bool = True 
my_float = 3.14
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}
my_dict = {"key1": "value1"}

print(type(my_int))
print(type(my_bool))
print(type(my_float))
print(type(my_list))
print(type(my_tuple))
print(type(my_set))
print(type(my_dict))

"""
<class 'int'>
<class 'bool'>
<class 'float'>
<class 'list'>
<class 'tuple'>
<class 'set'>
<class 'dict'>
"""
```

### 2.  数据类型转换

数据类型转换指一个数据从当前的数据类型转换为另一种数据类型，分为==显式类型转换==和==隐式类型==转换两种。

**隐式类型转换**：

> 是指解释器自动将一种数据类型的值转换为另一种数据类型的过程， 程序员无需操作，多发生在数学运算的过程中。
>
> 隐式类型转换的常用场景：算数运算中的类型转换 
>
> 需要注意的是，虽然Python允许一些隐式类型转换，但并不意味着所有类型都可以随意转换。因此为了确保程序的稳定性，应尽量避免不必要的隐式类型转换，或者使用显式类型转换。

```python
# 隐式类型转换
num1 = 1
num2 = 2.3
print(f"num1的类型为{type(num1)}")
print(f"num2的类型为{type(num2)}")
print(f"相加的类型为{type(num1 + num2)}")

num3 = 3
num4 = 2
print(f"num3的类型为{type(num3)}")
print(f"num4的类型为{type(num4)}")
print(f"相除的类型为{type(num3 / num4)}")

"""
num1的类型为<class 'int'>
num2的类型为<class 'float'>
相加的类型为<class 'float'>
num3的类型为<class 'int'>
num4的类型为<class 'int'>
相除的类型为<class 'float'>
"""
```

**显示类型转换：**

> 也叫做强制类型转换，由程序员明确地将某种数据类型的数据转化为其他数据类型（强转也要符合逻辑）。 
>
> 显示类型转换的使用场景：代码逻辑中所有需要数据类型转换的地方都可以使用显式类型转换 
>
> 需要注意的是，即使是强制类型转换，也不是所有对象都可以安全的转换为任意其他类型，转换的过程中可能会报错。

```python
# 显示类型转换
print(int(3.14))
print(float(1))
print(type(str(123)))
print(type(hex(10)))

"""
3
1.0
<class 'str'>
<class 'str'>
"""
```

**比较常用的强制类型转换函数**

| 函数         | 描述                                   |
| ------------ | -------------------------------------- |
| int(x)       | 将x转化为整型                          |
| float(x)     | 将x转化为浮点型                        |
| complex(x,y) | 将x、y转化为一个复数，x为实部，y为虚部 |
| str(x)       | 将x转化为字符串                        |
| tuple(s)     | 将序列s转化为一个元组                  |
| list(s)      | 将序列s转化为一个列表                  |
| hex(x)       | 将整数x转化为一个十六进制字符串        |

```python
x1 = 10
x2 = "666"
x3 = True
x4 = None
x5 = [10, 20, 30]
x6 = (10, 20, 30)
x7 = {10, 20, 30}
x8 = {"name": "张三", "age": 18}

# int str bool
print(int(x2))  # 字符串中不是纯数字，不能转换为int，会报错
print(int(x3))

print(bool(x1))  # 所有类型都可以转为bool -- 非空为 True，空为 False

# list tuple set dict
print(list((10, 20, 30)))  # 传入可迭代对象
res = list({10, 20, 30})
print(res)
print(tuple({10, 20, 30}))  # 传入可迭代对象
print(set(x2))  # 传入可迭代对象
# print(dict(x2))

# 怎么去除列表重复的元素
# 先转为集合，再转为列表
x = [10, 20, 30, 40, 50, 50]
x2 = list(set(x))
print(x2)

# str(所有数据都可以转为字符串)
```

## （十三）补充

#### 1. match...case

python3.10版本以后推出的，提供更强大的模式匹配方法

```python
match 表达式：
	case 模式1：
		代码块1
    case 模式2：
		代码块2
    case _：
		代码块3
```

