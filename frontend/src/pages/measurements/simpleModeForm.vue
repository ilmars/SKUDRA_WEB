<template>
  <v-card outlined class="pa-4">
    <v-form @submit.prevent="onSubmit">
      
    <v-row align="center" justify="start">
      <!-- Frequency Field -->
      <v-col cols="3">
        <v-number-input
          label="Frequency"
          v-model="frequency"
          :precision="4"
          
          variant="filled"
          class="mx-auto"
        />
      </v-col>

      <!-- Direction Finding -->
      <v-col cols="3" :class="is_directionfinder? 'text-center ':'text-center disabled-mode'">
        <div class="mb-2">Direction Finding</div>
        <v-btn icon color="success" @click="toggleDirectionFinding">
          <v-icon>
            {{ directionFindingActive ? "mdi-stop" : "mdi-play" }}
          </v-icon>
        </v-btn>
      </v-col>

      <!-- Spectrum Measurement -->
      <v-col cols="3" :class="is_levelmeter? 'text-center ':'text-center disabled-mode'">
        <div class="mb-2">Spectrum Measurement</div>
        <v-btn icon color="success" @click="toggleSpectrumMeasurement">
          <v-icon>
            {{ spectrumMeasurementActive ? "mdi-stop" : "mdi-play" }}
          </v-icon>
        </v-btn>
      </v-col>

      <!-- Record Button -->
      <v-col cols="3" class="text-center">
        <v-btn color="error" variant="contained" class="pa-4" @click="onRecord">
          RECORD
        </v-btn>
      </v-col>
    </v-row>
    </v-form>
  </v-card>
</template>

<script>
import { ref, defineComponent } from "vue";

export default defineComponent({
  name: "SimpleModeForm",
  props: {
    sensors: {
      type: Array,
      required: true,
    },
    isActive: {
      type: Boolean,
      default: false,
    },
  },
  setup(props, { emit }) {
    // Frequency is read-only for demonstration
    const frequency = ref("120 MHz");
    const is_levelmeter = ref(false);
    const is_directionfinder = ref(false);

    // State for toggles
    const directionFindingActive = ref(false);
    const spectrumMeasurementActive = ref(false);

    function toggleDirectionFinding() {
      directionFindingActive.value = !directionFindingActive.value;
    }

    function toggleSpectrumMeasurement() {
      spectrumMeasurementActive.value = !spectrumMeasurementActive.value;
    }

    function onRecord() {
      console.log("Recording started...");
    }
    function onSubmit() {
      // Handle form submission logic here
      console.log("Form submitted with frequency:", frequency.value);
    }

    return { 
        frequency, 
        directionFindingActive, 
        spectrumMeasurementActive, 
        is_levelmeter, 
        is_directionfinder, 
        toggleDirectionFinding, 
        toggleSpectrumMeasurement, 
        onRecord,
        onSubmit
    };
  },
});
</script>

<style scoped>
/* Adjust spacing, alignment, or other styles as needed */
.disabled-mode {
  pointer-events: none; 
  opacity: 0.5; 
}
.disabled-mode .v-btn {
  background-color: #686868!important; /* Light grey background for disabled button */
  color: #9e9e9e; /* Grey text color for disabled button */
}
</style>
