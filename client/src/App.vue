<template>
  <div id="app">
    <div id="nav">
      <div class="navOne">
        <router-link to="/"><a href="">Home</a></router-link>
      </div>
      <form class="search" v-if="$route.path === '/'">
        <input
          type="text"
          placeholder="Enter what your looking for"
          name="search"
        />
        <button>Submit</button>
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
        <button @click="submitForm" v-if="$store.state.authenticated">
          Logout
        </button>
      </div>
    </div>
    <router-view />
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
    click: false
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
  mounted() {
    setInterval(() => {
      this.getAccess();
    }, 60000);
  },
  methods: {
    submitForm(e) {
      e.preventDefault();
      this.$store.commit('removeToken');
      axios.defaults.headers.common['Authorization'] = '';
      localStorage.clear();

      window.location.reload();
    },
    // Followed this youtube tutorial for the JWT auth https://youtu.be/IsOtVyYbPto
    getAccess() {
      if (this.$store.state.access !== '') {
        axios
          .post(`${BASE_URL}/api/v1/jwt/refresh/`, {
            refresh: this.$store.state.refresh
          })
          .then((res) => {
            const access = res.data.access;
            console.log(res.data.access);

            localStorage.setItem('access', access);
            this.$store.commit('setAccess', access);
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
    filter() {
      this.click = !this.click;
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

@media (max-width: 450px) {
  .search {
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
