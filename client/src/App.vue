<template>
  <div id="app">
    <div id="nav">
      <div class="navOne" @click="restart">
        <router-link to="/">Home</router-link>
      </div>
      <div>
        <select v-model="categories">
          <option>Categories</option>
          <option
            :key="element.id"
            v-for="element in productsApp"
            :value="element.category"
          >
            <button @click="getCategories">
              {{ element.category }}
            </button>
          </option>
        </select>
      </div>
      <form @submit.prevent="searchProducts" class="search-bar">
        <input
          type="text"
          placeholder="Enter what your looking for"
          name="search"
          @change="handleChange"
          class="search"
        />
        <button class="search-submit">Submit</button>
      </form>
      <a @click="filter" class="toggle-button">
        <span class="bar"></span>
        <span class="bar"></span>
        <span class="bar"></span>
      </a>
      <div class="navTwo" v-bind:class="{ active: click }">
        <router-link to="/products">Products</router-link>
        <router-link to="/about">About</router-link>
        <router-link to="/signup" v-if="!$store.state.authenticated"
          >Sign Up</router-link
        >

        <router-link to="/login" v-if="!$store.state.authenticated"
          >Login</router-link
        >
        <router-link to="/create">Create</router-link>
        <button
          @click="submitForm"
          v-if="$store.state.authenticated"
          class="delete"
        >
          Logout
        </button>
      </div>
    </div>

    <router-view />
    <div></div>
    <div class="product">
      <div
        :key="element.title"
        v-for="element in searchedProducts"
        @click="getDetails(element.id)"
      >
        <div v-if="searched && searchedProducts && $route.path === '/'">
          <h1>{{ element.title }}</h1>
          <img :src="element.image" alt="post" class="phone" />
        </div>
      </div>
    </div>
    <footer>
      <div class="footer">
        <h3>Dbuy</h3>
        <p>Sell it.</p>
        <ul class="socials">
          <li>
            <a href="https://www.facebook.com/abidurrahman.dipta"
              ><img src="https://i.imgur.com/WU2QIzp.png" alt="facebook"
            /></a>
            <a href="https://github.com/dipta3214"
              ><img src="https://i.imgur.com/xPR8CjH.png" alt="github"
            /></a>
            <a href="https://www.linkedin.com/in/abidurrahmandipta/"
              ><img src="https://i.imgur.com/t4xt0xL.png" alt="LinkdIn"
            /></a>
            <a href="https://www.instagram.com/diiptoo/"
              ><img src="https://i.imgur.com/SLGbQRQ.png" alt="Instagram"
            /></a>
          </li>
        </ul>
      </div>
      <div class="footer-ending">
        <p>copyright &copy;2022 Dbuy. Designed by <span>Abidur </span></p>
      </div>
    </footer>
  </div>
</template>

