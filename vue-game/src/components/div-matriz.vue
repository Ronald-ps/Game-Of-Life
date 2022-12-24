<template>
  <div>
    <div v-for="linha in linhas" :key="linha" class="flex">
      <div v-for="coluna in colunas" :key="coluna">
        <quad class="quad" :esta-ativo="estaNaListaDeAtivas(linha, coluna)" />
      </div>
    </div>
  </div>
</template>

<script>
import quad from '@/components/atomic/div-quad'
export default {
  props:{
    colunas: {
      type: Number,
      default: 0
    },
    linhas:{
      type: Number,
      default: 0
    },
    celulasAtivas:{
      type: Array,
      default: () => []
    }
  },
  components:{
    quad
  },
  data(){
    return{
    }
    },
  methods:{
    estaNaListaDeAtivas(linha, coluna){
      for (let coordenadas of this.celulasAtivas){
        if (coordenadas[0] == linha && coordenadas[1] == coluna) return true
      }
    }
  }
  }
</script>

<style scoped>
.quad {
  border: 0.1px rgb(243, 249, 214) solid;
  width: 20px;
  height: 20px;
}
.flex {
  display: flex;
  box-sizing: border-box;
}
</style>
