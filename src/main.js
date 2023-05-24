import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueRouter from 'vue-router'
import heroIndex from '@/components/heroIndex.vue'
import Redirect from '@/components/redirect.vue'

Vue.config.productionTip = false

Vue.use(VueRouter)

const routes = [
    { path: '/', component: heroIndex },
    { path: '/:slug', component: Redirect }
]

const router = new VueRouter

({
    mode: 'history',
    routes
})

Vue.prototype.$http = axios.create({
    baseURL: 'http://localhost:5000/api'
})

new Vue({
    router,
    render: h => h(App)
}).$mount('#app')
