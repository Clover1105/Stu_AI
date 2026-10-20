# 一、HTML5 基础认知
## 1.1 什么是 HTML
1. HTML 全称：**超文本标记语言（HyperText Markup Language）**
2. 作用：搭建网页骨架，定义页面上文字、图片、按钮、视频等所有内容的结构
3. 本质：不是编程语言（无逻辑、无计算），只是**标记标签**，用来给内容分类
4. HTML5：HTML 第五代标准，新增大量新标签、多媒体、表单、本地存储等功能，是现在网页统一标准

## 1.2 网页三层结构（必记）
1. HTML：结构层 → 搭建页面骨架（房子墙体、房间分区）
2. CSS：样式层 → 美化页面（粉刷墙壁、家具颜色、尺寸）
3. JavaScript：行为层 → 实现交互（开门、灯光开关、点击弹窗）

## 1.3 浏览器与网页运行原理
1. 浏览器作用：解析 HTML 代码，渲染成可视化页面
2. 主流浏览器：Chrome、Edge、Firefox、Safari
3. 渲染流程：浏览器读取 HTML 文件 → 识别标签 → 构建DOM树 → 绘制页面

## 1.4 开发工具
1. 简易工具：记事本、系统自带文本编辑器（缺点：无代码提示）
2. 专业推荐：VS Code（免费、轻量、HTML插件齐全）
3. 运行方式：写完代码保存为 `.html` 文件，双击用浏览器打开

# 二、HTML5 文件基础结构
## 2.1 完整标准模板（通用所有页面）
```html
<!DOCTYPE html>
<!-- 声明文档类型：告诉浏览器这是HTML5页面 -->
<html lang="zh-CN">
<!-- 根标签，整个网页所有内容都写在html内部 -->
<!-- lang="zh-CN" 代表页面语言为中文，利于搜索引擎识别 -->
<head>
    <!-- 头部：存放页面配置，内容不会直接显示在网页可视区域 -->
    <meta charset="UTF-8">
    <!-- 设置文字编码UTF-8，解决中文乱码问题 -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- HTML5移动端适配核心：自动适配手机屏幕宽度，禁止默认缩放 -->
    <title>页面标题</title>
    <!-- 浏览器标签栏显示的文字，必须写 -->
</head>
<body>
    <!-- 主体：所有可见内容（文字、图片、按钮、视频）全部写在这里 -->
    这里是网页显示的内容
</body>
</html>
```

## 2.2 各标签详细解释
1. `<!DOCTYPE html>`
   - 无闭合标签，放在文件第一行
   - 作用：区分 HTML4 / HTML5，不加会导致浏览器怪异模式，样式错乱
2. `<html>`
   - 整个页面根节点，只有一对
3. `<head>` 头部区域
   - 不会展示给用户，仅配置页面信息
   - 常用子标签：`meta`、`title`、`link`、`style`
4. `<body>` 主体区域
   - 页面所有看得见的内容全部存放于此

## 2.3 标签两大分类
### 1）双标签（开始标签+结束标签，包裹内容）
格式：`<标签名>内容</标签名>`
示例：`<h1>标题</h1>`、`<p>段落文字</p>`

### 2）单标签（自闭合，无内部内容）
格式：`<标签名 />` / `<标签名>`（HTML5可省略斜杠）
示例：`<img>` 图片、`<br>` 换行、`<hr>` 分割线

## 2.4 标签属性
1. 定义：写在**开始标签内部**，用来给标签附加功能、样式、参数
2. 格式：`属性名="属性值"`，值必须用双引号包裹
3. 示例：`<img src="图片地址" alt="图片描述">`
   - src、alt 都是属性

# 三、HTML5 基础文本标签
## 3.1 标题标签 h1~h6
- 作用：页面分级标题，自带加粗、自动换行、上下间距
- 层级：h1（最大，一个页面只能1个，SEO优化）> h2 > h3 > h4 > h5 > h6（最小）
```html
<h1>一级标题（页面主标题）</h1>
<h2>二级标题</h2>
<h3>三级标题</h3>
```

