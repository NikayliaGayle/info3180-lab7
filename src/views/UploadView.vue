
<template>
    <div class="container">
      <div class="text-left">
        <h1>{{ message }}</h1>
        <UploadForm />
      </div>
    </div>
</template>

<script>
import UploadForm from '@/components/UploadForm.vue'
export default {
  
    data() {
        return {
            description: "description",
            photo: undefined,
            message: "Upload an Image"
        };
    },
    components: { UploadForm }
}
</script>

<style>
    .container{
        width:50%;
        
    
    }

</style>