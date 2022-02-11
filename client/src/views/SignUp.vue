<template>
  <div class="body">
    <div class="signup">
      <div class="title">Registration</div>
      <form @submit.prevent="submitForm">
        <div class="user-detail">
          <div class="input-box">
            <label for="username">Username: </label>
            <input type="text" name="username" v-model="username" />
          </div>
          <div class="input-box">
            <label for="email">Email: </label>
            <input type="email" name="email" v-model="email" />
          </div>
          <div class="input-box">
            <label for="password">Password: </label>
            <input type="password" name="password" v-model="password" />
          </div>
          <div class="input-box">
            <label for="phone">Phone: </label>
            <input
              type="phone"
              name="phone"
              v-model="phone"
              placeholder="optional"
            />
          </div>
          <div class="input-box">
            <label for="insta">Instagram username: </label>
            <input
              type="insta"
              name="insta"
              v-model="insta"
              placeholder="optional"
            />
          </div>
          <div class="button">
            <button type="submit">Sign Up</button>
          </div>
        </div>
      </form>
    </div>
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

<style scoped>
.body {
  height: 100vh;

  padding: 10px;
  background: linear-gradient(#e1e6eb, #fcfcfc, #dae7f5);
}

.signup {
  display: 'flex';
  justify-content: center;
  align-items: center;
  max-width: 700px;
  width: 100%;
  background: #fff;
  padding: 25px 30px;
  border-radius: 5px;
}

.signup .title {
  font-size: 25px;
  font-weight: 500;
  position: relative;
}

.signup .title:before {
  content: '';
  position: absolute;
  height: 3px;
  width: 30px;
  background: #9b59b6;
}

.signup form .user-detail {
  margin: 20px 0 12px 0;
  display: flex;
  flex-wrap: wrap;
}

.form .user-detail .input-box {
  margin-bottom: 15px;
  width: calc(100% / 2 - 20px);
}

.user-detail .input-box label {
  display: block;
  font-weight: 500;
  margin-bottom: 5px;
}

.user-detail .input-box input {
  height: 45px;
  width: 100%;
  outline: none;
  border-radius: 5px;
  border: 1px solid #ccc;
  padding-left: 15px;
  font-size: 16px;
  border-bottom-width: 2px;
  transition: all 0.3s ease;
}

.user-detail .input-box input:focus,
.user-detail .input-box input:valid {
  border-color: #ccc;
}

form .button {
  height: 45px;
  margin: 45px 0;
}
</style>