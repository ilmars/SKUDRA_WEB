<template>
  <div>
    <ReceiverStream 
      :device-id="deviceId"
      :token="token"
      :deviceIp="deviceIp"
      :devicePort="devicePort"
      :username="username"
      :serverToken="serverToken"
      :isGuestUser="isGuestUser"
    />
  </div>
</template>

<script>
import ReceiverStream from './ReceiverStream.vue';

export default {
  components: {
    ReceiverStream
  },
  data() {
    return {
      deviceId: "1",
      token: 'your-initial-token-if-any',
      deviceIp: '10.0.222.39',
      devicePort: 19010,
      username: 'testuser',
      serverToken: 'some-server-token',
      isGuestUser: false
    };
  }
};
</script>
