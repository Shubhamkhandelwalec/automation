<template>
  <div>
    <logo_section message="fa fa-facebook-f" url="#" style="display:inline-block;margin:15px"/>
    <logo_section message="fa fa-twitter" url="#" style="display:inline-block;margin:15px"/>
    <logo_section message="fa fa-google-plus" url="#" style="display:inline-block;margin:15px"/>
    <logo_section message="fa fa-rss" url="#" style="display:inline-block;margin:15px"/>
  </div>
</template>

<script>
import axios from 'axios';
// @ is an alias to /src
import logo_section from "@/components/Logo_Section.vue";

export default {
  name: "view_logo_section",
  components: {
    logo_section
  },
  mounted() {
    axios.get("http://127.0.0.1:8000/cmspages/viewuser")
    .then(response => console.log(response))
  }
};
</script>


