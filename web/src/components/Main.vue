<script setup>
import { RouterView } from 'vue-router'
import { ref, onMounted } from 'vue'
import { getRoot } from '../api/index.js'

// 定义响应式数据
const message = ref('')
const loading = ref(false)
const error = ref('')

// 组件挂载时调用API
onMounted(async () => {
  try {
    loading.value = true
    const response = await getRoot()
    message.value = response.data.message
  } catch (err) {
    error.value = '获取数据失败: ' + err.message
    console.error(err)
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="main-content">
    <h1>主内容区</h1>
    
    <!-- 显示API响应 -->
    <div v-if="loading" class="loading">加载中...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <div v-else-if="message" class="message">
      <h2>从后端获取的消息:</h2>
      <p>{{ message }}</p>
    </div>
    
    <RouterView />
  </div>
</template>

<style scoped>
/* 主内容区域样式 */
.main-content {
  width: 60%;        /* 占总宽度的60% */
  height: 100%;      /* 高度填满父容器 */
  background-color: #ffffff;  /* 白色背景 */
  padding: 20px;     /* 内边距20px，使内容不贴边 */
  box-sizing: border-box;  /* 确保padding不会增加元素实际宽度 */
  overflow-y: auto;  /* 内容超出时在Y轴方向显示滚动条 */
}

.loading {
  color: #666;
  margin: 20px 0;
}

.error {
  color: #e74c3c;
  margin: 20px 0;
  padding: 10px;
  border: 1px solid #e74c3c;
  border-radius: 4px;
}

.message {
  margin: 20px 0;
  padding: 15px;
  background-color: #f8f9fa;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
</style> 