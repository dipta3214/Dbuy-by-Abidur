<template>
  <div class="signup">
    <h1>Sign Up</h1>
    <form @submit.prevent="submitForm">
      <label for="username">Username: </label>
      <input type="text" name="username" v-model="username" />
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
      password: ``
    };
  },
  methods: {
    submitForm() {
      const formData = {
        username: this.username,
        password: this.password
      };

      axios
        .post('http://localhost:8000/api/v1/users/', formData)
        .then((response) => {
          console.log(response);
          this.$router.push('/');
        })
        .catch((error) => {
          console.log(error);
        });
    }
  }
};
</script>