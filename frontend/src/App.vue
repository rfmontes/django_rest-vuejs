<template>
  <div>
    <router-view/>
  </div>
</template>

<script>

export default {
  name: 'App'
}
</script>

<style>

.main {
    display: flex;
    height: 100vh;
}

.content-pagina {
    width: 100%;
    height: auto;
    padding: 20px;
}

.titulo-pagina {
    font-size: 35px;
}

.cadastro {
    background-color: lightseagreen;
    padding: 30px;
    border-radius: 1%;
}

</style>
