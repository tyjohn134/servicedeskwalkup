<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title class="headline text-uppercase">
        <v-img
          :src="require('./assets/logo.jpg')"
          class="my-3"
          contain
          width="200"
        ></v-img>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        text
        href="https://xxxx.service-now.com/"
        target="_blank"
      >
        <h4 class="mr-2">Service Desk Website</h4>
      </v-btn>
    </v-app-bar>
    <v-container fluid>
      <v-content>
        <Header/>
        <StepperComp />
      </v-content>
    </v-container>
  </v-app>
</template>

<script>
import Header from './components/Header';
import StepperComp from './components/StepperComp'
export default {
  name: 'App',
  components: {
    Header,
    StepperComp
  },
  data: () => ({
    //
  }),
};
</script>
