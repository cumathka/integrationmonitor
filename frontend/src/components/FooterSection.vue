<template>
    <footer class="full-width-footer">
      <div class="footer-content">
        <div class="flags-container">
          <img src="@/assets/uri-flag.png" alt="Uri Canton Flag" class="flag-img left-flag">
          <img src="@/assets/swiss-flag.png" alt="Swiss Flag" class="flag-img right-flag">
        </div>
        
        <div class="row">
          <div class="col-md-4">
            <h5 class="text-black mb-3">Kontakt</h5>
            <p class="text-black">+49 176 2064 5533</p>
            <p class="text-black">info@integrationmonitor.de</p>
            <div class="social-links mt-3">
              <a href="#" class="me-3"><i class="bi bi-facebook"></i></a>
              <a href="#" class="me-3"><i class="bi bi-twitter"></i></a>
              <a href="#" class="me-3"><i class="bi bi-instagram"></i></a>
              <a href="#"><i class="bi bi-linkedin"></i></a>
            </div>
          </div>
          
          <div class="col-md-4">
            <h5 class="text-black mb-3">Adresse</h5>
            <p class="text-black">
              Integrationmonitor e.V.<br>
              Goethestraße <br>
              6460 Altdorf<br>
            </p>
          </div>
          
          <div class="col-md-4">
            <h5 class="text-black mb-3">Tags</h5>
            <div class="tags">
              <span class="tag">#Integration</span>
              <span class="tag">#Bildung</span>
              <span class="tag">#Gemeinschaft</span>
              <span class="tag">#Kultur</span>
            </div>
          </div>
        </div>
        
        <div class="mt-4 text-center">
          <p class="text-black">© 2025 Integrationmonitor. Alle Rechte vorbehalten.</p>
        </div>
      </div>
    </footer>
  </template>
  
  <script>
  export default {
    name: 'FooterSection'
  }
  </script>
  
  <style scoped>
  .full-width-footer {
    width: 100vw;
    position: relative;
    left: 50%;
    right: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
    background-color: var(--yellow-500); /* Changed to yellow */
    padding: 4rem 0;
    min-height: 300px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .footer-content {
    max-width: 1318px;
    width: 100%;
    padding: 0 20px;
    margin: 0 auto;
    text-align: center;
    position: relative;
  }
  
  .flags-container {
    position: absolute;
    width: 100%;
    top: 50%;
    transform: translateY(-50%);
    display: flex;
    justify-content: space-between;
    padding: 0;
  }
  
  .flag-img {
    height: 180px;
    width: auto;
    border: 2px solid ;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
  }
  
  .left-flag {
    margin-left: -230px;
  }
  
  .right-flag {
    margin-right: -230px;
  }
  
  .text-black {
    color: #000000;
  }
  
  .social-links a {
    color: #000000;
    font-size: 1.5rem;
    text-decoration: none;
    transition: opacity 0.3s;
  }
  
  .social-links a:hover {
    opacity: 0.8;
  }
  
  .tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    justify-content: center;
  }
  
  .tag {
    background-color: rgba(0, 0, 0, 0.1);
    color: #000000;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-size: 0.9rem;
  }
  
  @media (max-width: 768px) {
    .full-width-footer {
      height: auto;
      padding: 3rem 0 2rem;
    }
    
    .col-md-4 {
      margin-bottom: 2rem;
      text-align: center;
    }
    
    .flags-container {
      top: -30px;
    }
    
    .flag-img {
      height: 120px;
    }
    
    .left-flag {
      margin-left: -30px;
    }
  
    .right-flag {
      margin-right: -30px;
    }
  }
  </style>