<template>
    <div class="chat-container">
        <!-- 左侧历史记录栏 -->
        <aside class="sidebar">
            <div class="sidebar-header">
                <div class="sidebar-logo">
                    <el-icon :size="22"><ChatDotRound /></el-icon>
                    <span class="sidebar-title">Clover</span>
                </div>
                <el-button class="new-chat-btn" type="primary" size="small" round @click="newChat">
                    <el-icon :size="16"><Plus /></el-icon>
                    <span>新对话</span>
                </el-button>
            </div>

            <div class="sidebar-search">
                <el-input
                    v-model="searchKeyword"
                    placeholder="搜索历史记录..."
                    :prefix-icon="Search"
                    size="small"
                    clearable
                    @keyup.enter="searchHistory"
                />
            </div>

            <div class="history-list">
                <div
                    v-for="(item, index) in historyList"
                    :key="index"
                    class="history-item"
                    :class="{ active: item.active }"
                    @click="conversationLog(item.historyId)"
                >
                    <el-icon :size="16" class="history-icon"><ChatLineSquare /></el-icon>
                    <div class="history-content">
                        <span class="history-title">{{ item.title }}</span>
                        <span class="history-time">{{ item.time }}</span>
                    </div>
                    <!-- 更多操作：删除等 -->
<!--                    <el-icon :size="14" class="history-more" @click.stop><MoreFilled /></el-icon>-->
                  <el-popconfirm title="Are you sure to delete this?" @confirm="confirmEvent(item.historyId)" @cancel="cancelEvent">
                    <template #reference>
                      <el-button class="history-more" @click.stop>Delete</el-button>
                    </template>
                  </el-popconfirm>
                </div>
            </div>

            <div class="sidebar-footer">
                <div class="user-info">
                    <el-avatar :size="32" class="user-avatar">{{ username.charAt(0).toUpperCase() }}</el-avatar>
                    <span class="user-name">{{ username }}</span>
                </div>
            </div>
        </aside>

        <!-- 右侧主聊天区域 -->
        <main class="main-area">
            <!-- 顶部标题栏 -->
            <header class="chat-header">
                <div class="header-left">
                    <el-icon :size="20" class="header-icon"><ChatDotRound /></el-icon>
                    <span class="header-title">对话中...</span>
                </div>
                <div class="header-right">
                    <el-tooltip content="清空对话" placement="bottom">
                        <el-button class="header-btn" :icon="Delete" circle size="small" />
                    </el-tooltip>
                </div>
            </header>

            <!-- 消息显示区域 -->
            <div class="message-area" ref="messageAreaRef">
                <div v-if="messages.length === 0" class="empty-state">
                    <div class="empty-icon">
                        <el-icon :size="64"><ChatDotRound /></el-icon>
                    </div>
                    <h2 class="empty-title">你好，{{ username }}</h2>
                    <p class="empty-desc">有什么我可以帮助你的吗？</p>
                    <div class="quick-prompts">
                        <div
                            v-for="(prompt, idx) in quickPrompts"
                            :key="idx"
                            class="prompt-chip"
                            @click="question = prompt.text"
                        >
                            <el-icon :size="14"><Sunny /></el-icon>
                            <span>{{ prompt.text }}</span>
                        </div>
                    </div>
                </div>

                <div
                    v-for="(item, index) in messages"
                    :key="index"
                    class="message-item"
                    :class="item.role"
                >
                    <div class="message-avatar">
                        <el-avatar :size="36" v-if="item.role === 'user'">
                            {{ username.charAt(0).toUpperCase() }}
                        </el-avatar>
                        <el-avatar :size="36" v-else :src="assistantAvatar" class="ai-avatar">
                            AI
                        </el-avatar>
                    </div>
                    <div class="message-body">
                        <div class="message-role-name">
                            {{ item.role === 'user' ? username : 'Clover' }}
                        </div>
                        <div class="message-bubble">
                            <div class="message-content">{{ item.content }}</div>
                        </div>
                    </div>
                </div>

