<template>
  <view class="container">
    <view class="table-header">
      <text class="table-header-item">题目</text>
      <text class="table-header-item">难度</text>
      <text class="table-header-item">通过率</text>
    </view>
    <scroll-view class="table-content">
      <view v-for="(item, index) in problemList" :key="item.id" class="table-row" @click="goToProblemInfo(item.id)">
        <text class="table-row-item">{{ item.title }}</text>
        <text class="table-row-item">{{ item.difficulty }}</text>
        <text class="table-row-item">{{ item.acceptance }}</text>
      </view>
    </scroll-view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      problemList: []
    }
  },
  mounted() {
    // 从服务器获取数据表数据
    this.getProblemList()
  },
  methods: {
    getProblemList() {
      // 使用 uni.request() 方法从服务器获取数据表数据
      uni.request({
        url: 'http://127.0.0.1:5000/get_problem_list',
        success: (res) => {
          this.problemList = res.data.problem_list;
		  //console.log(this.problemList)
        }
      })
    },
    goToProblemInfo(id) {
      // 跳转到题目信息页面，传递题目的 id 参数
      uni.navigateTo({
        url: '/pages/problem_info?id=' + id
      })
    }
  }
}
</script>

<style>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 20px;
}

.table-header {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 100%;
  height: 40px;
  background-color: #f5f5f5;
  border-bottom: 1px solid #ddd;
}

.table-header-item {
  width: 33.33%;
  text-align: center;
  line-height: 40px;
  font-size: 16px;
}

.table-content {
  width: 100%;
  height: 500px;
  overflow-y: scroll;
}

.table-row {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 100%;
  height: 40px;
  border-bottom: 1px solid #ddd;
  cursor: pointer;
}

.table-row-item {
  width: 33.33%;
  text-align: center;
  line-height: 40px;
  font-size: 14px;
}
</style>
