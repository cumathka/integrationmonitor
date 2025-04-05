<template>
    <header>
        <!-- Filters Section -->
        <div class="container mt-4">
            <div class="row mb-3">
                <div class="col-md-3">
                    <input type="text" class="form-control" placeholder="Nach Ort filtern">
                </div>
                <div class="col-md-3">
                    <input type="text" class="form-control" placeholder="Nach Themen filtern">
                </div>
                <div class="col-md-3">
                    <input type="text" class="form-control" placeholder="Nach Sprache filtern">
                </div>
                <div class="col-md-3">
                    <button class="btn btn-secondary w-100">Alle löschen</button>
                </div>
            </div>
        </div>

        <!-- Map Section -->
        <div class="container mt-4">
            <div id="map" class="osm-map"></div>
        </div>
    </header>
</template>

<script>
import L from 'leaflet'

export default {
    name: 'TheHeader',
    components: {},
   
    
    mounted() {
        // Initialize map
        const map = L.map('map').setView([46.7712, 8.6280], 10); // Switzerland center coordinates
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors'
        }).addTo(map);

        this.startRotation();
    },
    methods: {
        handleCantonHover(cantonData) {
            this.hoveredCanton = cantonData
        },
    }
}
</script>

<style>

.highlight {
    background-color: #f57223;
    color: white;
    padding: 20px;
    text-align: center;
    min-height: 100px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 10px;
}

.main-text {
    font-size: 2.5rem;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.translation-text {
    font-size: 1.3rem;
    font-style: italic;
    opacity: 0.9;
}

.navbar {
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.navbar-brand {
    font-weight: bold;
    color: #333;
}

.nav-link {
    color: #666;
}

.nav-link:hover {
    color: #f57223;
}

.map-container {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.swiss-map {
    min-height: 400px;
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 20px;
    margin-top: 15px;
}

.canton-tooltip {
    position: absolute;
    background: rgba(0, 0, 0, 0.8);
    color: white;
    padding: 5px 10px;
    border-radius: 4px;
    font-size: 14px;
}

.osm-map {
    height: 500px;
    width: 100%;
    border-radius: 8px;
    margin: 20px 0;
}

.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>