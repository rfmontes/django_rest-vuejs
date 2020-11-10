<template>
    <NavBar>
        <div slot="slot-pagina" class="content-pagina">
            <div class="container">
                <div>
                    <p class="titulo-pagina">Cadastro de Chuteiras</p>
                    <div class="mt-5 cadastro">
                        <b-form-group label="Cor" label-for="cor">
                            <b-form-input id="cor" v-model="chuteira.cor"></b-form-input>
                        </b-form-group>
                        
                        <b-form-group label="Fabricante" label-for="fabr">
                            <b-form-input id="fabr" v-model="chuteira.fabricante"></b-form-input>
                        </b-form-group>
                        
                        <b-form-group label="Tipo" label-for="tipo">
                            <b-form-select id="tipo" v-model="chuteira.tipo" :options="options"></b-form-select>
                        </b-form-group>  
                        
                        <b-form-group label="Preço" label-for="preco">
                            <b-form-input id="preco" v-model="chuteira.preco"></b-form-input>
                        </b-form-group>
                        
                        <b-form-group label="Quantidade" label-for="quant">
                            <b-form-input id="quant" v-model="chuteira.quantidade"></b-form-input>
                        </b-form-group>

                        <b-button variant='primary' class="m-2" @click="sendForm" :disabled="loading">Enviar</b-button>
                        <b-button variant='primary' class="m-2" to="/chuteiras" :disabled="loading">Cancelar</b-button>
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
    nome: 'EditChuteiras',

    components: {
        NavBar,
    },
    data() {
        return {
            loading: false,
            chuteira: {
                cor: '',
                fabricante: '',
                tipo: '',
                preco: '',
                quantidade: '',
            },
            options: [
                { value: 'Campo', text: 'Campo'},
                { value: 'Society', text: 'Society'},
                { value: 'Salão', text: 'Salão'}
            ]
        }
    },
    mounted() {
        if (!this.$route.params.id) {
            return;
        }
        axios.get('http://127.0.0.1:8000/produtos/chuteiras/' + this.$route.params.id)
        .then(res => {
            this.chuteira = res.data;
        });
    },
    methods: {
        sendForm() {
            this.loading = true;

            if (this.$route.params.id) {
                axios.put('http://127.0.0.1:8000/produtos/chuteiras/' + this.$route.params.id + '/', this.chuteira)
                .then(() => {
                    this.loading = false;
                    this.$router.push('/chuteiras');
                })
                .catch(() => {
                    this.loading = false;
                    alert('Houve um erro');
                })
            } else {
                axios.post('http://127.0.0.1:8000/produtos/chuteiras/', this.chuteira)
                .then(() => {
                    this.loading = false;
                    this.$router.push('/chuteiras');
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