function initTomSelect(container = document) {

    container.querySelectorAll('select.form-control').forEach(el => {

        // Prevent double initialization
        if (el.tomselect) {
            return;
        }

        new TomSelect(el, {
            copyClassesToDropdown: false,
            dropdownParent: 'body',
            controlInput: '<input>',
            render: {
                item: function (data, escape) {
                    if (data.customProperties) {
                        return `
                            <div>
                                <span class="dropdown-item-indicator">
                                    ${escape(data.customProperties)}
                                </span>
                                ${escape(data.text)}
                            </div>
                        `;
                    }
                    return `<div>${escape(data.text)}</div>`;
                },
                option: function (data, escape) {
                    if (data.customProperties) {
                        return `
                            <div>
                                <span class="dropdown-item-indicator">
                                    ${escape(data.customProperties)}
                                </span>
                                ${escape(data.text)}
                            </div>
                        `;
                    }
                    return `<div>${escape(data.text)}</div>`;
                }
            }
        });
    });
}

/* Init on page load */
document.addEventListener("DOMContentLoaded", function () {
    initTomSelect();
});
