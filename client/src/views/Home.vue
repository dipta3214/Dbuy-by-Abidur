<template>
  <div class="home">
    <span :src="user_data" v-if="user_data"
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

    <div :key="element.id" v-for="element in searchedProducts">
      <div v-if="searchedProducts">
        <h1>{{ element.title }}</h1>
        <img :src="element.image" alt="post" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Home',
  data() {
    return {
      user_data: '',
      search: '-',
      searchedProducts: ''
    };
  },
  mounted: async function () {
    await this.searchProducts();
    this.getMe();
  },
  methods: {
    getMe() {
      axios
        .get('http://localhost:8000/api/v1/users/me')
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
    },
    handleChange(e) {
      this[e.target.name] = e.target.value;
    },
    async searchProducts() {
      const res = await axios.get(
        `http://localhost:8000/products?search=${this.search}`
      );
      this.searchedProducts = res.data;
    }
  }
};
</script>
