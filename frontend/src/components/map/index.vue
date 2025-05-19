<template>
  <div class="map-container ma-0 pa-0">
    <v-card class="map-card">

        <div id="map" ref="mapContainer" class="map"></div>
        <v-progress-circular
          v-if="loading"
          indeterminate
          color="primary"
          class="map-loader"
        ></v-progress-circular>
        <div class="map-controls">
          <v-btn-toggle v-model="mapStyle" mandatory>
            <v-btn 
              v-for="control in mapControls.styles" 
              :key="control.value" 
              :value="control.value" 
              small
            >
              {{ control.label }}
            </v-btn>
          </v-btn-toggle>
        </div>

    </v-card>
  </div>
</template>

<script>
import { ref, onMounted, computed, watch } from 'vue'
import { useStore } from 'vuex'
import { useTheme } from "vuetify";
import * as maplibregl from 'maplibre-gl'
import 'maplibre-gl/dist/maplibre-gl.css'

export default {
  name: 'MapComponent',
  setup() {
    const mapContainer = ref(null)
    const map = ref(null)
    const markers = ref([])
    const loading = ref(true)
    const mapStyle = ref('light')
    
    // Initialize store with error handling
    const store = useStore()
    const vuetifyTheme = useTheme();
    const theme = ref(null); // Will hold 'light' or 'dark'
    
    // Map controls configuration
    const mapControlsMockup = {
      styles: [
        { label: 'Light', value: 'light' },
        { label: 'Dark', value: 'dark' }
      ],
      navigation: {
        position: 'top-right',
        enabled: true
      },
      scale: {
        position: 'bottom-left',
        enabled: true
      }
    }

    // Get map controls from store or fallback to mockup
    const mapControls = computed(() => {
      return store.state.maps?.controls || mapControlsMockup
    })

    // Map style definitions - mockup data (will be replaced by Vuex store call)
    const mapStylesMockup = {
      light: {
        version: 8,
        sources: {
          'raster-tiles': {
            type: 'raster',
            tiles: ['https://cartodb-basemaps-a.global.ssl.fastly.net/light_all/{z}/{x}/{y}.png'],
            tileSize: 256,
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
          }
        },
        layers: [
          {
            id: 'simple-tiles',
            type: 'raster',
            source: 'raster-tiles',
            minzoom: 0,
            maxzoom: 22
          }
        ]
      },
      dark: {
        version: 8,
        sources: {
          'raster-tiles': {
            type: 'raster',
            tiles: ['https://cartodb-basemaps-a.global.ssl.fastly.net/dark_all/{z}/{x}/{y}.png'],
            tileSize: 256,
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
          }
        },
        layers: [
          {
            id: 'simple-tiles',
            type: 'raster',
            source: 'raster-tiles',
            minzoom: 0,
            maxzoom: 22
          }
        ]
      }
    }

    // Get map styles from store or fallback to mockup
    const mapStyles = computed(() => {
      return store.state.maps?.styles || mapStylesMockup
    })
    
    // Mock data to use if store is unavailable
    const fallbackLocations = ref([
      {
        id: 1,
        name: 'Default Location',
        description: 'Fallback when store is unavailable',
        state: 'active',
        coordinates: [24.1052, 56.9496]
      }
    ])
    
    // Location data with fallback
    const locationsList = computed(() => {
      return store.state.locations?.list || fallbackLocations.value
    })
    
    // Get status color based on state
    const getMarkerColor = (state) => {
      switch (state) {
        case 'READY':
          return '#4CAF50' // Green
        case 'UNAVAILABLE':
          return '#9E9E9E' // Orange
        case 'ERROR':
          return '#F44336' // Red
        default:
          return '#2196F3' // Blue (default)
      }
    }

    // Initialize map
    const initializeMap = () => {
      // Check if map container exists
      if (!mapContainer.value) return
      
      // Initialize the map
      // Get the current Vuetify theme (light/dark)
      let theme = vuetifyTheme.global.current.value.dark ? 'dark' : 'light'

      // Automatically set the map style based on the current theme if not explicitly set
      if (mapStyle.value === 'light' && theme === 'dark') {
        mapStyle.value = 'dark'
      } else if (mapStyle.value === 'dark' && theme === 'light') {
        mapStyle.value = 'light'
      }
      console.warn('Initializing map with style:', mapStyles.value[mapStyle.value], mapStyle.value, 'theme', theme)
      map.value = new maplibregl.Map({
        container: mapContainer.value,
        style: mapStyles.value[mapStyle.value],
        center: [24.1052, 56.9496], // default center on Latvia
        zoom: 6
      })

      // Add navigation controls if enabled
      if (mapControls.value.navigation && mapControls.value.navigation.enabled) {
        map.value.addControl(
          new maplibregl.NavigationControl(), 
          mapControls.value.navigation.position || 'top-right'
        )
      }
      
      // Add scale if enabled
      if (mapControls.value.scale && mapControls.value.scale.enabled) {
        map.value.addControl(
          new maplibregl.ScaleControl(), 
          mapControls.value.scale.position || 'bottom-left'
        )
      }
      
      // When the map is loaded
      map.value.on('load', () => {
        loading.value = false
        addMarkers()
      })
    }

    // Add markers to the map
    const addMarkers = () => {
      // Clear existing markers
      markers.value.forEach(marker => marker.remove())
      markers.value = []
      
      // First ensure the map has the source if it doesn't already
      if (!map.value.getSource('locations')) {
        map.value.addSource('locations', {
          'type': 'geojson',
          'data': {
            'type': 'FeatureCollection',
            'features': []
          }
        });
      }
      
      // Remove any existing circle layers
      if (map.value.getLayer('location-circles')) {
        map.value.removeLayer('location-circles');
      }


      console.warn('locationsList', locationsList.value)
      
      // Create GeoJSON data from locations
      const geojsonData = {
        'type': 'FeatureCollection',
        'features': locationsList.value.map(location => {
          if (!location.coordinates || !location.coordinates[0]) return null;
          return {
            'type': 'Feature',
            'geometry': {
              'type': 'Point',
              'coordinates': [location.coordinates[0], location.coordinates[1]]
            },
            'properties': {
              'name': location.driver_name || 'Location',
              'description': location.description || '',
              'state': location.state || 'unknown',
              'color': getMarkerColor(location.state)
            }
          };
        }).filter(Boolean) // Remove nulls
      };
      
      // Update the source data
      map.value.getSource('locations').setData(geojsonData);
      
      // Add the circle layer
      map.value.addLayer({
        'id': 'location-circles',
        'type': 'circle',
        'source': 'locations',
        'paint': {
          'circle-radius': 10,
          'circle-opacity': 0.7,
          'circle-color': ['get', 'color'],
          'circle-stroke-width': 1,
          'circle-stroke-color': '#ffffff',
          'circle-stroke-opacity': 0.7
        }
      });
      
      // Add popups on click
      map.value.on('click', 'location-circles', (e) => {
        const coordinates = e.features[0].geometry.coordinates.slice();
        const properties = e.features[0].properties;
        
        const popupHtml = `
          <h3>${properties.name}</h3>
          <p>Status: ${properties.state}</p>
        `;
        
        new maplibregl.Popup()
          .setLngLat(coordinates)
          .setHTML(popupHtml)
          .addTo(map.value);
      });
      
      // Change cursor on hover
      map.value.on('mouseenter', 'location-circles', () => {
        map.value.getCanvas().style.cursor = 'pointer';
      });
      
      map.value.on('mouseleave', 'location-circles', () => {
        map.value.getCanvas().style.cursor = '';
      });
      
      // If there are locations, fit bounds
      if (geojsonData.features.length > 0) {
        const bounds = new maplibregl.LngLatBounds();
        geojsonData.features.forEach((feature) => {
          bounds.extend(feature.geometry.coordinates);
        });
        map.value.fitBounds(bounds, { padding: 50 });
      }
    }

    // Change map style
    const changeMapStyle = (style) => {
      if (!map.value) return
      
      // Save the current center and zoom
      const center = map.value.getCenter()
      const zoom = map.value.getZoom()
      
      // Set the new style
      map.value.setStyle(mapStyles.value[style])
      
      // After the style loads, restore center/zoom and add markers
      map.value.once('styledata', () => {
        map.value.setCenter(center)
        map.value.setZoom(zoom)
        addMarkers()
      })
    }

    // Fetch location data
    const fetchLocations = async () => {
      loading.value = true
      try {
        // Check if the locations module exists in the store
        if (store.hasModule && store.hasModule('locations')) {
          await store.dispatch('locations/fetchLocations')
          console.log('Locations fetched from store')
        } else {
          console.warn('Locations module not found in store, using fallback data')
          // If module doesn't exist, we'll use the fallback data
          // No need to do anything as we already have fallbackLocations defined
        }
      } catch (error) {
        console.error('Failed to fetch locations:', error)
        // On error, we'll still use the fallback data
      } finally {
        loading.value = false
      }
    }

    // Fetch map styles and controls
    const fetchMapStyles = async () => {
      try {
        await store.dispatch('maps/fetchMapConfig')
        console.log('Map configuration fetched from store')
      } catch (error) {
        console.error('Failed to fetch map configuration:', error)
      }
    }

    // Watch for changes in the locations data
    watch(locationsList, () => {
      if (map.value) {
        addMarkers()
      }
    }, { deep: true })

    // Watch for map style changes
    watch(mapStyle, (newStyle) => {
      changeMapStyle(newStyle)
    })

    // Watch for changes in the map controls
    watch(() => mapControls.value, () => {
      // If controls change significantly, we might need to reinitialize the map
      if (map.value) {
        // We could implement more sophisticated handling here
        console.log('Map controls updated')
      }
    }, { deep: true })

    // Watch for changes in the map styles data
    watch(() => mapStyles.value, () => {
      if (map.value) {
        changeMapStyle(mapStyle.value)
      }
    }, { deep: true })

    // Initialize component
    onMounted(async () => {
      await fetchMapStyles()
      await fetchLocations()
      initializeMap()
    })

    return {
      mapContainer,
      loading,
      mapStyle,
      mapControls
    }
  }
}
</script>

<style>
.map-container {
  width: 100%;
  /* height: 100%; */
  height: calc(100vh - 74px); /* Adjust as needed for your layout */
  padding: 16px;
}

.map-card {
  height: 100%;
  position: relative;
}

.map {
  width: 100%;
  height: calc(100vh - 64px); /* Adjust as needed for your layout */
  border-radius: 4px;
}

.map-loader {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.map-title {
  font-weight: 500;
}

.map-controls {
  position: absolute;
  top: 5px;
  right: 45px;
  z-index: 1;
  padding: 5px;
  border-radius: 4px;
}

:deep(.custom-marker) {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  cursor: pointer;
  border: 2px solid white;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
}


.v-theme--dark .maplibregl-popup-content {
  background-color: rgb(69, 69, 69)!important;
  max-width: 200px;
  font-size: 14px;
  line-height: 1.5;
}
.v-theme--dark .maplibregl-popup-anchor-bottom .maplibregl-popup-tip {
  border-top-color: rgb(69, 69, 69)!important;
}
</style>