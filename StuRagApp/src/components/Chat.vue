<template>
    <div class="chat-container">
        <!-- 左侧历史记录栏 -->
        <aside class="sidebar">
            <div class="sidebar-header">
                <div class="sidebar-logo">
                    <el-icon :size="22"><ChatDotRound /></el-icon>
                    <span class="sidebar-title">AI 助手</span>
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
                    <el-icon :size="14" class="history-more" @click.stop><MoreFilled /></el-icon>
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
                    <span class="header-title">AI 智能对话</span>
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
                            {{ item.role === 'user' ? username : 'AI 助手' }}
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
                    <div class="input-row">
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
                    </div>
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

// 加载页面后自动执行
onMounted(() => {
  username.value = sessionStorage.getItem("username");
  // 获取历史记录菜单栏
  query_history_menu();
})
</script>

<style scoped>
/* ========== 全局变量 ========== */
:root {
    --sidebar-width: 280px;
    --sidebar-bg: #f1f5f9;
    --sidebar-hover: #e2e8f0;
    --sidebar-active: #dbeafe;
    --primary: #6366f1;
    --primary-light: #818cf8;
    --primary-bg: rgba(99, 102, 241, 0.08);
    --user-bubble: #6366f1;
    --ai-bubble: #f1f5f9;
    --text-primary: #1e293b;
    --text-secondary: #64748b;
    --border-color: #e2e8f0;
    --bg-main: #ffffff;
    --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.04);
    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 16px;
    --radius-xl: 20px;
}

/* ========== 整体布局 ========== */
.chat-container {
    display: flex;
    height: 100vh;
    width: 100vw;
    overflow: hidden;
    background: #f8fafc;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
}

/* ========== 左侧边栏 ========== */
.sidebar {
    width: var(--sidebar-width);
    min-width: var(--sidebar-width);
    height: 100vh;
    background: var(--sidebar-bg);
    display: flex;
    flex-direction: column;
    border-right: 1px solid #e2e8f0;
    user-select: none;
}

.sidebar-header {
    padding: 20px 16px 16px;
    display: flex;
    flex-direction: column;
    gap: 14px;
    border-bottom: 1px solid #e2e8f0;
}

.sidebar-logo {
    display: flex;
    align-items: center;
    gap: 10px;
    color: #1e293b;
}

.sidebar-title {
    font-size: 18px;
    font-weight: 700;
    letter-spacing: 0.5px;
    color: #1e293b;
}

.new-chat-btn {
    width: 100%;
    background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
    border: none !important;
    font-weight: 500;
    height: 38px;
    transition: all 0.3s ease;
}

.new-chat-btn:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(99, 102, 241, 0.4) !important;
}

.sidebar-search {
    padding: 12px 16px;
}

.sidebar-search :deep(.el-input__wrapper) {
    background: #fff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    box-shadow: none;
    transition: all 0.2s;
}

.sidebar-search :deep(.el-input__wrapper:hover) {
    background: #fff;
    border-color: #cbd5e1;
}

.sidebar-search :deep(.el-input__wrapper.is-focus) {
    background: #fff;
    border-color: var(--primary);
    box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2);
}

.sidebar-search :deep(.el-input__inner) {
    color: #1e293b;
}

.sidebar-search :deep(.el-input__inner::placeholder) {
    color: #94a3b8;
}

.sidebar-search :deep(.el-input__prefix) {
    color: #94a3b8;
}

/* 历史记录列表 */
.history-list {
    flex: 1;
    overflow-y: auto;
    padding: 4px 12px;
    scroll-behavior: smooth;
}

.history-list::-webkit-scrollbar {
    width: 4px;
}

.history-list::-webkit-scrollbar-track {
    background: transparent;
}

.history-list::-webkit-scrollbar-thumb {
    background: #cbd5e1;
    border-radius: 4px;
}

.history-list::-webkit-scrollbar-thumb:hover {
    background: #94a3b8;
}

