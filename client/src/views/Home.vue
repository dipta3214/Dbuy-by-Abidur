<template>
  <div class="home">
    <span v-if="user_data"
      ><h1>Welcome {{ user_data }}! What are you looking for?</h1></span
    >
    <form @submit.prevent="searchProducts">
      <input
        type="text"
        placeholder="Enter what your looking for"
        name="search"
        @change="handleChange"
      />
      <button>Submit</button>
    </form>

    <div :key="element.title" v-for="element in searchedProducts">
      <div v-if="searched && searchedProducts">
        <h1>{{ element.title }}</h1>
        <img :src="element.image" alt="post" class="phone" />
      </div>
    </div>
    <div :key="element.id" v-for="element in products" class="categories">
      <div v-if="products">
        <span @click="getCategories(element.category)">{{
          element.category
        }}</span>
      </div>
    </div>
    <div :key="element.brand" v-for="element in category">
      <div v-if="catClick && category">
        <h1>{{ element.title }}</h1>
        <img :src="element.image" alt="post" class="phone" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
const BASE_URL = process.env.VUE_APP_API_URL;
export default {
  name: 'Home',
  data() {
    return {
      user_data: '',
      search: '-',
      searchedProducts: '',
      products: '',
      category: '',
      searched: false,
      catClick: false
    };
  },
  mounted: async function () {
    await this.getProducts();
    await this.searchProducts();
    this.getMe();
  },
  methods: {
    handleChange(e) {
      this[e.target.name] = e.target.value;
    },
    async searchProducts() {
      const res = await axios.get(`${BASE_URL}/products?search=${this.search}`);
      this.searchedProducts = res.data;
      this.searched = true;
      this.catClick = false;
    },
    async getProducts() {
      const res = await axios.get(`${BASE_URL}/products`);
      this.products = res.data;
    },
    getMe() {
      if (this.$store.state.access !== '') {
        axios
          .get(`${BASE_URL}/api/v1/users/me`)
          .then((response) => {
            const username = response.data.username;
            const id = response.data.id;

            this.user_data = username;

            this.$store.commit('setUserId', id);
            this.$store.commit('setUsername', username);

            localStorage.setItem('id', id);
            localStorage.setItem('username', username);
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
    async getCategories(value) {
      const res = await axios.get(`${BASE_URL}/products?category=${value}`);
      this.category = res.data;
      this.searched = false;
      this.catClick = true;
    }
  }
};
</script>

<style>
.categories div {
  display: flex;
  flex-direction: row;
  justify-content: center;
}

/* .categories div span {
  display: flex;
  justify-content: center;
} */

@media (max-width: 400px) {
  .phone {
    width: 30vw;
  }
}
</style>
