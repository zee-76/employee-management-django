document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            let isValid = true;
            const requiredFields = form.querySelectorAll('[required]');
            requiredFields.forEach(field => {
                if (field.value.trim() === '') {
                    alert(`Please fill in the ${field.name} field.`);
                    isValid = false;
                    event.preventDefault();
                }
            });
            if (!isValid) return; // Stop if basic validation fails

            const imageInputs = form.querySelectorAll('input[type="file"][name="image"]'); // Target by name
            imageInputs.forEach(input => {
                input.addEventListener('change', function(event) {
                    const previewId = "id_image-preview";
                    let preview = document.getElementById(previewId);
                    if (!preview) {
                        preview = document.createElement('img');
                        preview.id = previewId;
                        preview.style.maxWidth = '200px';
                        preview.style.maxHeight = '200px';
                        input.parentNode.insertBefore(preview, input.nextSibling);
                    }
                    const file = this.files[0];

                    if (file) {
                        const allowedTypes = ['image/png', 'image/jpeg', 'image/jpg'];
                        const maxSize = 2 * 1024 * 1024; // 2MB
                        if (!allowedTypes.includes(file.type)) {
                            alert("Only .png and .jpg images are allowed.");
                            this.value = '';
                            preview.src = '';
                            event.preventDefault();
                            return;
                        }
                        if (file.size > maxSize) {
                            alert("Image file size should not exceed 2MB.");
                            this.value = '';
                            preview.src = '';
                            event.preventDefault();
                            return;
                        }
                        const reader = new FileReader();
                        reader.onload = function(e) {
                            preview.src = e.target.result;
                        }
                        reader.readAsDataURL(file);
                    } else {
                        preview.src = ''; // Clear preview if no file selected
                    }
                });
            });
        });
    });
