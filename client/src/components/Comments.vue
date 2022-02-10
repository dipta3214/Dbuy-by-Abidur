<template>
  <div>
    <h2>new</h2>
    <div :key="element.id" v-for="element in comments">
      <div v-if="parseInt($route.params.id) === element.product_id">
        <h3>{{ element.username }}</h3>
        <p>{{ element.content }}</p>
        <button @click="deleteComment(element.id)">Delete</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Comment',
  data: () => ({
    comments: null
  }),
  mounted: async function () {
    await this.getComments();
  },
  methods: {
    async getComments() {
      const res = await axios.get(`http://localhost:8000/comments/`);
      this.comments = res.data;
    },
    async deleteComment(element) {
      await axios.delete(`http://localhost:8000/comments/${element}`);
    }
  }
};
</script>