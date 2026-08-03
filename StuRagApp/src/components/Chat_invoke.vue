<template>
  <div>
    <div>
      用户名：{{username}}
    </div>
    <div style="border: 3px solid green;height: 250px;width: 99%">
      <div v-for="(item,index) in messages" :kind="index">
        <div v-if="index%2==0">问题：{{item.content}}</div>
        <div v-else>回复：{{item.content}}</div>
      </div>
    </div>
    <div>
      <el-input v-model="question" placeholder="请输入问题："></el-input>
    </div>
    <el-button type="primary" @click="chat">发送</el-button>

  </div>
</template>

<script setup>
import {ref, getCurrentInstance, onMounted} from "vue";

// 创建代理对象
let proxy = getCurrentInstance().proxy;

// 定义接收用户名的变量
let username = ref("");

// 定义接收用户问题的变量
let question = ref("");

// 定义保存聊天消息的对象
let messages = ref([
  {role: "user", content: "你好"},
  {role: "assistant", content: "你好，我是AI助手，你可以向我提问任何问题。"},
  {role: "user", content: "你喜欢什么"},
  {role: "assistant", content: "我喜欢聊天，你可以向我提问任何问题。"}
])

// 聊天函数
function chat() {
  messages.value.push({role: 'user', content: question});
  messages.value.push({role: 'assistant', content: 'AI正在努力的生成回复ing~~~'});
  proxy.$axios({
    url: 'users/chat',
    method: 'get',
    params: {
      question: question.value
    }
  }).then(res => {
      messages.value[messages.value.length - 1].content = res.data.data;
  })
}

// 加载页面后自动执行
onMounted(() => {
  username.value = sessionStorage.getItem("username");
})
</script>

<style scoped>

</style>