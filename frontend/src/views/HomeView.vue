<template>
  <div>
    <HeroSection />
    <MainContent />
  </div>
</template>

<script>
import HeroSection from '@/components/HeroSection.vue';
import MainContent from '@/components/MainContent.vue';

export default {
  name: 'HomeView',
  components: {
    HeroSection,
    MainContent
  }
}
</script>
