<template>
  <matriz :colunas="40" :linhas="40" :celulasAtivas="celulasAtivas" />
</template>

<script>
import matriz from '@/components/div-matriz.vue'
import g from '@/helpers/gameoflife'
export default {
  components:{
    matriz
  },
  props:{
    ativo:{
      type: Boolean,
      default: false
    }
  },
  data(){
    return{
      celulasAtivas : this.celulasAleatorias()
    }
  },
  methods:{
    gameOfLife(){
        setInterval(
          () => {
            if (this.celulasAtivas.length){
            this.celulasAtivas = g.geraNovaListaDeCelulasAtivas(this.celulasAtivas)
            console.log('rodando')
              }
            }
          , 1000);
    },
    celulasAleatorias(){
      let celulas = []
      for (let i = 0; i <= 30; i++){
        celulas.push([Math.floor(Math.random() * 10) , Math.floor(Math.random() * 10)])
        celulas.push([Math.floor(Math.random() * 10) , Math.floor(Math.random() * 10)])
        celulas.push([Math.floor(Math.random() * 10) , Math.floor(Math.random() * 10)])
        console.log(celulas)
      }
      return celulas
    }
  },
  watch:{
    ativo(v){
      console.log(v)
      this.gameOfLife()
    }
  }
}
</script>
