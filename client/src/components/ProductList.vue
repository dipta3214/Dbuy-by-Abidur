<template>
  <div>
    <div
      :key="element.id"
      v-for="element in products"
      @click="getDetails(element.id)"
    >
      <h2>{{ element.title }}</h2>
      <img :src="element.image" />
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'ProductList',
  data() {
    return {
      products: null
    };
  },
  mounted: async function () {
    await this.getProducts();
  },
  methods: {
    async getProducts() {
      const res = await axios.get('http://localhost:8000/products/');
      this.products = res.data;
    },
    getDetails(id) {
      this.$router.push(`/products/${id}`);
    }
  }
};
</script>