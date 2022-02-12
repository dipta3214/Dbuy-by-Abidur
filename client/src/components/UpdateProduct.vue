<template>
  <div>
    <form @submit="handleSubmit" class="form">
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
            class="field-style field-full align-none"
          />
        </li>

        <li>
          <input
            type="text"
            name="condition"
            @change="handleChange"
            :value="condition"
            placeholder="Condition"
            class="field-style field-full align-none"
          />
        </li>

        <li>
          <input
            type="text"
            name="brand"
            @change="handleChange"
            :value="brand"
            placeholder="Brand"
            class="field-style field-full align-none"
          />
        </li>

        <li>
          <input
            type="text"
            name="color"
            @change="handleChange"
            :value="color"
            placeholder="Color"
            class="field-style field-full align-none"
          />
        </li>

        <li>
          <input
            type="text"
            name="price"
            @change="handleChange"
            :value="price"
            placeholder="Price"
            class="field-style field-full align-none"
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

<style scoped>
.form {
  max-width: 550px;
  background: #fafafa;
  padding: 30px;
  margin: 50px auto;
  box-shadow: 1px 1px 25px rgba(0, 0, 0, 0.35);
  border-radius: 10px;
  border: 6px solid #305a72;
}
.form ul {
  padding: 0;
  margin: 0;
  list-style: none;
}
.form ul li {
  display: block;
  margin-bottom: 10px;
  min-height: 35px;
}
.form ul li .field-style {
  box-sizing: border-box;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  padding: 8px;
  outline: none;
  border: 1px solid #b0cfe0;
  -webkit-transition: all 0.3s ease-in-out;
  -moz-transition: all 0.3s ease-in-out;
  -ms-transition: all 0.3s ease-in-out;
  -o-transition: all 0.3s ease-in-out;
}
.form ul li .field-style:focus {
  box-shadow: 0 0 5px #b0cfe0;
  border: 1px solid #b0cfe0;
}
.form ul li .field-split {
  width: 49%;
}
.form ul li .field-full {
  width: 100%;
}
.form ul li input.align-left {
  float: left;
}
.form ul li input.align-right {
  float: right;
}
.form ul li textarea {
  width: 100%;
  height: 100px;
}
.form ul li input[type='button'],
.form ul li input[type='submit'] {
  -moz-box-shadow: inset 0px 1px 0px 0px #3985b1;
  -webkit-box-shadow: inset 0px 1px 0px 0px #3985b1;
  box-shadow: inset 0px 1px 0px 0px #3985b1;
  background-color: #216288;
  border: 1px solid #17445e;
  display: inline-block;
  cursor: pointer;
  color: #ffffff;
  padding: 8px 18px;
  text-decoration: none;
  font: 12px Arial, Helvetica, sans-serif;
}
.form ul li input[type='button']:hover,
.form ul li input[type='submit']:hover {
  background: linear-gradient(to bottom, #2d77a2 5%, #337da8 100%);
  background-color: #28739e;
}

@media (max-width: 450px) {
  .form {
    max-width: 280px;
  }
}
</style>