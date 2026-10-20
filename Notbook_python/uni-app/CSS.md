## 目录
1. CSS 基础概念（什么是CSS、作用、和HTML关系）
2. CSS 三种引入方式（行内、内部、外部，优缺点对比）
3. CSS 基础选择器（全部选择器分类+示例）
4. 选择器优先级（权重计算，零基础秒懂）
5. CSS 基础文本样式（文字、字体、对齐、行高、颜色）
6. CSS 基础盒模型（核心重点：内容、内边距、边框、外边距）
7. 块级、行内、行内块元素（三大元素特性+转换）
8. 背景样式（颜色、图片、平铺、定位、尺寸）
9. 列表样式（ul/ol 去除圆点、自定义符号）
10. 超链接伪类（LVHA 顺序记忆法）
11. 浮动 float（布局原理、高度塌陷、清除浮动4种方案）
12. 定位 position（静态、相对、绝对、固定、粘性定位）
13. 弹性布局 Flex（现代主流布局，一维布局全套属性）
14. 网格布局 Grid（二维表格布局，完整属性讲解）
15. 样式三大特性：层叠、继承、优先级
16. 圆角、阴影、透明度、渐变
17. 过渡 transition、动画 animation、变换 transform
18. 媒体查询（响应式适配手机/平板/电脑）
19. 单位详解（px、em、rem、vw、vh、%）
20. 常用重置样式（CSS Reset 消除浏览器默认差异）
21. 常见开发坑与易错点

---

# 1. CSS 基础概念

## 1.1 什么是CSS
- 全称：**Cascading Style Sheets 层叠样式表**
- HTML 负责：搭建网页结构（文字、图片、按钮、段落）
- CSS 负责：美化网页（颜色、大小、布局、间距、动画）
## 1.2 语法格式（固定写法，所有CSS通用）
```css
选择器 {
  属性名: 属性值;
  属性名2: 属性值2;
}
```
拆解说明：
1. **选择器**：选中要修改样式的HTML标签
2. `{}`：样式包裹区域
3. `属性`：要修改的样式功能（color颜色、font-size字号）
4. `属性值`：给属性设置效果
5. `;` 每条样式结束必须加分号，最后一条可省略，建议统一加上

示例：修改所有段落文字为红色
```css
p {
  color: red;
}
```

# 2. CSS 三种引入方式
## 2.1 行内样式（写在标签内部）
写法：标签上加 `style="样式"`
```html
<p style="color: blue; font-size: 20px;">蓝色文字</p>
```
优点：快速单独修改一个标签
缺点：结构样式混在一起，无法复用，不推荐开发使用

## 2.2 内部样式表（写在HTML页面head里）
```html
<head>
  <style>
    p {
      color: green;
    }
  </style>
</head>
```
优点：当前页面所有相同标签统一修改，结构样式分离
缺点：只能作用于当前页面，多页面无法共用

## 2.3 外部样式表（开发最推荐，单独`.css`文件）
1. 新建文件 `style.css`，只写css代码
```css
p {
  color: orange;
}
```
2. HTML页面用 `<link>` 引入
```html
<link rel="stylesheet" href="style.css">
```
- `rel="stylesheet"`：固定，代表引入样式表
- `href`：css文件路径
优点：多页面共用，结构和样式完全分离，便于维护
缺点：需要额外创建文件

## 三种引入优先级（就近原则）
行内样式 > 内部样式 > 外部样式

# 3. CSS 选择器大全
## 3.1 基础选择器
1. **通配符选择器 `*`**：选中页面所有标签
```css
* { margin: 0; padding: 0; }
```
2. **标签选择器**：直接写标签名（div/p/h1/img）
```css
div { background: pink; }
```
3. **类选择器 `.类名`**：给标签加class，一个类可多个标签共用
HTML：`<div class="box">盒子</div>`
CSS：
```css
.box { width: 100px; }
```
4. **ID选择器 `#id名`**：id页面唯一，只能一个标签使用
HTML：`<div id="main">主区域</div>`
CSS：
```css
#main { height: 200px; }
```

## 3.2 复合选择器
1. **后代选择器 空格**：父标签 子标签，选中所有后代
```css
div p { color: red; } /* div里面所有p标签 */
```
2. **子元素选择器 `>`**：只选直接子元素，不包含孙子
```css
div > p { color: red; }
```
3. **并集选择器 `,`**：同时选中多个选择器，共用样式
```css
h1, p, .box { font-size: 16px; }
```
4. **交集选择器**：标签+类，同时满足两个条件
```css
div.box { background: yellow; }
```

