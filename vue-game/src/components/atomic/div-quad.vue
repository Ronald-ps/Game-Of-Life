<template>
  <div :class="[estaAtivo ? 'ativo' : 'desativo']"></div>
</template>

<script>
export default {
 props:{
  estaAtivo: {
    type: Boolean,
    default: false
  }
 },
}
</script>

<style scoped>
.desativo {
  background-color: gray;
}
.ativo {
  background-color: blue;
}
</style>
