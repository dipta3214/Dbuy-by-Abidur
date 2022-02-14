<template>
  <div class="home">
    <!-- <span v-if="user_data"
      ><h1>Welcome {{ user_data }}! What are you looking for?</h1></span
    > -->
    <form @submit.prevent="searchProducts" class="search-home">
      <input
        type="text"
        placeholder="Enter what your looking for"
        name="search"
        @change="handleChange"
        class="search-bar-home"
      />
      <button class="search-submit">Submit</button>
    </form>
    <!-- I will work on the commented out stuffs after this bootcamp. I couldn't finish it before presentation and didn't want to delete it -->
    <!-- <div class="product">
      <div
        :key="element.title"
        v-for="element in searchedProducts"
        @click="getDetails(element.id)"
      >
        <div v-if="searched && searchedProducts">
          <h1>{{ element.title }}</h1>
          <img :src="element.image" alt="post" class="phone" />
        </div>
      </div>
    </div>
    <div :key="element.id" v-for="element in products" class="categories">
      <div v-if="products">
        <span @click="getCategories(element.category)">{{
          element.category
        }}</span>
      </div>
    </div> -->
    <!-- <div
      :key="element.brand"
      v-for="element in category"
      @click="getDetails(element.id)"
      class="product"
    >
      <div v-if="catClick && category">
        <h1>{{ element.title }}</h1>
        <img :src="element.image" alt="post" class="phone" />
      </div>
    </div> -->

    <section class="main" id="main" v-if="$store.state.main">
      <div class="content">
        <h3>Dbuy</h3>
        <span>Sell it</span>
        <p>
          This webiste was created using VueJS, Django REST Framework and
          Postgres.
        </p>
        <a href="/products" class="btn">Browse products</a>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios';
const BASE_URL = process.env.VUE_APP_API_URL;
export default {
  name: 'Home',
  data() {
    return {
      user_data: '',
      search: '-',
      searchedProducts: '',
      products: '',
      category: '',
      searched: false,
      catClick: false
    };
  },
  mounted: async function () {
    await this.getProducts();
    this.getMe();
  },
  methods: {
    handleChange(e) {
      this[e.target.name] = e.target.value;
    },
    async searchProducts() {
      const res = await axios.get(`${BASE_URL}/products?search=${this.search}`);
      this.searchedProducts = res.data;
      this.searched = true;
      this.catClick = false;
      this.$store.state.main = false;
    },
    async getProducts() {
      const res = await axios.get(`${BASE_URL}/products`);
      this.products = res.data;
    },
    getMe() {
      if (this.$store.state.access !== '') {
        axios
          .get(`${BASE_URL}/api/v1/users/me`)
          .then((response) => {
            const username = response.data.username;
            const id = response.data.id;

            this.user_data = username;

            this.$store.commit('setUserId', id);
            this.$store.commit('setUsername', username);

            localStorage.setItem('id', id);
            localStorage.setItem('username', username);
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
    // Will work on this after presentation
    // async getCategories(value) {
    //   const res = await axios.get(`${BASE_URL}/products?category=${value}`);
    //   this.category = res.data;
    //   this.searched = false;
    //   this.catClick = true;
    //   this.$store.state.main = false;
    // },
    getDetails(id) {
      this.$router.push(`/products/${id}`);
    }
  }
};
</script>

<style>
.product img {
  width: 300px;
}

.product {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
}

.search-bar-home {
  width: 250px;
  padding: 6px 16px;
  /* border-radius: 3px; */
}

.search-submit {
  margin: 0 5px;
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
  border-radius: 3px;
}
.search-submit:hover {
  background: linear-gradient(to bottom, #2d77a2 5%, #337da8 100%);
  background-color: #28739e;
}

/* Home main section */

section {
  padding: 2rem 9%;
}

.main {
  display: flex;
  align-items: center;
  min-height: 100vh;
  background: url(https://i.imgur.com/vuZc0rL.jpg) no-repeat;
  background-size: cover;
  background-position: center;
}

.main .content {
  max-width: 50rem;
  text-align: left;
}

.main .content h3 {
  font-size: 4.5rem;
  color: #fff;
}

.main .content span {
  font-size: 2.5rem;
  color: #fff;
  padding: 1rem 0;
  line-height: 0.5;
}

.main .content p {
  font-size: 1.5rem;
  color: #fff;
  padding: 1rem 0;
  line-height: 1.5;
}

.btn {
  display: inline-block;
  margin-top: 1rem;
  border-radius: 5rem;
  background: #fff;
  color: #333;
  padding: 0.9rem 2.8rem;
  cursor: pointer;
  font-size: 1.7rem;
  text-decoration: none;
}

.btn:hover {
  background: #2c3e52;
  color: white;
}

@media (min-width: 450px) {
  .search-home {
    display: none;
  }
}

@media (max-width: 450px) {
  .product div div img {
    width: 150px;
  }

  .product {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }

  /* Home main */
  section {
    padding: 2rem;
  }

  .main {
    background-position: left;
  }
}

@media (max-width: 390px) {
  .search-bar-home {
    width: 180px;
  }
}
</style>
