<template>
    <form @submit.prevent="uploadPhoto" id="uploadForm">
        <div class="uploads">
            <label>Description</label>
            <textarea name="description" v-model="description" id="description" placeholder="describe the image"></textarea>
            <br>
            <input type="file" id="photo" name="photo" @change="selectImage">
            <br>
            <button>Upload</button>
        </div>
    
    </form>
</template>

<script>
export default {

    data() {
        return {
        csrf_token: '',
        }
    },
    created() {
        this.getCsrfToken();
    },
    
    methods: {
        uploadPhoto(){
            let uploadForm = document.getElementById('uploadForm');
            let form_data = new FormData(uploadForm);
            fetch("/api/upload", {
                method: 'POST',
                body: form_data,
                headers: {'X-CSRFToken': this.csrf_token}
            })
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                // display a success message
                console.log(data);
            })
            .catch(function (error) {
                console.log(error);
            });
        },
        getCsrfToken() {
            let self = this;
            fetch('/api/csrf-token')
            .then((response) => response.json())
            .then((data) => {
            console.log(data);
            self.csrf_token = data.csrf_token;
            })
        }
    }
}
</script>

<style>
.uploads{
    display:flex;
    flex-direction:column;
}

#description{

}
</style>