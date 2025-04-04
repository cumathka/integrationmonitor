<template>
    <main class="container py-5 my-5">
      <section class="mb-5">
        <h2 class="text-h1 mb-4" style="color: var(--orange-600);">Hier kommen Sie weiter</h2>
        <p class="text-regular">
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
      
      <section class="my-5">
        <div class="row g-4">
          <div class="col-md-3" v-for="(card, index) in cards" :key="index">
            <div class="card h-100 border-0" style="border-radius: 31px;">
              <div class="card-body text-center py-5" :style="{ backgroundColor: index % 2 ? 'var(--cyan-600)' : 'var(--cyan-700)' }">
                <div class="mb-4">
                  <img :src="card.icon" :alt="card.title" width="128" height="128">
                </div>
                <h3 class="text-h3 text-white">{{ card.title }}</h3>
              </div>
            </div>
          </div>
        </div>
      </section>
      
      <section class="my-5">
        <h2 class="text-h1 mb-4" style="color: var(--orange-600);">Events</h2>
        <p class="text-regular mb-4">
          Entdecken Sie Veranstaltungen in Uri und Umgebung, die Ihnen helfen, neue Kontakte zu knüpfen und sich
          zu integrieren.
        </p>
        <img 
          src="https://c.animaapp.com/m939jagjfdOBIu/img/image-1.png" 
          alt="Events" 
          class="img-fluid rounded"
          style="height: 638px; width: 100%; object-fit: cover;"
        >
      </section>
      
      <img 
        src="https://c.animaapp.com/m939jagjfdOBIu/img/group-2.png" 
        alt="Content bottom" 
        class="img-fluid w-100 mt-5"
        style="height: 499px; object-fit: cover;"
      >
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
            icon: 'https://c.animaapp.com/m939jagjfdOBIu/img/union-8.svg'
          },
          { 
            title: 'Lernen',
            icon: 'https://c.animaapp.com/m939jagjfdOBIu/img/union-23.svg'
          },
          { 
            title: 'Jobs',
            icon: 'https://c.animaapp.com/m939jagjfdOBIu/img/union-11.svg'
          },
          { 
            title: 'Events',
            icon: 'https://c.animaapp.com/m939jagjfdOBIu/img/union-10.svg'
          }
        ]
      }
    }
  }
  </script>