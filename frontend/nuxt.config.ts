// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  css: ["./assets/css/main.css"],
    defaults: {
      nuxtLink: {
        // default values
        componentName: 'NuxtLink',
        activeClass: 'router-link-active',
        exactActiveClass: 'router-link-exact-active',
       
      }
    }
  }
)
