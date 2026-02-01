
function clearSearch() {
    const form = document.getElementById('searchForm');
    
    form.querySelectorAll('input').forEach(input => input.value = '');
    form.querySelectorAll('select').forEach(select => select.selectedIndex = 0);
    form.submit();
  }
