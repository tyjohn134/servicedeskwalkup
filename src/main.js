import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import store from './store'
import VueQrcodeReader from "vue-qrcode-reader";

Vue.config.productionTip = false
Vue.use(VueQrcodeReader);

new Vue({
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app')