<!--                <div v-if="isLoading" class="message-item assistant">-->
<!--                    <div class="message-avatar">-->
<!--                        <el-avatar :size="36" class="ai-avatar">AI</el-avatar>-->
<!--                    </div>-->
<!--                    <div class="message-body">-->
<!--                        <div class="message-role-name">AI 助手</div>-->
<!--                        <div class="message-bubble typing-bubble">-->
<!--                            <span class="typing-dot"></span>-->
<!--                            <span class="typing-dot"></span>-->
<!--                            <span class="typing-dot"></span>-->
<!--                        </div>-->
<!--                    </div>-->
<!--                </div>-->
            </div>

            <!-- 底部输入区域 -->
            <footer class="input-area">
                <div class="input-wrapper">
                    <el-input
                        v-model="question"
                        placeholder="输入你的问题，按 Enter 发送..."
                        class="chat-input"
                        size="large"
                        :disabled="isLoading"
                        @keyup.enter="chat"
                    >     <!-- @keyup.enter="chat"   按下Enter键时触发 -->
                        <template #suffix>
                            <el-button
                                type="primary"
                                :icon="Promotion"
                                circle
                                size="small"
                                :disabled="isLoading || !question.trim()"
                                @click="chat"
                                class="send-btn"
                            />  <!-- @click="chat"   点击按钮时触发 -->
                        </template>
                    </el-input>
                    <p class="input-hint">AI 回答仅供参考，请核实重要信息</p>
                </div>
            </footer>
        </main>
    </div>
</template>

<script setup>
import {ref, getCurrentInstance, onMounted} from "vue";
import {ElMessage} from "element-plus";
import {
    ChatDotRound,
    ChatLineSquare,
    Delete,
    MoreFilled,
    Plus,
    Promotion,
    Search,
    Sunny
} from "@element-plus/icons-vue";

// 创建代理对象
let proxy = getCurrentInstance().proxy;

// 定义接收用户名的变量
let username = ref("");

// 定义接收用户问题的变量
let question = ref("");

// 定义保存聊天消息的对象
let messages = ref([])

// 定义一个变量，用于控制发送按钮的禁用状态
let isLoading = ref(false); // 默认不禁用

// 历史记录测试数据
const searchKeyword = ref("");  // 存储搜索关键字
const assistantAvatar = ref("");  // 存储助手头像
const historyList = ref([]);  // 存储历史记录列表
const quickPrompts = ref([
    { text: "帮我写一段代码" },
    { text: "解释一个技术概念" },
    { text: "帮我优化这段代码" },
    { text: "推荐学习路线" },
]);
const currentChatID = ref(0)  // 存储当前点击的是哪一个对话窗口的 historyId

// 聊天函数 -- 点击发送按钮和enter键时触发
function chat() {
  // 基于用户输入的内容判断是否输入的有效内容
  let myQuestion = question.value.trim(); // trim()：去除字符串首尾的空格
  if (myQuestion.length === 0) { // 判断是否输入了数据
    ElMessage.warning("请输入有效内容");
    return;
  }
  isLoading.value = true; // 聊天按钮点击时，设置isLoading为true，表示正在聊天中，禁用发送按钮
  question.value = "";  // 点击发送按钮后，立即清空输入框

  // 访问服务器 -- 往聊天列表末尾加消息
  messages.value.push({role: 'user', content: myQuestion});
  messages.value.push({role: 'assistant', content: '思考中，请耐心等待^3^......'});

  // 构造SSE请求
  // 创建参数对象
  let urlSerchParams = new URLSearchParams({  // URLSearchParams 是浏览器原生提供的一个对象。它的唯一作用，就是把一个键值对字典，转换成符合网络标准的 URL 查询参数格式。
    question: myQuestion,
    historyId: currentChatID.value
  });
  // 创建请求对象
  let es = new EventSource("http://localhost:8000/chat/chat?"+urlSerchParams.toString());
  // 定义拼接字符串变量
  let s = "";
  // 三个监听事件：
  // 1. 监听服务器响应的流式数据
  es.onmessage = (e) => {
    // 取出数据为json格式，转换为js对象
    let data = JSON.parse(e.data).content;
    if (data === "end_end"){
      es.close();
      isLoading.value = false;// 聊天结束，恢复按钮可用
      saveConversationResult(myQuestion, s) // 保存对话结果
      return;
    }
    s += data;  // 拼接字符串
    messages.value[messages.value.length - 1].content = s;  // 更新数据，替换思考
  };
  // 2. 监听错误的发送、连接中断的发生
  es.onerror = (e) => {
    console.log("SSE获取数据失败",e);
    es.close();
  };
  // 3. 监听连接成功
  // es.onopen = () => {
  //   console.log("SSE连接成功");
  // }
}

// 查询聊天历史记录菜单栏 -- 进入页面后自动执行
function query_history_menu() {
    proxy.$axios({
        url: "history/queryHistoryMenu",
        method: "get",
        params: {
          username: username.value
        }
    })
    .then(res => {
      // 第一个 .data 是 Axios 框架的固定格式（Axios 自动包装的），第二个 .data 才是后端自定义的字段名
      // { data: {'code': 200, 'msg': '...', 'data': [...]}, status: 200 }  里面的那个data才是我们需要的数据
      historyList.value = res.data.data;
    })
}

