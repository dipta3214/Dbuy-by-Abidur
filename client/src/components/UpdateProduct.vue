<template>
  <div>
    <form @submit="handleSubmit">
      <label for="title">Title: </label>
      <input type="text" name="title" @change="handleChange" :value="title" />

      <label for="category">Category: </label>
      <input
        type="text"
        name="category"
        @change="handleChange"
        :value="category"
      />

      <label for="image">Image: </label>
      <input type="text" name="image" @change="handleChange" :value="image" />

      <label for="description">Description: </label>
      <input
        type="text"
        name="description"
        @change="handleChange"
        :value="description"
      />

      <label for="location">Location: </label>
      <input
        type="text"
        name="location"
        @change="handleChange"
        :value="location"
      />

      <label for="condition">Condition: </label>
      <input
        type="text"
        name="condition"
        @change="handleChange"
        :value="condition"
      />

      <label for="brand">Brand: </label>
      <input type="text" name="brand" @change="handleChange" :value="brand" />

      <label for="color">Color: </label>
      <input type="text" name="color" @change="handleChange" :value="color" />

      <label for="price">Price: </label>
      <input type="text" name="price" @change="handleChange" :value="price" />

      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
const BASE_URL = process.env.VUE_APP_API_URL;
export default {
  name: 'UpdateProduct',
  data: () => ({
    title: '',
    category: '',
    image: '',
    description: '',
    location: '',
    condition: '',
    brand: '',
    color: '',
    price: '',
    user_id: ''
  }),
  mounted: async function () {
    await this.getDetails();
  },
  methods: {
    async getDetails() {
      const res = await axios.get(
        `${BASE_URL}/products/${this.$route.params.id}`
      );
      this.title = res.data.title;
      this.category = res.data.category;
      this.image = res.data.image;
      this.description = res.data.description;
      this.location = res.data.location;
      this.condition = res.data.condition;
      this.brand = res.data.brand;
      this.color = res.data.color;
      this.price = res.data.price;
      this.user_id = res.data.user_id;
    },
    handleChange(e) {
      this[e.target.name] = e.target.value;
    },
    async handleSubmit() {
      const formData = {
        title: this.title,
        category: this.category,
        image: this.image,
        description: this.description,
        location: this.location,
        condition: this.condition,
        brand: this.brand,
        color: this.color,
        price: this.price,
        user_id: this.$store.state.id
      };
      await axios.put(
        `${BASE_URL}/products/${this.$route.params.id}`,
        formData
      );
      // this.$router.push('/');
    }
  }
};
</script>