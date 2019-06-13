import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui';
import router from './router'
import 'element-ui/lib/theme-chalk/index.css'
import '@/common/scss/index.scss'
import VCharts from 'v-charts'
// import locale from 'element-ui/lib/locale/lang/zh-TW'

Vue.config.productionTip = false;
Vue.use(ElementUI);
Vue.use(VCharts);

new Vue({
  el: '#app',
  router,
  render: h => h(App)
}).$mount('#app');
