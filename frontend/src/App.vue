<template>
  <div id="wrapper">
  <nav class="navbar is-dark" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item"><strong>Shop</strong></router-link>

      <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>

    <div id="navbarBasicExample" class="navbar-menu">
      <div class="navbar-start">
        <a class="navbar-item">
          Home
        </a>

        <a class="navbar-item">
          Documentation
        </a>

        <div class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link">
            More
          </a>

          <div class="navbar-dropdown">
            <a class="navbar-item">
              About
            </a>
            <a class="navbar-item">
              Jobs
            </a>
            <a class="navbar-item">
              Contact
            </a>
            <hr class="navbar-divider">
            <a class="navbar-item">
              Report an issue
            </a>
          </div>
        </div>
      </div>

      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <a class="button is-primary">
              <strong>Sign up</strong>
            </a>
            <a class="button is-light">
              Log in
            </a>
          </div>
        </div>
        <div class="navbar-item">
        <router-link to="/cart" class="button is-success">
                <span class="icon"><i class="fas fa-shopping-cart"></i> </span>
                <span>Cart ({{ cartTotalLength }})</span>
              </router-link>
              </div>
      </div>
    </div>
  </nav>



  <router-view/>



    <footer class="footer">
      <div class="content has-text-centered">
        <router-link to="/" class="title"><strong>Shop-footer</strong></router-link>

      </div>
    </footer>
  </div>
</template>

<style lang="scss">
@import '../node_modules/bulma';


</style>