## 3.2 段落标签 `<p>`
- 存放大段文字，段落自动换行，自带上下空白间距
```html
<p>这是第一段文字</p>
<p>这是第二段文字，两段之间自动有空隙</p>
```

## 3.3 换行与分割线
1. `<br>`：强制换行，无间距
2. `<hr>`：水平分割线，页面分割内容

## 3.4 文本格式化标签（文字样式）
| 标签                    | 效果                           |
| ----------------------- | ------------------------------ |
| `<b>文字</b>`           | 文字加粗                       |
| `<strong>文字</strong>` | 语义加粗（推荐，强调重要内容） |
| `<i>文字</i>`           | 文字斜体                       |
| `<em>文字</em>`         | 语义斜体（强调）               |
| `<u>文字</u>`           | 文字下划线                     |
| `<s>文字</s>`           | 文字删除线                     |
| `<sup>上标</sup>`       | 数字上标 例：x<sup>2</sup>     |
| `<sub>下标</sub>`       | 数字下标 例：H<sub>2</sub>O    |

## 3.5 特殊字符（转义字符）
网页中部分符号无法直接输入，需要转义代码
| 符号 | 转义代码 | 用途             |
| ---- | -------- | ---------------- |
| 空格 | `&nbsp;` | 页面多个连续空格 |
| <    | `&lt;`   | 小于号           |
| >    | `&gt;`   | 大于号           |
| &    | `&amp;`  | 和符号           |
| ©    | `&copy;` | 版权符号         |

# 四、HTML5 多媒体标签（HTML5新增核心）
## 4.1 图片标签 `<img>` 单标签
### 核心属性
1. `src`：必填，图片路径（本地图片/网络图片地址）
2. `alt`：必填，图片加载失败时显示的文字，利于无障碍阅读
3. `width`：设置图片宽度（单位px像素）
4. `height`：设置图片高度，只写宽高其中一个，图片自动等比例缩放
5. `title`：鼠标悬浮图片显示提示文字

### 路径两种写法
1. 相对路径（本地文件，推荐）
   - 同文件夹：`src="logo.jpg"`
   - 下级文件夹：`src="img/logo.jpg"`
   - 上级文件夹：`src="../logo.jpg"`
2. 绝对路径（网络图片）
   `src="shturl.cc/Wp7jy35NCpbuB"`

示例：
```html
<img src="cat.jpg" alt="小猫图片" width="300" title="可爱小猫">
```

## 4.2 音频标签 `` HTML5新增
无需插件，直接播放音乐
### 属性
- `src`：音频地址（mp3格式兼容性最好）
- `controls`：显示播放、暂停、音量控件（必须加才能看见按钮）
- `autoplay`：页面打开自动播放（多数浏览器限制）
- `loop`：循环播放
```html
<audio src="music.mp3" controls loop>
```

## 4.3 视频标签 `<video>` HTML5新增
播放本地/网络视频
### 属性
- `src`：视频地址（mp4通用）
- `controls`：播放控制器
- `width/height`：视频尺寸
- `autoplay` 自动播放、`loop` 循环、`muted` 静音自动播放
```html
<video src="movie.mp4" width="600" controls></video>
```

## 4.4 背景音乐兼容写法（多格式适配）
使用 `<source>` 兼容多种音视频格式
```html
<audio controls>
    <source src="music.mp3" type="audio/mpeg">
    <source src="music.ogg" type="audio/ogg">
    您的浏览器不支持音频播放

```

# 五、超链接标签 `<a>`
## 5.1 基础用法
```html
<a href="跳转地址">点击文字/图片</a>
```
### 核心属性
1. `href`：跳转目标地址，必填
   - 外网网址：`href="https://www.baidu.com"`
   - 本地页面：`href="index.html"`
   - 空链接：`href="#"` 点击不跳转，回到页面顶部
