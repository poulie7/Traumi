<template>
    <main>
        <template>
    <main>
       <nav class="navigation">
            <div class="homeLink">
                <NuxtLink to="/">home</NuxtLink>
            </div>
            <div class="otherLinks">
                <NuxtLink to="eshop" >eshop</NuxtLink>
                <NuxtLink to="blog" >blog</NuxtLink>
                <NuxtLink to="login" >login</NuxtLink>
            </div>
       </nav>
    </main>
</template>


    </main>
</template>

<style scoped>

.navigation {
    background-color: #DCD0C0; /* Summer Sky */
    padding: 10px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  margin: 2em;
}

.homeLink,
.otherLinks {
    display: inline-block;
}

.homeLink a,
.otherLinks a {
    color: #C0B283; /* Warm Peach */
    text-decoration: none;
    margin-right: 20px;

  font-size: x-large;
}

.otherLinks a:last-child {
    margin-right: 0;
}

/* Hover effect */
.otherLinks a:hover {
    color: #F4F4F4; /* Breeze */
}


.homeLink router-link-active {
    color: #F4F4F4; /* Field */
}




</style>