<template>
  <div>
    <form>
      邮箱号：<input type="text" v-model="email" :disabled="!isCode"><br>
      验证码：<input type="text" v-model="code" :disabled="isCode"><br>
      <button type="button" v-show="isCode" @click="sendEmail">发送验证码</button>
      <button type="button" v-show="!isCode" @click="checkCode">验证验证码</button>
    </form>
  </div>

</template>

<script setup>
import {ref, getCurrentInstance} from "vue";

import {useRouter} from "vue-router"; // 导入路由对象
let router = useRouter(); // 创建路由跳转对象

import {ElMessage} from "element-plus"; // 导入弹窗组件

// 定义变量
let email = ref("");
let code = ref("");
let isCode = ref(true);

// 创建当前实例对象 -- 通过这个对象才可以访问到 main.js 中定义的 $axios 变量
let proxy = getCurrentInstance().proxy;
console.log(getCurrentInstance())

// 定义函数
function sendEmail() {  // 发送验证码的函数
  let sendEmail = email.value;  // 获取用户输入的邮箱号
  console.log("发送邮箱：", sendEmail)
  proxy.$axios({  // {}：里面写的就是访问服务器接口的信息，比如请求地址【自动拼接前缀】、请求方式【默认get】、请求参数
    url: 'users/sendEmail', // 请求地址
    method: 'get',  // 请求方式
    params: { // 请求参数
      email: sendEmail  // 参数的key必须和服务器接口的形参一致
    },
  }).then(res => {
    console.log("接收到的数据：", res)
    let code = res.data.code;
    let msg = res.data.msg;
    let data = res.data.data;
    // 逻辑判断处理 --- 【=== ：表示全等（数据类型和值都相等为true） ； == ：表示值相等就为true】
    if (code === 200) {
      isCode.value = !isCode.value;

      // 将用户名存储到sessionStorage中 -- setItem(key,value)、getItem(key)
      sessionStorage.setItem("username", data);

      ElMessage.info(msg);
    } else {
      ElMessage.error(msg);
    }
  })
}

function checkCode() {
  let checkCode = { // 把输入的邮箱号和验证码封装成一个js对象
        email: email.value,
        code: code.value
  }
  proxy.$axios({  // {}：里面写的就是访问服务器接口的信息，比如请求地址【自动拼接前缀】、请求方式【默认get】、请求参数
    url: 'users/checkCode', // 请求地址
    method: 'post',  // 请求方式
    data: JSON.stringify(checkCode) // 请求参数，参数的key必须和服务器接口的形参一致
  }).then(res => {
    console.log("接收到的数据：", res)
    let result = res.data;
    if (result.code === 200) {
      ElMessage.success(result.msg);
      setTimeout(() => {
        router.push("/chat");
      }, 1000)
    } else {
      ElMessage.error(result.msg);
    }
  })
}

</script>

<style scoped>

</style>