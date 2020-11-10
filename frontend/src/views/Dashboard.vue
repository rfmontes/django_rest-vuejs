<template>
    <NavBar>
        <div slot="slot-pagina" class="content-pagina">
            <div class="container">
                <p class="titulo-pagina">Dashboard</p>
                
                <div class="card mb-4">
                    <div class="card-header titulo-grafico">
                        <i class="fas fa-chart-area mr-1"></i>
                        Quantidade no Estoque 
                    </div>
                    <div class="card-body"><AxiosChartContainer/></div>
                </div>
                
                <div class="card mb-4">
                    <div class="card-header titulo-grafico">
                        <i class="fas fa-chart-area mr-1"></i>
                        Preço dos Produtos
                    </div>
                    <div class="card-body"><AreaChartContainer/></div>
                </div>
                <div class="row">
                    <div class="col-lg-6">
                        <div class="card mb-4">
                            <div class="card-header titulo-grafico">
                                <i class="fas fa-chart-bar mr-1"></i>
                                Preço dos Produtos 
                            </div>
                            <div class="card-body"><BarChartContainer/></div>
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <div class="card mb-4">
                            <div class="card-header titulo-grafico">
                                <i class="fas fa-chart-pie mr-1"></i>
                                Quantidade no Estoque  
                            </div>
                            <div class="card-body"><PieChartContainer/></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </NavBar>
</template>


<script>
import NavBar from '../components/NavBar.vue'
import AxiosChartContainer from '../charts/AxiosChartContainer.vue'
import AreaChartContainer from '../charts/AreaChartContainer.vue'
import BarChartContainer from '../charts/BarChartContainer.vue'
import PieChartContainer from '../charts/PieChartContainer.vue'

export default {
  name: 'Home',

  components: {
    NavBar,
    AxiosChartContainer,
    AreaChartContainer,
    BarChartContainer,
    PieChartContainer,
  }
    
}
</script>


<style scoped>

.titulo-grafico {
    font-size: 20px;
}

</style>