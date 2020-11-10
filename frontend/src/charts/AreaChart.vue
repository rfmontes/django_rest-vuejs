<script>
import { Line } from 'vue-chartjs'

export default {
  extends: Line,
  data: () => ({
    chartdata: {
      labels: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho'],
      datasets: [
        {
            label: 'Vendas',
            backgroundColor: [
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
                'rgba(255, 99, 132, 1)'
            ],
            borderWidth: 1,
            data: [12, 19, 3, 5, 15, 3]
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false
    }
  }),
  mounted () {
    this.renderChart(this.chartdata, this.options)
  }
}
</script>