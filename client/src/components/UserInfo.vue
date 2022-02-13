<template>
  <div>
    <div :key="element.id" v-for="element in seller">
      <div v-if="element.username === username">
        <p v-if="element.email">Email : {{ element.email }}</p>
        <p v-if="element.phone">Phone : {{ element.phone }}</p>
        <p v-if="element.instagram_username">
          Instagram Username : {{ element.instagram_username }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
const BASE_URL = process.env.VUE_APP_API_URL;
export default {
  name: 'Userinfo',
  props: ['username'],
  data: () => ({
    seller: ''
  }),
  mounted: async function () {
    await this.getInfo();
  },
  methods: {
    async getInfo() {
      const res = await axios.get(`${BASE_URL}/contacts/`);
      this.seller = res.data;
    }
  }
};
</script>