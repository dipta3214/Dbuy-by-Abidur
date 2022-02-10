import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import ProductDetails from '../components/ProductDetails.vue'
import Login from '../views/Login.vue'
import SignUp from '../views/SignUp.vue'
import CreateProduct from '../components/CreateProduct.vue'
import ProductList from '../components/ProductList'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/products',
    name: 'ProductList',
    component: ProductList
  },
  {
    path: '/products/:id',
    name: 'ProductDetails',
    component: ProductDetails
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/create',
    name: 'CreateProduct',
    component: CreateProduct
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
