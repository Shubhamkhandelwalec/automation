<template>
    <div>
         <dots_logo message="logo.png"/>
    </div>
</template>

<script>
// @ is an alias to /src
import dots_logo from "@/components/company_logo.vue";

export default {
  name: "view_company_logo",
  components: {
    dots_logo
  }
};
</script>
