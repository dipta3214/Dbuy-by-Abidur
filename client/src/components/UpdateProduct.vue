<template>
  <div>
    <form @submit="handleSubmit">
      <ul>
        <li>
          <input
            type="text"
            name="title"
            @change="handleChange"
            :value="title"
            placeholder="Title"
            class="field-style field-full align-none"
          />
        </li>
        <li>
          <input
            type="text"
            name="category"
            @change="handleChange"
            :value="category"
            placeholder="Category"
            class="field-style field-full align-none"
          />
        </li>

        <li>
          <input
            type="text"
            name="image"
            @change="handleChange"
            :value="image"
            placeholder="Image(URL)"
            class="field-style field-full align-none"
          />
        </li>

        <li>
          <input
            type="text"
            name="description"
            @change="handleChange"
            :value="description"
            placeholder="Description"
            class="field-style field-full align-none"
          />
        </li>

        <li>
          <input
            type="text"
            name="location"
            @change="handleChange"
            :value="location"
            placeholder="Location"
          />
        </li>

        <li>
          <input
            type="text"
            name="condition"
            @change="handleChange"
            :value="condition"
            placeholder="Condition"
          />
        </li>

        <li>
          <input
            type="text"
            name="brand"
            @change="handleChange"
            :value="brand"
            placeholder="Brand"
          />
        </li>

        <li>
          <input
            type="text"
            name="color"
            @change="handleChange"
            :value="color"
            placeholder="Color"
          />
        </li>

        <li>
          <input
            type="text"
            name="price"
            @change="handleChange"
            :value="price"
            placeholder="Price"
          />
        </li>

        <li>
          <input type="submit" value="Post" />
        </li>
      </ul>
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