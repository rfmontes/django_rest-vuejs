import Vue from 'vue';
import Router from 'vue-router';

import Home from './views/Home';
import Login from './views/Login';
import Camisas from './views/Camisas';
import Chuteiras from './views/Chuteiras';
import EditCamisa from './views/EditCamisa';
import EditChuteira from './views/EditChuteira';

import Dashboard from './views/Dashboard';


Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    { path: '/home', name: 'home', component: Home }, 
    { path: '/', name: 'login', component: Login },

    { path: '/camisas', component: Camisas }, 
    { path: '/camisas/add', component: EditCamisa }, 
    { path: '/camisas/:id/edit', component: EditCamisa },

    { path: '/chuteiras', component: Chuteiras }, 
    { path: '/chuteiras/add',component: EditChuteira }, 
    { path: '/chuteiras/:id/edit', component: EditChuteira },

    { path: '/dashboard', component: Dashboard }
  ]
});