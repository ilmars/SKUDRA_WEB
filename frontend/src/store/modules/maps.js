// maps.js - Vuex store module for map configuration
// This module handles map styles and map-related configuration

const state = () => ({
  styles: {
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
  },
  controls: {
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
  },
  loading: false,
  error: null
})

const getters = {
  getMapStyles: (state) => state.styles,
  getMapControls: (state) => state.controls,
  isLoading: (state) => state.loading,
  getError: (state) => state.error
}

const actions = {
  // Fetch map configuration from API (simulated for now)
  async fetchMapConfig({ commit }) {
    try {
      commit('SET_LOADING', true)
      
      // In a real application, this would be an API call
      // For now we're simulating a successful API response
      await new Promise(resolve => setTimeout(resolve, 500))
      
      // This would normally come from an API
      const mapStyles = {
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
      
      const mapControls = {
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
      
      commit('SET_MAP_STYLES', mapStyles)
      commit('SET_MAP_CONTROLS', mapControls)
      commit('SET_ERROR', null)
    } catch (error) {
      console.error('Error fetching map configuration:', error)
      commit('SET_ERROR', 'Failed to load map configuration')
    } finally {
      commit('SET_LOADING', false)
    }
  }
}

const mutations = {
  SET_MAP_STYLES(state, styles) {
    state.styles = styles
  },
  SET_MAP_CONTROLS(state, controls) {
    state.controls = controls
  },
  SET_LOADING(state, isLoading) {
    state.loading = isLoading
  },
  SET_ERROR(state, error) {
    state.error = error
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}