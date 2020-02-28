import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import BootstrapVue from 'bootstrap-vue';
import { library } from '@fortawesome/fontawesome-svg-core'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faUserSecret)

Vue.use(BootstrapVue);
Vue.component('logo_section', FontAwesomeIcon)


Vue.config.productionTip = false;

new Vue({
    router,
    render: h => h(App)
}).$mount("#app");