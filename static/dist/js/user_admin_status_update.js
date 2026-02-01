
function toggleUserAdminStatus(userId) {
    const toggleUrl = document.getElementById("user_admin_status").dataset.toggleUrl;
    $.ajax({
        url: toggleUrl,
        type: "POST",
        data: {
            "user_id": userId,
            "csrfmiddlewaretoken": document.querySelector('[name=csrfmiddlewaretoken]').value,
        },
        success: function (response) {
          let message = response.is_staff 
              ? "User activated successfully." 
              : "User deactivated successfully.";

          // Append a Bootstrap alert message
          $("#alert-container").html(`
              <div class="alert alert-success alert-dismissible fade show" role="alert">
                  ${message}
                  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
              </div>
          `);
        },
        error: function () {
          $("#alert-container").html(`
              <div class="alert alert-danger alert-dismissible fade show" role="alert">
                  An error occurred. Please try again.
                  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
              </div>
          `);
        }
    });
  }