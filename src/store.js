import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  strict:true,
  state: {
    qr_data: "",
    error_msg: "",
    fname: "",
    lname: "",
    loc: "",
    res: "",
    agent: "",
    split_data: [],
  },
  mutations: {
    set_qrdata (state, d) {
      state.qr_data = d
      state.split_data = String(state.qr_data).split(',')
      state.fname = state.split_data[1]
      state.lname = state.split_data[3]
    },
    reset_qrdata(state){
      state.qr_data = ''
    },
    set_error (state, e) {
      state.error_msg = e
    },
    set_answers (state, a){
      state.answers = a
    },

  },
  actions: {

  }
})
