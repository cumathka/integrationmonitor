<template>
  <div class="not-found">
    <h1>404 - Seite nicht gefunden</h1>
    <p>Die angeforderte Seite konnte nicht gefunden werden.</p>
    <router-link to="/" class="home-link">Zurück zur Startseite</router-link>
  </div>
</template>

<style scoped>
.not-found {
  text-align: center;
  padding: 50px 20px;
}

.home-link {
  display: inline-block;
  margin-top: 20px;
  padding: 10px 20px;
  background-color: var(--cyan-600);
  color: white;
  text-decoration: none;
  border-radius: 5px;
}

.home-link:hover {
  background-color: var(--cyan-700);
}
</style>
