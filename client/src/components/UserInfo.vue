<template>
  <div></div>
</template>

<script>
import axios from 'axios';
const BASE_URL = process.env.VUE_APP_API_URL;
export default {
  name: 'Userinfo',
  data: () => ({
    seller: ''
  }),
  mounted: async function () {
    await this.getInfo();
  },
  methods: {
    async getInfo() {
      const res = await axios.get(`${BASE_URL}/contacts/`);
    }
  }
};
</script>