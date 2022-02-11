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
      <button type="submit">Sign Up</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'SignUp',
  data() {
    return {
      username: ``,
      email: ``,
      password: ``
    };
  },
  methods: {
    submitForm() {
      axios.post('http://localhost:8000/api/v1/users/', {
        username: this.username,
        email: this.email,
        password: this.password
      });
      this.$router.push('/login');
    }
  }
};
</script>