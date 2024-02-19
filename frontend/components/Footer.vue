<template>
  <main>
    <footer>
      <div class="firstcl">
      <NuxtLink to="/">slot 1</NuxtLink>
      <NuxtLink to="/">slot 2</NuxtLink>
      <NuxtLink to="/">slot 3</NuxtLink>
      </div>
      <div class="secondcl">
      <NuxtLink to="eshop/">slot 1</NuxtLink>
      <NuxtLink to="eshop/">slot 2</NuxtLink>
      <NuxtLink to="eshop/">slot 3</NuxtLink>
      </div>
      <div class="thirdcl">
      <NuxtLink to="blog/">slot 1</NuxtLink>
      <NuxtLink to="blog/">slot 2</NuxtLink>
      <NuxtLink to="blog/">slot 3</NuxtLink>
      </div>
    </footer>
  </main>
</template>

<style scoped>

footer {
  display: flex;
  justify-content: space-around;
  height: 20vh;
  background-color: #373737;
}

footer a {
  color: #F4F4F4; 
    text-decoration: none;
}

footer a:hover {
    color: #C0B283; 
}

footer a.router-link-exact-active {
    color: #C0B283; 
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