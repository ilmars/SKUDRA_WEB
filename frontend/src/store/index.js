import { createStore } from 'vuex'
import maps from './modules/maps'
import locations from './modules/locations'

// Import other modules as needed
// import auth from './modules/auth'
// import locations from './modules/locations'

export default createStore({
  modules: {
    maps,
    locations
    // Add other modules here
    // auth,
    // locations
  }
})