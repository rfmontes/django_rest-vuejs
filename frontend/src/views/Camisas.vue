<template>
    <NavBar>
        <div slot="slot-pagina" class="content-pagina">
            <div class="container">
                <div class="text-right">
                    <b-button class="mt-2" variant="primary" to="/camisas/add">Adicionar</b-button>
                </div>
                <div>
                    <p class="titulo-pagina">Camisas</p>
                    <b-card-group deck>
                        <li class="lista m-4" v-for="c in camisas" :key="c.id">
                            <div class="card border-primary mb-3" style="max-width: 20rem;">
                                <div class="card-header" style="font-size: 23px;">{{ c.fabricante }}</div>
                                <div class="card-body text-primary">
                                    <h5 class="card-title">{{ c.time }}</h5>
                                    <p class="card-text">Cor: {{ c.cor }}</p>
                                    <p class="card-text">Fabricante: {{ c.fabricante }}</p>
                                    <p class="card-text">Quantidade: {{ c.quantidade }}</p>
                                    <p class="card-text">R$: {{ c.preco }}</p>
                                    <p class="card-text">US$: {{ c.preco_dolar }}</p>
                                    <b-button variant='primary' class="ml-2 mb-2" :to="'/camisas/' + c.id + '/edit'">Editar</b-button>
                                    <b-button variant='danger' class="ml-2 mb-2" @click="deleteItem(c.id)">Excluir</b-button>
                                </div>
                            </div>
                        </li>
                    </b-card-group>
                </div>
            </div>
        </div>
    </NavBar>
</template>

<script>
import axios from 'axios'
import NavBar from '../components/NavBar.vue'

export default {
    nome: 'Camisas',
  
    components: {
        NavBar,
    },

    data() {
        return {
            camisas: [],
        }
    },
    mounted () {
        axios.get('http://127.0.0.1:8000/produtos/camisas/')
        .then(res => {
            this.camisas = res.data.results;
        });
    },   
    methods: {
        deleteItem(camisaId) {
        if (!confirm('Você deseja realmente apagar essa Camisa?')) {
            return;
        }
        axios.delete('http://127.0.0.1:8000/produtos/camisas/' + camisaId)
            .then(() => {
            this.camisas = this.camisas.filter(l => l.id != camisaId);
            });
        }
    }
}
</script>

<style scoped>
.lista {
    list-style: none;
}
</style>