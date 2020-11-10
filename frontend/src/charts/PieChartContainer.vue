<template>
  <div class="container">
    <PieChart
      v-if="loaded"
      :chartdata="chartdata"
      :options="options"/>
  </div>
</template>

<script>
import axios from 'axios';
import PieChart from '../charts/PieChart.vue' 

export default {
  name: 'PieChartContainer',
  components: { 
    PieChart 
  },
  data: () => ({
    loaded: false,
    chartdata: null,
    options: null
  }),

  async mounted () {
    this.loaded = false
    try {
      const { data } = await axios.get('http://127.0.0.1:8000/produtos/camisas/')

      let times = data.results.map(function(e){
      return e.time
      })
      let quantidades = data.results.map(function(e){
        return e.quantidade
      })

      this.chartdata = {
        labels: times,
        datasets: [
          {
              label: 'Preço em R$',
              backgroundColor: [
                'rgba(255, 99, 132, 0.5)',
                'rgba(54, 162, 235, 0.5)',
                'rgba(255, 206, 86, 0.5)',
                'rgba(75, 192, 192, 0.5)',
                'rgba(153, 102, 255, 0.5)',
                'rgba(255, 159, 64, 0.5)',
                'rgba(255, 99, 132, 0.5)',
                'rgba(54, 162, 235, 0.5)',
                'rgba(255, 206, 86, 0.5)',
                'rgba(75, 192, 192, 0.5)',
                'rgba(153, 102, 255, 0.5)',
                'rgba(255, 159, 64, 0.5)'
              ],
              borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
              ],
              borderWidth: 1,
              data: quantidades
          },
        ]
      }
      this.options = {
        responsive: true,
        maintainAspectRatio: false,
      }
      this.loaded = true

    } catch (e) {
      console.error(e)
    }
  }
}

</script>