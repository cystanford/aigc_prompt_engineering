<template>
  <view class="container">
    <text class="title">{{ count }}</text>
    <button class="btn" type="primary" @click="increment">+1</button>
  </view>
</template>

<script>
  export default {
    data() {
      return {
        count: 0
      }
    },
    methods: {
      increment() {
        this.count++
      }
    }
  }
</script>

<style>
  .container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
  .title {
    font-size: 40px;
    margin-bottom: 20px;
  }
  .btn {
    width: 200px;
    height: 80px;
  }
</style>
