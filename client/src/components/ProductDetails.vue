<template>
  <div>
    <div
      v-if="click"
      v-bind:class="{ active: !confirm, 'non-opacity': confirm }"
    >
      <UpdateProduct />
    </div>
    <div v-if="!click">
      <div class="buttons">
        <div>
          <button class="delete_button" @click="confirmWindow">
            Seller Contact
          </button>
          <button @click="clickTrue">
            <img src="https://i.imgur.com/A4CD9e2.png" alt="update" />
          </button>
          <button @click="deleteProduct">
            <img src="https://i.imgur.com/RaQAlDa.png" alt="delete" />
          </button>
        </div>
      </div>
      <div v-if="details" class="grid">
        <div class="img"><img :src="details.image" alt="new" /></div>
        <div class="flex">
          <div>
            <h1>{{ details.title }}</h1>
            <h4>Price: {{ details.price }}</h4>
            <h3>Brand: {{ details.brand }}</h3>
            <h3>Category: {{ details.category }}</h3>
            <h3>Location: {{ details.location }}</h3>
            <h3>Color: {{ details.color }}</h3>
            <h3>Condition: {{ details.condition }}</h3>
            <p>{{ details.description }}</p>
          </div>
        </div>
      </div>
      <CreateComment />
      <Comments />
    </div>
    <section v-if="confirm">
      <div class="confirm">
        <div class="confirm__window">
          <div class="confirm__titlebar">
            <span class="confirm__title">User Information</span>
            <button @click="unConfirm()" class="confirm__close">X</button>
          </div>
          <div class="confirm__content">
            <UserInfo v-bind:username="details.username" />
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios';
import UpdateProduct from './UpdateProduct.vue';
import Comments from './Comments.vue';
import CreateComment from './CreateComment.vue';
import UserInfo from './UserInfo.vue';
const BASE_URL = process.env.VUE_APP_API_URL;
export default {
  name: 'ProductDetails',
  props: ['title'],
  components: {
    UpdateProduct,
    Comments,
    CreateComment,
    UserInfo
  },
  data: () => ({
    details: null,
    click: false,
    confirm: false,

    edited: false
  }),
  mounted: async function () {
    await this.getDetails();
  },
  methods: {
    async getDetails() {
      const res = await axios.get(
        `${BASE_URL}/products/${this.$route.params.id}`
      );
      this.details = res.data;
      //   console.log(this.details.id);
    },
    async deleteProduct() {
      await axios.delete(`${BASE_URL}/products/${this.$route.params.id}`);
      this.$router.push(`/`);
    },
    clickTrue() {
      this.click = true;
    },

    // For the modal
    confirmWindow() {
      this.confirm = true;
    },
    unConfirm() {
      this.confirm = false;
    },
    startEdit() {
      this.edited = true;
    }
  }
};
</script>

<style scoped>
.grid {
  display: grid;
  grid-template-columns: 4fr 3fr;
  grid-template-rows: 1fr;
}

.grid img {
  width: 400px;
  margin-top: 10px;
}

.flex {
  display: flex;
  justify-content: flex-start;
}

.flex div {
  text-align: left;
}

.buttons {
  display: flex;
  justify-content: flex-end;
}

.buttons div button {
  padding: 6px;
  margin: 12px 8px;
}

.buttons div button img {
  width: 25px;
}

/* Modal */

.non-opacity {
  opacity: 0.1;
}

.confirm {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
  padding: 10px;
  box-sizing: border-box;
  animation-name: confirm---open;
  animation-duration: 0.2s;
  animation-fill-mode: forwards;

  display: flex;
  align-items: center;
  justify-content: center;
}

.confirm__window {
  width: 100%;
  max-width: 600px;
  background: white;
  font-size: 14px;
  border-radius: 5px;
  overflow: hidden;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);

  opacity: 0;
  transform: scale(0.75);
  animation-name: confirm__window---open;
  animation-duration: 0.2s;
  animation-fill-mode: forwards;
  animation-delay: 0.2s;
}

.confirm__titlebar,
.confirm__content {
  padding: 1.25em;
  font-size: larger;
  font-family: bolder;
}

.confirm__titlebar {
  background-color: #216288;
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.confirm__title {
  font-weight: bold;
  font-size: 1.1em;
}

.confirm__close {
  background: none;
  outline: none;
  border: none;
  transform: scale(2.5);
  color: #ffffff;
  transition: color 0.2s;
}

.confirm__content {
  line-height: 2.8em;
}

@keyframes confirm---open {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes confirm__window---open {
  to {
    opacity: 1;
    transform: scale(1);
  }
}

/* Modal Ending */

@media (max-width: 450px) {
  .grid img {
    width: 300px;
  }

  .grid {
    display: grid;
    grid-template-columns: 1fr;
  }

  .flex {
    margin: 10px 35px;
  }

  .buttons {
    margin-bottom: 20px;
  }

  .buttons div button img {
    width: 20px;
  }
}
</style>