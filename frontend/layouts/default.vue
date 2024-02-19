<template>
  <NavBar/>
  <div class="wrapper">
    <slot/>
  </div>
  <Footer/>
</template>

<style scoped>
.wrapper {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.Footer {
  margin-top: auto; /* Pushes the footer to the bottom of the wrapper */
}
</style>

<script setup lang="ts">
</script>