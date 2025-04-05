<template>
  <div class="info-view">
    <div class="image-container">
      <img 
        src="@/assets/events.png"
        @click="toggleFullscreen"
        :class="{ 'fullscreen': isFullscreen }"
        alt="Information"
      />
      <div class="hero-overlay">
        <div class="overlay-content">
          <img src="@/assets/logo1.png" alt="Uri Flag" class="logo">
        <h2>INTEGRATIONSEVENTS</h2>
        </div>
      </div>
      <div class="container">
      <nav class="breadcrumb">
        <router-link to="/">Home</router-link> > <router-link to="/events">Events</router-link>
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

        <div class="events-calendar">
          <div class="event-categories">
            <button 
              v-for="category in categories" 
              :key="category.id"
              :class="['category-btn', { active: selectedCategory === category.id }]"
              @click="selectCategory(category.id)"
            >
              {{ category.name }}
            </button>
          </div>

          <div class="events-list">
            <div v-for="(events, date) in filteredEventsByCategory" :key="date" class="event-date-group">
              <div class="date-header" @click="toggleEventDetails(date)">
                <h3>{{ date }}</h3>
                <span class="arrow" :class="{ 'expanded': expandedDate === date }">▼</span>
              </div>
              
              <div class="event-details" v-if="expandedDate === date">
                <div v-for="event in events" :key="event.id" class="event-card">
                  <h4>{{ event.title }}</h4>
                  <p class="event-time">{{ event.time }}</p>
                  <p class="event-location">📍 {{ event.location }}</p>
                  <p class="event-description">{{ event.description }}</p>
                  <button class="register-btn">Anmelden</button>
                </div>
              </div>
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
      isFullscreen: false,
      showDropdown: false,
      selectedMonth: 'April 2025',
      expandedDate: null,
      selectedCategory: 'all',
      categories: [
        { id: 'all', name: 'Alle Events' },
        { id: 'beruf', name: 'Berufsmesse' },
        { id: 'sprache', name: 'Sprachcafé' },
        { id: 'kurs', name: 'Konversationskurse' },
        { id: 'schnupper', name: 'Schnuppertage' },
        { id: 'sport', name: 'Sportevents' }
      ],
      events: {
        'April 2025': [
          {
            id: 1,
            category: 'beruf',
            title: 'Berufsmesse Uri 2025',
            time: '09:00 - 17:00',
            location: 'Messe Uri, Altdorf',
            description: 'Grosse Berufsmesse mit Ausbildungsmöglichkeiten und Karrierechancen.'
          }
        ],
        'Mai 2025': [
          {
            id: 2,
            category: 'sprache',
            title: 'Internationales Sprachcafé',
            time: '14:00 - 16:00',
            location: 'Kulturhaus Uri, Altdorf',
            description: 'Sprachenaustausch in entspannter Atmosphäre.'
          }
        ],
        'Juni 2025': [
          {
            id: 3,
            category: 'kurs',
            title: 'Deutsch Konversationskurs A2/B1',
            time: '18:00 - 19:30',
            location: 'VHS Uri',
            description: 'Praktischer Konversationskurs für Fortgeschrittene.'
          }
        ],
        'Juli 2025': [
          {
            id: 4,
            category: 'schnupper',
            title: 'Schnuppertag Gesundheitsberufe',
            time: '09:00 - 15:00',
            location: 'Kantonsspital Uri',
            description: 'Einblick in verschiedene Gesundheitsberufe.'
          }
        ],
        'August 2025': [
          {
            id: 5,
            category: 'sport',
            title: 'Internationales Fussballturnier',
            time: '13:00 - 18:00',
            location: 'Sportanlage Schützenmatte',
            description: 'Freundschaftsturnier mit Teams aus der Region.'
          }
        ]
      }
    }
  },
  computed: {
    filteredEventsByCategory() {
      if (this.selectedCategory === 'all') {
        return this.events;
      }
      const filtered = {};
      Object.entries(this.events).forEach(([date, eventsList]) => {
        const filteredEvents = eventsList.filter(event => event.category === this.selectedCategory);
        if (filteredEvents.length > 0) {
          filtered[date] = filteredEvents;
        }
      });
      return filtered;
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
    },
    toggleEventDetails(date) {
      this.expandedDate = this.expandedDate === date ? null : date;
    },
    selectCategory(categoryId) {
      this.selectedCategory = categoryId;
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
  width: 40%;
  min-width: 200px;
  background: rgba(0, 123, 167, 0.55);
  padding: 10px;
  border-radius: 20px;
  text-align: center;
  color: yellow;
  pointer-events: none;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
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

.hero-overlay h2 {
  margin: 0;
  font-size: 2.5em;
  font-weight: 800;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
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

.events-calendar {
  margin-top: 30px;
}

.event-categories {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  margin-bottom: 20px;
}

.category-btn {
  padding: 8px 16px;
  border: 2px solid #007ba7;
  border-radius: 20px;
  background: transparent;
  color: #007ba7;
  cursor: pointer;
  transition: all 0.3s ease;
}

.category-btn.active {
  background: #007ba7;
  color: white;
}

.category-btn:hover {
  background: #007ba7;
  color: white;
}

.events-list {
  margin-top: 20px;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.event-date-group {
  margin-bottom: 10px;
  border: 1px solid #eee;
}

.date-header {
  padding: 15px 20px;
  background-color: #f8f9fa;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
}

.date-header:hover {
  background-color: #e9ecef;
}

.arrow {
  transition: transform 0.3s ease;
}

.arrow.expanded {
  transform: rotate(180deg);
}

.event-details {
  padding: 20px;
}

.event-card {
  background: white;
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 15px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.event-card h4 {
  margin: 0 0 10px 0;
  color: #007ba7;
}

.event-time {
  color: #666;
  font-size: 0.9em;
  margin: 5px 0;
}

.event-location {
  color: #444;
  margin: 5px 0;
}

.event-description {
  margin: 10px 0;
  color: #555;
  line-height: 1.4;
}

.register-btn {
  background-color: #007ba7;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.register-btn:hover {
  background-color: #006086;
}

@media (max-width: 768px) {
  .hero-overlay {
    width: 60%;
    padding: 15px;
  }
  
  .overlay-content {
    gap: 10px;
  }
  
  .logo {
    height: 30px;
  }
  
  .hero-overlay h2 {
    font-size: 1.8em;
  }

  .page-header h1 {
    font-size: 1.8em;
  }

  .event-card {
    padding: 15px;
  }
}
</style>