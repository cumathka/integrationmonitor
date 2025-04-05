<template>
    <section class="hero-section">
      <div class="hero-container">
        <img src="@/assets/1.jpg" alt="Hero Background" class="hero-image" />
        <div class="hero-overlay">
          <div class="hero-text">
            <div class="main-greeting">
              <img src="@/assets/logo1.png" alt="Uri Flag" class="uri-flag">
              <h1 class="hero-title">Griäzi! Willkommen!</h1>
            </div>
            <div class="greetings">
              <p v-for="(greeting, index) in greetings" 
                 :key="index"
                 :class="['greeting-item', `pulse-${index % 5}`]">
                {{ greeting.text }}
                <span class="language-name">{{ greeting.lang }}</span>
              </p>
            </div>
          </div>
        </div>
      </div>
      <!-- New Orange Section -->
      <div class="orange-section pt-5 pb-5">
        <div class="orange-content">
          <h1 class="section-title">Gemeinsam Weg und Wissen Teilen</h1>
          <p class="section-subtitle" :key="currentIndex">{{ translations[currentIndex].text }}</p>
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
        ],
        greetings: [
          { text: 'مرحبا', lang: 'Arabisch' },
          { text: 'Merhaba', lang: 'Türkisch' },
          { text: 'سلام', lang: 'Persisch' },
          { text: 'ሰላም', lang: 'Tigrinya' },
          { text: 'Здравствуйте', lang: 'Russisch' },
          { text: 'வணக்கம்', lang: 'Tamil' },
          { text: 'Përshëndetje', lang: 'Albanisch' },
          { text: 'नमस्ते', lang: 'Hindi' },
          { text: 'Zdravo', lang: 'Serbisch' },
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
  
  /* Arka plan resmi */
  .hero-image {
    width: 100%;
    height: 800px;
    object-fit: cover;
    display: block;
  }
  
  /* Şeffaf mavi kutu */
  .hero-overlay {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 50%;
    background: rgba(8, 121, 144, 0.8); /* Şeffaf mavi */
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    color:rgb(255, 255, 255);
  }
  
  /* Başlık */
  .hero-title {
    font-family: var(--text-h1-font-family);
    font-weight: var(--text-h1-font-weight);
    font-size:5.5rem;
    margin-bottom: 10px;
  }
  
  /* Emoji */
  .emoji {
    font-size: 5rem;
  }
  
  .main-greeting {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 20px;
    margin-bottom: 30px;
  }
  
  .uri-flag {
    height: 80px;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.2);
  }
  
  .greetings {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    padding: 15px;
  }
  
  .greeting-item {
    font-size: 2.5rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 5px;
    animation: none; /* Remove the old animation */
  }
  
  /* New pulsing animations with different timings */
  .pulse-0 {
    animation: pulse 4s ease-in-out infinite;
  }
  
  .pulse-1 {
    animation: pulse 4s ease-in-out infinite 0.8s;
  }
  
  .pulse-2 {
    animation: pulse 4s ease-in-out infinite 1.6s;
  }
  
  .pulse-3 {
    animation: pulse 4s ease-in-out infinite 2.4s;
  }
  
  .pulse-4 {
    animation: pulse 4s ease-in-out infinite 3.2s;
  }
  
  @keyframes pulse {
    0%, 100% { 
      opacity: 0.3;
      transform: scale(0.95);
    }
    50% { 
      opacity: 1;
      transform: scale(1);
    }
  }
  
  /* Remove old delay classes and fadeIn animation */
  
  .language-name {
    font-size: 1.65rem;
    opacity: 0.6;
    margin-top: 2px;
  }
  
  @media (max-width: 992px) {
    .hero-overlay {
      width: 70%;
    }
  
    .hero-title {
      font-size: 2rem;
    }
  
    .greetings {
      grid-template-columns: repeat(2, 1fr);
    }
  }
  
  @media (max-width: 768px) {
    .hero-overlay {
      width: 90%;
      padding: 20px;
    }
  
    .hero-title {
      font-size: 1.8rem;
    }
  
    .greetings {
      grid-template-columns: repeat(2, 1fr);
      gap: 10px;
    }

    .greeting-item .lang {
      font-size: .6rem;
    }
  
    .greeting-item {
      font-size: 1.1rem;    
    }
  
    .language-name {
      font-size: 0.6rem;
    }
  }

  .orange-section {
    width: 100%;
    background-color: rgba(253, 126, 20, 0.9);
    padding: 1rem 0;
  }

  .orange-content {
    max-width: 1200px;
    margin: 0 auto;
    text-align: center;
    padding: 0 20px;
  }

  .section-title {
    font-family: var(--text-h1-font-family);
    font-weight: var(--text-h1-font-weight);
    font-size: 4rem;
    color: white;
    margin-bottom: 1.5rem;
  }

  .section-subtitle {
    font-family: var(--text-h3-font-family);
    font-weight: var(--text-h3-font-weight);
    font-size: 2.5rem;
    color: white;
    margin: 0;
    animation: fadeInOut 1.5s ease-in-out;
  }

  @keyframes fadeInOut {
    0% { opacity: 0; }
    20%, 80% { opacity: 1; }
    100% { opacity: 0; }
  }

  @media (max-width: 768px) {
    .section-title {
      font-size: 2rem;
    }

    .section-subtitle {
      font-size: 1.2rem;
    }
  }
  </style>