// 查询某一条详细的对话记录 -- 点击某一个历史记录时触发
function conversationLog(historyId){
    // console.log(historyId);
    currentChatID.value = historyId;  // 存储当前点击的是哪一个对话窗口的 historyId
    proxy.$axios({
        url: "history/conversationLog",
        method: "get",
        params: {
          historyId: historyId
        }
    }).then(res => {
        messages.value = res.data.data;
    })
}

// 保存对话聊天记录
function saveConversationResult(question,answer) {
  proxy.$axios({
    url: "chat/saveConversationResult",
    method: "post",
    data: JSON.stringify({
      question: question,
      username: username.value,
      parentId: currentChatID.value,
      answer: answer
    })
  }).then(res => {
      // 只有当currentChatId=0的时候，才需要把新增的数据的historyId赋值给它【表示一个新对话的开始】
      // 如果currentChatId!=0，说明当前点击的是一个已有的对话窗口，那么就不需要在赋值了【因为新传过来的historyId是子对话的】
      if (currentChatID.value === 0){
        currentChatID.value = res.data.data;
      }
      // 刷新历史记录菜单栏
      query_history_menu();
  })
}

// 新对话
function newChat(){
  currentChatID.value = 0;  // 设置currentChatId为0，表示一个新对话的开始
  messages.value = [];  // 清空聊天框数据
}

// 删除历史记录 -- 确认删除
const confirmEvent = (historyID) => {
  console.log('confirm!')
  proxy.$axios({
    url: '/history/deleteHistory',
    method: 'get',
    params: {
      historyId: historyID
    }
  }).then(res => {
    console.log(res.data)
    // 刷新历史记录菜单栏
    query_history_menu();
  })
}
// 删除历史记录 -- 取消删除
const cancelEvent = () => {
  console.log('cancel!')
}

// 模糊搜索历史记录
function searchHistory(){
  let mySearchKeyword = searchKeyword.value.trim(); //trim()：去除字符串首尾的空格
  if (mySearchKeyword.length === 0) { // 判断是否输入了数据
    ElMessage.warning("请输入有效内容");
    return;
  }
  searchKeyword.value = "";
  proxy.$axios({
    url: '/history/searchHistory',
    method: 'get',
    params: {
      username: username.value,
      searchHistory: mySearchKeyword,
    }
  }).then(res => {
    console.log(res.data)
    historyList.value = res.data.data;
  })

}

// 加载页面后自动执行
onMounted(() => {
  username.value = sessionStorage.getItem("username");
  // 获取历史记录菜单栏
  query_history_menu();
})
</script>

<style scoped>
/* ========== 全局基础 ========== */
.chat-container {
  display: flex;
  height: 100vh;
  width: 100vw;
  background-color: #f5f5f0; /* 温暖的米灰底色 */
  font-family: 'Helvetica Neue', Helvetica, 'PingFang SC', 'Hiragino Sans GB', Arial, sans-serif;
  color: #2c2c2c;
  overflow: hidden;
}

/* ========== 左侧边栏 ========== */
.sidebar {
  width: 260px;
  background-color: #ffffff;
  border-right: 1px solid #e8e8e3;
  display: flex;
  flex-direction: column;
}

.sidebar-header {
  padding: 24px 20px 20px;
  border-bottom: 1px solid #e8e8e3;
}

