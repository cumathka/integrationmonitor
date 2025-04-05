<template>
    <main class="main-content">
      <!-- Hakkımızda Bölümü -->
      <section class="content-section">
        <h2 class="section-title mt-5">Hier kommen Sie weiter</h2>
        <p class="section-text">
          Wir freuen uns, Sie auf unserer Plattform begrüssen zu dürfen! Wir wissen, dass der Start in einem
          neuen Land viele Herausforderungen mit sich bringt, aber auch unzählige Chancen bietet.
          <br><br>
          Hier finden Sie wertvolle Informationen und hilfreiche Angebote, die Ihnen den Start in
          Uri und der Schweiz erleichtern sollen.<br><br>
          Entdecken Sie die vielfältigen Möglichkeiten, die
          Uri zu bieten hat. Von Sprachkursen über Bewerbungstipps bis hin zu Veranstaltungen – wir sind für Sie
          da und unterstützen Sie auf eurem Weg.<br>
          Lassen Sie uns gemeinsam diese Reise antreten, voneinander
          lernen und uns gegenseitig helfen. Wir freuen uns darauf, Sie kennenzulernen!
        </p>
      </section>
      
      <!-- Kartlar Bölümü -->
      <section class="card-section">
        <div class="card-grid">
          <router-link 
            v-for="(card, index) in cards" 
            :key="index"
            :to="card.route"
            class="card-item"
          >
            <div class="card-inner" :class="index % 2 ? 'cyan-light' : 'cyan-dark'">
              <div class="card-icon">
                <img :src="card.icon" :alt="card.title" width="128" height="128">
              </div>
              <h3 class="card-title">{{ card.title }}</h3>
            </div>
          </router-link>
        </div>
      </section>
      
      <!-- Etkinlikler Bölümü -->
      <section class="event-section">
        <h2 class="section-title">Events</h2>
        <p class="section-text">
          Entdecken Sie Veranstaltungen in Uri und Umgebung, die Ihnen helfen, neue Kontakte zu knüpfen und sich
          zu integrieren.
        </p>
        <div class="event-image">
          <img 
            src="https://c.animaapp.com/m939jagjfdOBIu/img/image-1.png" 
            alt="Events" 
            class="img-fluid"
          >
        </div>
      </section>
    </main>
  </template>
  
  <script>
  export default {
    name: 'MainContent',
    data() {
      return {
        cards: [
          { 
            title: 'Informationen',
            icon: 'https://c.animaapp.com/m939jagjfdOBIu/img/union-8.svg',
            route: '/info'
          },
          { 
            title: 'Lernen',
            icon: 'https://c.animaapp.com/m939jagjfdOBIu/img/union-23.svg',
            route: '/learning'
          },
          { 
            title: 'Jobs',
            icon: 'https://c.animaapp.com/m939jagjfdOBIu/img/union-11.svg',
            route: '/jobs'
          },
          { 
            title: 'Events',
            icon: 'https://c.animaapp.com/m939jagjfdOBIu/img/union-10.svg',
            route: '/events'
          }
        ]
      }
    }
  }
  </script>
  
  <style scoped>
  .main-content {
    max-width: 1518px;
    margin: 0 auto;
    padding: 0 20px;
  }
  
  /* Bölüm Stilleri */
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
  
  /* Kart Grid Sistemi */
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
  
  .card-item:hover {
    transform: scale(1.02);
  }
  
  .card-inner {
    height: 100%;
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  
  .cyan-light {
    background-color: var(--cyan-600);
  }
  
  .cyan-dark {
    background-color: var(--cyan-700);
  }
  
  .card-icon {
    margin-bottom: 20px;
  }
  
  .card-icon img {
    width: 80px;
    height: 80px;
  }
  
  .card-title {
    font-family: var(--text-h3-font-family);
    font-weight: var(--text-h3-font-weight);
    font-size: 1.2rem;
    color: white;
    margin: 10px 0 0 0;
  }
  
  /* Etkinlik Görseli */
  .event-image {
    margin-top: 28px;
  }
  
  .event-image img {
    width: 100%;
    height: 638px;
    object-fit: cover;
    border-radius: 8px;
  }
  
  .bottom-image-container {
  width: 100vw;
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  margin-top: 60px;
}

.bottom-image {
  width: 100%;
  height: 499px;
  object-fit: cover;
  display: block;
}

@media (max-width: 768px) {
  .bottom-image {
    height: 300px;
  }
}
  
  /* Responsive Düzen */
  @media (max-width: 968px) {
    .card-grid {
      grid-template-columns: repeat(2, 1fr);
    }
  }
  
  @media (max-width: 480px) {
    .card-grid {
      grid-template-columns: 1fr;
    }
  }
  
  @media (max-width: 768px) {
    .event-image img,
    .bottom-image img {
      height: auto;
      max-height: 400px;
    }
    
    .section-title {
      font-size: 2rem;
    }
  }
  </style>