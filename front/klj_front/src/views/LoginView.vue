<template>
  <div>
    <div class="login-components">
      <h3>로그인 하세요</h3>
  
      <!-- <account-error-list v-if="authError"></account-error-list> -->

      <form class="login-form" @submit.prevent="login(credentials)">
        <div class="form-wrap">
          <div class="login-name">
            <label for="username">사용자 이름: </label>
            <input v-model="credentials.username" type="text" id="username" required />
          </div>
    
          <div class="login-password">
            <label for="password">비밀번호: </label>
            <input v-model="credentials.password" type="password" id="password" required />
          </div>
        </div>
        <button class="login-button">Login</button>  
      </form>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'LoginView',
  data() {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  // computed: {
  //   ...mapGetters(['authError'])
  // },
  methods: {
    ...mapActions(['login']),
  }
}
</script>

<style>

</style>