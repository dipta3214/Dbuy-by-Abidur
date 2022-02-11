<template>
  <div>
    <form @submit="handleSubmit">
      <label for="content">Content: </label>
      <input type="text" name="content" @change="handleChange" />

      <button>Submit</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
const BASE_URL = process.env.VUE_APP_API_URL;
export default {
  name: 'CreateComment',
  data: () => ({
    content: ''
  }),
  methods: {
    handleChange(e) {
      this[e.target.name] = e.target.value;
    },
    async handleSubmit() {
      const formData = {
        username: this.$store.state.username,
        content: this.content,
        user_id: this.$store.state.id,
        product: `${BASE_URL}/products/${this.$route.params.id}`,
        product_id: this.$route.params.id
      };
      await axios.post(`${BASE_URL}/comments/`, formData);
    }
  }
};
</script>