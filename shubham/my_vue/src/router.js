import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import logo_section from "./views/logosection.vue";
import dots_logo from "./views/companylogo.vue";

Vue.use(Router);

export default new Router({
    mode: "history",
    base: process.env.BASE_URL,
    routes: [{
            path: "/",
            name: "home",
            component: Home
        },
        {
            path: "/about",
            name: "about",
            // route level code-splitting
            // this generates a separate chunk (about.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () =>
                import ( /* webpackChunkName: "about" */ "./views/About.vue")
        },
        {
            path: "/logo",
            name: "/logo_section",
            component: logo_section
        },
        {
            path: "/company_logo",
            name: "/dots_logo",
            component: dots_logo
        },
    ]
});