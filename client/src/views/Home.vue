<template>
  <div class="home">
    <span :src="user_data">{{ user_data }}</span>
    <div
      :key="element.id"
      v-for="element in products"
      @click="getDetails(element.id)"
    >
      <h2>{{ element.title }}</h2>
      <img :src="element.image" />
    </div>
    <h2>hi</h2>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Home',
  data() {
    return {
      user_data: '',
      products: null
    };
  },
  mounted: async function () {
    await this.getProducts();
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
    async getProducts() {
      const res = await axios.get('http://localhost:8000/products/');
      this.products = res.data;
      console.log(res);
    },
    getDetails(id) {
      this.$router.push(`/products/${id}`);
    }
  }
};
</script>
