<template>
  <div class="landing-page">
    <!-- Arka plan daireleri -->
    <div class="ellipse"></div>
    <div class="div"></div>
    <div class="ellipse-2"></div>
    <div class="ellipse-3"></div>

    <TheNavbar />

    <!-- Main content with proper container -->
    <div >
      <router-view v-if="$route.path !== '/'" />
      <HomeView v-else />
    </div>

    <!-- Full-width bottom image -->
    <div class="full-width-image">
      <img src="@/assets/footer.png" alt="Content bottom" class="img-fluid">
    </div>

    <!-- Footer will be full-width -->
    <FooterSection />
  </div>
</template>

<script>
import TheNavbar from '@/components/TheNavbar.vue';
import FooterSection from '@/components/FooterSection.vue';
import HomeView from '@/views/HomeView.vue';

export default {
  name: 'App',
  components: {
    TheNavbar,
    HomeView,
    FooterSection
  }
}
</script>

<style>
@import url("https://cdnjs.cloudflare.com/ajax/libs/meyer-reset/2.0/reset.min.css");
@import url("https://fonts.googleapis.com/css?family=ABeeZee|Roboto:400|Roboto+Condensed:400");
@import url('https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css');
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css");

:root {
  --cyan-600: rgba(10, 162, 192, 1);
  --cyan-700: rgba(8, 121, 144, 1);
  --hitbox: rgba(255, 255, 255, 0.0);
  --green-600: rgba(20, 108, 67, 1);
  --yellow-100: rgba(255, 243, 205, 1);
  --orange-100: rgba(255, 229, 208, 1);
  --body-textbody-color: rgba(33, 37, 41, 1);
  --grayblack: rgba(0, 0, 0, 1);
  --gray-700: rgba(73, 80, 87, 1);
  --gray-900: rgba(33, 37, 41, 1);
  --blue-600: rgba(10, 88, 202, 1);
  --blue-100: rgba(231, 241, 255, 1);
  --blue-300: rgba(110, 168, 254, 1);
  --graywhite: rgba(255, 255, 255, 1);
  --componentsdropdownsborder: rgba(0, 0, 0, 0.15);
  --gray-600: rgba(108, 117, 125, 1);
  --gray-400: rgba(206, 212, 218, 1);
  --themeprimary: rgba(13, 110, 253, 1);
  --orange-500: rgba(253, 126, 20, 1);
  --orange-600: rgba(202, 101, 16, 1);
  --yellow-500: rgba(255, 193, 7, 1);
  --yellow-600: rgba(255, 211, 39, .9);
  --gray-200: rgba(233, 236, 239, 1);
  --componentsbuttonprimaryhovered-background: rgba(11, 94, 215, 1);
  --componentsdropdownslight-hovered-item-text: rgba(30, 33, 37, 1);
  --componentsinputfocused-border: rgba(134, 183, 254, 1);
  --componentsbuttonprimaryhovered-border: rgba(10, 88, 202, 1);
  --componentsbuttonprimaryactive-background: rgba(10, 88, 202, 1);
  --componentsbuttonprimaryactive-border: rgba(10, 83, 190, 1);
  --text-h3-font-family: "Roboto Condensed", Helvetica;
  --text-h3-font-weight: 400;
  --text-h3-font-size: 40px;
  --text-h3-letter-spacing: 0px;
  --text-h3-line-height: 115%;
  --text-h3-font-style: normal;
  --text-regular-font-family: "Roboto", Helvetica;
  --text-regular-font-weight: 400;
  --text-regular-font-size: 20px;
  --text-regular-letter-spacing: 0.5px;
  --text-regular-line-height: 24px;
  --text-regular-font-style: normal;
  --body-lead-font-family: "ABeeZee", Helvetica;
  --body-lead-font-weight: 400;
  --body-lead-font-size: 20px;
  --body-lead-letter-spacing: 0px;
  --body-lead-line-height: 150%;
  --body-lead-font-style: normal;
  --body-regular-font-family: "ABeeZee", Helvetica;
  --body-regular-font-weight: 400;
  --body-regular-font-size: 16px;
  --body-regular-letter-spacing: 0px;
  --body-regular-line-height: 150%;
  --body-regular-font-style: normal;
  --text-h0-font-family: "Roboto Condensed", Helvetica;
  --text-h0-font-weight: 400;
  --text-h0-font-size: 96px;
  --text-h0-letter-spacing: 0px;
  --text-h0-line-height: 150%;
  --text-h0-font-style: normal;
  --text-h1-font-family: "Roboto Condensed", Helvetica;
  --text-h1-font-weight: 400;
  --text-h1-font-size: 64px;
  --text-h1-letter-spacing: 0px;
  --text-h1-line-height: 115%;
  --text-h1-font-style: normal;
  --heading-h5-font-family: "ABeeZee", Helvetica;
  --heading-h5-font-weight: 400;
  --heading-h5-font-size: 20px;
  --heading-h5-letter-spacing: 0px;
  --heading-h5-line-height: 120.00000762939453%;
  --heading-h5-font-style: normal;
  --active-shadow-primary: 0px 0px 0px 4px rgba(49, 132, 253, 0.5);
  --active-shadow-outline-primary: 0px 0px 0px 4px rgba(13, 110, 253, 0.25);
}

