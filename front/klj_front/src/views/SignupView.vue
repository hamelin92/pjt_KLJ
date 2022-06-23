<template>
  <div class="signup-wrap">
    <div div class="signup-components">
      <h3>회원가입</h3>
  
      <!-- <account-error-list v-if="authError"></account-error-list> -->
  
      <form class="signup-form" @submit.prevent="signup(credentials)">
      <div class="signupform-wrap">
        <div class="signup-name">
          <label for="username">사용자 이름: </label>
          <input v-model="credentials.username" type="text" id="username" required />
        </div>
  
        <div class="signup-email">
          <label for="email">email: </label>
          <input v-model="credentials.email" type="email" id="email" required />
        </div>
      
        <div class="signup-password1">
          <label for="password1">비밀번호: </label>
          <input v-model="credentials.password1" type="password" id="password1" required />
        </div>

        <div class="signup-password2">
          <label for="password2">비밀번호 재입력:</label>
          <input v-model="credentials.password2" type="password" id="password2" required />
        </div>
      </div>
        <button class="signup-button">Signup</button>
      </form>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'SignupView',
  data(){
    return{
      credentials: {
        username: '',
        password1: '',
        password2: '',
        email: '',
      }
    }
  },
  // computed: {
  //   ...mapGetters(['authError'])
  // },
  methods: {
    ...mapActions(['signup'])
  },
}
</script>

<style>

</style>