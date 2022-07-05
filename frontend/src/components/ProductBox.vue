<template>
    <div 
      class="column is-3">
        <div class="box">
          <figure class="image is-5by3 mb-4">
            <img :src="product.photos">
          </figure>

            <div class="columns is-12 mt-2 mb-2 has-text-centered">
                <div class="column is-4">
                    <h3 class="is-size-4">{{ product.type }}</h3>
                </div>
                <div class="column is-4">
                    <h3 class="is-size-4">{{ product.brand }}</h3>
                </div>
                <div class="column is-4">
                    <h3 class="is-size-4">{{ product.name }}</h3>
                </div>
                

            </div>
            

            <div class="columns is-12 mt-2 mb-2 has-text-centered">
                <div class="column is-6">
                <p class="is-size-6 has-text-gray">Price: {{ product.price }}</p>
                </div>
                <div class="column is-6">
                <p class="is-size-6 has-text-gray">Disc: {{ product.discount.discount_price }}</p>
                </div>
            </div>
          </div>
    </div>

</template>

<script>
export default {
    name: 'ProductBox',
    props: {
        product: Object 
    },
    methods: {
      
    }
}

</script>

<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
    
  }
</style>