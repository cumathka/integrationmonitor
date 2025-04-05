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
  background: rgba(40, 40, 40, 0.7); /* Changed from blue to dark gray */
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
  font-size: 2.5em; /* Increased from 2em */
  font-weight: bold;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
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
</style>