## 3.3 属性选择器
```css
/* 带有title属性的标签 */
[title] {}
/* title等于文字的标签 */
[title="测试"] {}
/* class包含test的标签 */
[class*="test"] {}
```

## 3.4 伪类选择器（匹配标签状态）
- `:hover` 鼠标放上去
- `:active` 鼠标按住不放
- `:visited` 链接访问后
- `:link` 未访问链接
- `:first-child` 第一个子元素
- `:last-child` 最后一个子元素
- `:nth-child(n)` 第n个子元素

## 3.5 伪元素选择器（创建虚拟元素）
- `::before` 元素内部最前面加内容
- `::after` 元素内部最后面加内容
必须搭配 `content:"内容"` 使用
```css
.box::after {
  content: "末尾文字";
}
```

# 4. 选择器权重（优先级）
权重数字越大，样式优先级越高，高权重会覆盖低权重
1. 通配符`*`：0001
2. 标签选择器：0010
3. 类/伪类/属性选择器：0100
4. ID选择器：1000
5. 行内style样式：10000
6. `!important`：无限大，强制最高优先级（谨慎使用）

权重计算规则：从左到右依次比较，高位大直接覆盖，不用算总和
示例：`#box .list p` = 1000 + 0100 + 0010 = 1110

# 5. 文本与字体样式
## 5.1 字体相关
1. `font-size: 20px;` 字号，px像素单位
2. `font-family: "微软雅黑", sans-serif;` 字体，多字体逗号分隔，找不到第一个自动切换下一个
3. `font-weight: bold;` 字重（粗细）
   - normal 正常400，bold加粗700，数字100~900
4. `font-style: italic;` 斜体，normal正常
5. 复合简写（顺序固定：粗细 斜体 字号/行高 字体）
```css
font: bold italic 18px/1.5 "微软雅黑";
```

## 5.2 文字样式
1. `color: #ff0000;` 文字颜色，三种写法
   - 英文单词：red
   - 十六进制：#fff #ff0000
   - rgb/rgba：rgb(255,0,0) rgba(0,0,0,0.5) 最后一位透明度0~1
2. `text-align: center;` 水平对齐 left左 right右 center居中
3. `line-height: 30px;` 行高，文字垂直居中技巧：行高=盒子高度
4. `text-indent: 2em;` 首行缩进，2em=两个汉字宽度
5. `text-decoration: none;` 文字装饰
   - none 无下划线（去除链接默认下划线）
   - underline 下划线 overline上划线 line-through删除线
6. `letter-spacing: 2px;` 字间距
7. `word-spacing: 4px;` 单词间距（英文）
8. `text-shadow: 2px 2px 5px #ccc;` 文字阴影

# 6. 盒模型（CSS核心）
网页所有标签都可以看作一个矩形盒子，由4部分组成：
## 6.1 四部分结构（从内到外）
1. **content 内容区**：width height 文字图片存放区域
2. **padding 内边距**：内容和边框之间距离，会撑大盒子
3. **border 边框**：盒子边线
4. **margin 外边距**：盒子和其他盒子之间间距，不会撑大盒子

## 6.2 边框 border
```css
/* 简写：粗细 样式 颜色 */
border: 2px solid #000;
/* 单边设置 */
border-top: 1px red solid; /* 上边框 */
border-radius: 10px; /* 圆角 */
```
边框样式 solid实线 dashed虚线 dotted点线 double双线

## 6.3 内边距 padding
四个值顺序：上 右 下 左（顺时针）
```css
padding: 10px; /* 四周全部10px */
padding: 10px 20px; /* 上下10 左右20 */
padding: 10px 20px 5px; /* 上10 左右20 下5 */
padding: 1px 2px 3px 4px; /* 上 右 下 左 */
```

## 6.4 外边距 margin
写法和padding完全一致，作用是盒子之间拉开距离
```css
margin: 0 auto; /* 块级盒子水平居中 */
```
### 外边距塌陷（坑）
1. 垂直两个块盒子上下margin会合并，取最大值
2. 父盒子无边框/内边距，子盒子margin-top会传递给父盒子
解决：父盒子加border、padding、overflow:hidden

## 6.5 标准盒模型 / 怪异盒模型
1. **标准盒（默认 box-sizing: content-box）**
盒子实际宽度 = width + 左右padding + 左右border
2. **怪异盒（推荐 box-sizing: border-box）**
设置的width就是盒子总宽度，padding和边框向内压缩内容，不会撑大盒子
全局统一设置（开发必写）
```css
* {
  box-sizing: border-box;
}
```

