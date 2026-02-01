document.addEventListener("DOMContentLoaded", function() {
    const checkAllCheckbox = document.getElementById("check-all");
    const checkboxes = document.querySelectorAll("input[type='checkbox']:not(#check-all)");

    // Add event listener to check all checkbox
    checkAllCheckbox.addEventListener("change", function() {
        checkboxes.forEach(checkbox => {
            checkbox.checked = checkAllCheckbox.checked;
        });
    });

    // Add event listener to individual checkboxes to uncheck "check all" checkbox if any checkbox is unchecked
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener("change", function() {
            if (!this.checked) {
                checkAllCheckbox.checked = false;
            }
        });
    });
});
