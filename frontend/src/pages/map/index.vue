<template>
  <v-app>
    <v-main>
      <!--
            Use a full-viewport row:
            - width: 100vw ensures full width
            - height: 100vh ensures full height
            - margin: 0 avoids default row spacing
          -->
      <v-row style="width: 100vw; height: 100vh; margin: 0" class="no-scroll">
        <!-- LEFT SIDE: Data Table -->
        <v-col cols="4" class="sensors-sidebar">
          <v-treeview
            :items="locationsList"
            item-title="driver_name"
            item-children="receivers"
            item-value="id"
            dense
            hoverable
            activatable
            class="mb-12 pb-3"
          >
            <!-- Optional: Custom appearance for tree items -->
            <template v-slot:prepend="{ item, isOpen }">
              <v-icon
                v-if="item.driver_name"
                :icon="isOpen ? 'mdi-domain' : 'mdi-domain'"
                :color="StatusToColor[item.state]"
              ></v-icon>
              <v-icon
                v-else
                icon="mdi-radiobox-marked"
                :color="StatusToColor[item.state]"
              ></v-icon>
            </template>
            <template v-slot:title="{ item }">
              <span v-if="item.driver_name">
                <!-- {{ item.driver_name }} -->
                <v-checkbox
                  v-model="selectSensors"
                  :value="item.id"
                  :disabled="item.state !== 'READY'"
                >
                  <template v-slot:label>
                    <span>{{ item.driver_name }}</span></template
                  >
                </v-checkbox>
              </span>
              <span v-if="item.name">{{ item.name }} ({{ item.state }})</span>

              <!-- {{ item }} -->
            </template>
          </v-treeview>
          <v-btn
            class="start-btn"
            v-if="selectSensors"
            @click="startMeasurements"
          >
            Start measurements</v-btn
          >

          <!-- <v-data-table
                :headers="headers"
                :items="items"
              >
              </v-data-table> -->
        </v-col>

        <!-- RIGHT SIDE: Map container -->
        <v-col cols="8" style="overflow: hidden" class="ma-0 pa-0">
          <div
            id="map"
            class="ma-0"
            style="width: 100%; height: 100%; background-color: lightgray"
          >
            <!-- Placeholder text -->
            <div style="text-align: center">
              <mapComonent> </mapComonent>
            </div>
          </div>
        </v-col>
      </v-row>
      <v-row>
        <v-col
          cols="12"
          style="
            position: absolute;
            z-index: 1000;
            background-color: red;
            width: 600px;
            height: 100px;
            right: 0;
            bottom: 200px;
          "
        >
          <ReceiverStream :deviceId="1" deviceIp="10.0.222.39" :devicePort="19010" />
        </v-col>
      </v-row>
    </v-main>
    <measurementComponent
      :isActive="showMeasurementDialoge"
      @update:isActive="showMeasurementDialoge = $event"
      :sensors="selectSensors"
    >
    </measurementComponent>
  </v-app>
</template>
    
    <script>
import { ref, computed } from "vue";
import { useStore } from "vuex";
import mapComonent from "@/components/map/index.vue";
// import mapComonente from "@/pages/map/index.vue";
import measurementComponent from "@/pages/measurements/index.vue";
import ReceiverStream from "@/pages/measurements/test.vue";
// Remove the problematic VTreeView import
import { VTreeview } from "vuetify/labs/VTreeview";

export default {
  name: "MapPage",
  components: {
    mapComonent,
    VTreeview,
    measurementComponent,
    ReceiverStream
    // Remove VTreeView from components registration - it should be globally registered by Vuetify
  },

  setup() {
    const StatusToColor = {
      READY: "success",
      UNAVAILABLE: "blue-grey-darken-2",
      DISABLED: "blue-grey-darken-2",
      BUSY: "warning",
    };
    const selectSensors = ref([]);
    const showMeasurementDialoge = ref(false);

    const store = useStore();
    const fallbackLocations = ref([
      {
        id: 1,
        name: "Default Location",
        description: "Fallback when store is unavailable",
        state: "active",
        coordinates: [24.1052, 56.9496],
      },
    ]);
    const locationsList = computed(() => {
      return store.state.locations?.list || fallbackLocations.value;
    });
    const startMeasurements = () => {
      // alert("Starting measurements for selected sensors: " + selectSensors.value);
      showMeasurementDialoge.value = true;
      // Here you can add the logic to start measurements for the selected sensors
      // For example, you might want to dispatch a Vuex action or call an API endpoint
    };

    return {
      fallbackLocations,
      locationsList,
      StatusToColor,
      selectSensors,
      startMeasurements,
      showMeasurementDialoge,
    };

    // Sample data for the table:
    // const headers = ref([
    //   { text: 'Name', value: 'name' },
    //   { text: 'Age', value: 'age' },
    // ])

    // const items = ref([
    //   { name: 'Alice', age: 25 },
    //   { name: 'Bob', age: 30 },
    //   { name: 'Carol', age: 28 },
    //   { name: 'Dave', age: 35 },
    // ])
  },
};
</script>
    
    <style>
/* Force the HTML/body to take up the entire viewport,
       and disable scrollbars for the entire page */
html,
body,
#app {
  margin: 0;
  padding: 0;
  height: 100%;
  width: 100%;
  overflow: hidden;
}
.sensors-sidebar {
  overflow-y: scroll;
  height: calc(100vh - 80px); /* Adjust height to account for the app bar */
}

/* Optional: just a helper class name for no-scroll if needed */
.no-scroll {
  overflow: hidden !important;
}
.v-treeview .v-input__details {
  display: none;
}
.start-btn {
  position: fixed;
  bottom: 30px;
  left: 12px;
}
</style>
  