2. `target`：打开页面方式
   - `target="_self"` 默认：当前窗口打开
   - `target="_blank"` 新标签页打开（最常用）

## 5.2 锚点链接（页面内跳转）
1. 给目标标签设置 `id` 属性
2. a标签 href="#id名称"
```html
<h2 id="m1">第一节内容</h2>
<a href="#m1">跳转到第一节</a>
```

## 5.3 特殊链接
1. 邮箱链接：`href="mailto:123@qq.com"`
2. 电话链接（手机网页）：`href="tel:13800138000"`
3. 图片作为链接：
```html
<a href="https://baidu.com" target="_blank">
    <img src="logo.jpg" alt="百度">
</a>
```

# 六、列表标签
## 6.1 无序列表 `<ul>` + `<li>`
无数字序号，默认圆点，常用于导航、商品列表
```html
<ul>
    <li>苹果</li>
    <li>香蕉</li>
    <li>橙子</li>
</ul>
```

## 6.2 有序列表 `<ol>` + `<li>`
自带数字序号，用于步骤、排行榜
```html
<ol>
    <li>起床</li>
    <li>刷牙</li>
    <li>吃饭</li>
</ol>
```

## 6.3 自定义列表 `<dl>` + `<dt>` + `<dd>`
用于术语解释、图文介绍
- `<dt>`：标题名词
- `<dd>`：对应描述，自动缩进
```html
<dl>
    <dt>HTML5</dt>
    <dd>搭建网页结构的标记语言</dd>
    <dt>CSS</dt>
    <dd>美化网页样式</dd>
</dl>
```

# 七、表格标签 HTML5
## 7.1 基础表格结构
1. `<table>`：整个表格容器
2. `<tr>` table row：一行
3. `<td>` table data：单元格（普通内容）
4. `<th>` table header：表头单元格，自动加粗居中
```html
<table border="1">
    <!-- border设置边框，方便查看结构 -->
    <tr>
        <th>姓名</th>
        <th>年龄</th>
    </tr>
    <tr>
        <td>小明</td>
        <td>18</td>
    </tr>
</table>
```

## 7.2 表格结构化标签（HTML5语义化）
- `<thead>`：表格头部
- `<tbody>`：表格主体数据（必须存在）
- `<tfoot>`：表格底部汇总

## 7.3 单元格合并
1. 跨列合并 `colspan="数字"`：横向合并单元格
2. 跨行合并 `rowspan="数字"`：纵向合并单元格

# 八、表单标签 HTML5（重点，新增大量表单功能）
表单作用：收集用户输入信息（登录框、注册、搜索框）
## 8.1 基础外层 `<form>`
所有输入框必须包裹在form内，用于提交数据
```html
<form action="提交地址" method="提交方式">
    输入框、按钮写在这里
</form>
```
- action：数据提交到后台接口地址
- method：两种提交方式
  - get：数据拼接在网址，适合少量简单数据
  - post：数据隐藏传输，适合密码、大量内容（推荐）

## 8.2 输入框 `<input>` 单标签，type决定类型
### 传统基础类型
1. `type="text"` 单行文本输入框
2. `type="password"` 密码框，内容隐藏黑点
3. `type="radio"` 单选框，同一组name相同才能互斥
4. `type="checkbox"` 多选框
5. `type="submit"` 提交按钮，自动提交表单
6. `type="reset"` 重置按钮，清空所有输入
7. `type="button"` 普通按钮，无默认功能

### HTML5 新增input类型（核心考点）
1. `type="email"` 邮箱框，浏览器自动校验邮箱格式
2. `type="tel"` 手机号输入框（手机弹出数字键盘）
3. `type="number"` 数字输入框，只能输入数字
4. `type="date"` 日期选择器，弹出日历
5. `type="range"` 滑动条
6. `type="file"` 文件上传按钮
7. `type="search"` 搜索框

