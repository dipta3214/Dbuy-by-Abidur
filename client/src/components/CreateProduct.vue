<template>
  <div>
    <form @submit.prevent="handleSubmit">
      <li>
        <input
          type="text"
          name="title"
          @change="handleChange"
          placeholder="Title"
          class="field-style field-full align-none"
        />
      </li>

      <li>
        <input
          type="text"
          name="category"
          @change="handleChange"
          placeholder="Category"
          class="field-style field-full align-none"
        />
      </li>

      <li>
        <input
          type="text"
          name="image"
          @change="handleChange"
          placeholder="Image(URL)"
          class="field-style field-full align-none"
        />
      </li>

      <li>
        <textarea
          name="description"
          @change="handleChange"
          placeholder="Description"
        ></textarea>
      </li>

      <li>
        <input
          type="text"
          name="location"
          @change="handleChange"
          placeholder="Location"
        />
      </li>

      <li>
        <input
          type="text"
          name="condition"
          @change="handleChange"
          placeholder="Condition"
        />
      </li>

      <li>
        <input
          type="text"
          name="brand"
          @change="handleChange"
          placeholder="Brand"
        />
      </li>

      <li>
        <input
          type="text"
          name="color"
          @change="handleChange"
          placeholder="Color"
        />
      </li>

      <li>
        <input
          type="text"
          name="price"
          @change="handleChange"
          placeholder="Price"
        />
      </li>

      <input type="submit" value="Post" />
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