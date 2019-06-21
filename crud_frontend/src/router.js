import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Medicamentos from "./views/Medicamentos";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    },
    {
      path: '/medicamentos',
      name: 'medicamentos',
      component: Medicamentos
    },
    {
      path: '/medicamentos/crear',
      name: 'medicamentos-crear',
      component: Home
    },
    {
      path: '/medicamentos/:id/editar',
      name: 'medicamentos-editar',
      component: Home
    }
  ]
})
