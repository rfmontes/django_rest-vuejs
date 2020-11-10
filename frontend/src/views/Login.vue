<template>
<div class="main">
    <div class="login">
        <div class="content-login">
            <header>
                <h2>Login</h2>
            </header>
        
            <div class="form">
                <form @submit.prevent="enviarForm">
                    <div class="form-group">
                        <label for="email">E-mail</label>
                        <input type="text" class="form-control" v-model="usuario.email">
                    </div>
                    <div class="form-group">
                        <label for="senha">Senha</label>
                        <input type="password" class="form-control" v-model="usuario.senha">
                    </div>
                    <button class="btn btn-primary mr-3" type="submit">Entrar</button>
                </form>
            </div>
        </div>
    </div>  
</div>
</template>

<script>
export default {
    name: 'Login',

    data: function() {
        return {
            usuario: {
                email: '',
                senha: ''
            }
        }
    },
    methods: {
        enviarForm() {
            this.$router.push({name: 'home'})
        }
    }

}
</script>


<style scoped>

.login {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    background-color: ghostwhite;
}

.content-login {
    width: 390px;
    height: 400px;
    background-color: silver;
    border-radius: 7px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.form {
    width: 83%;
    margin-top: 30px;
}

</style>