<template>

  <!--  图书展示-->
  <!-- 添加悬浮购物车 -->
  <div class="floating-cart" @mousedown="dragStart" @mouseup="dragEnd" @click="redirectToTestName">
    <!-- 使用伪元素 ::before 来添加图标 -->
  </div>
  <!-- 搜索输入框和按钮 -->
  <div class="search-container">
    <el-input
        v-model="searchQuery"
        placeholder="搜索图书"
        style="width: 200px;"
    ></el-input>
    <el-button type="primary" @click="performSearch">搜索</el-button>
  </div>
  <el-row>
    <el-col :span="4" v-for="(book, index) in displayedData" :key="book.id" :offset="index > -1 ? 1 : 0">
      <div class="card-container">
        <el-card :body-style="{ padding: '0px' }">
          <img :src="book.validCoverUrl" class="image" alt="书籍封面">
          <div style="padding: 14px;">
            <span>{{ book.book_name }}</span>
            <div class="bottom clearfix">
              <time class="time">出版社：{{ book.Publishing_house }}</time>
              <br> <br>

              <time class="time">作者：{{ book.author }}</time>
              <br> <br>
              <time class="time">价格：{{ book.Price }}</time>
              <br> <br>

              <time class="time">编号：{{ book.mobile }}</time>
              <br> <br>

              <time class="time">状态：{{ book.status === 1 ? '启用' : '禁用' }}</time>
              <br> <br>
              <el-button type="success" v-if="!book.added" @click="toggleBookStatus(book)">添加借阅</el-button>
              <el-button type="info" v-else @click="toggleBookStatus(book)">已添加</el-button>
            </div>
          </div>
        </el-card>
      </div>
    </el-col>
  </el-row>
  <div class="pagination-container">
    <el-pagination
        @current-change="handlePageChange"
        :current-page="currentPage"
        :page-size="pageSize"
        layout="prev, pager, next"
        :total="data.length"
    />
  </div>
</template>

<script>
import {getCookie, setCookie} from '@/components/utils/utils.js'

export default {
  computed: {
    displayedData() {
      const filteredData = this.searchQuery
          ? this.data.filter(book => book.book_name.includes(this.searchQuery))
          : this.data;

      const startIndex = (this.currentPage - 1) * this.pageSize;
      const endIndex = startIndex + this.pageSize;
      return filteredData.slice(startIndex, endIndex);
    },
  },
  data() {
    return {
      hasDragged: false, // 添加一个新的数据项
      isJustClicked: true,
      isDragging: false,
      startX: 0,
      startY: 0,
      offsetX: 0,
      offsetY: 0,
      data: [],
      currentPage: 1,
      pageSize: 20,
      searchQuery: '',
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    //点击购物车
    redirectToTestName() {
      // 使用 vue-router 进行页面跳转
      this.$router.push({name: 'ShoppingHome'});
      // 更新 Vuex 状态或者设置一个状态来表示购物车标签被选中
      this.$store.commit('setSelectedTab', 'cart');
    },
    //购物车移动逻辑
    dragStart(e) {
      this.isDragging = true;
      this.hasDragged = false; // 初始化为 false
      this.startX = e.clientX - this.offsetX;
      this.startY = e.clientY - this.offsetY;
      document.addEventListener('mousemove', this.drag);
      document.addEventListener('mouseup', this.dragEnd);
    },
    drag(e) {
      this.hasDragged = true; // 设置为 true，表示拖动了
      if (!this.isDragging) return;
      const deltaX = e.clientX - this.startX;
      const deltaY = e.clientY - this.startY;

      const cart = document.querySelector('.floating-cart');
      const computedStyle = window.getComputedStyle(cart);
      const x = parseFloat(computedStyle.getPropertyValue('left')) + deltaX;
      const y = parseFloat(computedStyle.getPropertyValue('top')) + deltaY;

      cart.style.left = `${x}px`;
      cart.style.top = `${y}px`;

      this.startX = e.clientX;
      this.startY = e.clientY;
    },
    dragEnd(e) {
      this.isDragging = false;
      document.removeEventListener('mousemove', this.drag);
      document.removeEventListener('mouseup', this.dragEnd);
      this.isJustClicked = true;
      this.isDragging = false;
      document.removeEventListener('mousemove', this.drag);
      document.removeEventListener('mouseup', this.dragEnd);
      // 如果起始点和终点相同，认为是点击事件
      if (this.startX === e.clientX && this.startY === e.clientY) {
        this.redirectToTestName();
      }
    },
    openCart() {
      console.log("购物车被点击了");
    },
    performSearch() {
      this.currentPage = 1;
    },
    handlePageChange(newPage) {
      this.currentPage = newPage;
    },
    getData() {
      // Fetching the cart items from the cookies
      const cartItems = JSON.parse(getCookie('cartItems') || '[]');
      fetch('http://seqnqc.natappfree.cc/api/publishes/')
          .then(response => response.json())
          .then(data => {
            data.forEach(book => {
              // Set the added status based on the cookie data
              book.added = cartItems.some(item => item.id === book.id);

              this.checkImageValidity(book.coverUrl)
                  .then(validUrl => {
                    book.validCoverUrl = validUrl;
                    this.data.push(book);
                  });
            });
          });
    },
    toggleBookStatus(book) {
      // 获取当前的UTC日期
      const utcDate = new Date();

      // 使用 toLocaleString 将 UTC 日期转换为中国时区 (UTC+8)
      const chinaTime = utcDate.toLocaleString("zh-CN", {timeZone: "Asia/Shanghai"});

      const cartItems = JSON.parse(getCookie('cartItems') || '[]');
      if (!book.added) {
        book.added = true;
        // 将中国时区的时间直接添加到书籍对象中
        book.date = chinaTime;
        cartItems.push(book);
      } else {
        const index = cartItems.findIndex(item => item.id === book.id);
        if (index > -1) {
          cartItems.splice(index, 1);
        }
        book.added = false;
      }
      // 将购物车信息存储为 cookie，有效期为7天
      setCookie('cartItems', JSON.stringify(cartItems), 7);
    },
    checkImageValidity(url) {
      return new Promise((resolve, reject) => {
        const img = new Image();
        img.src = url;
        img.onload = () => resolve(url);
        img.onerror = () => resolve('default-image-url');
      });
    },
  },
};
</script>

<style>
.floating-cart {
  width: 50px; /* 与图标宽度一致 */
  height: 50px; /* 与图标高度一致 */
  position: fixed;
  right: 20px;
  top: 200px;
  cursor: pointer; /* 鼠标样式为手指，表示可点击 */
}

.floating-cart::before {
  content: "";
  display: block;
  width: 100%;
  height: 100%;
  background-image: url('shoppingcart_120371.ico'); /* 将路径替换为您的ico图标的实际路径 */
  background-size: cover;
  background-repeat: no-repeat;
}

.card-container {
  width: 300px;
  margin: 30px;
}

.time {
  font-size: 13px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
}


.image {
  width: 100%;
  display: block;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both;
}

.pagination-container {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.search-container {
  display: flex;
  justify-content: center; /* 水平居中对齐 */
  align-items: center; /* 垂直居中对齐 */
  margin-bottom: 10px;
}


</style>
