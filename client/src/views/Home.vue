<template>
  <div class="home">
    <span :src="user_data" v-if="user_data"
      ><h1>Welcome {{ user_data }}! What are you looking for?</h1></span
    >
    <form>
      <input type="text" placeholder="Enter what your looking for" />
      <button>Submit</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Home',
  data() {
    return {
      user_data: ''
    };
  },
  mounted: async function () {
    this.getMe();
  },
  methods: {
    getMe() {
      axios
        .get('http://localhost:8000/api/v1/users/me')
        .then((response) => {
          const username = response.data.username;
          const id = response.data.id;

          this.user_data = username;

          this.$store.commit('setUserId', id);
          this.$store.commit('setUsername', username);

          localStorage.setItem('id', id);
          localStorage.setItem('username', username);
        })
        .catch((error) => {
          console.log(error);
        });
    }
  }
};
</script>
