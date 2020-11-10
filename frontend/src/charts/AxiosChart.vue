<script>
import { Line } from 'vue-chartjs';
import axios from 'axios'; 

export default {
  async created() {
    const { data } = await axios.get('http://127.0.0.1:8000/produtos/camisas/');
    console.log(data);
  }
}
</script>