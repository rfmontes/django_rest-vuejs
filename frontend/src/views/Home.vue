<template>
    <NavBar>
        <div slot="slot-pagina" class="content-pagina">
            <div class="container">
                <p class="titulo-pagina">Home</p>
            </div>
        </div>
    </NavBar>
</template>


<script>
import NavBar from '../components/NavBar.vue'

export default {
  name: 'Home',

  components: {
    NavBar,
  }
    
}
</script>


<style scoped>


</style>