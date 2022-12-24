<template>
  <div>
    <button @click="jogar = !jogar">Iniciar</button>
    <gameoflife :ativo="jogar" />
  </div>
</template>

<script>
import gameoflife from '@/components/game-of-life.vue'

export default {
  name: 'App',
  components: {
    gameoflife
  },
  data(){
    return{
      jogar : false
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
