<template>
  <footer class="full-width-footer">
    <div class="footer-content">
      <div class="flags-container">
        <img src="@/assets/uri-flag.png" alt="Uri Canton Flag" class="flag-img left-flag">
        <img src="@/assets/swiss-flag.png" alt="Swiss Flag" class="flag-img right-flag">
      </div>
      
      <div class="footer-grid">
        <div class="footer-column">
          <h5 class="text-black mb-3">Kontakt</h5>
          <p class="text-black">+41 100 2064 5533</p>
          <p class="text-black">info@integrationmonitor.ch</p>
          <div class="social-links mt-3">
            <a href="#" class="me-3"><i class="bi bi-facebook"></i></a>
            <a href="#" class="me-3"><i class="bi bi-twitter"></i></a>
            <a href="#" class="me-3"><i class="bi bi-instagram"></i></a>
            <a href="#"><i class="bi bi-linkedin"></i></a>
          </div>
        </div>
        
        <div class="footer-column">
          <h5 class="text-black mb-3">Adresse</h5>
          <p class="text-black">
            Integrationmonitor e.V.<br>
            Goethestraße <br>
            6460 Altdorf<br>
          </p>
        </div>
        
        <div class="footer-column">
          <h5 class="text-black mb-3">Tags</h5>
          <div class="tags">
            <span class="tag">#Integration</span>
            <span class="tag">#Bildung</span>
            <span class="tag">#Gemeinschaft</span>
            <span class="tag">#Kultur</span>
          </div>
        </div>
      </div>
      
      <div class="footer-bottom">
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
  width: 100%;
  background-color: var(--yellow-600);
  padding: 4rem 0;
  position: relative;
  overflow: hidden;
}

.footer-content {
  max-width: 1318px;
  width: 100%;
  padding: 0 20px;
  margin: 0 auto;
  position: relative;
}

.flags-container {
  position: absolute;
  width: 100%;
  top: 50%;
  left: 0;
  transform: translateY(-50%);
  display: flex;
  justify-content: space-between;
  pointer-events: none;
  z-index: 0;
}

.flag-img {
  height: 180px;
  width: auto;
  opacity: 0.7;
}

.left-flag {
  margin-left: -180px;
}

.right-flag {
  margin-right: -180px;
}

.footer-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  position: relative;
  z-index: 1;
}

.footer-column {
  text-align: center;
  padding: 0 1rem;
}

.text-black {
  color: #000000;
}

.social-links a {
  color: #000000;
  font-size: 1.5rem;
  text-decoration: none;
  transition: opacity 0.3s;
  display: inline-block;
  margin: 0 0.5rem;
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

.footer-bottom {
  margin-top: 3rem;
  text-align: center;
}

@media (max-width: 992px) {
  .footer-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .footer-column:nth-child(3) {
    grid-column: span 2;
  }
  
  .flag-img {
    height: 140px;
  }
  
  .left-flag {
    margin-left: 20px;
    margin-top: -250px;
  }
  
  
  .right-flag {
    margin-right: 20px;
    margin-top: -250px;
  }
  .footer-grid {
    grid-template-columns: 1fr;
  }
  
  .footer-column:nth-child(3) {
    grid-column: span 1;
  }
}

@media (max-width: 768px) {
  .full-width-footer {
    padding: 3rem 0;
  }
  
  .flag-img {
    height: 120px;
  }
  
  .left-flag {
    margin-left: 20px;
    margin-top: -200px;
  }
  
  .right-flag {
    margin-right: 20px;
    margin-top: -200px;
  }
  
  .footer-grid {
    gap: 1.5rem;
  }
  .footer-grid {
    grid-template-columns: 1fr;
  }
  .footer-column:nth-child(3) {
    grid-column: span 1;
  }
}

@media (max-width: 576px) {
  .footer-grid {
    grid-template-columns: 1fr;
  }
  
  .footer-column:nth-child(3) {
    grid-column: span 1;
  }
  
  .flag-img {
    height: 100px;
    opacity: 0.5;
  }
  
  .left-flag {
    margin-left: 45px;
    margin-top: -260px;
  }
  
  .right-flag {
    margin-right: 45px;
    margin-top: -260px;
  }
  
  .flag-img {
    height: 80px;
    opacity: 0.5;
  }
  
  .left-flag {
    margin-left: 45px;
    margin-top: -260px;
  }
  
  .right-flag {
    margin-right: 45px;
    margin-top: -260px;
  }
  
  .footer-column {
    padding: 0;
  }
  
  .tags {
    justify-content: center;
  }
  
  .social-links a {
    font-size: 1.25rem;
    margin: 0 0.3rem;
  }
}

@media (max-width: 400px) {
  .flag-img {
    display: none;
  }
  
  .full-width-footer {
    padding: 2rem 0;
  min-height: auto;
  }
  
  .footer-bottom {
    margin-top: 2rem;
  }
}
</style>