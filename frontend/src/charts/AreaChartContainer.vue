<template>
  <div class="container">
    <AreaChart
      v-if="loaded"
      :chartdata="chartdata"
      :options="options"/>
  </div>
</template>

<script>
import axios from 'axios';
import AreaChart from '../charts/AreaChart.vue' 

export default {
  name: 'AreaChartContainer',
  components: { 
    AreaChart 
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
      let precos = data.results.map(function(e){
        return e.preco
      })

      this.chartdata = {
        labels: times,
        datasets: [
          {
              label: 'Preço em R$',
              backgroundColor: [
                  'rgba(255, 99, 132, 0.3)',
                  'rgba(255, 99, 132, 0.3)',
                  'rgba(255, 99, 132, 0.3)',
                  'rgba(255, 99, 132, 0.3)',
                  'rgba(255, 99, 132, 0.3)',
                  'rgba(255, 99, 132, 0.3)',
                  'rgba(255, 99, 132, 0.3)',
                  'rgba(255, 99, 132, 0.3)',
                  'rgba(255, 99, 132, 0.3)',
                  'rgba(255, 99, 132, 0.3)',
                  'rgba(255, 99, 132, 0.3)'
              ],
              borderColor: [
                  'rgba(255, 99, 132, 1)',
                  'rgba(255, 99, 132, 1)',
                  'rgba(255, 99, 132, 1)',
                  'rgba(255, 99, 132, 1)',
                  'rgba(255, 99, 132, 1)',
                  'rgba(255, 99, 132, 1)',
                  'rgba(255, 99, 132, 1)',
                  'rgba(255, 99, 132, 1)',
                  'rgba(255, 99, 132, 1)',
                  'rgba(255, 99, 132, 1)',
                  'rgba(255, 99, 132, 1)'
              ],
              borderWidth: 1,
              data: precos
          },
        ]
      }
      this.options = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          yAxes: [{
              ticks: {
                  beginAtZero: true
              }
          }]
        }
      }
      this.loaded = true

    } catch (e) {
      console.error(e)
    }
  }
}
</script>