<template>
  <div>
    <div :key="element.id" v-for="element in comments">
      <div
        v-if="parseInt($route.params.id) === element.product_id"
        class="comment"
      >
        <ul>
          <li>
            <h3>{{ element.username }}</h3>
          </li>
          <li>
            <p>{{ element.content }}</p>
          </li>
          <li>
            <button
              @click="deleteComment(element.id)"
              v-if="element.user_id == $store.state.id"
            >
              Delete
            </button>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
const BASE_URL = process.env.VUE_APP_API_URL;
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
      const res = await axios.get(`${BASE_URL}/comments/`);
      this.comments = res.data;
    },
    async deleteComment(element) {
      confirm('Do you wanna delete the comment?');
      if (confirm) {
        await axios.delete(`${BASE_URL}/comments/${element}`);
      }
    }
  }
};
</script>

<style scoped>
/* Style design was inspired from sanwebe.com */
.comment {
  max-width: 750px;
  background: #fafafa;
  padding: 30px;
  margin: 50px auto;
  box-shadow: 1px 1px 25px rgba(0, 0, 0, 0.35);
  border-radius: 10px;
}
.comment ul {
  padding: 0;
  margin: 0;
  list-style: none;
}
.comment ul li {
  display: block;
  margin-bottom: 10px;
  min-height: 35px;
}

.comment ul li h3,
p {
  display: flex;
}

.comment ul li button,
.comment ul li button[type='submit'] {
  float: left;
  -moz-box-shadow: inset 0px 1px 0px 0px #3985b1;
  -webkit-box-shadow: inset 0px 1px 0px 0px #3985b1;
  box-shadow: inset 0px 1px 0px 0px #4b0505;
  background-color: #c22a2a;
  border: 1px solid #d38484;
  display: inline-block;
  cursor: pointer;
  color: #ffffff;
  padding: 8px 18px;
  text-decoration: none;
  font: 12px Arial, Helvetica, sans-serif;
}
.comment ul li button:hover,
.comment ul li button[type='submit']:hover {
  background: linear-gradient(to bottom, #761d1d 5%, #bb3d45 100%);
  background-color: #ac3e3e;
}

@media (max-width: 450px) {
  .comment {
    max-width: 250px;
  }
}
</style>