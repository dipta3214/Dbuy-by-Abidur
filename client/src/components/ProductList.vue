<template>
  <div class="product">
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
const BASE_URL = process.env.VUE_APP_API_URL;
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
      const res = await axios.get(`${BASE_URL}/products/`);
      this.products = res.data;
    },
    getDetails(id) {
      this.$router.push(`/products/${id}`);
    }
  }
};
</script>

<style scoped>
.product img {
  width: 300px;
}

.product {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
}

@media (max-width: 450px) {
  .product img {
    width: 150px;
  }

  .product {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }
}
</style>