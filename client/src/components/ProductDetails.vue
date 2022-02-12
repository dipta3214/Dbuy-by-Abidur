<template>
  <div>
    <div v-if="click">
      <UpdateProduct />
    </div>
    <div v-if="!click">
      <button @click="clickTrue">Update</button>
      <button @click="deleteProduct">Delete</button>
      <div v-if="details" class="grid">
        <div class="img"><img :src="details.image" alt="new" /></div>
        <div class="flex">
          <div>
            <h1>{{ details.title }}</h1>
            <h4>Price: {{ details.price }}</h4>
            <h3>Brand: {{ details.brand }}</h3>
            <h3>Category: {{ details.category }}</h3>
            <h3>Location: {{ details.location }}</h3>
            <h3>Color: {{ details.color }}</h3>
            <h3>Condition: {{ details.condition }}</h3>
            <p>{{ details.description }}</p>
          </div>
        </div>
      </div>
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
const BASE_URL = process.env.VUE_APP_API_URL;
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
        `${BASE_URL}/products/${this.$route.params.id}`
      );
      this.details = res.data;
      //   console.log(this.details.id);
    },
    async deleteProduct() {
      await axios.delete(`${BASE_URL}/products/${this.$route.params.id}`);
      this.$router.push(`/`);
    },
    clickTrue() {
      this.click = true;
    }
  }
};
</script>

<style scoped>
.grid {
  display: grid;
  grid-template-columns: 4fr 3fr;
  grid-template-rows: 1fr;
}

.grid img {
  width: 400px;
}

.flex {
  display: flex;
  justify-content: flex-start;
}

.flex div {
  text-align: left;
}

@media (max-width: 450px) {
  .grid img {
    width: 300px;
  }

  .grid {
    display: grid;
    grid-template-columns: 1fr;
  }

  .flex {
    margin: 10px 35px;
  }
}
</style>