<template>
  <v-stepper v-model="e1">
    <v-stepper-header>
      <v-stepper-step :complete="e1 > 1" step="1">Sign In</v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step :complete="e1 > 2" step="2">Scan Your Badge</v-stepper-step>

      <v-divider></v-divider>
      <v-stepper-step :complete="e1 > 3" step="3">Contact Information<small>Optional</small></v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step step="4">Review Your Information</v-stepper-step>
    </v-stepper-header>

    <v-stepper-items>
      <v-stepper-content step="1">
        <v-layout pb-5 wrap align-center>
            <v-flex>
              <h3 id=q1>Where are you located?</h3>
              <v-select
              v-model="loc"
              hide-details
              :items="locations"
              label="Select your location"
              prepend-icon="mdi-city"
              single-line
              required
              ></v-select>
             <v-spacer/>
             <h3 id=q2>What is the reason for your visit?</h3>
              <v-select
              v-model="res"
              hide-details
              :items="reasons"
              label="Select your reason"
              prepend-icon="mdi-wrench-outline"
              single-line
              required
              ></v-select>
              <h3 id=q2>Who will you be working with?</h3>
              <v-select
              v-model="agent"
              hide-details
              :items="techs"
              label="Select your agent"
              prepend-icon="mdi-face-agent"
              single-line
              required
              ></v-select>
              <h3 id=q2>Do you have your badge?</h3>
              <v-select
              v-model="badge_answer"
              hide-details
              :items="badge_question"
              label="Select your answer"
              prepend-icon="mdi-account-badge"
              single-line
              required
              ></v-select>
             <v-spacer/>
            </v-flex>
        </v-layout>

        <v-btn
          v-if="badge_answer == 'Yes' || badge_answer == ''" 
          pa-2
          :disabled="isDisabledQs"
          color="primary"
          @click="e1 = 2"
        >
          Continue
        </v-btn>
        <v-btn
          v-if="badge_answer == 'No'"
          pa-2
          :disabled="isDisabledQs"
          color="primary"
          @click="e1 = 3"
        >
          Continue
        </v-btn>

      </v-stepper-content>

      <v-stepper-content step="2">
        
        <QRScanner></QRScanner>
           
        <v-btn
        v-if="hasError == false"
        :disabled="isDisabled"
          color="primary"
          @click="handler(4)"
        >
          Continue
        </v-btn>

        <v-btn
        v-if="hasError == true"
          color="primary"
          @click="e1 = 3"
        >
          Continue
        </v-btn>
        <v-btn text
        @click="e1 = 3"
        color="secondary"
        >Skip</v-btn>
        <v-btn text
        @click="e1 -= 1"
        >Back</v-btn>
      </v-stepper-content>
      <v-stepper-content step="3">
        <h3 id=q1>Please type in your first name</h3>
            <v-text-field
            v-model="firstname"
            :counter="10"
            label="First name"
            required
            prepend-icon="mdi-text"
          ></v-text-field>
           <v-spacer/>
      <h3 id=q1>Please type in your last name</h3>
            <v-text-field
            v-model="lastname"
            :counter="10"
            label="Last name"
            required
            prepend-icon="mdi-text"
          ></v-text-field>
           <v-spacer/>
            <h3 id=q1>Please type in your email address</h3>
            <v-autocomplete
                    v-model="email"
                    :items="entries"
                    :loading="isLoadingSearch"
                    :search-input.sync="search"
                    hide-no-data
                    hide-selected
                    item-text="Email Address"
                    item-value="Email"
                    label="Email address"
                    placeholder="Start typing to Search"
                    return-object
                  ></v-autocomplete>
           <v-spacer/>
      
        <v-btn
          color="primary"
          @click="e1 = 4"
        >
          Continue
        </v-btn>

        <v-btn text
        @click="e1 -= 1"
        >Back</v-btn>
  
      </v-stepper-content>
      <v-stepper-content step="4">
      <h2>Please review your information to ensure it is correct:</h2>
      <v-form v-model="valid" ref="form" @submit.prevent="handleSubmit">
        <v-layout pb-5 wrap align-center>
            <v-flex>
              
              <h3 id=q1>Where are you located?</h3>
              <v-select
              v-model="loc"
              hide-details
              :items="locations"
              label="Select your location"
              prepend-icon="mdi-city"
              single-line
              required
              readonly
              ></v-select>
             <v-spacer/>
             <h3 id=q2>What is the reason for your visit?</h3>
              <v-select
              v-model="res"
              hide-details
              :items="reasons"
              label="Select your reason"
              prepend-icon="mdi-wrench-outline"
              single-line
              required
              readonly
              ></v-select>
              <h3 id=q2>Who will you be working with?</h3>
              <v-select
              v-model="agent"
              hide-details
              :items="techs"
              label="Select your agent"
              prepend-icon="mdi-face-agent"
              single-line
              required
              readonly
              ></v-select>
            
             <h3 id=q2>Your First Name</h3>
            <v-text-field
            v-model="firstname"
            :counter="20"
            :rules=nameRules
            label="First name"
            prepend-icon="mdi-text"
            required
            readonly
          ></v-text-field>
         
            <h3 >Your Last Name</h3>
                  <v-text-field
                  v-model="lastname"
                  :counter="20"
                  label="Last name"
                  :rules=nameRules
                  required
                  prepend-icon="mdi-text"
                  readonly
                ></v-text-field>
              
                  <h3>Please type in your email address</h3>
                  <v-autocomplete
                    v-model="email"
                    :items="items"
                    @input="search=null"
                    :loading="isLoadingSearch"
                    :search-input.sync="search"           
                    hide-no-data
                    item-text="Email Address"
                    item-value="Email"
                    label="Email address"
                    placeholder="Start typing to Search"
                    prepend-icon="mdi-contact-mail"
                    return-object
                  ></v-autocomplete>
                
                <v-spacer/>
                
            </v-flex>
        </v-layout>
     </v-form>

        <v-btn
          color="primary"
          @click="handleSubmit"
          :disabled="isDisabledFinalQ"
          :loading="loading"
          type="submit"
        >
          Finish
        </v-btn>

        <v-btn text
        @click="e1 -= 1"
        >Back</v-btn>
              <v-btn text
        @click="cleanUp"
        >Start Over</v-btn>
      </v-stepper-content>
      <v-snackbar color="success" :bottom="snackbar" :timeout="timeout" v-model="snackbar">{{response.data.message}}
         <v-btn
        color="white"
        text
        @click="snackbar = false"
      >
        Close
      </v-btn>
      </v-snackbar>
    </v-stepper-items>
  </v-stepper>
