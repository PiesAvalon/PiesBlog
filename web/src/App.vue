<script setup>
import { RouterView } from 'vue-router'
import LeftBar from './components/LeftBar.vue'
import RightBar from './components/RightBar.vue'
import Main from './components/Main.vue'
</script>

<template>
  <div class="app-container">
    <LeftBar />
    <Main />
    <RightBar />
  </div>
</template>

<style>
/* 全局CSS重置，应用于所有元素 */
* {
  margin: 0;        /* 移除所有元素的外边距 */
  padding: 0;       /* 移除所有元素的内边距 */
  box-sizing: border-box;  /* 使元素的宽度和高度包含padding和border */
}

/* 设置HTML和body元素填满整个视口 */
html, body {
  width: 100%;      /* 宽度100%填满视口 */
  height: 100%;     /* 高度100%填满视口 */
  margin: 0;        /* 移除外边距 */
  padding: 0;       /* 移除内边距 */
  overflow: hidden; /* 隐藏溢出内容，防止出现滚动条 */
}

/* 设置Vue应用的根元素(#app)填满整个视口 */
#app {
  width: 100%;      /* 宽度100%填满父容器 */
  height: 100%;     /* 高度100%填满父容器 */
  margin: 0;        /* 移除外边距 */
  padding: 0;       /* 移除内边距 */
}

/* 主容器的样式，用于布局三栏结构 */
.app-container {
  display: flex;    /* 使用弹性布局 */
  flex-direction: row; /* 子元素水平排列 */
  width: 100%;      /* 宽度100%填满父容器 */
  height: 100%;     /* 高度100%填满父容器 */
  margin: 0;        /* 移除外边距 */
  padding: 0;       /* 移除内边距 */
  overflow: hidden; /* 隐藏溢出内容 */
}
</style>
