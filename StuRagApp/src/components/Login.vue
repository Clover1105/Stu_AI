<template>
  <div class="login-container">
    <el-card class="login-card" shadow="always">
      <div class="login-header">
        <div class="logo">
          <el-icon>
            <Message/>
          </el-icon>
        </div>
        <h2>邮箱验证码登录</h2>
        <p>请输入邮箱获取验证码完成登录</p>
      </div>
      <el-form class="login-form" label-position="top">
        <el-form-item label="邮箱号">
          <el-input v-model="email" :disabled="!isCode" placeholder="请输入邮箱地址">
            <template #prefix>
              <el-icon>
                <Message/>
              </el-icon>
            </template>
          </el-input>
        </el-form-item>
        <el-form-item label="验证码">
          <el-input v-model="code" :disabled="isCode" placeholder="请输入邮箱验证码">
            <template #prefix>
              <el-icon>
                <Key/>
              </el-icon>
            </template>
          </el-input>
        </el-form-item>
        <el-form-item>
          <el-button v-show="isCode" type="primary" class="login-btn" @click="sendEmail">
            <el-icon>
              <Promotion/>
            </el-icon>
            发送验证码
          </el-button>
          <el-button v-show="!isCode" type="success" class="login-btn" @click="checkCode">
            <el-icon>
              <CircleCheck/>
            </el-icon>
            验证并登录
          </el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script setup>
import {ref, getCurrentInstance} from "vue";
import {useRouter} from "vue-router";
import {ElMessage} from "element-plus";
import {Message, Key, Promotion, CircleCheck} from "@element-plus/icons-vue";
let router = useRouter();
let email = ref("");
let code = ref("");
let isCode = ref(true);
let proxy = getCurrentInstance().proxy;
console.log(getCurrentInstance())

function sendEmail() {
  let sendEmail = email.value;
  console.log("发送邮箱：", sendEmail)
  proxy.$axios({
    url: 'users/sendEmail',
    method: 'get',
    params: {
      email: sendEmail
    },
  }).then(res => {
    console.log("接收到的数据：", res)
    let code = res.data.code;
    let msg = res.data.msg;
    let data = res.data.data;
    if (code === 200) {
      isCode.value = !isCode.value;
      sessionStorage.setItem("username", data);
      ElMessage.info(msg);
    } else {
      ElMessage.error(msg);
    }
  })
}

function checkCode() {
  let checkCode = {
    email: email.value,
    code: code.value
  }
  proxy.$axios({
    url: 'users/checkCode',
    method: 'post',
    data: JSON.stringify(checkCode)
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
.login-container {
  width: 100%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, #667eea, #764ba2);
}
.login-card {
  width: 500px;
  padding: 35px 45px 40px;
  border-radius: 20px;
  background: rgba(255,255,255,0.95);
}
.login-header {
  text-align: center;
  margin-bottom: 35px;
}
.logo {
  width: 70px;
  height: 70px;
  margin: 0 auto 15px;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #409eff;
  color: white;
  font-size: 35px;
}
.login-header h2 {
  margin: 0;
  font-size: 28px;
  color: #303133;
}
.login-header p {
  margin-top: 12px;
  color: #909399;
  font-size: 15px;
}
.login-form {
  margin-top: 10px;
}
:deep(.el-form-item__label) {
  font-size: 16px;
  font-weight: 600;
  color: #303133;
}
:deep(.el-input__wrapper) {
  height: 48px;
  border-radius: 10px;
  padding-left: 15px;
}
:deep(.el-input__inner) {
  font-size: 16px;
}
.login-btn {
  width: 100%;
  height: 48px;
  border-radius: 10px;
  font-size: 17px;
  margin-top: 15px;
}
</style>