.history-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px 12px;
    margin-bottom: 2px;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.2s ease;
    color: #334155;
    position: relative;
}

.history-item:hover {
    background: var(--sidebar-hover);
    color: #1e293b;
}

.history-item:hover .history-more {
    opacity: 1;
}

.history-item.active {
    background: var(--sidebar-active);
    color: #1e293b;
}

.history-item.active .history-icon {
    color: var(--primary);
}

.history-icon {
    flex-shrink: 0;
    color: #64748b;
    transition: color 0.2s;
}

.history-content {
    flex: 1;
    min-width: 0;
    display: flex;
    flex-direction: column;
    gap: 2px;
}

.history-title {
    font-size: 13px;
    font-weight: 500;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.history-time {
    font-size: 11px;
    color: #94a3b8;
}

.history-more {
    flex-shrink: 0;
    opacity: 0;
    transition: opacity 0.2s;
    color: #94a3b8;
    cursor: pointer;
}

.history-more:hover {
    color: #1e293b;
}

/* 侧边栏底部用户信息 */
.sidebar-footer {
    padding: 14px 16px;
    border-top: 1px solid #e2e8f0;
}

.user-info {
    display: flex;
    align-items: center;
    gap: 10px;
}

.user-avatar {
    background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
    color: #fff;
    font-weight: 600;
    font-size: 14px;
}

.user-name {
    font-size: 14px;
    font-weight: 500;
    color: #1e293b;
}

/* ========== 右侧主区域 ========== */
.main-area {
    flex: 1;
    display: flex;
    flex-direction: column;
    min-width: 0;
    background: var(--bg-main);
}

/* 顶部标题栏 */
.chat-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 16px 24px;
    background: #fff;
    border-bottom: 1px solid var(--border-color);
    flex-shrink: 0;
}

.header-left {
    display: flex;
    align-items: center;
    gap: 10px;
}

.header-icon {
    color: var(--primary);
}

.header-title {
    font-size: 16px;
    font-weight: 600;
    color: var(--text-primary);
}

.header-right {
    display: flex;
    align-items: center;
    gap: 8px;
}

.header-btn {
    color: var(--text-secondary) !important;
    border: 1px solid var(--border-color) !important;
    transition: all 0.2s;
}

.header-btn:hover {
    color: #ef4444 !important;
    border-color: #fecaca !important;
    background: #fef2f2 !important;
}

