var colvis = $('#colvis').val();
var csv = $('#csv').val();
var copy = $('#copy').val();
var excel = $('#excel').val();
var pdf = $('#pdf').val();
var printall = $('#printall').val();
var printselected = $('#printselected').val();

for(let i = 1; i <= 10; i++){
    new DataTable('#dataTable'+i, {
        columnDefs: [
            {
                visible: false
            }
        ],
        layout: {
            topStart: {
                buttons: [
                'pageLength',
                ...(parseInt(colvis) === 1 ? [{
                    extend: 'colvis',
                    postfixButtons: ['colvisRestore']
                }] : []),
                ...(parseInt(csv) === 1 ? [{
                    extend: 'csvHtml5',
                    exportOptions: {
                        columns: ':visible'
                    }
                }] : []),
                ...(parseInt(copy) === 1 ? [{
                    extend: 'copyHtml5',
                    exportOptions: {
                        columns: ':visible'
                    }
                }] : []),
                ...(parseInt(excel) === 1 ? [{
                    extend: 'excelHtml5',
                    exportOptions: {
                        columns: ':visible'
                    }
                }] : []),
                ...(parseInt(pdf) === 1 ? [{
                    extend: 'pdfHtml5',
                    exportOptions: {
                        columns: ':visible'
                    },
                    footer: false,
                    download: 'open'
                }] : []),
                ...(parseInt(printall) === 1 ? [{
                    extend: 'print',
                    text: 'Print',
                    exportOptions: {
                        columns: ':visible',
                    
                    },
                    footer: false
                }] : []),
                ...(parseInt(printselected) === 1 ? [{
                    extend: 'print',
                    text: 'Print selected',
                    exportOptions: {
                        columns: ':visible',
                    
                    },
                    footer: false,
                }] : []),
                
                ]
            }
        },
        ...(parseInt(printselected) === 1 ? {select: true} : {select: false}),
        lengthMenu: [10, 25, 50, 100], // Select per page options
        pageLength: 10 // Default select per page option
    })
};