<template>
  <div>
    <v-alert type="error" v-if="this.$store.state.error_msg" show>{{this.$store.state.error_msg}}.Please press continue</v-alert>
    <v-alert type="success" v-if="this.$store.state.qr_data" show>Your badge has successfuuly scanned!</v-alert>
    <h2 text-align="center">Please place the QR code on your badge in front of the camera:</h2>
    <small>You may need to move your badge closer to the camera. It can also take several seconds to scan. Please be paitent.</small>
    <qrcode-stream @decode="onDecode" @init="onInit" />
  </div>
</template>

<script>
import store from '../store'
import { QrcodeStream } from 'vue-qrcode-reader'

export default {
  components: { QrcodeStream },
  data () {
    return {
      result: '',
      error: '',
      split_data: '',
    }
  },
  methods: {
    onDecode (result) {
     store.commit('set_qrdata', result)
   
    },
    async onInit (promise) {
      try {
        await promise
      } catch (error) {
        if (error.name === 'NotAllowedError') {
          this.error = "ERROR: you need to grant camera access permisson"
        } else if (error.name === 'NotFoundError') {
          this.error = "ERROR: no camera on this device"
        } else if (error.name === 'NotSupportedError') {
          this.error = "ERROR: secure context required (HTTPS, localhost)"
        } else if (error.name === 'NotReadableError') {
          this.error = "ERROR: is the camera already in use?"
        } else if (error.name === 'OverconstrainedError') {
          this.error = "ERROR: installed cameras are not suitable"
        } else if (error.name === 'StreamApiNotSupportedError') {
          this.error = "ERROR: Stream API is not supported in this browser"
        }
        store.commit('set_error', error)
      }
    }, 
  }
}
</script>

<style scoped>
.error {
  font-weight: bold;
  color: red;
}
</style>