# 7. 元素三大显示类型
## 7.1 块级元素 block
代表：div、h1~h6、p、ul、li、form
特性：
1. 独占一行，自动换行
2. 宽高、内外边距都可以设置
3. 不写width默认占满父盒子100%

## 7.2 行内元素 inline
代表：span、a、b、i、em
特性：
1. 一行多个并排显示
2. 宽高设置无效，大小由内容撑开
3. 左右margin/padding有效，上下垂直边距失效

## 7.3 行内块 inline-block
代表：img、input
特性：
1. 一行多个并排，中间有默认空白缝隙
2. 可以设置宽高、内外边距

## 7.4 类型转换 display
```css
display: block; /* 转为块级 */
display: inline; /* 转为行内 */
display: inline-block; /* 转为行内块 */
display: none; /* 完全隐藏，不占页面空间 */
visibility: hidden; /* 隐藏但保留占位 */
```

# 8. 背景 background
## 8.1 基础属性
```css
background-color: #eee; /* 背景颜色 */
background-image: url("bg.jpg"); /* 背景图片 */
background-repeat: no-repeat; /* 平铺 */
/* repeat-x 水平平铺 repeat-y垂直 no-repeat不平铺 */
background-position: center top; /* 定位 */
/* 方向词 left/center/right top/center/bottom 也可以px数值 */
background-size: cover; /* 背景尺寸 */
/* cover铺满盒子，图片不变形 contain完整显示图片 */
```
## 8.2 复合简写（无顺序要求）
```css
background: #fff url(bg.png) no-repeat center/cover;
```

# 9. 列表样式 ul ol
```css
ul {
  list-style: none; /* 去除默认小圆点 */
  list-style-type: square; /* 方块标记 */
  list-style-position: inside; /* 符号在内容内部 */
}
```

# 10. 超链接 a 伪类 LVHA 顺序（必须遵守）
1. `:link` 未访问链接
2. `:visited` 访问过后
3. `:hover` 鼠标悬浮
4. `:active` 鼠标点击按住
```css
a:link { color: black; }
a:visited { color: gray; }
a:hover { color: red; }
a:active { color: orange; }
```

# 11. 浮动 float（传统布局）
## 11.1 作用
让块级元素横向并排，脱离标准文档流
```css
float: left; /* 左浮动 */
float: right; /* 右浮动 */
float: none; /* 不浮动 */
```
## 11.2 浮动特性
1. 脱离标准流，不占原本页面位置
2. 多个浮动元素紧贴一行排列，宽度不够自动换行
3. 浮动元素自动转为行内块，可以设置宽高

## 11.3 高度塌陷（浮动最大问题）
父盒子没有设置高度，子元素全部浮动后，父盒子高度变为0，下面布局错乱
### 四种清除浮动方案
1. 父盒子设置固定高度（简单，不灵活）
2. 额外标签法：浮动末尾加空div `clear:both`
```css
.clear { clear: both; }
```
3. 父盒子添加 `overflow: hidden;`（最简单常用）
4. 伪元素清除浮动（开发通用最优方案）
```css
.clearfix::after {
  content: "";
  display: block;
  clear: both;
  visibility: hidden;
  height: 0;
}
.clearfix {
  *zoom: 1; /* 兼容旧浏览器 */
}
```

# 12. 定位 position
## 12.1 static 静态定位（默认）
所有标签默认值，无特殊定位，top/left无效

## 12.2 relative 相对定位
1. 不脱离文档流，原本位置保留占位
2. 相对于自身原始位置移动
3. `top left right bottom` 设置偏移量
```css
position: relative;
top: 10px;
left: 10px;
```

## 12.3 absolute 绝对定位
1. 脱离文档流，不占位
2. 相对于**最近设置非static定位的父盒子**
3. 父盒子没定位，则相对于浏览器页面
居中技巧：
```css
position: absolute;
left: 50%;
top: 50%;
transform: translate(-50%, -50%);
```

## 12.4 fixed 固定定位
1. 脱离文档流
2. 永远相对于浏览器窗口，滚动页面位置不变（导航栏、回到顶部按钮）

## 12.5 sticky 粘性定位
相对+固定结合，滚动到边界固定住（侧边导航）
## 12.6 z-index 层级
只有定位元素生效，数字越大层级越靠上，默认0

# 13. Flex 弹性布局（现代一维布局，推荐）
给父盒子设置 `display: flex;`，子元素自动变成弹性项
## 13.1 父容器属性
1. `flex-direction` 主轴方向
   - row 默认水平从左到右
   - column 垂直从上到下
