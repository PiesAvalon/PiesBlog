<template>
  <div class="left-bar">
    <h2>左侧栏</h2>
    <!-- 这里可以添加左侧栏的内容 -->
  </div>
</template>

<style scoped>
/* 左侧栏样式 */
.left-bar {
  width: 15%;        /* 占总宽度的20% */
  height: 100%;      /* 高度填满父容器 */
  background-color: #2c3e50;  /* 深蓝灰色背景 */
  padding: 20px;     /* 内边距20px，使内容不贴边 */
  box-sizing: border-box;  /* 确保padding不会增加元素实际宽度 */
  color: #ffffff;    /* 文字颜色为白色 */
  overflow-y: auto;  /* 内容超出时在Y轴方向显示滚动条 */
}
</style> 