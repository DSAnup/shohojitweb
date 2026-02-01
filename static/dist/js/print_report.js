function printReport() {
    var tableContent = document.getElementById("table-default").innerHTML;
    var printWindow = window.open("", "", "height=600,width=800");
    printWindow.document.write("<html><head><title>Report</title>");
    printWindow.document.write("<style>body{font-family: Arial, sans-serif;} table {width: 100%; border-collapse: collapse;} th, td {padding: 8px; text-align: left; border: 1px solid #ddd;} th {background-color: #f2f2f2;} </style>");
    printWindow.document.write("</head><body >");
    printWindow.document.write(tableContent);
    printWindow.document.write("</body></html>");
    printWindow.document.close();
    printWindow.print();
}