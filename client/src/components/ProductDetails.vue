<template>
  <div>
    <div v-if="click">
      <UpdateProduct />
    </div>
    <div v-if="!click">
      <button @click="clickTrue">Update</button>
      <button @click="deleteProduct">Delete</button>
      <h1>hi</h1>
      <h1>{{ details.title }}</h1>
      <img :src="details.image" alt="new" />
      <h2>{{ details.brand }}</h2>
      <CreateComment />
      <Comments />
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import UpdateProduct from './UpdateProduct.vue';
import Comments from './Comments.vue';
import CreateComment from './CreateComment.vue';
export default {
  name: 'ProductDetails',
  props: ['title'],
  components: {
    UpdateProduct,
    Comments,
    CreateComment
  },
  data: () => ({
    details: null,
    click: false
  }),
  mounted: async function () {
    await this.getDetails();
  },
  methods: {
    async getDetails() {
      const res = await axios.get(
        `http://localhost:8000/products/${this.$route.params.id}`
      );
      this.details = res.data;
      //   console.log(this.details.id);
    },
    async deleteProduct() {
      await axios.delete(
        `http://localhost:8000/products/${this.$route.params.id}`
      );
      this.$router.push(`/`);
    },
    clickTrue() {
      this.click = true;
    }
  }
};
</script>