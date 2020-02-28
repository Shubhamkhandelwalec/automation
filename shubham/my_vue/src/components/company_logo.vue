<template>
    <div>
        <img v-bind:src="require('../assets/static/img/'+message)"/>
    </div>
</template>

<script>

export default {
  name: "dots_logo",
  props: {
    message: String,
    
  }
};
</script>