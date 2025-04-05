<template>
    <nav class="navbar navbar-expand-lg py-2" style="background-color: var(--blue-100);">
      <div class="container">
        <div class="d-flex align-items-center">
          <router-link to="/" class="navbar-brand">
            <img 
              src="@/assets/logo1.png" 
              alt="Logo" 
              width="60" 
              height="60"
              class="me-2"
            >
            <span class="body-lead text-dark opacity-90">Griäzi!</span>
          </router-link>
        </div>
        
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent">
          <span class="navbar-toggler-icon"></span>
        </button>
        
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0 ms-auto">
            <li class="nav-item px-3">
              <router-link to="/info" class="nav-link text-regular" style="color: var(--cyan-700);">Informationen</router-link>
            </li>
            <li class="nav-item px-3">
              <router-link to="/learning" class="nav-link text-regular" style="color: var(--cyan-700);">Lernen</router-link>
            </li>
            <li class="nav-item px-3">
              <router-link to="/jobs" class="nav-link text-regular" style="color: var(--cyan-700);">Jobs</router-link>
            </li>
            <li class="nav-item px-3">
              <router-link to="/events" class="nav-link text-regular" style="color: var(--cyan-700);">Events</router-link>
            </li>
          </ul>
          
          <form class="d-flex">
            <div class="input-group">
              <input 
                class="form-control body-regular" 
                type="search" 
                placeholder="Search" 
                style="color: var(--gray-600);"
              >
              <button class="btn btn-outline-primary body-regular" type="submit">
                Search
              </button>
            </div>
          </form>
        </div>
      </div>
    </nav>
</template>

<script>
export default {
  name: 'TheNavbar'
}
</script>

<style>
.router-link-active {
  font-weight: bold;
  color: var(--blue-600) !important;
}
</style>