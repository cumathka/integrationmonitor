<template>
  <div class="info-view">
    <div class="image-container">
      <img 
        src="@/assets/arbeit.png"
        @click="toggleFullscreen"
        :class="{ 'fullscreen': isFullscreen }"
        alt="Information"
      />
      <div class="hero-overlay">
        <div class="overlay-content">
          <img src="@/assets/logo1.png" alt="Uri Flag" class="logo">
          <h2>ARBEITSMÖGLICHKEITEN</h2>
        </div>
      </div>
    </div>

    <div class="container">
      <nav class="breadcrumb">
        <router-link to="/">Home</router-link> > <router-link to="/jobs">Arbeitsmöglichkeiten</router-link>
      </nav>
      
      <header class="page-header">
        <h1>Ihre Karrierechancen in Uri</h1>
      </header>
      
      <section class="content-section">
        <p>
          Der Einstieg in den Arbeitsmarkt ist ein wichtiger Schritt auf Ihrem Weg in der Schweiz. 
          Auf dieser Seite finden Sie Links zu Jobportalen, die speziell für Neuankömmlinge geeignet sind. 
          Erfahren Sie mehr über die Arbeitswelt in Uri und nutzen Sie die Chance, Ihre beruflichen 
          Ziele zu verwirklichen. Wir unterstützen Sie dabei, den passenden Job zu finden und sich 
          erfolgreich in den Arbeitsmarkt zu integrieren. Ihre Karriere beginnt hier!
        </p>
        
        <div class="job-links">
          <div class="job-card">
            <a href="https://www.job-room.ch/home/job-seeker" class="job-link" target="_blank">
              <span class="link-text">www.job-room.ch/home/job-seeker</span>
              <span class="link-icon">↗</span>
            </a>
            <div class="job-info">
              <p>Das offizielle Jobportal des Kantons Uri mit Stellenangeboten in der ganzen Region. Besonders nützlich für die Suche nach lokalen Arbeitsstellen in verschiedenen Branchen.</p>
            </div>
          </div>
          
          <div class="job-card">
            <a href="https://www.path2work.ethz.ch/" class="job-link" target="_blank">
              <span class="link-text">www.path2work.ethz.ch/</span>
              <span class="link-icon">↗</span>
            </a>
            <div class="job-info">
              <p>Ein Projekt der ETH Zürich, das sich auf die Integration von qualifizierten Migrantinnen und Migranten in den Schweizer Arbeitsmarkt spezialisiert hat. Bietet Coaching und Netzwerkmöglichkeiten.</p>
            </div>
          </div>
          
          <div class="job-card">
            <a href="https://www.arbeit.swiss/secola/v.de/home" class="job-link" target="_blank">
              <span class="link-text">www.arbeit.swiss/secola/v.de/home</span>
              <span class="link-icon">↗</span>
            </a>
            <div class="job-info">
              <p>Das Staatssekretariat für Wirtschaft (SECO) bietet hier Informationen zum Arbeitsmarkt, Berufsanerkennungen und spezielle Programme für Arbeitssuchende in der Schweiz.</p>
            </div>
          </div>
        </div>
      </section>
    </div>

  </div>
</template>

<script>
export default {
  name: 'InfoView',
  data() {
    return {
      isFullscreen: false
    }
  },
  methods: {
    toggleFullscreen() {
      this.isFullscreen = !this.isFullscreen;
      if (this.isFullscreen) {
        document.body.style.overflow = 'hidden';
      } else {
        document.body.style.overflow = '';
      }
    }
  }
}
</script>

<style scoped>
:root {
  --primary-color: #007ba7;
  --secondary-color: #f8f9fa;
  --text-color: #333;
  --link-color: #007ba7;
  --footer-bg: #f8f9fa;
}

.info-view {
  position: relative;
  width: 100%;
}

.image-container {
  position: relative;
  width: 100%;
  overflow: hidden;
}

img {
  width: 100%;
  height: auto;
  display: block;
  cursor: pointer;
  transition: all 0.3s ease;
}

.fullscreen {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100vw;
  height: 100vh;
  object-fit: contain;
  z-index: 1000;
  background: rgba(0, 0, 0, 0.9);
  cursor: zoom-out;
  padding: 20px;
  box-sizing: border-box;
}

.hero-overlay {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 40%;
  min-width: 200px;
  background: rgba(8, 121, 144, 0.8); /* Şeffaf mavi */
  padding: 10px;
  border-radius: 20px;
  text-align: center;
  color: yellow;
  pointer-events: none;
}

.overlay-content {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 15px;
}

.logo {
  height: 80px;
  width: auto;
  margin: 0;
  box-shadow: 0 2px 4px rgba(0,0,0,0.2);
  pointer-events: auto;
  object-fit: contain;
}

.hero-overlay h2 {
  margin: 0;
  font-size: 2.5em; /* Increased from 2em */
  font-weight: bold;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.breadcrumb {
  padding: 15px 0;
  font-size: 14px;
  color: #666;
}

.breadcrumb a {
  color: #666;
  text-decoration: none;
}

.breadcrumb a:hover {
  text-decoration: underline;
}

.page-header {
  margin: 30px 0;
}

.page-header h1 {
  font-family: var(--text-h1-font-family);
  font-weight: var(--text-h1-font-weight);
  font-size: var(--text-h1-font-size);
  color: var(--orange-600);
  margin-bottom: 28px;
}

.content-section {
  margin-bottom: 40px;
  padding: 30px;
  background-color: var(--secondary-color);
  border-radius: 8px;
}

.content-section p {
  font-size: 1.1rem;
  margin-bottom: 25px;
}

.job-links {
  margin-top: 30px;
}

.job-card {
  margin-bottom: 30px;
  background: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.job-link {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  text-decoration: none;
  color: white;
  background-color: #0E7490;
  border: none;
  border-radius: 8px 8px 0 0;
}

.link-text {
  font-weight: 500;
}

.link-icon {
  font-size: 1.2em;
}

.job-info {
  padding: 20px;
  background: white;
}

.job-info p {
  margin: 0;
  color: #333;
  font-size: 0.95rem;
  line-height: 1.5;
}

.job-link:hover {
  background-color: #155E75;
  transform: none;
}

footer {
  background-color: var(--footer-bg);
  padding: 30px 0;
  text-align: center;
  margin-top: 50px;
}

@media (max-width: 768px) {
  .hero-overlay {
    width: 60%; /* Reduced from 80% */
    padding: 15px;
  }
  
  .overlay-content {
    gap: 10px;
  }
  
  .logo {
    height: 30px;
  }
  
  .hero-overlay h2 {
    font-size: 1.8em; /* Increased from 1.2em */
  }
  
  .page-header h1 {
    font-size: 2rem;
  }
  
  .content-section {
    padding: 20px;
  }
}
</style>