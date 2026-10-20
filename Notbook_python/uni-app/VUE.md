# 一、核心认知

在学习具体语法前，请先记住这三个要点，它们是理解 `uni-app` 的基石。

1. **`uni-app` 使用的是 `.vue` 文件**，而不是 `.html` 文件。每一个页面都由一个 `.vue` 文件构成。
2. **`uni-app` 的语法遵循 Vue.js 规范**，你需要学习 Vue 的模板语法、数据绑定、事件处理等核心概念。
3. **`uni-app` 的标签和 API 更接近微信小程序**，而不是传统的 HTML。比如，用 `<view>` 替代 `<div>`，用 `uni.request` 替代 `axios` 或 `fetch`。

学习网址：

[HTML 教程 | 菜鸟教程](https://www.runoob.com/html/html-tutorial.html)

[CSS 教程 | 菜鸟教程](https://www.runoob.com/css/css-tutorial.html)

[JavaScript 教程 | 菜鸟教程](https://www.runoob.com/js/js-tutorial.html)

[Vue3 教程 | 菜鸟教程](https://www.runoob.com/vue3/vue3-tutorial.html)

[简介 | Vue[简介 | Vue.js](https://cn.vuejs.org/guide/introduction)

## 什么是`Vue`

Vue (发音为 /vjuː/，类似 **view**) 是一款用于构建用户界面的 JavaScript 框架。它基于标准 ==HTML、CSS 和 JavaScript== 构建，并提供了一套声明式的、组件化的编程模型，帮助你高效地开发用户界面。无论是简单还是复杂的界面，Vue 都可以胜任。

# 二、`.vue` 文件的结构（第一个页面）

一个 `.vue` 文件由三部分组成，这三部分共同定义了一个页面或组件。这个结构和标准 Vue 单文件组件完全一致

```vue
<template>
  <!-- 1. 模板部分：负责定义界面的结构和布局 -->
  <!-- 这里使用 uni-app 的组件标签，如 view, text 等 -->
  <view>
    <text>{{ message }}</text>
  </view>
</template>

<script>
  // 2. 脚本部分：负责定义数据、业务逻辑、生命周期等
  // 这里使用 Vue 的语法
  export default {
    data() {
      return {
        message: 'Hello uni-app!'
      }
    },
    onLoad() {
      // 页面加载时的生命周期函数
      console.log('页面加载了');
    },
    methods: {
      // 自定义方法
    }
  }
</script>

<style>
  /* 3. 样式部分：负责定义页面的样式 */
  /* 支持常见的 CSS 语法 */
  view {
    background-color: #f0f0f0;
  }
</style>
```

# 三、模板语法（写界面）

在 `<template>` 中，你需要掌握两个要点：**用什么标签** 和 **如何绑定数据**

## 1. 核心组件标签：告别 `div` 和 `span`

在 `uni-app` 中，我们会使用一套内置的、能跨平台运行的组件来搭建界面。

| 你的用途   | 在 HTML 里用            | 在 `uni-app` 里用       |
| :--------- | :---------------------- | :---------------------- |
| **容器**   | `<div>`, `<section>`    | `<view>`                |
| **文本**   | `<span>`, `<p>`, `<h1>` | `<text>`                |
| **图片**   | `<img>`                 | `<image>`               |
| **输入框** | `<input>`, `<textarea>` | `<input>`, `<textarea>` |
| **按钮**   | `<button>`              | `<button>`              |

**示例：** 一个简单页面的模板部分。

```vue
<template>
  <view>
    <text>我的第一个页面</text>
    <image src="/static/logo.png"></image>
    <input placeholder="请输入内容" />
    <button type="primary">点击我</button>
  </view>
</template>
```

## 2. 数据绑定与指令

这部分是 Vue 的核心。你的数据定义在 `<script>` 的 `data` 函数中，然后通过特定的“指令”绑定到模板上。

### **文本插值 **

**`{{ }}`**：在 `text` 组件中显示数据。

```vue
<template>
  <text>{{ userName }}</text>
</template>
<script>
export default {
  data() {
    return {
      userName: '张三'
    }
  }
}
</script>
```

### **属性绑定 **

**`v-bind` (缩写为 `:` )**：动态设置组件的属性。

```vue
<template>
  <!-- 动态绑定 image 的 src 属性 -->
  <image :src="imageUrl"></image>
  <!-- 动态绑定按钮的禁用状态 -->
  <button :disabled="isDisabled">按钮</button>
</template>
<script>
export default {
  data() {
    return {
      imageUrl: '/static/avatar.png',
      isDisabled: true
    }
  }
}
</script>
```

### **事件绑定**

**`v-on` (缩写为 `@` )**：监听用户操作。

```vue
<template>
  <button @click="handleClick">点我</button>
</template>
<script>
export default {
  methods: {
    handleClick() {
      console.log('按钮被点击了！');
    }
  }
}
</script>
```

### **双向数据绑定**

**`v-model`**：常用于输入框，实现数据与界面的实时同步。

```vue
<template>
  <view>
    <!-- 输入框内容变化时，inputValue 会自动更新 -->
    <input v-model="inputValue" placeholder="输入文字" />
    <text>你输入的是：{{ inputValue }}</text>
  </view>
</template>
<script>
export default {
  data() {
    return {
      inputValue: ''
    }
  }
}
</script>
```

### **条件渲染**

**`v-if` / `v-show`**：根据条件决定是否显示元素。

```vue
<template>
  <view>
    <button @click="toggleLogin">切换登录状态</button>
    <!-- 当 isLoggedIn 为 true 时显示 -->
    <view v-if="isLoggedIn">
      <text>已登录，欢迎回来！</text>
    </view>
    <!-- 当 isLoggedIn 为 false 时显示 -->
    <view v-else>
      <text>请先登录</text>
    </view>
  </view>
</template>
<script>
export default {
  data() {
    return {
      isLoggedIn: false
    }
  },
  methods: {
    toggleLogin() {
      this.isLoggedIn = !this.isLoggedIn;
    }
  }
}
</script>
```

### **列表渲染 **

**`v-for`**：根据数组循环生成一组元素。必须提供 `:key` 以优化性能。

```vue
<template>
  <!-- items 是数组，item 是当前项，index 是索引 -->
  <view v-for="(item, index) in items" :key="index">
    <text>{{ index }} - {{ item.name }}</text>
  </view>
</template>
<script>
export default {
  data() {
    return {
      items: [
        { name: '苹果' },
        { name: '香蕉' },
        { name: '橙子' }
      ]
    }
  }
}
</script>
```

# 四、JavaScript 与 API（写逻辑）

在 `<script>` 中，除了遵循 Vue 的语法（如 `data`, `methods`, `生命周期`），你还会频繁调用 uni-app 提供的 API。

## 1. 页面生命周期

uni-app 的页面和 Vue 的生命周期略有不同，有一些专属于页面的生命周期函数。

```vue
<script>
export default {
  onLoad(options) {
    // 页面加载时触发，options 是页面跳转时携带的参数
    console.log('页面加载', options);
  },
  onShow() {
    // 页面显示时触发（每次进入页面都会触发）
    console.log('页面显示');
  },
  onReady() {
    // 页面初次渲染完成时触发
    console.log('页面初次渲染完成');
  },
  onHide() {
    // 页面隐藏时触发（如跳转到其他页面）
    console.log('页面隐藏');
  },
  onUnload() {
    // 页面卸载时触发
    console.log('页面卸载');
  }
}
</script>
```

## 2. 常用 API 一览

uni-app 将所有能力都挂载到 `uni` 对象上，调用方式非常统一。

### **网络请求**

**`uni.request`**：用于从服务器获取或发送数据。

```javascript
uni.request({
  url: 'https://api.example.com/data', // 接口地址
  method: 'GET',
  success: (res) => {
    // 请求成功时的回调
    console.log(res.data);
  },
  fail: (err) => {
    // 请求失败时的回调
    console.error(err);
  }
});
```

### **数据缓存**

**`uni.setStorageSync` / `uni.getStorageSync`**：在本地存储数据，类似于浏览器的 `localStorage`。

```javascript
// 存储数据（同步方式）
uni.setStorageSync('userInfo', { name: '李四' });

// 读取数据（同步方式）
const userInfo = uni.getStorageSync('userInfo');
console.log(userInfo.name); // 输出: 李四
```

### **页面跳转 **

**`uni.navigateTo` / `uni.switchTab`**：

- `uni.navigateTo`：保留当前页面，跳转到应用内的某个页面（可返回）。
- `uni.switchTab`：跳转到 `tabBar` 页面（底部导航），并关闭其他所有非 tabBar 页面。

```javascript
// 跳转到详情页，并传递参数 id
uni.navigateTo({
  url: '/pages/detail/detail?id=123'
});
```

# 五、样式编写（写样式）

在 `<style>` 中，你可以书写标准的 CSS，uni-app 基本支持所有常见的 CSS 选择器和属性。

- **支持 `rpx`**：`rpx`（responsive pixel）是 uni-app 中独有的尺寸单位，可以根据屏幕宽度自适应，是移动端开发的利器。**设计稿通常以 750px 宽度为标准，在 uni-app 中，`1rpx` 等于设计稿上的 `1px`。**
- **支持 `@import`**：可以引入外部样式文件。
- **支持 `scoped`**：在 `<style>` 标签上添加 `scoped` 属性，可以使样式仅作用于当前页面，避免全局污染。

```vue
<style scoped>
/* 使用 rpx 单位 */
.container {
  padding: 20rpx;
  background-color: #ffffff;
}

.title {
  font-size: 36rpx;
  color: #333333;
  margin-top: 20rpx;
}

/* 支持 Flexbox 布局 */
.flex-row {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
</style>
```

# 六、总结：学习路径建议

1. **搭建环境**：下载并安装 **HBuilderX**。通过 `文件 -> 新建 -> 项目` 选择 `uni-app` 模板，创建一个项目。
2. **掌握 Vue 基础**：确保理解 `data`、`methods`、`v-bind`、`v-on`、`v-if` 和 `v-for` 这几个最常用的概念。
3. **熟悉 uni-app 组件和 API**：多翻看官方文档，知道 `view`、`text`、`image` 组件，以及 `uni.request` 和 `uni.navigateTo` 等常用 API 的用法。
4. **动手实践**：尝试做一个简单的 Todo List 应用，把上面学到的 `v-model`、`v-for`、`点击事件` 和 `数据缓存` 都用上。在实践中发现问题、解决问题是最高效的学习方式。

# 七、`uni-app`项目结构介绍

```
旅游助手
│
├─ pages
│  ├─ index
│  │  └─ index.vue
│  └─ 新建页面
│
├─ static
├─ unpackage
│
├─ .editorconfig
├─ .gitignore
├─ App.vue
├─ index.html
├─ main.js
├─ manifest.json
├─ pages.json
├─ uni.promisify.adaptor.js
└─ uni.scss
```

这是一个典型的 `uni-app` 工程目录。官方定义中，`pages` 存放页面，`static` 存放静态资源，`App.vue` 是应用入口组件，`main.js` 是 Vue 初始化入口，`pages.json` 管理页面路由，`manifest.json` 管理应用配置。

## （一）项目根目录：旅游助手

旅游助手：这个就是你的项目名称。它代表整个 uni-app 工程。

里面所有代码最终会被编译成：

- 微信小程序
- H5网页
- Android App
- iOS App

等多个平台。

`uni-app `最大特点就是：写一套 Vue 代码，多端运行。

## （二）pages 页面目录（最重要）

路径：pages/

作用：存放项目中的所有页面。

官方规定：所有页面都必须放在 pages 目录中，并且需要在 `pages.json` 注册，否则无法运行。

uni-app规定：一个页面 = 一个目录 + 一个.vue文件

要在配置文件`pages.json`中一一对应：`"path":"pages/index/index"`

### 1. pages/index/index.vue

`index.vue`：这是你的首页。

路径：`pages/index/index.vue`

`uni-app` 默认首页。打开 App 后第一个显示的页面。

启动流程：打开APP\==>pages.json\==>第一项（启动页）\==>pages/index/index.vue

代码结构：

```vue
<template>

页面结构

</template>


<script>

页面逻辑

</script>


<style>

页面样式

</style>
```

例如：

```vue
<template>
  <view>
     旅游助手首页
  </view>
</template>
```

这里的 view，类似HTML里面的 `<div></div>`，但是 `uni-app` 推荐使用：view、image、text、utton 这些跨端组件。

## （三）static 静态资源

路径：static/

作用：存放静态资源。

```vue
<image src="/static/images/beijing.jpg">
</image>
```

注意：uni-app规定，静态资源一般放这里。（图片、图标、字体、音频、视频）

## （四）unpackage 编译生成目录

路径：unpackage/

作用：编译生成目录。

`unpackage/dist/cache/.vite/deps`：它不是源码，是编译产生的临时文件。

点击运行 → 运行到浏览器：.vue文件 → 编译 → 生成 → unpackage

所以该文件夹中的内容一般不要手动修改，但是可以删除，重新运行会再次生成。它类似于vue：dist目录

## （五）.editorconfig 编辑器规范

作用：编辑器配置。

控制：代码格式（缩进、编码等）

作用：保证团队开发时，大家的代码格式一致

## （六）.gitignore Git忽略配置

Git配置文件。

作用：告诉 Git 哪些文件不要上传，因为这些文件太大。

提交代码：忽略。

## （七）App.vue 应用根组件（项目总入口）

路径：App.vue

作用：整个应用的根组件，可以理解为整个 APP 的外壳

执行顺序：main.js → App.vue → pages页面

主要负责：

1. APP生命周期
2. 全局样式

## （八）main.js（启动文件）

`import App from './App'`：引入App.vue

项目 Vue3 因为 `"vueVersion":"3"`，所以真正运行 `createSSRApp(App)`

流程：main.js → 创建Vue实例 → 挂载App → 显示页面

## （九）pages.json（路由核心）

目前最重要的配置文件

`"pages":[]` —— 里面记录所有页面

例如：（首页）`"path":"pages/index/index"`

pages数组顺序非常重要，谁在第一个谁就是首页，也就是打开APP后的第一个进入的页面

## （十）manifest.json（APP身份证）

`"name":"旅游助手"` —— APP名称。

`appid`：`"appid":"__UNI__358D1BF"`，DCloud分配的唯一ID，发布APP、小程序需要

`version`：`"versionName":"1.0.0"`、`"versionCode":"100"`，表示版本

vue版本：`"vueVersion":"3"`说明该项目为Vue3

## （十一）index.html

标准H5入口

```html
<div id="app"></div>

<script type="module" src="/main.js">
</script>
```

意思是：加载main.js，启动Vue应用

注意，如果开发微信小程序基本不用关注

## （十二）uni.promisify.adaptor.js

```javascript
uni.addInterceptor({
 returnValue(res){

 }
})
```

作用：处理Promise返回，一般不修改

## （十三）uni.scss

作用：全局样式变量

例如 uni官方 ：`$uni-color-primary`

## （十四）项目真实运行关系

```
index.html
    |
    |
 main.js
    |
    |
 App.vue
    |
    |
 pages.json
    |
    |
 pages/index/index.vue
    |
    |
 页面显示
```

# 八、标签

## 1. template

是 **Vue 的容器标签**，用于包裹多个元素，但**不会渲染为真实的 DOM 节点**

### 核心特点

| 特点           | 说明                                       |
| :------------- | :----------------------------------------- |
| **不渲染**     | 最终生成的 HTML 中不会有 `<template>` 标签 |
| **无样式影响** | 不能添加 `class` 或 `style`                |
| **逻辑分组**   | 配合 `v-if`、`v-for`、`v-show` 使用        |

### 常用场景

```html
<!-- ✅ 配合 v-if 包裹多个元素 -->
<template v-if="isLogin">
  <text>欢迎回来</text>
  <text>用户名：张三</text>
  <button>退出</button>
</template>

<!-- ✅ 配合 v-for 渲染多个元素 -->
<template v-for="item in list" :key="item.id">
  <text>{{ item.name }}</text>
  <text>{{ item.price }}</text>
</template>

<!-- ❌ 不能添加 class/style，不会生效 -->
<template class="wrapper">  <!-- 无效 -->
  <text>内容</text>
</template>
```

### 与 block 的区别

在 uni-app 中，`template` 和 `block` 都可以作为无渲染容器：

| 对比     | `<template>` | `<block>`                |
| :------- | :----------- | :----------------------- |
| Vue 标准 | ✅ 是         | ❌ 不是（`uni-app` 特有） |
| 是否渲染 | 不渲染       | 不渲染                   |
| 跨平台   | Vue 通用     | 小程序兼容性更好         |

## 2. swiper

### 作用

是 **`uni-app`** 中内置的**轮播图容器组件**，用于实现图片或内容的滑动切换效果

就是 **`uni-app` 的轮播图组件**，配合 `swiper-item` 使用，支持自动播放、指示点、循环滑动等常见功能，是开发首页 Banner、广告位等场景的必备组件

### 基本结构

```html
<swiper>
  <swiper-item>
    <image src="图片地址"></image>
  </swiper-item>
  <swiper-item>
    <image src="图片地址"></image>
  </swiper-item>
  <swiper-item>
    <image src="图片地址"></image>
  </swiper-item>
</swiper>
```

### 核心属性

| 属性             | 类型    | 默认值 | 作用                             |
| :--------------- | :------ | :----- | :------------------------------- |
| `indicator-dots` | Boolean | false  | 是否显示面板指示点（底部小圆点） |
| `autoplay`       | Boolean | false  | 是否自动播放                     |
| `interval`       | Number  | 5000   | 自动切换时间间隔（毫秒）         |
| `duration`       | Number  | 500    | 滑动动画时长（毫秒）             |
| `circular`       | Boolean | false  | 是否采用衔接滑动（无限循环）     |
| `current`        | Number  | 0      | 当前所在滑块的索引               |
| `vertical`       | Boolean | false  | 滑动方向是否为纵向               |

### 常用事件

| 事件               | 触发时机           |
| :----------------- | :----------------- |
| `@change`          | 当前滑块改变时触发 |
| `@transition`      | 滑动过程中触发     |
| `@animationfinish` | 动画结束时触发     |

### 注意事项

| 要点                           | 说明                                                     |
| :----------------------------- | :------------------------------------------------------- |
| **必须设置高度**               | `swiper` 需要明确的高度，否则内容可能不显示              |
| **`swiper-item` 是唯一子元素** | `swiper` 下只能放 `swiper-item`，不能直接放其他标签      |
| **图片模式**                   | 建议给 `image` 设置 `mode="aspectFill"` 保证图片比例协调 |
| **循环播放**                   | 配合 `circular="true"` 实现无限轮播效果                  |

## 3. view

是 `uni-app` 的**视图容器组件**，相当于 HTML 的 `<div>`，是最基础的**块级元素**

### 核心特点

| 特点               | 说明                       |
| :----------------- | :------------------------- |
| **块级元素**       | 占满一行，可设置宽高       |
| **渲染为真实节点** | 最终会渲染为 DOM 元素      |
| **可添加样式**     | 支持 class、style          |
| **可绑定事件**     | 支持 click、tap 等交互事件 |

### 常用属性

| 属性                     | 类型    | 说明                 |
| :----------------------- | :------ | :------------------- |
| `hover-class`            | String  | 按下时的样式类       |
| `hover-stop-propagation` | Boolean | 是否阻止冒泡         |
| `hover-start-time`       | Number  | 按下后多久出现点击态 |
| `hover-stay-time`        | Number  | 松开后多久消失       |

### 常用场景

```html
<!-- ✅ 基础布局 -->
<view class="container">
  <view class="header">标题</view>
  <view class="content">内容</view>
</view>

<!-- ✅ 添加点击事件 -->
<view @click="handleClick" hover-class="active">
  点击我
</view>

<!-- ✅ 样式控制 -->
<view class="card" style="color: red;">
  卡片内容
</view>
```

```css
.container {
  display: flex;
  flex-direction: column;
  padding: 20px;
}

.card {
  background: #fff;
  border-radius: 12px;
  padding: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.active {
  background: #f0f0f0;
}
```

## 4. image

### 作用

是 **`uni-app`** 中用于**显示图片**的基础组件，相当于 HTML 中的 `img` 标签，但功能更强大

是 `uni-app` 的**图片显示组件**，核心优势是内置了 `mode` 属性，无需额外 CSS 即可实现图片的缩放和裁剪适配，配合懒加载和错误处理，能很好地应对多端开发中的图片展示需求。

### 基本用法

```html
<image src="图片地址"></image>
```

### 核心属性

| 属性                     | 类型    | 默认值        | 作用                                   |
| :----------------------- | :------ | :------------ | :------------------------------------- |
| `src`                    | String  | —             | 图片资源地址（网络、本地、base64）     |
| `mode`                   | String  | `scaleToFill` | 图片裁剪、缩放模式（**最常用**）       |
| `lazy-load`              | Boolean | false         | 是否开启懒加载（滚动到可视区域才加载） |
| `fade-show`              | Boolean | true          | 图片加载时是否显示渐入动画             |
| `webp`                   | Boolean | false         | 是否使用 `WebP` 格式（仅网络图片生效） |
| `show-menu-by-longpress` | Boolean | false         | 长按是否显示菜单（保存/扫码等）        |
| `draggable`              | Boolean | true          | 是否允许拖动（H5 平台）                |

#### mode（重点）

决定图片如何适应容器，有 14 种取值：

**缩放模式**

| 值            | 效果                                 |
| :------------ | :----------------------------------- |
| `scaleToFill` | **默认**。不保持比例，拉伸填满容器   |
| `aspectFit`   | 保持比例，完整显示图片（可能有空白） |
| `aspectFill`  | 保持比例，填满容器（可能裁切）       |
| `widthFix`    | 宽度固定，高度自适应（**最常用**）   |
| `heightFix`   | 高度固定，宽度自适应                 |

**裁剪模式（配合 `widthFix`/`heightFix` 使用）**

| 值             | 效果                     |
| :------------- | :----------------------- |
| `top`          | 裁剪顶部区域             |
| `bottom`       | 裁剪底部区域             |
| `center`       | 裁剪居中区域（**常用**） |
| `left`         | 裁剪左侧区域             |
| `right`        | 裁剪右侧区域             |
| `top left`     | 裁剪左上角               |
| `top right`    | 裁剪右上角               |
| `bottom left`  | 裁剪左下角               |
| `bottom right` | 裁剪右下角               |

```html
<!-- ✅ 宽度固定，高度自适应（Banner 常用） -->
<image src="..." mode="widthFix"></image>

<!-- ✅ 覆盖容器，居中裁剪（头像/封面图常用） -->
<image src="..." mode="aspectFill"></image>

<!-- ✅ 完整显示，不裁剪（商品图常用） -->
<image src="..." mode="aspectFit"></image>
```

### 注意事项

| 要点             | 说明                                                   |
| :--------------- | :----------------------------------------------------- |
| **必须设置宽高** | `image` 默认 `width: 320px; height: 240px`，需手动设置 |
| **底部间隙**     | 默认是行内元素，建议加 `display: block` 消除间隙       |
| **网络图片**     | 需配置图片域名到白名单（小程序）                       |
| **占位图**       | 建议配合 `@error` 事件显示默认图                       |
| **大图优化**     | 使用 `lazy-load` 和 `WebP` 提升性能                    |

### 与 HTML中 `img` 的区别

| 对比     | HTML `<img>` | `uni-app` `<image>`      |
| :------- | :----------- | :----------------------- |
| 标签名   | `img`        | `image`                  |
| 自适应   | 需 CSS 配合  | 内置 `mode` 属性         |
| 懒加载   | 需手动实现   | 内置 `lazy-load`         |
| 长按菜单 | 不支持       | `show-menu-by-longpress` |
| 跨平台   | 仅 Web       | 支持小程序/App/H5        |

## 5. style

在 `uni-app/Vue` 中用于**定义组件的样式**，相当于 HTML 中的 `<style>` 标签，但增加了 **scoped** 等特性

### 基本用法

```html
<style>
  /* 全局样式 */
  .title {
    color: red;
    font-size: 20px;
  }
</style>
```

### 核心属性

| 属性     | 说明                                      |
| :------- | :---------------------------------------- |
| `scoped` | 样式仅作用于当前组件，不污染全局          |
| `lang`   | 指定预处理器，如 `scss`、`less`、`stylus` |

#### scoped（最重要）

作用：让样式**只对当前组件生效**，不会影响其他页面或组件

```html
<style scoped>
  .title {
    color: red;  /* 只在当前组件中生效 */
  }
</style>
```

原理：Vue 会自动给元素添加唯一的 `data-v-xxx` 属性，然后通过属性选择器限制样式范围

```html
<!-- 编译前 -->
<div class="title">标题</div>

<!-- 编译后 -->
<div class="title" data-v-7ba5bd90>标题</div>
```

```css
/* 编译后自动变成 */
.title[data-v-7ba5bd90] {
  color: red;
}
```

### 注意事项

| 要点                    | 说明                                                         |
| :---------------------- | :----------------------------------------------------------- |
| **根节点**              | `template` 中只能有一个根节点，但 `style` 没有此限制         |
| **scoped 不影响子组件** | 父组件 `scoped` 样式不会渗透到子组件内部（除非用 `:deep`）   |
| **全局样式**            | 不加 `scoped` 就是全局样式，影响所有页面                     |
| **优先级**              | 不加 `scoped` > 加 `scoped`，样式权重更高                    |
| **多个 style**          | 一个组件可以写多个 `<style>` 标签（部分场景用于区分 scoped 和全局） |

### 全局样式 vs 局部样式

```html
<!-- 局部样式：仅当前组件 -->
<style scoped>
  .title { color: red; }
</style>

<!-- 全局样式：影响所有页面/组件 -->
<style>
  .title { color: blue; }
</style>
```

