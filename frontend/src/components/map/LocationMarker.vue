<template>
  <div 
    class="location-marker" 
    :class="`state-${location.state}`"
    @click="selectLocation"
  >
    <div class="marker-inner"></div>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
import { useStore } from 'vuex'

export default defineComponent({
  name: 'LocationMarker',
  props: {
    location: {
      type: Object,
      required: true
    }
  },
  setup(props) {
    const store = useStore()

    const selectLocation = () => {
      store.dispatch('locations/selectLocation', props.location)
    }

    return {
      selectLocation
    }
  }
})
</script>

<style scoped>
.location-marker {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  border: 2px solid white;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
  transition: transform 0.2s ease;
}

.location-marker:hover {
  transform: scale(1.2);
}

.marker-inner {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background-color: rgba(255, 255, 255, 0.6);
}

.state-active {
  background-color: #4CAF50;
}

.state-warning {
  background-color: #FF9800;
}

.state-error {
  background-color: #F44336;
}

.state-inactive {
 
    background-color: #9E9E9E;
}
</style>