### input通用属性
- `name`：必须写，后台接收数据的标识
- `value`：输入框默认文字/默认选中值
- `placeholder`：灰色提示文字，输入内容自动消失
- `checked`：单选/多选框默认选中
- `required`：HTML5新增，设置输入框必填，不填无法提交
- `max/min`：数字、日期最大值最小值

## 8.3 下拉选择框 `<select>` + `<option>`
```html
<select name="city">
    <option value="chengdu">成都</option>
    <option value="chongqing">重庆</option>
</select>
```
- `selected`：默认选中项
- `<select multiple>`：开启多选下拉

## 8.4 多行文本域 `<textarea>`
大段文字输入（评论、简介）
- rows：行数
- cols：列宽
```html
<textarea rows="5" cols="30" placeholder="请输入评论"></textarea>
```

## 8.5 标签 `<label>` 优化点击体验
点击文字自动选中输入框，提升易用性
```html
<label for="user">用户名：</label>
<input type="text" id="user" name="username">
```

# 九、HTML5 语义化标签（HTML5最大更新）
## 9.1 什么是语义化
以前HTML4只用 `<div>` 划分页面，无含义；
HTML5新增自带含义的标签，浏览器、搜索引擎能读懂页面结构，利于SEO、无障碍阅读。

## 9.2 全部语义标签及用途
| 标签           | 作用                             |
| -------------- | -------------------------------- |
| `<header>`     | 页面/区块头部（导航栏、标题区）  |
| `<nav>`        | 导航菜单区域，存放超链接         |
| `<main>`       | 页面唯一主体内容，一个页面仅1个  |
| `<section>`    | 独立内容区块（文章分块、模块）   |
| `<article>`    | 完整独立内容（新闻、帖子、评论） |
| `<aside>`      | 侧边栏（推荐、广告、侧边菜单）   |
| `<footer>`     | 页面底部（版权、联系方式）       |
| `<figure>`     | 包裹图片+图片说明                |
| `<figcaption>` | 图片标题说明，搭配figure使用     |
| `<time>`       | 标记时间日期，机器可识别         |

### 标准语义化页面结构示例
```html
<body>
    <header>页面头部LOGO导航</header>
    <nav>网站导航菜单</nav>
    <main>
        <section>
            <article>文章内容</article>
        </section>
        <aside>侧边推荐栏</aside>
    </main>
    <footer>底部版权信息</footer>
</body>
```

## 9.3 无语义容器标签（仅布局用）
1. `<div>`：块级容器，独占一行，页面大区域划分
2. `<span>`：行内容器，不换行，用于局部文字样式修改

# 十、HTML5 新增高级功能
## 10.1 画布 `<canvas>`
用途：绘制图形、动画、小游戏、图表
- 本身只是空白画布，绘图逻辑需要JavaScript实现
- 属性 width/height 设置画布尺寸
```html
<canvas id="canvas1" width="500" height="300"></canvas>
```

## 10.2 矢量图 `<svg>`
和canvas区别：
- canvas：位图，放大模糊，JS绘制
- svg：矢量图形，放大不失真，标签直接定义图形（圆形、矩形、线条）

## 10.3 本地存储（HTML5 Web Storage）
无需后端数据库，浏览器本地保存数据，两种存储：
1. `localStorage`：永久存储，关闭浏览器数据不消失
2. `sessionStorage`：会话存储，关闭页面数据清空

## 10.4 地理定位 Geolocation API
JS获取用户设备当前地理位置（经纬度），用于地图、同城服务

## 10.5 拖拽API
HTML5原生支持元素拖拽，不用第三方插件

## 10.6 离线缓存 Application Cache
页面无网络时依旧可以打开，适合移动端网页

# 十一、标签分类：块级、行内、行内块
## 11.1 块级元素 block
特点：
1. 独占一整行，自动换行
2. 宽高、内外边距均可设置
代表标签：div、h1~h6、p、ul、ol、li、table、header、section、form

## 11.2 行内元素 inline
特点：
1. 同行显示，不自动换行
2. 宽高无法手动设置，尺寸跟随文字内容
代表标签：span、a、b、em、u、i

