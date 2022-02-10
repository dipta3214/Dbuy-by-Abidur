<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <router-link to="/signup">Sign Up</router-link> |
      <router-link to="/login">Login</router-link> |
      <router-link to="/create">Create</router-link> |
      <button @click="submitForm">Logout</button>
    </div>
    <router-view />
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'App',
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
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b984;
}
</style>