</template>

<script>
import QRScanner from '../components/QRScanner';
import axios from 'axios'
import store from '../store'
  export default {
    components: {QRScanner},
    data () {
      return {
        e1: 1,
        loc: '',
        res:'',
        agent:'',
        firstname: '',
        lastname:'',
        email:null,
        badge_answer: '',
        error:'',
        valid: false,
        item: 1,
        loading: false,
        timeout: 10000,
        response:{data: {message:""}},
        snackbar: false,
        isLoadingSearch: false,
        entries: [],
        model: null,
        search: null,
        
        nameRules: [
        v => !!v || 'Name is required',
        v => v.length <= 20 || 'Name must be less than 20 characters',
        ],
        emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || 'E-mail must be valid',
        ],
        locations: [
          'Virginia, USA', 'Zurich, Switerzland', 
        ],
        reasons: [
          'I am having issues with Office (Excel, Outlook, Word)',
          'I am not able to access the internet',
          'I need my account unlocked',
          'I need my password reset',
          'My computer has run out of space',
          'My VPN is not working',
          'My screen is not working',
          'Other'
        ],
        techs: [
          '',
          '',
          '',
          '',
          ''
        ],
        badge_question: [
          'Yes','No'
        ],
      }
    },
    computed: {
      isDisabled: function() {
        if(this.$store.state.qr_data != ''){
          return false;
        }
        return true;
      },
      isDisabledQs: function() {
        if(this.loc != '' && this.res != '' && this.agent != '' && this.badge_answer != ''){
          return false
        }
        return true
      },
     hasError:function () {
      if(this.$store.state.error_msg == ''){
          return false;
        }
        return true;
     },
     isDisabledFinalQ: function() {
        if(this.loc != '' && this.res != '' && this.agent != '' && this.fname != ''&& this.lname != ''&& this.email != ''){
          return false
        }
        return true
     },
     getFirstName: function() {
       return this.$store.state.fname;
     },
      getLastName: function() {
       return this.$store.state.lname;
     },
     items () {
       const emailarray = this.entries.map(entry => entry)
       return emailarray
     }
    },
    methods: {
        handler: function(arg1) {
            this.e1 = arg1

            this.firstname = this.getFirstName;
            this.lastname = this.getLastName;
        },
      handleSubmit: function() {
          this.loading = true;
          axios.defaults.headers.post['Content-Type'] = 'application/json';
          axios.post('http://localhost:5000/ticket/create',
            {
              firstName: this.firstname,
              lastName: this.lastname,
              reason: this.res,
              assignedTo: this.agent,
              email: this.email,
              location: this.loc
            })
            .then(res => {
              this.response = res
              this.loading = false
              this.snackbar = true
              
            })
            .catch(err => {
              this.loading = false
              
            }) 
      },
      cleanUp: function() {
        this.e1 = 1;
        this.loc = '';
        this.res ='';
        this.agent ='';
        this.firstname = '';
        this.lastname ='';
        this.email ='';
        this.badge_answer = '';
        this.error ='';
        this.entries.length = 0;
        this.items.length = 0;
        this.response.data.message = ""
        store.commit('reset_qrdata');

      },
    },
    watch: {
      search(val) {
      
        // Items have already been requested
        if (this.isLoadingSearch) return
        this.model = val
        this.isLoadingSearch = true

        fetch('http://localhost:5000/ticket/searchuser?fname=' + this.firstname + '&lname=' + this.lastname)
          .then(res => res.json())
          .then(res => { 
         
          this.entries = res
          })
          .catch(err => {
            console.log(err)
          })
          .finally(() => (this.isLoadingSearch = false))
      }
    }
  }

</script>

<style scoped>
#q2 {
  margin-top: 30px;
}

</style>