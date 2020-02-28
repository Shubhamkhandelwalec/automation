<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <router-link to="/logo">Social Icon</router-link> |
      <router-link to="/company_logo">Logo</router-link>

    </div>
    <router-view />
  </div>
</template>

<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
<style lang="scss">
  @import './assets/static/css/reponsive.css';
  @import './assets/static/css/main.css';
  @import './assets/static/css/font-awesome.css';
  @import './assets/static/css/easy-responsive-tabs.css';
  @import './assets/static/css/custom.css';
  @import './assets/static/css/component.css';
  @import './assets/static/css/bootstrap.css';
  @import './assets/static/css/animate.css';
</style>