/* 消息显示区域 */
.message-area {
    flex: 1;
    overflow-y: auto;
    padding: 24px;
    scroll-behavior: smooth;
    background: linear-gradient(180deg, #fafbfc 0%, #f8fafc 100%);
}

.message-area::-webkit-scrollbar {
    width: 6px;
}

.message-area::-webkit-scrollbar-track {
    background: transparent;
}

.message-area::-webkit-scrollbar-thumb {
    background: #cbd5e1;
    border-radius: 3px;
}

.message-area::-webkit-scrollbar-thumb:hover {
    background: #94a3b8;
}

/* 空状态 */
.empty-state {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
    gap: 8px;
    padding: 40px 20px;
}

.empty-icon {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    background: var(--primary-bg);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 12px;
    color: var(--primary);
}

.empty-title {
    font-size: 24px;
    font-weight: 700;
    color: var(--text-primary);
    margin: 0;
}

.empty-desc {
    font-size: 15px;
    color: var(--text-secondary);
    margin: 0 0 20px;
}

.quick-prompts {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: center;
    max-width: 500px;
}

.prompt-chip {
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 8px 16px;
    border-radius: 20px;
    border: 1px solid var(--border-color);
    background: #fff;
    color: var(--text-secondary);
    font-size: 13px;
    cursor: pointer;
    transition: all 0.2s ease;
    box-shadow: var(--shadow-sm);
}

.prompt-chip:hover {
    border-color: var(--primary-light);
    color: var(--primary);
    transform: translateY(-1px);
    box-shadow: var(--shadow-md);
}

/* 消息项 */
.message-item {
    display: flex;
    gap: 14px;
    margin-bottom: 24px;
    animation: messageIn 0.3s ease;
}

@keyframes messageIn {
    from {
        opacity: 0;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.message-item.user {
    flex-direction: row-reverse;
}

.message-item.user .message-body {
    align-items: flex-end;
}

.message-item.user .message-role-name {
    text-align: right;
}

.message-avatar {
    flex-shrink: 0;
    margin-top: 4px;
}

.message-avatar :deep(.el-avatar) {
    box-shadow: var(--shadow-sm);
}

.ai-avatar {
    background: linear-gradient(135deg, #818cf8, #c084fc) !important;
    color: #fff !important;
    font-weight: 600;
    font-size: 14px;
}

.message-body {
    display: flex;
    flex-direction: column;
    gap: 4px;
    max-width: 70%;
}

.message-role-name {
    font-size: 12px;
    font-weight: 600;
    color: var(--text-secondary);
    padding: 0 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.message-bubble {
    padding: 12px 18px;
    border-radius: var(--radius-xl);
    line-height: 1.6;
    font-size: 14px;
    word-break: break-word;
    position: relative;
}

.message-item.user .message-bubble {
    background: linear-gradient(135deg, #6366f1, #7c3aed);
    color: #fff;
    border-bottom-right-radius: 6px;
    box-shadow: 0 2px 8px rgba(99, 102, 241, 0.25);
}

.message-item.assistant .message-bubble {
    background: #fff;
    color: var(--text-primary);
    border-bottom-left-radius: 6px;
    box-shadow: var(--shadow-sm);
    border: 1px solid #f1f5f9;
}

.message-content {
    white-space: pre-wrap;
}

/* 打字动画 */
.typing-bubble {
    display: flex;
    align-items: center;
    gap: 4px;
    padding: 18px !important;
}

.typing-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #94a3b8;
    animation: typingBounce 1.4s infinite ease-in-out;
}

.typing-dot:nth-child(1) {
    animation-delay: 0s;
}

.typing-dot:nth-child(2) {
    animation-delay: 0.2s;
}

.typing-dot:nth-child(3) {
    animation-delay: 0.4s;
}

@keyframes typingBounce {
    0%, 60%, 100% {
        transform: translateY(0);
        opacity: 0.4;
    }
    30% {
        transform: translateY(-6px);
        opacity: 1;
    }
}

/* 底部输入区域 */
.input-area {
    padding: 16px 24px 20px;
    background: #fff;
    border-top: 1px solid var(--border-color);
    flex-shrink: 0;
}

.input-wrapper {
    max-width: 900px;
    margin: 0 auto;
}

.input-row {
    display: flex;
    align-items: center;
}

.chat-input :deep(.el-input__wrapper) {
    border-radius: 24px;
    padding: 6px 16px;
    background: #f8fafc;
    border: 2px solid transparent;
    box-shadow: var(--shadow-sm);
    transition: all 0.3s ease;
}

.chat-input :deep(.el-input__wrapper:hover) {
    background: #f1f5f9;
}

.chat-input :deep(.el-input__wrapper.is-focus) {
    border-color: var(--primary);
    background: #fff;
    box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
}

.chat-input :deep(.el-input__inner) {
    font-size: 14px;
    color: var(--text-primary);
}

.chat-input :deep(.el-input__inner::placeholder) {
    color: #94a3b8;
}

.send-btn {
    background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
    border: none !important;
    transition: all 0.3s ease;
}

.send-btn:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 12px rgba(99, 102, 241, 0.4) !important;
}

.send-btn.is-disabled {
    background: #cbd5e1 !important;
    transform: none !important;
    box-shadow: none !important;
}

.input-hint {
    text-align: center;
    font-size: 11px;
    color: #94a3b8;
    margin: 8px 0 0;
}
</style>