<script>
import axios from 'axios';
const BASE_URL = process.env.VUE_APP_API_URL;
export default {
  name: 'App',
  data: () => ({
    click: false,
    search: '-',
    searchedProducts: '',
    productsApp: '',
    categories: '',
    categoriesProducts: null,
    main: true
  }),
  beforeCreate() {
    this.$store.commit('initializeStore');

    const access = this.$store.state.access;

    if (access) {
      axios.defaults.headers.common['Authorization'] = 'JWT ' + access;
    } else {
      axios.defaults.headers.common['Authorization'] = '';
    }
  },
  mounted: async function () {
    await this.getProducts();
    await this.getCategories();
    setInterval(() => {
      this.getAccess();
    }, 59000);
  },
  methods: {
    handleChange(e) {
      this[e.target.name] = e.target.value;
    },
    submitForm(e) {
      e.preventDefault();
      this.$store.commit('removeToken');
      axios.defaults.headers.common['Authorization'] = '';
      localStorage.clear();

      window.location.reload();
    },
    // Followed this youtube tutorial for the JWT auth https://youtu.be/IsOtVyYbPto
    getAccess() {
      axios
        .post(`${BASE_URL}/api/v1/jwt/refresh/`, {
          refresh: this.$store.state.refresh
        })
        .then((res) => {
          console.log(res.data.access);
          const access = res.data.access;
          // const refresh = res.data.refresh;
          localStorage.setItem('access', access);
          // localStorage.setItem('refresh', refresh);
          this.$store.commit('setAccess', access);
          // this.$store.commit('setRefresh', refresh);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    filter() {
      this.click = !this.click;
    },
    restart() {
      window.location.reload();
    },

    async searchProducts() {
      if (this.$route.path !== '/') {
        this.$router.push('/');
      }
      const res = await axios.get(`${BASE_URL}/products?search=${this.search}`);
      this.searchedProducts = res.data;
      this.searched = true;
      this.catClick = false;
      this.$store.state.main = false;
    },
    getDetails(id) {
      this.$router.push(`/products/${id}`);
    },
    async getProducts() {
      const res = await axios.get(`${BASE_URL}/products`);
      this.productsApp = res.data;
    },
    async getCategories() {
      const res = await axios.get(
        `${BASE_URL}/products?category=${this.categories}`
      );
      this.categoriesProducts = res.data;
      this.searched = false;
      this.catClick = true;
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e52;
  box-sizing: border-box;
}

footer {
  background-color: #2c3e52;
  color: white;
  height: auto;
  width: 100vw;
  /* position: absolute;
  bottom: 0;
  left: 0;
  right: 0; */
}

.footer {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  text-align: center;
  margin-bottom: 0;
}

.search {
  width: 600px;
  padding: 6px 16px;
}

.footer h3 {
  font-size: 1.8rem;
  font-weight: 400;
  text-transform: capitalize;
  line-height: 1rem;
}

.footer p {
  max-width: 500px;
  margin: 10px auto;
  line-height: 14px;
  font-size: 14px;
}

.socials {
  list-style: none;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 1rem 0 3rem 0;
}

.socials li {
  margin: 0 10px;
}

.socials a {
  text-decoration: none;
  color: #fff;
}

body {
  margin: 0;
  padding: 0;
}

#nav {
  padding: 31px;
  display: flex;
  justify-content: space-between;
  align-content: center;
}

#nav a {
  font-weight: bold;
  color: #2c3e51;
  text-decoration: none;
}

.navTwo a {
  padding: 1rem;
}

.toggle-button {
  position: absolute;
  top: 2rem;
  right: 1rem;
  display: none;
  flex-direction: column;
  justify-content: space-between;
  width: 30px;
  height: 21px;
}

.toggle-button .bar {
  height: 3px;
  width: 100%;
  background-color: black;
  border-radius: 10px;
}

.delete {
  -moz-box-shadow: inset 0px 1px 0px 0px #b13939;
  -webkit-box-shadow: inset 0px 1px 0px 0px #b13939;
  box-shadow: inset 0px 1px 0px 0px #a02222;
  background-color: #c12b2b;
  border: 1px solid #5e0d0d;
  display: inline-block;
  cursor: pointer;
  color: #ffffff;
  padding: 8px 18px;
  text-decoration: none;
  font: 12px Arial, Helvetica, sans-serif;
}
.delete:hover {
  background: linear-gradient(to bottom, #c92d2d 5%, #8a1a1a 100%);
  background-color: #bd3636;
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

@media (max-width: 1165px) {
  .search {
    width: 300px;
  }
}

@media (max-width: 810px) {
  .search {
    width: 200px;
  }
}

@media (max-width: 660px) {
  .search {
    width: 100px;
  }
}

@media (max-width: 450px) {
  .search-bar {
    display: none;
  }

  .toggle-button {
    display: flex;
  }

  /* .navTwo {
    display: none;
  } */

  #nav {
    flex-direction: column;
    /* align-items: flex-start; */
  }

  .navTwo {
    display: none;
  }

  .navOne {
    display: flex;
    justify-content: flex-start;
  }

  .navTwo a {
    padding: 0.5rem 1rem;
    width: 100%;
  }

  .navTwo.active {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    transition: 0.5s;
  }
}

#nav a.router-link-exact-active {
  color: #42b984;
}
</style>
