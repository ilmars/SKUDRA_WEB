<template>
    <v-dialog v-model="isActive" max-width="1000">
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn
        v-bind="activatorProps"
        color="surface-variant"
        text="Show Measurements"
        variant="flat"
      ></v-btn>
    </template>
  
    <v-card title="Measurements">
      <v-card-text>
      
      <simpleModeForm :sensors="sensors" />
    </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>

        <v-btn
          text="Close"
          @click="closeDialog"
        ></v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { ref } from "vue";
import { useStore } from "vuex";
import { defineComponent } from "vue";
import SimpleModeForm from "@/pages/measurements/simpleModeForm.vue";

export default defineComponent({
  name: "Measurements",
  props: {
    sensors: {
      type: Array,
      required: true
    },
    isActive: {
      type: Boolean,
      default: false
    }
  },
  components: {
    simpleModeForm: SimpleModeForm
  },
  emits: ['update:isActive'],
  setup(props, { emit }) {
    const closeDialog = () => {
      emit('update:isActive', false);
    };
    
    return { closeDialog };
  }
});
</script>