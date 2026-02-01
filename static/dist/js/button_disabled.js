const fileInput = document.getElementById('id_profile_picture');
const profile_picture_update = document.getElementById('profile_picture_update');

// Add event listener to file input
fileInput.addEventListener('change', function() {
    if (fileInput.files.length > 0) {
        profile_picture_update.removeAttribute('disabled');
    } else {
        profile_picture_update.setAttribute('disabled', 'disabled');
    }
});

const profile_picture_clear = document.getElementById('profile_picture-clear_id');
const profile_picture_delete_submit = document.getElementById('profile_picture_delete_submit');

profile_picture_clear.addEventListener('change', function() {
    // If checkbox is checked, enable the button; otherwise, disable it
    profile_picture_delete_submit.disabled = !this.checked;
});

// Initially disable the button if checkbox is not checked
profile_picture_delete_submit.disabled = !profile_picture_clear.checked;