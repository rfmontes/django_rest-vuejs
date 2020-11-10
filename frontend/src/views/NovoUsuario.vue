<template>
    <div class="container">
        <h1>Novo usuário</h1>
        <form @submit.prevent="enviarForm">
            <div class="form-group">
                <label for="nome">Nome</label>
                <input type="text" class="form-control" v-model="usuario.nome">
            </div>
            <div class="form-group">
                <label for="email">E-mail</label>
                <input type="text" class="form-control" v-model="usuario.email">
            </div>
            <div class="form-group">
                <label for="senha">Senha</label>
                <input type="password" class="form-control" v-model="usuario.senha">
            </div>
            <button class="btn btn-primary mr-3" type="submit">Salvar</button>
            <b-button variant='danger' class="mr-3" to="/">Cancelar</b-button>
        </form>
    </div>

</template>

<script>
export default {

    data: function() {
        return {
            usuario: {
                nome: '',
                email: '',
                senha: ''
            }
        }
    },
    methods: {
        enviarForm() {
            console.log(this.usuario)
        }
    }

}
</script>


<style scoped>

</style>