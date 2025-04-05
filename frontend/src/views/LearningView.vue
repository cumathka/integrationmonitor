<template>
  <div class="info-view">
    <div class="image-container">
      <img 
        src="@/assets/lebenslag.png"
        @click="toggleFullscreen"
        :class="{ 'fullscreen': isFullscreen }"
        alt="Information"
      />
      <div class="hero-overlay">
        <div class="overlay-content">
          <img src="@/assets/logo1.png" alt="Uri Flag" class="logo">
          <h2>LEBENSLAG LERNEN</h2>
        </div>
      </div>
      <div class="container">
        <nav class="breadcrumb">
          <router-link to="/">Home</router-link> > <router-link to="/learning">Lernen</router-link>
        </nav>
      </div>
    </div>
    <div class="events-content">
      <header class="page-header">
        <h1>Netzwerken und Gemeinschaft erleben</h1>
      </header>
      <section class="content-section">
        <p class="description">
          Veranstaltungen sind eine wunderbare Möglichkeit, neue Menschen kennenzulernen und sich in der Gemeinschaft zu integrieren. 
          Auf dieser Seite finden Sie eine Übersicht über Networking-Events, Career Cafés und Tandem-Programme in Uri. 
          Diese Veranstaltungen bieten Ihnen die Gelegenheit, Kontakte zu knüpfen, Erfahrungen auszutauschen und sich in einem 
          unterstützenden Umfeld weiterzuentwickeln. Kommen Sie vorbei und werden Sie Teil unserer lebendigen Gemeinschaft!
        </p>
      </section>
      
      <div class="learning-cards">
        <div class="row g-4">
          <!-- Deutschkurse -->
          <div class="col-md-6">
            <div class="card h-100">
              <img src="@/assets/lern1.png" class="card-img-top" alt="Deutschkurse">
              <div class="card-body">
                <h5 class="card-title">Deutschkurse</h5>
                <p class="card-text">
                  Das Verstehen und Sprechen der Deutschen Sprache ist ein wichtiger Schritt, um sich in Uri zurecht zu finden und Kontakte mit Urnerinnen und Urnern zu knüpfen.                </p>
                <ul class="list-unstyled">
                  <li><a href="https://treffpunkt26.jimdofree.com/angebote/lernpunkt26/deutschangebote/" target="_blank" class="link-primary">Deutsch üben im Treffpunkt26 (Gratis)</a></li>
                  <li><a href="https://lernatelierluzern.ch/index.php/de-ch/" target="_blank" class="link-primary">Lernatelier Luzern (Gratis)</a></li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Lebenslauf verbessern -->
          <div class="col-md-6">
            <div class="card h-100">
              <img src="@/assets/lern2.png" class="card-img-top" alt="Lebenslauf">
              <div class="card-body">
                <h5 class="card-title">Lebenslauf verbessern</h5>
                <p class="card-text">
                  Ein professioneller Lebenslauf ist Ihre Visitenkarte im Bewerbungsprozess. Hier finden Sie Hilfe bei der Erstellung und Optimierung Ihrer Bewerbungsunterlagen.
                </p>
                <ul class="list-unstyled">
                  <li><a href="#" class="link-primary">Kostenlose Lebenslauf-Vorlagen</a></li>
                  <li><a href="#" class="link-primary">Bewerbungscoaching beim RAV</a></li>
                  <li><a href="#" class="link-primary">Tipps für erfolgreiche Bewerbungen</a></li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Schweizer Kultur -->
          <div class="col-md-6">
            <div class="card h-100">
              <img src="@/assets/lern3.png" class="card-img-top" alt="Kultur">
              <div class="card-body">
                <h5 class="card-title">Schweizer- und Urner Kultur</h5>
                <p class="card-text">
                  Als Gründungskanton ist Uri seit 1291 ein Teil der Schweizer Eidgenossenschaft. Der Kanton ist reich an Kulturgeschichte und Traditionen.
                </p>
                <ul class="list-unstyled">
                  <li><a href="#" class="link-primary">Alles über Uri auf urikon.ch</a></li>
                  <li><a href="#" class="link-primary">Kultur in Urner Museen</a></li>
                  <li><a href="#" class="link-primary">Gelebte Traditionen in Uri</a></li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Weiterbildungen -->
          <div class="col-md-6">
            <div class="card h-100">
              <img src="@/assets/lern4.png" class="card-img-top" alt="Weiterbildungen">
              <div class="card-body">
                <h5 class="card-title">Weiterbildungen</h5>
                <p class="card-text">
                  Lebenslanges Lernen ist der Schlüssel zum beruflichen Erfolg. Entdecken Sie vielfältige Weiterbildungsangebote im Kanton Uri.
                </p>
                <ul class="list-unstyled">
                  <li><a href="https://weiterbildung.bwzuri.ch/" target="_blank" class="link-primary">BWZ Uri Weiterbildungen</a></li>
                  <li><a href="https://weiterbildung.ur.ch/" target="_blank" class="link-primary">Weiterbildung Kanton Uri</a></li>
                  <li><a href="https://www.srk-uri.ch/kurswesen" target="_blank" class="link-primary">SRK Uri Kurse</a></li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
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
  background: rgba(8, 121, 144, 0.8); /* Şeffaf mavi */
  cursor: zoom-out;
  padding: 20px;
  box-sizing: border-box;
}

.hero-overlay {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 40%; /* Reduced from 50% */
  min-width: 200px; /* Reduced from 300px */
  background: rgba(0, 123, 167, 0.55);; 
  padding: 10px; /* Reduced padding */
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

.events-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 20px;
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

.description {
  line-height: 1.6;
  color: #444;
  margin-bottom: 40px;
  text-align: justify;
}

.learning-cards {
  padding: 40px 0;
  background-color: #f8f9fa;
}

.card {
  border-radius: 1rem;
  overflow: hidden;
  transition: transform 0.2s ease-in-out;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}

.card-title {
  font-size: 1.25rem;
  color: var(--orange-600);
  margin-bottom: 1rem;
}

.card-body {
  padding: 1.5rem;
}

.link-primary {
  color: #007ba7;
  text-decoration: none;
  display: inline-block;
  margin: 0.25rem 0;
}

.link-primary:hover {
  color: #006086;
  text-decoration: underline;
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

  .page-header {
    padding: 30px 0;
  }

  .page-header h1 {
    font-size: 1.8em;
    margin-bottom: 15px;
  }

  .description {
    font-size: 1em;
    line-height: 1.6;
    padding: 20px;
  }
}
</style>