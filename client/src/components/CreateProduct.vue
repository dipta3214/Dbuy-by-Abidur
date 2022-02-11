<template>
  <div>
    <form @submit.prevent="handleSubmit">
      <label for="title">Title: </label>
      <input type="text" name="title" @change="handleChange" />

      <label for="category">Category: </label>
      <input type="text" name="category" @change="handleChange" />

      <label for="image">Image: </label>
      <input type="text" name="image" @change="handleChange" />

      <label for="description">Description: </label>
      <input type="text" name="description" @change="handleChange" />

      <label for="location">Location: </label>
      <input type="text" name="location" @change="handleChange" />

      <label for="condition">Condition: </label>
      <input type="text" name="condition" @change="handleChange" />

      <label for="brand">Brand: </label>
      <input type="text" name="brand" @change="handleChange" />

      <label for="color">Color: </label>
      <input type="text" name="color" @change="handleChange" />

      <label for="price">Price: </label>
      <input type="text" name="price" @change="handleChange" />

      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
const BASE_URL = process.env.VUE_APP_API_URL;
export default {
  name: 'CreateProduct',
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
  methods: {
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
      await axios.post(`${BASE_URL}/products/`, formData);
      this.$router.push('/');
    }
  }
};
</script>