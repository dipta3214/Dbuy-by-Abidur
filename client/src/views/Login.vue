<template>
  <div class="login">
    <h1>Log in</h1>
    <form @submit.prevent="submitForm">
      <label for="username">Username: </label>
      <input type="text" name="username" v-model="username" />
      <label for="password">Password: </label>
      <input type="password" name="password" v-model="password" />
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
const BASE_URL = process.env.VUE_APP_API_URL;
export default {
  name: 'Login',
  data() {
    return {
      username: ``,
      password: ``
    };
  },
  methods: {
    // Followed this youtube tutorial for the JWT auth https://youtu.be/IsOtVyYbPto
    submitForm() {
      axios.defaults.headers.common['Authorization'] = '';
      localStorage.removeItem('access');

      axios
        .post(`${BASE_URL}/api/v1/jwt/create/`, {
          username: this.username,
          password: this.password
        })
        .then((res) => {
          const access = res.data.access;
          const refresh = res.data.refresh;

          this.$store.commit('setAccess', access);
          this.$store.commit('setRefresh', refresh);

          axios.defaults.headers.common['Authorization'] = 'JWT ' + access;
          localStorage.setItem('access', access);
          localStorage.setItem('refresh', refresh);

          this.$router.push('/');
        })
        .catch((error) => {
          console.log(error);
        });
    }
  }
};
</script>