<template>
  <div class="signup">
    <h1>Sign Up</h1>
    <form @submit.prevent="submitForm">
      <label for="username">Username: </label>
      <input type="text" name="username" v-model="username" />
      <label for="email">Email: </label>
      <input type="email" name="email" v-model="email" />
      <label for="password">Password: </label>
      <input type="password" name="password" v-model="password" />
      <label for="phone">Phone: </label>
      <input type="phone" name="phone" v-model="phone" />
      <label for="insta">Instagram username: </label>
      <input type="insta" name="insta" v-model="insta" />
      <button type="submit">Sign Up</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
const BASE_URL = process.env.VUE_APP_API_URL;
export default {
  name: 'SignUp',
  data() {
    return {
      username: ``,
      email: ``,
      password: ``,
      phone: ``,
      insta: ``
    };
  },
  methods: {
    submitForm() {
      axios.post(`${BASE_URL}/api/v1/users/`, {
        username: this.username,
        email: this.email,
        password: this.password
      });
      this.$router.push('/login');
    }
  }
};
</script>