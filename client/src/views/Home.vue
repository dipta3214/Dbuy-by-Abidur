<template>
  <div class="home">
    <span v-if="user_data"
      ><h1>Welcome {{ user_data }}! What are you looking for?</h1></span
    >
    <form @submit.prevent="searchProducts" class="search-home">
      <input
        type="text"
        placeholder="Enter what your looking for"
        name="search"
        @change="handleChange"
        class="search-bar-home"
      />
      <button class="search-submit">Submit</button>
    </form>

    <div class="product">
      <div
        :key="element.title"
        v-for="element in searchedProducts"
        @click="getDetails(element.id)"
      >
        <div v-if="searched && searchedProducts">
          <h1>{{ element.title }}</h1>
          <img :src="element.image" alt="post" class="phone" />
        </div>
      </div>
    </div>
    <div :key="element.id" v-for="element in products" class="categories">
      <div v-if="products">
        <span @click="getCategories(element.category)">{{
          element.category
        }}</span>
      </div>
    </div>
    <div
      :key="element.brand"
      v-for="element in category"
      @click="getDetails(element.id)"
      class="product"
    >
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
    },
    getDetails(id) {
      this.$router.push(`/products/${id}`);
    }
  }
};
</script>

<style>
.product img {
  width: 300px;
}

.product {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
}

.search-bar-home {
  width: 250px;
  padding: 6px 16px;
  /* border-radius: 3px; */
}

.search-submit {
  margin: 0 5px;
  -moz-box-shadow: inset 0px 1px 0px 0px #3985b1;
  -webkit-box-shadow: inset 0px 1px 0px 0px #3985b1;
  box-shadow: inset 0px 1px 0px 0px #3985b1;
  background-color: #216288;
  border: 1px solid #17445e;
  display: inline-block;
  cursor: pointer;
  color: #ffffff;
  padding: 8px 18px;
  text-decoration: none;
  font: 12px Arial, Helvetica, sans-serif;
  border-radius: 3px;
}
.search-submit:hover {
  background: linear-gradient(to bottom, #2d77a2 5%, #337da8 100%);
  background-color: #28739e;
}

@media (min-width: 450px) {
  .search-home {
    display: none;
  }
}

@media (max-width: 390px) {
  .search-bar-home {
    width: 180px;
  }
}
</style>
