<template>
    <nav class="navbar navbar-expand-lg py-2" style="background-color: var(--blue-100);">
      <div class="container">
        <div class="d-flex align-items-center">
          <img 
            src="https://c.animaapp.com/m939jagjfdOBIu/img/bull-frontal-head-svgrepo-com.svg" 
            alt="Logo" 
            width="60" 
            height="60"
            class="me-2"
          >
          <span class="body-lead text-dark opacity-90">Griäzi!</span>
        </div>
        
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent">
          <span class="navbar-toggler-icon"></span>
        </button>
        
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0 ms-auto">
            <li class="nav-item px-3">
              <a class="nav-link text-regular" style="color: var(--cyan-700);">Informationen</a>
            </li>
            <li class="nav-item px-3">
              <a class="nav-link text-regular" style="color: var(--cyan-700);">Lernen</a>
            </li>
            <li class="nav-item px-3">
              <a class="nav-link text-regular" style="color: var(--cyan-700);">Jobs</a>
            </li>
            <li class="nav-item px-3">
              <a class="nav-link text-regular" style="color: var(--cyan-700);">Events</a>
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
    name: 'Navbar'
  }
  </script>