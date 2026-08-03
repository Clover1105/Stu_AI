<template>
  <div class="chat-container">
    <div class="history-panel">
      <div class="logo">
        AI Assistant
      </div>
      <button class="new-chat">
        + 新建对话
      </button>
      <div class="history-title">
        历史记录
      </div>
      <div class="history-item">
        RAG知识问答
        <span>今天</span>
      </div>
      <div class="history-item">
        LangChain学习
        <span>昨天</span>
      </div>
      <div class="history-item">
        项目开发记录
        <span>7月30日</span>
      </div>
    </div>
    <div class="chat-panel">
      <div class="header">
        <div>
          AI智能助手
        </div>
        <div class="username">
          {{username}}
        </div>
      </div>
      <div class="message-box">
        <div v-for="(item,index) in messages" :key="index" class="message-item" :class="item.role==='user'?'user':'assistant'">
          <div class="avatar">
            {{item.role==='user'?'我':'AI'}}
          </div>
          <div class="message-content">
            {{item.content}}
          </div>
        </div>
      </div>
      <div class="input-box">
        <el-input v-model="question" placeholder="输入你的问题..." size="large" @keyup.enter="chat"></el-input>
        <el-button type="primary" size="large" @click="chat" :disabled="isloading">
          发送
        </el-button>
      </div>
    </div>
  </div>
</template>

<script setup>
import {ref, getCurrentInstance, onMounted} from "vue";
import {ElMessage} from "element-plus";

let proxy = getCurrentInstance().proxy;

let username = ref("");

let question = ref("");

let messages = ref([])

let isloading = ref(false);

function chat() {
  isloading.value = true;
  let myQuestion = question.value.trim();
  question.value = "";
  if (myQuestion.length === 0) {
    ElMessage.warning("请输入有效内容");
    return;
  }
  messages.value.push({role: 'user', content: myQuestion});
  messages.value.push({role: 'assistant', content: '思考中，请耐心等待^3^......'});
  let urlSerchParams = new URLSearchParams({
    question: myQuestion,
  });
  let es = new EventSource("http://localhost:8000/chat/chat?"+urlSerchParams.toString());
  let s = "";
  es.onmessage = (e) => {
    let data = JSON.parse(e.data).count;
    if (data === "end_end"){
      es.close();
      isloading.value = false;
      return;
    }
    s += data;
    messages.value[messages.value.length - 1].content = s;
  };
  es.onerror = (e) => {
    console.log("SSE获取数据失败",e);
    es.close();
  };
  es.onopen = () => {
    console.log("SSE连接成功");
  }
}

onMounted(() => {
  username.value = sessionStorage.getItem("username");
})
</script>

<style scoped>
.chat-container{
  height:100vh;
  width:100%;
  display:flex;
  background:#f7f8fa;
}
.history-panel{
  width:280px;
  background:#111827;
  color:white;
  padding:20px;
}
.logo{
  font-size:22px;
  font-weight:bold;
  margin-bottom:25px;
}
.new-chat{
  width:100%;
  height:45px;
  border:none;
  border-radius:10px;
  background:#2563eb;
  color:white;
  font-size:15px;
  cursor:pointer;
  margin-bottom:30px;
}
.history-title{
  color:#9ca3af;
  font-size:14px;
  margin-bottom:15px;
}
.history-item{
  padding:14px;
  border-radius:10px;
  background:#1f2937;
  margin-bottom:12px;
  cursor:pointer;
}
.history-item:hover{
  background:#374151;
}
.history-item span{
  display:block;
  color:#9ca3af;
  font-size:12px;
  margin-top:8px;
}
.chat-panel{
  flex:1;
  display:flex;
  flex-direction:column;
}
.header{
  height:65px;
  background:white;
  border-bottom:1px solid #eee;
  display:flex;
  align-items:center;
  justify-content:space-between;
  padding:0 35px;
  font-size:20px;
  font-weight:bold;
}
.username{
  font-size:14px;
  color:#666;
}
.message-box{
  flex:1;
  padding:30px;
  overflow-y:auto;
}
.message-item{
  display:flex;
  margin-bottom:25px;
  align-items:flex-start;
}
.avatar{
  width:42px;
  height:42px;
  border-radius:50%;
  display:flex;
  justify-content:center;
  align-items:center;
  color:white;
  font-size:14px;
  flex-shrink:0;
}
.message-content{
  max-width:65%;
  padding:15px 20px;
  margin-left:15px;
  border-radius:15px;
  line-height:1.7;
  font-size:16px;
}
.user{
  justify-content:flex-end;
}
.user .avatar{
  order:2;
  margin-left:15px;
  background:#2563eb;
}
.user .message-content{
  background:#2563eb;
  color:white;
  margin-left:0;
}
.assistant .avatar{
  background:#22c55e;
}
.assistant .message-content{
  background:white;
  box-shadow:0 3px 15px rgba(0,0,0,.08);
}
.input-box{
  background:white;
  padding:20px 30px;
  display:flex;
  gap:15px;
  border-top:1px solid #eee;
}
.input-box .el-input{
  flex:1;
}
</style>