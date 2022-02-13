<template>
  <div class="login">
    <form @submit.prevent="submitForm" class="form">
      <h1>Log in</h1>
      <ul>
        <li>
          <input
            type="text"
            name="username"
            v-model="username"
            placeholder="Username"
            class="field-style field-full align-none"
          />
        </li>
        <li>
          <input
            type="password"
            name="password"
            v-model="password"
            placeholder="Password"
            class="field-style field-full align-none"
          />
        </li>

        <li>
          <input type="submit" value="Login" />
        </li>
      </ul>
      <p>Don't have an account? <a href="/signup">Sign Up</a></p>
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
          // window.location.reload();
        })
        .catch((error) => {
          console.log(error);
        });
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