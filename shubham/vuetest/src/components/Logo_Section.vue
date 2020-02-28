<template>
  <div class="header">
    <div class="t_header">
          <ul class="header-social-icon">
            <li>
              <a v-bind:href="url"><i v-bind:class="message" aria-hidden="true"></i></a>
            </li>
          </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "logo_section",
 props: {
    message: String,
    url: String
  }
    
};
</script>

