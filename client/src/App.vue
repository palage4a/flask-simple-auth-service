<template>
  <div id="app">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-8">
          <h1>Flask service</h1>
          <b-nav tabs justified>
            <b-nav-item>
              <router-link to="/login">Login</router-link>
            </b-nav-item>
            <b-nav-item>
              <router-link to="/register">Register</router-link>
            </b-nav-item>
          </b-nav>
          <br>
          <router-view />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "App"
};
</script>

<style>
#app {
  text-align: center;
  margin-top: 60px;
}
</style>
