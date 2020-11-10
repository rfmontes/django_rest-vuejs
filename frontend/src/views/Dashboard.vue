<template>
    <NavBar>
        <div slot="slot-pagina" class="content-pagina">
            <div class="container">
                <p class="titulo-pagina">Dashboard</p>
                
                <div class="card mb-4">
                    <div class="card-header">
                        <i class="fas fa-chart-area mr-1"></i>
                        Axios Chart 
                    </div>
                    <div class="card-body"></div>
                </div>
                
                <div class="card mb-4">
                    <div class="card-header">
                        <i class="fas fa-chart-area mr-1"></i>
                        Area Chart 
                    </div>
                    <div class="card-body"><AreaChart/></div>
                </div>
                <div class="row">
                    <div class="col-lg-6">
                        <div class="card mb-4">
                            <div class="card-header">
                                <i class="fas fa-chart-bar mr-1"></i>
                                Bar Chart 
                            </div>
                            <div class="card-body"><BarChart/></div>
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <div class="card mb-4">
                            <div class="card-header">
                                <i class="fas fa-chart-pie mr-1"></i>
                                Pie Chart 
                            </div>
                            <div class="card-body"><PieChart/></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </NavBar>
</template>


<script>
import NavBar from '../components/NavBar.vue'
import AreaChart from '../charts/AreaChart.vue'
import BarChart from '../charts/BarChart.vue'
import PieChart from '../charts/PieChart.vue'

export default {
  name: 'Home',

  components: {
    NavBar,
    AreaChart,
    BarChart,
    PieChart,
  }
    
}
</script>


<style scoped>


</style>