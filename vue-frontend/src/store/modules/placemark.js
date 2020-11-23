export default{
  actions: {
    catchMessages (context) {
      context.commit('updateMessages')
  }
  },



  mutations: {
    updateMessages(state, messages){
      state.messages = messages
    }
  },


  state: {
      messages: [], 
      filter: {
        "danger": {
          "1": true,
          "2": true,
          "3": true,
        },
        "event": {
          "fire": true,
          "dtp": true,
          "warmwater": true,
        }
      }
  },


  getters: {
      getAllMessages(state){
        return state.messages;
    },
      getAllMessagesCount(state){
        return state.messages.length;
    }
  }
}
