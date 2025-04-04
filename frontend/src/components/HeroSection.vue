<template>
    <section class="hero-section">
      <div class="hero-container">
        <img 
          src="https://c.animaapp.com/m939jagjfdOBIu/img/group-1.png" 
          alt="Hero background" 
          class="hero-image"
        >
        
        <div class="hero-overlay">
          <div class="hero-text">
            <h1 class="hero-title">Gemeinsam Weg und Wissen Teilen</h1>
            <p class="hero-subtitle" :key="currentIndex">{{ translations[currentIndex].text }}</p>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script>
  export default {
    name: 'HeroSection',
    data() {
      return {
        currentIndex: 0,
        rotateInterval: null,
        translations: [
          { lang: 'tr', text: 'Yolu ve bilgiyi birlikte paylaşmak' },
          { lang: 'ar', text: 'مشاركة الطريق والمعرفة معا' },
          { lang: 'fa', text: 'به اشتراک گذاشتن راه و دانش با یکدیگر' },
          { lang: 'ps', text: 'د لارې او پوهې شریکول' },
          { lang: 'ti', text: 'መንገድን ፍልጠትን ብሓባር ምክፋል' },
          { lang: 'so', text: 'Wadajir u wadaagista wadada iyo aqoonta' },
          { lang: 'ur', text: 'راستہ اور علم کا مشترکہ اشتراک' },
          { lang: 'ku', text: 'Rê û zanînê bi hev re parve bikin' },
          { lang: 'am', text: 'መንገድና እውቀትን በአንድነት መካፈል' },
          { lang: 'sw', text: 'Kushiriki njia na maarifa pamoja' }
        ]
      }
    },
    mounted() {
      this.rotateInterval = setInterval(this.rotateText, 1500);
    },
    methods: {
      rotateText() {
        this.currentIndex = (this.currentIndex + 1) % this.translations.length;
      }
    },
    beforeUnmount() {
      clearInterval(this.rotateInterval);
    }
  }
  </script>
  
  <style scoped>
  .hero-section {
    width: 100%;
    position: relative;
    margin: 0;
    padding: 0;
  }
  
  .hero-container {
    position: relative;
    width: 100%;
    height: 100%;
  }
  
  .hero-image {
    width: 100%;
    height: 800px;
    object-fit: cover;
    display: block;
  }
  
  .hero-overlay {
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: rgba(253, 126, 20, 0.9); /* var(--orange-500) with opacity */
  }
  
  .hero-text {
    text-align: center;
    padding: 2rem;
    width: 100%;
    max-width: 1200px;
  }
  
  .hero-title {
    font-family: var(--text-h1-font-family);
    font-weight: var(--text-h1-font-weight);
    font-size: var(--text-h1-font-size);
    color: white;
    margin-bottom: 1rem;
    line-height: 1.2;
  }
  
  .hero-subtitle {
    font-family: var(--text-h3-font-family);
    font-weight: var(--text-h3-font-weight);
    font-size: var(--text-h3-font-size);
    color: white;
    margin: 0;
    transition: opacity 0.3s ease;
    animation: fadeInOut 1.5s ease-in-out;
  }
  
  @keyframes fadeInOut {
    0% { opacity: 0; }
    20%, 80% { opacity: 1; }
    100% { opacity: 0; }
  }
  
  /* Responsive adjustments */
  @media (max-width: 992px) {
    .hero-image {
      height: 600px;
    }
    
    .hero-title {
      font-size: 2.5rem;
    }
    
    .hero-subtitle {
      font-size: 1.5rem;
    }
  }
  
  @media (max-width: 768px) {
    .hero-image {
      height: 500px;
    }
    
    .hero-title {
      font-size: 2rem;
    }
    
    .hero-subtitle {
      font-size: 1.2rem;
    }
    
    .hero-text {
      padding: 1rem;
    }
  }
  </style>