## 11.3 行内块元素 inline-block（HTML多媒体/表单常用）
特点：
1. 同行排列，不换行
2. 支持设置宽高、边距
代表标签：img、input、video、audio、button

# 十二、HTML5 全局通用属性（所有标签都能用）
1. `id`：页面唯一标识，用于锚点、JS获取元素，一个页面id不能重复
2. `class`：类名，多个标签可共用同一个class，配合CSS批量改样式
3. `style`：行内样式，直接写CSS样式
4. `title`：鼠标悬浮显示提示文字
5. `hidden`：隐藏标签内容，页面不占位
6. `data-*`：HTML5自定义属性，存放自定义数据，JS读取

# 十三、注释规范
1. HTML注释格式：`<!-- 注释内容 -->`
2. 注释不会在页面显示，仅给开发者看
3. 作用：标记代码分区、临时隐藏代码、说明功能
4. 禁止嵌套注释

# 十四、HTML5 编码规范（零基础必遵守，减少错误）
1. 标签名统一小写，不要大写 `<DIV>` 错误
2. 属性值全部双引号包裹，禁止单引号/无引号
3. 代码缩进：父子标签缩进2个空格，层级清晰
4. 单标签规范书写：`<img src="">`，不用强制写 `/`
5. 语义化标签优先，少用纯div布局
6. 图片必须携带alt属性，利于无障碍与搜索引擎
7. 页面仅存在一个h1标题，优化搜索排名
8. 表单input必须写name属性，否则数据无法提交
9. 移动端页面必须添加viewport适配meta标签

# 十五、HTML4 与 HTML5 核心区别总结
1. 文档声明简化：`<!DOCTYPE html>` 替代复杂HTML4声明
2. 新增语义标签，淘汰纯div布局
3. 原生支持音视频audio/video，无需Flash插件
4. 新增大量表单输入类型与表单校验属性required
5. 新增canvas、svg绘图能力
6. 新增本地存储、地理定位、拖拽、离线缓存Web API
7. 弱化废弃标签：`<font>`、`<center>`、`<b>` 等样式标签，统一交给CSS处理

# 十六、完整综合示例页面（整合全部基础知识点）
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML5综合演示页面</title>
</head>
<body>
    <!-- 页面头部语义标签 -->
    <header>
        <h1>HTML5学习手册</h1>
        <!-- 导航 -->
        <nav>
            <a href="#text">文本模块</a>
            <a href="#media">多媒体模块</a>
            <a href="#form">表单模块</a>
        </nav>
    </header>

    <main>
        <!-- 文本区域 -->
        <section id="text">
            <h2>文本标签演示</h2>
            <p><strong>重要文字</strong>，普通文字，<em>斜体强调</em></p>
            <hr>
            <ul>
                <li>无序列表第一项</li>
                <li>无序列表第二项</li>
            </ul>
        </section>

        <!-- 多媒体区域 -->
        <section id="media">
            <h2>多媒体演示</h2>
            <img src="test.jpg" alt="测试图片" width="200">
            <audio src="test.mp3" controls>
        </section>

        <!-- 表单区域 -->
        <section id="form">
            <h2>HTML5表单</h2>
            <form action="#" method="get">
                <label>邮箱：</label>
                <input type="email" name="email" required placeholder="请输入邮箱">
                <br><br>
                <label>出生日期：</label>
                <input type="date" name="birth">
                <br><br>
                <textarea placeholder="留言内容" rows="4"></textarea>
                <br><br>
                <input type="submit" value="提交">
                <input type="reset" value="重置">
            </form>
        </section>
    </main>

    <!-- 侧边栏 -->
    <aside>
        <h3>侧边栏</h3>
        <p>辅助推荐内容</p>
    </aside>

    <!-- 底部 -->
    <footer>
        <p>&copy;2026 HTML5学习文档</p>
    </footer>
</body>
</html>
```
