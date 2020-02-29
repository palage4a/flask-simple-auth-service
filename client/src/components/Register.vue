<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Flask service</h1>
        <hr />
        <br />
        <alert v-if="showMessage" :message="message"></alert>
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
          <b-form-group
            id="form-name-group"
            label="If you dont have token, please register:"
            label-for="form-name-input"
          >
            <b-form-input
              id="form-name-input"
              type="text"
              v-model="registerForm.name"
              required
              placeholder="Enter name"
            ></b-form-input>
          </b-form-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-form>
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
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Alert from "./Alert";
export default {
  data() {
    return {
      registerForm: {
        name: ""
      },
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
      this.registerForm.name = "";
      this.loginForm.token = "";
    },
    // REGISTER
    register(payload) {
      const path = "http://localhost:5000/register";
      axios
        .post(path, payload)
        .then(res => {
          this.message = `User ${res.data.name} register!\nYour token is ${res.data.token}`;
          this.showMessage = true;
        })
        .catch(error => {
          console.error(error);
          this.initForms();
        });
    },
    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        name: this.registerForm.name
      };
      this.register(payload);
      this.initForms();
    },
    onReset(evt) {
      evt.preventDefault();
      this.initForms();
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
    }
  },
  created() {
    this.initForms();
  }
};
</script>