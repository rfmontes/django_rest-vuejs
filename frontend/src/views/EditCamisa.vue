<template>
    <NavBar>
        <div slot="slot-pagina" class="content-pagina">
            <div class="container">
                <div>
                    <p class="titulo-pagina">Cadastro de Camisas</p>
                    <div class="mt-5 cadastro">
                        <b-form-group label="Time" label-for="time">
                            <b-form-input id="time" v-model="camisas.time"></b-form-input>
                        </b-form-group>

                        <b-form-group label="Cor" label-for="cor">
                            <b-form-input id="cor" v-model="camisas.cor"></b-form-input>
                        </b-form-group>
                        
                        <b-form-group label="Fabricante" label-for="fabr">
                            <b-form-input id="fabr" v-model="camisas.fabricante"></b-form-input>
                        </b-form-group>
                        
                        <b-form-group label="Preço" label-for="preco">
                            <b-form-input id="preco" v-model="camisas.preco"></b-form-input>
                        </b-form-group>
                        
                        <b-form-group label="Quantidade" label-for="quant">
                            <b-form-input id="quant" v-model="camisas.quantidade"></b-form-input>
                        </b-form-group>

                        <b-button variant='primary' class="m-2" @click="sendForm" :disabled="loading">Enviar</b-button>
                        <b-button variant='primary' class="m-2" to="/camisas" :disabled="loading">Cancelar</b-button>
                    </div>
                </div>
            </div>
        </div>
    </NavBar>
</template>

<script>
import NavBar from '../components/NavBar.vue'
import axios from 'axios'

export default {
    nome: 'EditCamisas',

    components: {
        NavBar,
    },
    data() {
        return {
            loading: false,
            camisas: {
                time: '',
                cor: '',
                fabricante: '',
                preco: '',
                quantidade: '',
            }
        }
    },
    mounted() {
        if (!this.$route.params.id) {
            return;
        }
        axios.get('http://127.0.0.1:8000/produtos/camisas/' + this.$route.params.id)
        .then(res => {
            this.camisas = res.data;
        });
    },
    methods: {
        sendForm() {
            this.loading = true;

            if (this.$route.params.id) {
                axios.put('http://127.0.0.1:8000/produtos/camisas/' + this.$route.params.id + '/', this.camisas)
                .then(() => {
                    this.loading = false;
                    this.$router.push('/camisas');
                })
                .catch(() => {
                    this.loading = false;
                    alert('Houve um erro');
                })
            } else {
                axios.post('http://127.0.0.1:8000/produtos/camisas/', this.camisas)
                .then(() => {
                    this.loading = false;
                    this.$router.push('/camisas');
                })
                .catch(() => {
                    this.loading = false;
                    alert('Houve um erro');
                })
            }
        }
    }
}
</script>


<style scoped>

</style>