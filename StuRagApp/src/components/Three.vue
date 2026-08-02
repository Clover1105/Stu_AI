<!-- 写页面的逻辑（JavaScript / TypeScript） -->
<script setup>
  import {ref} from "vue";

  // 定义控制是否能更改的变量
  let isDisabled = ref(false);
  function changeInput() {
    isDisabled.value = !isDisabled.value;
  }

  // 定义控制 div 显示与隐藏的变量
  let isShow = ref(true);
  let isCode = ref(true);

  // 邮箱号、验证码的变量
  let email = ref("2920242909@qq.com");
  let code = ref("");

  // 发送验证码
  function sendEmail() {
    isCode.value = !isCode.value;
    console.log(email.value); // 输出邮箱号
  }

  // 验证验证码
  function checkCode() {
    // isCode.value = !isCode.value;
    console.log(email.value, code.value);
  }

  // 定义一个数组变量，用户和AI问答
  let messages = ref([
    {role: 'assistant', content: '你好，我是AI，你可以向我提问任何问题。'},
    {role: 'user', content: '你叫什么名字？'},
    {role: 'assistant', content: '我叫ChatGPT，一个基于OpenAI的AI模型。'},
    {role: 'user', content: '你喜欢什么书？'},
    {role: 'assistant', content: '我非常喜欢《哈利波特》系列，以及《1984》和《安徒生童话》。'},
    {role: 'user', content: '你喜欢什么电影？'},
    {role: 'assistant', content: '我非常喜欢《唐顿庄园》'}
  ])

</script>

<!-- 写页面结构（HTML） -->
<template>
  <div>
    <h1> 属性绑定指令和事件绑定指令 </h1>

    <form>
      账号：<input type="text" v-bind:disabled="isDisabled"><br>
      密码：<input type="password"><br>
      <button type="button" @click="changeInput">点我</button>
    </form>

    <h1>控制内容显示与隐藏指令</h1>

    <div v-show="isShow" style="border:1px solid yellow; width: 100%; height: 30px">
      点击前
    </div>
    <div v-show="!isShow" style="border:1px solid green; width: 100%; height: 30px">
      点击后
    </div>
    <button type="button" @click="isShow = !isShow">切换标签</button>

    <h1>双向绑定指令</h1>

    <form>
      邮箱号：<input type="text" v-model="email" :disabled="!isCode"><br>
      验证码：<input type="email" v-model="code" :disabled="isCode"><br>
      <button type="button" v-show="isCode" @click="sendEmail">发送验证码</button>
      <button type="button" v-show="!isCode" @click="checkCode">验证验证码</button>
    </form>

    <h1>循环指令</h1>

    <!-- 表单形式 -->
    <div>
      <table>
        <tr v-for="(item,index) in messages">
          第{{index+1}}行：{{item.content}}
        </tr>
      </table>
    </div>

    <hr>  <!-- 分割线 -->

    <!-- 列表形式 -->
    <div>
      <div v-for="(item,index) in messages">
        第{{index+1}}行：{{item.content}}
      </div>
    </div>


  </div>
</template>

<!-- 写样式（CSS） -->
<style scoped>

</style>