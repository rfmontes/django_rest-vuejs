<template>
  <div class="container">
    <AxiosChart
      v-if="loaded"
      :chartdata="chartdata"
      :options="options"/>
  </div>
</template>

<script>
import axios from 'axios';
import AxiosChart from '../charts/AxiosChart.vue' 

export default {
  name: 'AxiosChartContainer',
  components: { 
    AxiosChart 
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
              label: 'Estoque',
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
              data: quantidades
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