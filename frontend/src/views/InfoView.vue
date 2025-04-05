<template>
  <div class="info-view">
    <div class="image-container">
      <img 
        src="@/assets/info.png"
        @click="toggleFullscreen"
        :class="{ 'fullscreen': isFullscreen }"
        alt="Information"
      />
      <div class="hero-overlay">
        <div class="overlay-content">
          <img src="@/assets/logo1.png" alt="Uri Flag" class="logo">
          <h1>Fakten und Links</h1>
        </div>
      </div>

      <div class="container">
        <nav class="breadcrumb">
          <router-link to="/">Home</router-link> > <router-link to="/info">Information</router-link>
        </nav>
      </div>
    </div>

    <div class="container">
      <div class="events-content">
        <header class="page-header">
          <h1>Wissenswertes über Neuankömmlinge in Uri</h1>
        </header>
        <section class="content-section">
          <p class="description">
            Auf dieser Seite finden Sie wichtige Informationen und Statistiken über Neuankömmlinge in Uri. 
            Erfahren Sie mehr über die Herausforderungen, denen Menschen begegnen, die neu in der Region sind, 
            und wie Sie diese meistern können. Wir bieten Ihnen hilfreiche Links zu Ämtern, Behörden und 
            wichtigen Anlaufstellen, die Sie bei Ihren Fragen und Anliegen unterstützen. Lassen Sie uns 
            gemeinsam die Hürden überwinden und den Weg in eine erfolgreiche Zukunft ebnen.
          </p>
        </section>
        
        <header class="page-header">
          <h2>Erwerbstätigkeit nach sieben Jahren</h2>
        </header>
        <section class="content-section">
          <p class="description">
            Im Jahr 2023 lag die Erwerbstätigenquote von vorläufig Aufgenommenen und Flüchtlingen in Uri 
            sieben Jahre nach ihrer Einreise bei 83%. Dies ist im Vergleich zu anderen Kantonen ein hoher 
            Wert, weil sich die Daten auf wenige Personen im erwerbsfähigen Alter beziehen, können die 
            Unterschiede pro Jahr stark schwanken.
            <br><br>
            Die Aufnahme einer Arbeit wird von verschiedenen persönlichen und strukturellen Faktoren beeinflusst. 
            Unterschiede in der Erwerbstätigenquote können nicht nur durch erfolgreiche Integrationsförderung 
            erklärt werden. Auch die Struktur des Arbeitsmarktes und die wirtschaftliche Lage spielen eine 
            wichtige Rolle.
          </p>
        </section>
        
        <div class="map-container">
          <img 
            src="@/assets/map1.png" 
            alt="Uri Map" 
            class="map-image"
          />
          <div class="source-citation">
            Quelle: <a href="https://www.sem.admin.ch/sem/de/home/integration-einbuergerung/integrationsfoerderung/monitoring/erwerb-va-fl.html" target="_blank" rel="noopener noreferrer">Staatssekretariat für Migration SEM</a>
          </div>
        </div>
        
        <header class="page-header">
          <h2>Erwärbstätigkeit aktuell</h2>
        </header>
        
        <div class="image-info-container">
          <img 
            src="@/assets/inper.png" 
            alt="Erwerbstätigkeit Statistik" 
            class="info-image"
          />
        </div>

        <section class="content-section">
          <p class="description">
            Die Tabelle zeigt den Stand im März 2025. Von den 782 Flüchtlingen im Kanton Uri 
            (aus allen Aufenthaltsstatus), sind 515 arbeitsfähig. Von diesen sind 245 derzeit 
            erwerbstätig, was 47,57% entspricht.
          </p>
        </section>

        <div class="image-info-container">
          <img 
            src="@/assets/img6.png" 
            alt="Additional Statistics" 
            class="info-image"
          />
          <div class="source-citation">
            Quelle: <a href="https://www.sem.admin.ch/sem/de/home/integration-einbuergerung/integrationsfoerderung/monitoring/erwerb-va-fl.html" target="_blank" rel="noopener noreferrer">Staatssekretariat für Migration SEM</a>
            <span class="date-info">(Stand: 11.03
              .2025)</span>
          </div>
        </div>

        <header class="page-header">
          <h2>Tipps für den Alltag in Uri</h2>
        </header>
        
        <section class="content-section">
          <p class="description">
            Die Integration in eine neue Umgebung kann herausfordernd sein, aber mit ein paar hilfreichen Tipps 
            wird Ihnen der Einstieg leichter fallen. Diese Tipps sollen Sie dabei unterstützen, sich in Uri 
            zurechtzufinden und Teil der Gemeinschaft zu werden.
          </p>
        </section>

        <header class="page-header">
          <h3>Teilnahme und Sprache</h3>
        </header>

        <section class="content-section">
          <p class="description">
            Wochenmärkte und Konzerte, aber auch Spaziergänge und Wanderungen sind gute Gelegenheiten, 
            die Kulturellen Regeln und Menschen in Uri kennenzulernen. Es braucht keine Sprachkenntnisse, 
            um den öffentlichen Raum zu nutzen, um erste Kontakte mir Urnerinnen und Urnern zu knüpfen. 
            Das Lernen der Sprache ist allerdings ein wichtiger Aspekt, um Sprachbarrieren und Missverständnisse 
            zu verhindern und um Teil der Urner Gemeinschaft zu werden.
          </p>
        </section>

        <header class="page-header">
          <h2>Urner Feste und Bräuche</h2>
        </header>

        <section class="content-section">
          <p class="description">
            Fasnacht, Samichlaus, Alpaufzug, 1.August - die Menschen im Kanton Uri feiern viele 
            traditionelle Feste. Zu diesen Festen finden auch jedes Jahr grosse Märkte und Events 
            in Altdorf statt. Feiern Sie mit!
            <br><br>
            Ein Brauchtum, der das ganze Jahr stattfindet ist das gegenseitige Begrüssen in der 
            Nachbarschaft, beim Spazieren oder auf Wanderungen. Gegrüsst wird mit "Griäzi" und "Guete Tag".
            <br><br>
            Weitere Informationen über Urner Bräuche und gelebte Traditionen finden Sie auf der 
            <router-link to="/learning" class="content-link">Lernen-Seite</router-link>.
          </p>
        </section>

        <header class="page-header">
          <h1>Nützliche Links</h1>
        </header>

        <section class="content-section">
          <div class="links-container">
            <div class="link-item">
              <h4>Fachstelle Integration und Vernetzung Uri</h4>
              <p>Die Fachstelle Integration und Vernetzung Uri ist Ihre Anlaufstelle, wenn sie Beratungen in Anspruch nehmen möchten, oder wenn Sie sich über bestehenden Angebote im Kanton Uri informieren möchten.</p>
              <a href="https://www.ur.ch/unterinstanzen/1436" target="_blank" rel="noopener noreferrer" class="external-link">www.ur.ch/unterinstanzen/1436</a>
            </div>

            <div class="link-item">
              <h4>Integration Uri</h4>
              <p>Die Integrations-Agenda beschreibt den best-case Integrationsprozess, den "Soll-Integrationsprozess" für die 16-25- Jährige. Die einzelnen Phasen der Integration werden im Dokument "Integrationsagenda Schweiz: Bericht der Koordinationsgruppe vom 1. März 2018" ausführlich beschrieben.</p>
              <a href="https://www.integration-uri.ch" target="_blank" rel="noopener noreferrer" class="external-link">www.integration-uri.ch</a>
            </div>

            <div class="link-item">
              <h4>Staatssekretariat für Migration SEM</h4>
              <p>Weiterführende Informationen zur Integrationsagenda:</p>
              <div class="sub-links">
                <a href="https://www.sem.admin.ch/sem/fr/home/integration-einbuergerung/integrationsfoerderung/kantonale-programme/integrationsagenda" target="_blank" rel="noopener noreferrer" class="external-link">Integrationsagenda</a>
                <a href="https://www.sem.admin.ch/dam/sem/de/data/integration/agenda/ber-koordinationsgruppe-integrationsagenda-d.pdf.download.pdf/ber-koordinationsgruppe-integrationsagenda-d.pdf" target="_blank" rel="noopener noreferrer" class="external-link">Bericht der Koordinationsgruppe (PDF)</a>
              </div>
            </div>

            <div class="link-item">
              <h4>Familien Uri</h4>
              <p>Familien Uri ist eine Plattform für Familienevents, Betreuungsangebote und Bildungsangebote für Familien im Kanton Uri.</p>
              <a href="https://www.familien-uri.ch" target="_blank" rel="noopener noreferrer" class="external-link">www.familien-uri.ch</a>
            </div>
          </div>
        </section>
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
  width: 40%; /* Reduced from 50% */
  min-width: 200px; /* Reduced from 300px */
  background: rgba(8, 121, 144, 0.8); /* Şeffaf mavi */
  /* Changed from blue to dark gray */
  /*background: rgba(40, 40, 40, 0.7);  Changed from blue to dark gray */
  padding: 30px; /* Reduced padding */
  border-radius: 20px;
  text-align: center;
  color: rgb(255, 255, 255);
  font-family: var(--text-h1-font-family);
  font-weight: var(--text-h1-font-weight);
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

