<template>
    <section class="hero-section">
      <div class="hero-container">
        <img src="@/assets/1.jpg" alt="Hero Background" class="hero-image" />
        <div class="hero-overlay">
          <div class="hero-text">
            <div class="main-greeting">
              <img src="@/assets/uri-flag.png" alt="Uri Flag" class="uri-flag">
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
    </section>
  </template>
  
  <script>
  export default {
    name: 'HeroSection',
    data() {
      return {
        greetings: [
          { text: 'مرحبا', lang: 'Arabisch' },
          { text: 'Merhaba', lang: 'Türkisch' },
          { text: 'سلام', lang: 'Persisch' },
          { text: 'ሰላም', lang: 'Tigrinya' },
          { text: 'Здравствуйте', lang: 'Russisch' },
          { text: 'வணக்கம்', lang: 'Tamil' },
          { text: 'Përshëndetje', lang: 'Albanisch' },
          { text: 'नमस्ते', lang: 'Hindi' },
          { text: 'ہیلو', lang: 'Urdu' },
          { text: 'Olá', lang: 'Portugiesisch' },
          { text: 'Zdravo', lang: 'Serbisch' },
          { text: 'Tungjatjeta', lang: 'Kosovarisch' },
          { text: 'სალამი', lang: 'Georgisch' },
          { text: 'Jambo', lang: 'Swahili' },
          { text: 'hello', lang: 'Englisch' }
        ]
      }
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
    background: rgba(0, 123, 167, 0.55); /* Şeffaf mavi */
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    color: yellow;
  }
  
  /* Başlık */
  .hero-title {
    font-size: 2.5rem;
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
    font-size: 1.5rem;
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
    font-size: 0.65rem;
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
  </style>
