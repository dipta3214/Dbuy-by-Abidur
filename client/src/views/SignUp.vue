<template>
  <div class="body">
    <div class="signup">
      <h1>Registration</h1>
      <form @submit.prevent="submitForm" class="form">
        <ul>
          <li>
            <input
              type="text"
              name="username"
              v-model="username"
              placeholder="username"
              class="field-style field-split align-left"
            />

            <input
              type="email"
              name="email"
              v-model="email"
              placeholder="email"
              class="field-style field-split align-right"
            />
          </li>

          <li>
            <input
              type="password"
              name="password"
              v-model="password"
              placeholder="password"
              class="field-style field-full align-none"
            />
          </li>

          <li>
            <input
              type="phone"
              name="phone"
              v-model="phone"
              placeholder="Phone(optional)"
              class="field-style field-split align-left"
            />

            <input
              type="insta"
              name="insta"
              v-model="insta"
              placeholder="Instagram(optional)"
              class="field-style field-split align-right"
            />
          </li>
          <li>
            <input type="submit" value="Sign up" />
          </li>
        </ul>
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
/* Style design was inspired from sanwebe.com */
.form {
  max-width: 450px;
  background: #fafafa;
  padding: 30px;
  margin: 50px auto;
  box-shadow: 1px 1px 25px rgba(0, 0, 0, 0.35);
  border-radius: 10px;
  border: 6px solid #305a72;
}
.form ul {
  padding: 0;
  margin: 0;
  list-style: none;
}
.form ul li {
  display: block;
  margin-bottom: 10px;
  min-height: 35px;
}
.form ul li .field-style {
  box-sizing: border-box;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  padding: 8px;
  outline: none;
  border: 1px solid #b0cfe0;
}
.form ul li .field-style:focus {
  box-shadow: 0 0 5px #b0cfe0;
  border: 1px solid #b0cfe0;
}
.form ul li .field-split {
  width: 49%;
}
.form ul li .field-full {
  width: 100%;
}
.form ul li input.align-left {
  float: left;
}
.form ul li input.align-right {
  float: right;
}

.form ul li input[type='button'],
.form ul li input[type='submit'] {
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
}
.form ul li input[type='button']:hover,
.form ul li input[type='submit']:hover {
  background: linear-gradient(to bottom, #2d77a2 5%, #337da8 100%);
  background-color: #28739e;
}

@media (max-width: 450px) {
  .form {
    max-width: 250px;
  }
}
</style>