document.getElementById('deleteMulti').addEventListener('click', function(e) {
    e.preventDefault();
    var selectedRows = document.querySelectorAll('input[name="selected_rows"]:checked');
    var model_name = document.getElementById('model_name').value;
    var app_name = document.getElementById('app_name').value;
    var selectedIds = Array.from(selectedRows).map(function(checkbox) {
        return checkbox.value;
    });

    if (selectedIds.length > 0){
        fetch('/delete/multiple/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                // 'X-CSRFToken': getCookie('csrftoken')  // Uncomment if CSRF protection is enabled
            },
            body: JSON.stringify({ selected_ids: selectedIds, model_name: model_name, app_name: app_name })
        })
        .then(response => response.json())
        .then(data => {
            // console.log(data)
            window.location.reload()
        })
        .catch(error => console.log('Error:', error));
    } else {
        alert('Please select at least one record!')
    }
});