2. `justify-content` 主轴对齐（水平）
   - flex-start 左对齐 center居中 flex-end右对齐 space-between两端均分 space-around两侧留白均分
3. `align-items` 侧轴对齐（垂直）
   - center垂直居中 stretch拉伸填满 baseline文字对齐
4. `flex-wrap: wrap;` 自动换行，不设置会压缩子元素
5. `align-content` 多行侧轴对齐

## 13.2 子元素属性
1. `flex: 1;` 平分剩余宽度（等分栏核心）
2. `align-self: center;` 单独控制单个子元素垂直对齐
3. `order: 2;` 调整排序，数字越小越靠前

# 14. Grid 网格布局（二维布局，表格式）
父盒子 `display: grid;`，同时控制行和列
## 14.1 父容器
```css
/* 3列，每列100px */
grid-template-columns: 100px 100px 100px;
/* 均分3列 */
grid-template-columns: repeat(3, 1fr);
grid-template-rows: 80px 200px; /* 两行高度 */
gap: 10px; /* 行列间隙 */
justify-items: center; /* 单元格内水平居中 */
align-items: center; /* 单元格内垂直居中 */
```
## 14.2 子项
`grid-column: 1/3;` 跨列，`grid-row` 跨行

# 15. CSS三大特性
1. **层叠性**：相同选择器重复写样式，后面覆盖前面
2. **继承性**：文字相关样式自动继承给子元素（color font text-*），宽高边框内外边距不继承
3. **优先级**：权重高覆盖权重低，权重相同层叠性生效

# 16. 美化进阶样式
## 16.1 圆角
```css
border-radius: 10px;
/* 圆形：宽高相同，圆角50% */
border-radius: 50%;
```
## 16.2 盒子阴影
```css
box-shadow: 水平偏移 垂直偏移 模糊度 大小 颜色;
box-shadow: 0 2px 10px rgba(0,0,0,0.2);
```
## 16.3 透明度
1. `opacity: 0.5;` 整个盒子全部透明（文字一起透明）
2. `rgba(0,0,0,0.5)` 只让背景/颜色透明，文字不受影响

## 16.4 渐变
```css
/* 线性渐变 */
background: linear-gradient(red, yellow);
/* 径向渐变 */
background: radial-gradient(red, blue);
```

# 17. 变换、过渡、动画
## 17.1 transform 2D/3D变换
```css
transform: translate(10px,20px); /* 位移 x y */
transform: rotate(30deg); /* 旋转 角度deg */
transform: scale(1.2); /* 缩放 1=原大小 */
transform: skew(10deg); /* 倾斜 */
```
## 17.2 transition 过渡（平滑变化）
给元素加过渡，hover变化不会瞬间跳转
```css
transition: all 0.3s linear;
/* all所有属性 0.3秒完成 linear匀速 */
```
## 17.3 animation 关键帧动画（循环动画）
1. 定义动画
```css
@keyframes move {
  0% { transform: translateX(0); }
  100% { transform: translateX(200px); }
}
```
2. 使用动画
```css
animation: move 2s infinite alternate;
/* 动画名 时长 无限循环 往返播放 */
```

# 18. 单位详解
1. `px` 像素，固定尺寸
2. `em` 相对父元素字号 1em=父字体大小
3. `rem` 相对根html字号，移动端适配首选
4. `%` 百分比，相对父盒子宽高
5. `vw/vh` 视口单位，1vw=屏幕宽度1%，1vh=屏幕高度1%

# 19. 媒体查询 响应式适配
根据屏幕宽度切换样式，适配手机电脑平板
```css
/* 屏幕宽度小于768px 手机样式 */
@media screen and (max-width:768px) {
  div { width: 100%; }
}
```

# 20. 通用CSS重置代码（开发直接复制）
消除浏览器自带默认间距、样式差异
```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
ul,ol {
  list-style: none;
}
a {
  text-decoration: none;
  color: #333;
}
img {
  border: none;
  vertical-align: middle;
}
```

# 21. 高频易错点总结
1. 浮动父盒子高度塌陷，记得清除浮动
2. 行内元素宽高不生效，转block/inline-block
3. 定位居中用translate，不用计算宽高
4. a标签伪类顺序必须 LVHA，顺序错误hover失效
5. 外边距垂直塌陷，统一用padding代替垂直间距
6. 渐变、阴影、过渡不会改变盒子实际占用宽高
7. `display:none` 完全消失，`visibility:hidden` 保留位置
8. rem需要给html设置基础字号，vw不需要
9. 浮动元素会自动变成行内块，margin左右生效
10. 伪元素`::before/after`必须加content，否则不显示