.landing-page {
  position: relative;
  overflow-x: hidden;
  /* Prevent horizontal scroll */
}

.main-container {
  max-width: 1500px;
  margin: 0 auto;
  padding: 0 20px;
  position: relative;
  z-index: 2;
}

.full-width-image {
  width: 100vw;
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  margin-top: 60px;
}

.full-width-image img {
  width: 100%;
  height: 499px;
  object-fit: cover;
  display: block;
}

/* Dairelerin stilleri */
.landing-page .ellipse {
  position: absolute;
  width: 400px;
  height: 400px;
  top: 40%;
  left: -250px;
  background-color: var(--yellow-100);
  border-radius: 50%;
  z-index: 0;
}

.landing-page .div {
  position: absolute;
  width: 350px;
  height: 350px;
  top: 55%;
  right: -200px;
  background-color: var(--yellow-100);
  border-radius: 50%;
  z-index: 0;
}

.landing-page .ellipse-2 {
  position: absolute;
  width: 250px;
  height: 250px;
  top: 67%;
  left: -150px;
  background-color: var(--orange-100);
  border-radius: 50%;
  z-index: 0;
}

.landing-page .ellipse-3 {
  position: absolute;
  width: 469px;
  height: 475px;
  top: 32%;
  right: -300px;
  background-color: var(--orange-100);
  border-radius: 50%;
  z-index: 0;
}

/* Mobil uyumluluk */
@media (max-width: 768px) {

  .landing-page .ellipse,
  .landing-page .div,
  .landing-page .ellipse-2,
  .landing-page .ellipse-3 {
    display: none;
  }

  .main-container {
    padding: 0 15px;
  }
}

.text-h1 {
  font-family: var(--text-h1-font-family);
  font-weight: var(--text-h1-font-weight);
  font-size: var(--text-h1-font-size);
  letter-spacing: var(--text-h1-letter-spacing);
  line-height: var(--text-h1-line-height);
  font-style: var(--text-h1-font-style);
}

.text-h3 {
  font-family: var(--text-h3-font-family);
  font-weight: var(--text-h3-font-weight);
  font-size: var(--text-h3-font-size);
  letter-spacing: var(--text-h3-letter-spacing);
  line-height: var(--text-h3-line-height);
  font-style: var(--text-h3-font-style);
}

.text-regular {
  font-family: var(--text-regular-font-family);
  font-weight: var(--text-regular-font-weight);
  font-size: var(--text-regular-font-size);
  letter-spacing: var(--text-regular-letter-spacing);
  line-height: var(--text-regular-line-height);
  font-style: var(--text-regular-font-style);
}

.body-lead {
  font-family: var(--body-lead-font-family);
  font-weight: var(--body-lead-font-weight);
  font-size: var(--body-lead-font-size);
  letter-spacing: var(--body-lead-letter-spacing);
  line-height: var(--body-lead-line-height);
  font-style: var(--body-lead-font-style);
}

.body-regular {
  font-family: var(--body-regular-font-family);
  font-weight: var(--body-regular-font-weight);
  font-size: var(--body-regular-font-size);
  letter-spacing: var(--body-regular-letter-spacing);
  line-height: var(--body-regular-line-height);
  font-style: var(--body-regular-font-style);
}
/* Responsive adjustments */
@media (max-width: 1200px) {
  .landing-page .ellipse,
  .landing-page .div,
  .landing-page .ellipse-2,
  .landing-page .ellipse-3 {
    opacity: 0.5;
  }
}

@media (max-width: 992px) {
  .landing-page .ellipse,
  .landing-page .div,
  .landing-page .ellipse-2,
  .landing-page .ellipse-3 {
    opacity: 0.3;
  }
}

@media (max-width: 768px) {
  .landing-page .ellipse,
  .landing-page .div,
  .landing-page .ellipse-2,
  .landing-page .ellipse-3 {
    display: none;
  }

  .main-container {
    padding: 0 15px;
  }

  .full-width-image img {
    min-height: 200px;
  }
}
</style>