.hero-overlay h1 {
  margin: 0;
  font-size: 5em; /* Increased from 2em */
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

:root {
  --text-h1-font-family: 'Arial', sans-serif;
  --text-h1-font-weight: 700;
  --text-h1-font-size: 2rem;
  --text-regular-font-family: 'Arial', sans-serif;
  --text-regular-font-weight: 400;
  --text-regular-font-size: 1rem;
  --text-regular-line-height: 1.5;
  --orange-600: #c25e00;
  --secondary-color: #f5f5f5;
}

.events-content {
  padding: 40px 0;
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
}

.main-content {
  max-width: 1518px;
  margin: 0 auto;
  padding: 0 20px;
}

.content-section,
.card-section,
.event-section {
  margin-bottom: 60px;
}

.section-title {
  font-family: var(--text-h1-font-family);
  font-weight: var(--text-h1-font-weight);
  font-size: var(--text-h1-font-size);
  color: var(--orange-600);
  margin-bottom: 28px;
}

.section-text {
  font-family: var(--text-regular-font-family);
  font-weight: var(--text-regular-font-weight);
  font-size: var(--text-regular-font-size);
  line-height: var(--text-regular-line-height);
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.card-item {
  height: 100%;
  text-decoration: none;
  cursor: pointer;
  transition: transform 0.2s;
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

.page-header h2 {
  font-family: var(--text-h1-font-family);
  font-weight: var(--text-h1-font-weight);
  font-size: 2.75rem;
  color: var(--orange-600);
  margin-bottom: 20px;
}

.page-header h3 {
  font-family: var(--text-h1-font-family);
  font-weight: var(--text-h1-font-weight);
  font-size: 2rem;
  color: var(--orange-600);
  margin-bottom: 20px;
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

.map-container {
  margin: 40px 0;
  text-align: center;
}

.map-image {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.source-citation {
  margin-top: 10px;
  font-size: 0.9rem;
  color: #666;
  text-align: right;
}

.source-citation a {
  color: var(--orange-600);
  text-decoration: none;
}

.source-citation a:hover {
  text-decoration: underline;
}

.image-info-container {
  margin: 40px 0;
  text-align: center;
  background-color: var(--secondary-color);
  padding: 20px;
  border-radius: 8px;
}

.info-image {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.date-info {
  margin-left: 10px;
  color: #666;
}

.content-link {
  color: var(--orange-600);
  text-decoration: none;
}

.content-link:hover {
  text-decoration: underline;
}

.links-container {
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.link-item {
  padding: 20px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.link-item h4 {
  color: var(--orange-600);
  margin-bottom: 15px;
  font-size: 1.2rem;
}

.link-item p {
  margin-bottom: 15px;
  line-height: 1.5;
}

.external-link {
  color: var(--orange-600);
  text-decoration: none;
  display: inline-block;
  margin-top: 10px;
  font-weight: 500;
}

.external-link:hover {
  text-decoration: underline;
}

.sub-links {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
</style>