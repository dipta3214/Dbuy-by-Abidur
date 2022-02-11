<template>
  <div class="signup">
    <div>Registration</div>
    <form @submit.prevent="submitForm">
      <div>
        <label for="username">Username: </label>
        <input type="text" name="username" v-model="username" />
      </div>
      <div>
        <label for="email">Email: </label>
        <input type="email" name="email" v-model="email" />
      </div>
      <div>
        <label for="password">Password: </label>
        <input type="password" name="password" v-model="password" />
      </div>
      <div>
        <label for="phone">Phone: </label>
        <input type="phone" name="phone" v-model="phone" />
      </div>
      <div>
        <label for="insta">Instagram username: </label>
        <input type="insta" name="insta" v-model="insta" />
      </div>
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
      axios.post(`${BASE_URL}/contacts/`, {
        username: this.username,
        email: this.email,
        phone: this.phone,
        instagram_username: this.insta
      });
      this.$router.push('/login');
    }
  }
};
</script>