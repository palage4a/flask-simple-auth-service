<template>
  <div>
    <alert v-if="showMessage" :message="message"></alert>
    <b-form @submit="onSubmitLogin" @reset="onReset" class="w-100">
      <b-form-group id="form-name-group" label="Login in service:" label-for="form-name-input">
        <b-form-input
          id="form-name-input"
          type="text"
          v-model="loginForm.token"
          required
          placeholder="Enter your token"
        ></b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
  </div>
</template>

<script>
import axios from "axios";
import Alert from "./Alert";
export default {
  data() {
    return {
      loginForm: {
        token: ""
      },
      message: "",
      showMessage: false
    };
  },
  components: {
    alert: Alert
  },
  methods: {
    initForms() {
      this.loginForm.token = "";
    },
    //LOGIN
    login(payload) {
      const path = "http://localhost:5000/auth";
      axios
        .post(path, payload)
        .then(res => {
          if (res.data.access == "true") {
            this.message = ` User ${res.data.name} logged-in! Congrats! `;
          } else {
            this.message = `Your token is invalid!`;
          }
          this.showMessage = true;
        })
        .catch(error => {
          console.error(error);
          this.initForms();
        });
    },
    onSubmitLogin(evt) {
      evt.preventDefault();
      const payload = {
        token: this.loginForm.token
      };
      this.login(payload);
      this.initForms();
    },
    onReset(evt) {
      evt.preventDefault();
      this.initForms();
    }
  },
  created() {
    this.initForms();
  }
};
</script>