.sidebar-logo {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.sidebar-title {
  font-size: 18px;
  font-weight: 700;
  color: #1a1a1a;
  margin-left: 10px;
  letter-spacing: -0.5px;
}

.new-chat-btn {
  width: 100%;
  background-color: #1a1a1a;
  border: none;
  color: #ffffff;
  font-weight: 600;
  border-radius: 8px;
  height: 40px;
  transition: all 0.2s ease;
}

.new-chat-btn:hover {
  background-color: #333333;
  transform: translateY(-1px);
}

.new-chat-btn:active {
  transform: translateY(0);
}

.sidebar-search {
  padding: 16px 20px;
}

.sidebar-search :deep(.el-input__wrapper) {
  border-radius: 8px;
  box-shadow: none;
  border: 1px solid #e8e8e3;
  background-color: #fafaf7;
  transition: all 0.2s ease;
}

.sidebar-search :deep(.el-input__wrapper:hover) {
  border-color: #d1d1cc;
  background-color: #ffffff;
}

.sidebar-search :deep(.el-input__wrapper.is-focus) {
  border-color: #1a1a1a;
  box-shadow: 0 0 0 2px rgba(26, 26, 26, 0.08);
  background-color: #ffffff;
}

.sidebar-search :deep(.el-input__inner) {
  color: #2c2c2c;
}

.sidebar-search :deep(.el-input__inner::placeholder) {
  color: #999999;
}

/* 历史记录 */
.history-list {
  flex: 1;
  overflow-y: auto;
  padding: 8px 12px;
}

.history-list::-webkit-scrollbar {
  width: 4px;
}

.history-list::-webkit-scrollbar-thumb {
  background-color: #d1d1cc;
  border-radius: 2px;
}

.history-item {
  padding: 12px 14px;
  margin-bottom: 4px;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.15s ease;
  display: flex;
  align-items: center;
  color: #666666;
  font-size: 14px;
}

.history-item:hover {
  background-color: #f5f5f0;
  color: #1a1a1a;
}

.history-item.active {
  background-color: #1a1a1a;
  color: #ffffff;
}

.history-item.active .history-icon,
.history-item.active .history-time {
  color: rgba(255, 255, 255, 0.7);
}

.history-icon {
  margin-right: 10px;
  font-size: 14px;
  color: #999999;
  transition: color 0.15s ease;
}

.history-content {
  flex: 1;
  overflow: hidden;
}

.history-title {
  display: block;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  font-weight: 500;
}

.history-time {
  font-size: 11px;
  color: #999999;
  margin-top: 4px;
  transition: color 0.15s ease;
}

/* 修改了这里：使用 :deep() 穿透 Element Plus 的组件样式 */
.history-more :deep(.el-button) {
  opacity: 0;
  color: #000000;
  font-size: 12px;       /* 新增：字体缩小到 12px */
  transition: all 0.15s ease;
  padding: 0;
  height: auto;          /* 新增：让高度自适应内容 */
  min-height: auto;      /* 新增：取消最小高度限制 */
  width: auto;           /* 新增：让宽度自适应内容 */
}

/* 鼠标悬停时显示 */
.history-item:hover .history-more :deep(.el-button) {
  opacity: 1;
  color: #333333;
}

/* 列表项被选中时，保持为半透明白色 */
.history-item.active .history-more :deep(.el-button) {
  color: rgba(255, 255, 255, 0.7);
}

/* 侧边栏底部 */
.sidebar-footer {
  padding: 16px 20px;
  border-top: 1px solid #e8e8e3;
  background-color: #fafaf7;
}

.user-info {
  display: flex;
  align-items: center;
}

.user-avatar {
  background-color: #1a1a1a;
  color: #ffffff;
  font-weight: 700;
  font-size: 14px;
}

.user-name {
  margin-left: 10px;
  font-size: 14px;
  font-weight: 600;
  color: #1a1a1a;
}

/* ========== 右侧主区域 ========== */
.main-area {
  flex: 1;
  display: flex;
  flex-direction: column;
  background-color: #f5f5f0;
  position: relative;
}

.chat-header {
  height: 60px;
  padding: 0 30px;
  background-color: #ffffff;
  border-bottom: 1px solid #e8e8e3;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.header-left {
  display: flex;
  align-items: center;
  color: #1a1a1a;
}

.header-title {
  font-size: 15px;
  font-weight: 600;
  margin-left: 10px;
  color: #1a1a1a;
}

.header-btn {
  color: #666666;
  border-color: #e8e8e3;
  background-color: #ffffff;
  transition: all 0.15s ease;
}

.header-btn:hover {
  color: #d32f2f;
  border-color: #d32f2f;
  background-color: #fff5f5;
}

/* 消息区 */
.message-area {
  flex: 1;
  overflow-y: auto;
  padding: 30px;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.message-area::-webkit-scrollbar {
  width: 6px;
}

.message-area::-webkit-scrollbar-thumb {
  background-color: #d1d1cc;
  border-radius: 3px;
}

/* 空状态 */
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  text-align: center;
}

.empty-icon {
  width: 80px;
  height: 80px;
  background-color: #ffffff;
  border: 1px solid #e8e8e3;
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #1a1a1a;
  font-size: 32px;
  margin-bottom: 24px;
}

.empty-title {
  font-size: 22px;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 8px;
}

.empty-desc {
  font-size: 14px;
  color: #999999;
  margin-bottom: 30px;
}

.quick-prompts {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: center;
  max-width: 600px;
}

.prompt-chip {
  padding: 10px 18px;
  border: 1px solid #e8e8e3;
  border-radius: 20px;
  background-color: #ffffff;
  font-size: 13px;
  color: #666666;
  cursor: pointer;
  transition: all 0.15s ease;
  display: flex;
  align-items: center;
  gap: 6px;
}

.prompt-chip:hover {
  border-color: #1a1a1a;
  color: #1a1a1a;
  background-color: #ffffff;
  transform: translateY(-1px);
}

/* 消息气泡 */
.message-item {
  display: flex;
  gap: 14px;
  max-width: 80%;
  animation: fadeIn 0.25s ease;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(8px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.message-item.user {
  align-self: flex-end;
  flex-direction: row-reverse;
}

.message-item.assistant {
  align-self: flex-start;
}

.message-avatar {
  margin-top: 4px;
}

.ai-avatar {
  background-color: #1a1a1a;
  color: #ffffff;
  font-weight: 700;
  font-size: 14px;
}

.message-body {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.message-role-name {
  font-size: 12px;
  color: #999999;
  font-weight: 600;
  padding: 0 4px;
}

.message-bubble {
  padding: 14px 18px;
  border-radius: 12px;
  font-size: 14px;
  line-height: 1.7;
  position: relative;
}

.message-item.user .message-bubble {
  background-color: #1a1a1a;
  color: #ffffff;
  border-bottom-right-radius: 2px;
}

.message-item.assistant .message-bubble {
  background-color: #ffffff;
  color: #2c2c2c;
  border: 1px solid #e8e8e3;
  border-bottom-left-radius: 2px;
}

.message-content {
  white-space: pre-wrap;
  word-break: break-word;
}

/* 打字动画 */
.typing-bubble {
  display: flex;
  gap: 5px;
  padding: 18px;
  background-color: #ffffff;
  border: 1px solid #e8e8e3;
  border-radius: 12px;
  border-bottom-left-radius: 2px;
}

.typing-dot {
  width: 6px;
  height: 6px;
  background-color: #999999;
  border-radius: 50%;
  animation: bounce 1.4s infinite ease-in-out both;
}

.typing-dot:nth-child(1) {
  animation-delay: -0.32s;
}

.typing-dot:nth-child(2) {
  animation-delay: -0.16s;
}

@keyframes bounce {
  0%, 80%, 100% {
    transform: scale(0.6);
    opacity: 0.4;
  }
  40% {
    transform: scale(1);
    opacity: 1;
  }
}

/* 底部输入 */
.input-area {
  padding: 20px 30px;
  background-color: #ffffff;
  border-top: 1px solid #e8e8e3;
}

.input-wrapper {
  width: 100%;
  display: flex;
  flex-direction: column; /* 关键：让内部元素垂直堆叠 */
  gap: 12px;              /* 关键：设置上下元素之间的间距 */
}

.chat-input {
  flex: 1; /* 让输入框自动占满剩余空间 */
}

.chat-input :deep(.el-input__wrapper) {
  border-radius: 50px;
  padding: 10px 20px; /* 稍微增加了一点上下内边距，让框更高一点 */
  box-shadow: none;
  border: 1px solid #e8e8e3;
  background-color: #fafaf7;
  transition: all 0.2s ease;
}

.chat-input :deep(.el-input__wrapper:hover) {
  border-color: #d1d1cc;
  background-color: #ffffff;
}

.chat-input :deep(.el-input__wrapper.is-focus) {
  border-color: #1a1a1a;
  box-shadow: 0 0 0 2px rgba(26, 26, 26, 0.08);
  background-color: #ffffff;
}

.chat-input :deep(.el-input__inner) {
  color: #2c2c2c;
  font-size: 15px; /* 字号稍微大一点点，打字更清晰 */
}

.chat-input :deep(.el-input__inner::placeholder) {
  color: #999999;
}

.send-btn {
  background-color: #1a1a1a;
  border: none;
  border-radius: 12px;
  width: 44px; /* 发送按钮也跟着稍微变大了一点点 */
  height: 44px;
  color: #ffffff;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.send-btn:hover:not(.is-disabled) {
  background-color: #333333;
  transform: scale(1.05);
}

.send-btn:active:not(.is-disabled) {
  transform: scale(1);
}

.send-btn.is-disabled {
  background-color: #e8e8e3;
  color: #999999;
  cursor: not-allowed;
}

.input-hint {
  text-align: center;       /* 关键：文字左对齐 */
  font-size: 11px;        /* 关键：字体缩小到 11px */
  color: #999999;
  /* margin-top: 10px; */ /* 删除这一行，间距由 .input-wrapper 的 gap 属性统一管理 */
  //align-self: flex-start; /* 确保它靠左对齐，不受其他样式影响 */
}
</style>