<template>
  <div id="app">
    <div id="nav">
      <div class="navOne">
        <router-link to="/"><a href="">Home</a></router-link>
      </div>
      <div></div>
      <a @click="filter" class="toggle-button">
        <span class="bar"></span>
        <span class="bar"></span>
        <span class="bar"></span>
      </a>
      <div class="navTwo" v-bind:class="{ active: click }">
        <router-link to="/products"><a href="">Products</a></router-link>
        <router-link to="/about"><a href="">About</a></router-link>
        <router-link to="/signup" v-if="!$store.state.authenticated"
          ><a href="">Sign Up</a></router-link
        >

        <router-link to="/login" v-if="!$store.state.authenticated"
          ><a href="">Login</a></router-link
        >
        <router-link to="/create">Create</router-link>
        <button @click="submitForm" v-if="$store.state.authenticated">
          <a href="">Logout</a>
        </button>
      </div>
    </div>
    <router-view />
  </div>
</template>

<script>
import axios from 'axios';
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
    getAccess() {
      const accessData = {
        refresh: this.$store.state.refresh
      };

      axios
        .post('http://localhost:8000/api/v1/jwt/refresh/', accessData)
        .then((response) => {
          const access = response.data.access;
          console.log(access);

          localStorage.setItem('access', access);
          // localStorage.setItem('id', this.$store.state.id);
          this.$store.commit('setAccess', access);
        })
        .catch((error) => {
          console.log(error);
        });
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

@media (max-width: 400px) {
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
