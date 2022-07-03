<template>
  <div class="home">
    
    <section class="hero is-medium has-text-left mt-6 mb-6">
      <div class="hero-body">
        <p class="title has-text-white">
          Shop
        </p>
        <p class="subtitle has-text-white">
          Primary subtitle
        </p>
      </div>
    </section>

    <div class="tabs is-centered is-large mt-6 mb-6">
      <ul>
        <li><a>Last products</a></li>
        <li><a>All products</a></li>
        <li><a>Types</a></li>
        <li><a>Brands</a></li>
      </ul>
    </div>

    <div class="columns is-multiline box">
      
        <ProductBox
          v-for="product in latestProducts"
          v-bind:key="product.id"
          v-bind:product="product" />
        
    </div>
  </div>
</template>

<script>

import axios from 'axios'

import ProductBox from '@/components/ProductBox'

export default {
  name: 'HomeView',

  data () {
    return {
      latestProducts: []
    }
  },
  components: {
    ProductBox
  },
  mounted() {
    this.getLatestProducts()

    document.title = 'Home | Shop '
  },
  methods: {
    getLatestProducts() {
      axios
        .get('http://127.0.0.1:8000/api/v1/latest-products/')
        .then(response => {
          this.latestProducts = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>

<style>

.hero-body {
  
  background-image: linear-gradient(rgba(105, 102, 102, 0.5), rgba(0, 0, 0, 0.5)), url("https://imageup.ru/img193/3177012/6.jpg");
  background-position: 0px 0px, center;
  background-repeat: no-repeat;
}

</style>