<template>
  <div class="receiver-stream">
    <div class="receiver-list">
      <h3>Active Receivers</h3>{{ deviceId }} {{ deviceIp }} {{ devicePort }}
      <div v-for="receiver in receivers" :key="receiver.id" class="receiver-item">
        <div class="receiver-info">
          <span class="receiver-name">{{ receiver.name }}</span>
          <span class="receiver-status" :class="receiver.state.toLowerCase()">
            {{ receiver.state }}
          </span>
        </div>
        <div class="receiver-details">
          <span>Type: {{ receiver.type }}</span>
          <span>ID: {{ receiver.id }}</span>
        </div>
      </div>
    </div>
    <div class="controls">
      <button @click="startStream" :disabled="isStreaming">Start Stream</button>
      <button @click="stopStream" :disabled="!isStreaming">Stop Stream</button>
    </div>
  </div>
</template>

<script>
import { ApiClient } from './../../grpcModule/client';
import { ref, onMounted, onUnmounted } from 'vue';

export default {
  name: 'ReceiverStream',
  props: {
    deviceId: {
      type: String,
      required: true
    },
    token: {
      type: String,
      required: true
    },
    deviceIp: {
      type: String,
      required: true
    },
    devicePort: {
      type: [String, Number],
      required: true
    },
    username: {
      type: String,
      default: ''
    },
    serverToken: {
      type: String,
      default: ''
    },
    isGuestUser: {
      type: Boolean,
      default: false
    }
  },
  setup(props) {
    const client = new ApiClient('http://localhost:9090');
    const receivers = ref([]);
    const isStreaming = ref(false);
    let stream = null;

    const performHandshakeAndStream = async () => {
      try {
        // Use a default/placeholder username and serverToken if not available in props
        // Or, you might want to pass these as props if they are dynamic
        const username = props.username || ''; // Assuming username might be a prop
        const serverToken = props.serverToken || ''; // Assuming serverToken might be a prop
        const isGuestUser = props.isGuestUser !== undefined ? props.isGuestUser : false; // Assuming isGuestUser might be a prop

        const token = await client.handshake(
          props.deviceId, 
          username, 
          serverToken, 
          isGuestUser, 
          props.deviceIp, 
          props.devicePort
        );
        console.log("got token:", token);
        // Now that handshake is complete and token is stored in the client, start the stream
        startStreamLogic();
      } catch (error) {
        console.error('Handshake failed:', error);
        // Handle handshake error (e.g., show a message to the user)
        isStreaming.value = false; // Ensure streaming is not marked as active
      }
    };

    const startStreamLogic = () => {
      console.log('Starting stream...', isStreaming.value);
      // if (isStreaming.value) return;

      stream = client.streamReceiverList(
        props.deviceId,
        (data) => {
          receivers.value = data;
        },
        (error) => {
          console.error('Stream error:', error);
          isStreaming.value = false;
        },
        props.deviceIp,
        props.devicePort
      );
      isStreaming.value = true;
    };

    const startStream = () => {
      if (isStreaming.value) return;
      isStreaming.value = true; // Mark as streaming immediately to prevent multiple clicks
      performHandshakeAndStream();
    };

    const stopStream = () => {
      if (stream) {
        stream.cancel();
        stream = null;
      }
      isStreaming.value = false;
    };

    // Cleanup on component unmount
    onUnmounted(() => {
      if (stream) {
        stream.cancel();
      }
    });

    return {
      receivers,
      isStreaming,
      startStream, // This will now trigger the handshake first
      stopStream
    };
  }
};
</script>

<style scoped>
.receiver-stream {
  padding: 20px;
}

.receiver-list {
  margin-bottom: 20px;
}

.receiver-item {
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 10px;
  margin-bottom: 10px;
}

.receiver-info {
  display: flex;
  justify-content: space-between;
  margin-bottom: 5px;
}

.receiver-name {
  font-weight: bold;
}

.receiver-status {
  padding: 2px 8px;
  border-radius: 12px;
  font-size: 0.9em;
}

.receiver-status.ready {
  background-color: #4CAF50;
  color: white;
}

.receiver-status.disabled {
  background-color: #f44336;
  color: white;
}

.receiver-details {
  display: flex;
  gap: 20px;
  font-size: 0.9em;
  color: #666;
}

.controls {
  display: flex;
  gap: 10px;
}

button {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  background-color: #4CAF50;
  color: white;
  cursor: pointer;
}

button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

button:hover:not(:disabled) {
  background-color: #45a049;
}
</style>
