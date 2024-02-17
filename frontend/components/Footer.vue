<template>
  <main>
    <div class="footer">
      <div class="firstcl">
      <NuxtLink to="eshop/">slot 1</NuxtLink>
      <NuxtLink>slot 2</NuxtLink>
      <NuxtLink>slot 3</NuxtLink>
      </div>
      <div class="secondcl">
      <NuxtLink>slot 1</NuxtLink>
      <NuxtLink>slot 2</NuxtLink>
      <NuxtLink>slot 3</NuxtLink>
      </div>
      <div class="thirdcl">
      <NuxtLink>slot 1</NuxtLink>
      <NuxtLink>slot 2</NuxtLink>
      <NuxtLink>slot 3</NuxtLink>
      </div>
    </div>
  </main>
</template>

<style scoped>

.footer {
  display: flex;
  justify-content: space-around;

}
.firstcl {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

}
.secondcl {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

}
.thirdcl {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

}
</style>