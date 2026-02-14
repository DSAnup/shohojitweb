function setupDropdowns() {
    const dropdownIcons = document.querySelectorAll('.dropdown-icon');
    const navItems = document.querySelectorAll('.nav-item');
    
    // Handle dropdown icon clicks
    dropdownIcons.forEach(icon => {
        icon.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            
            const navItem = icon.closest('.nav-item');
            const dropdown = navItem.querySelector('.dropdown');
            const isActive = dropdown.classList.contains('active');
            
            // Close all other dropdowns on mobile
            if (window.innerWidth < 992) {
                document.querySelectorAll('.dropdown').forEach(d => {
                    if (d !== dropdown) {
                        d.classList.remove('active');
                        d.closest('.nav-item').querySelector('.dropdown-icon')?.classList.remove('rotated');
                    }
                });
            }
            
            // Toggle current dropdown
            dropdown.classList.toggle('active');
            icon.classList.toggle('rotated', !isActive);
        });
    });
    
    // Desktop hover functionality
    navItems.forEach(item => {
        const dropdown = item.querySelector('.dropdown');
        const icon = item.querySelector('.dropdown-icon');
        
        if (dropdown && icon) {
            // Desktop hover
            item.addEventListener('mouseenter', () => {
                if (window.innerWidth >= 992) {
                    dropdown.classList.add('active');
                    icon.classList.add('rotated');
                }
            });
            
            item.addEventListener('mouseleave', () => {
                if (window.innerWidth >= 992) {
                    dropdown.classList.remove('active');
                    icon.classList.remove('rotated');
                }
            });
            
            // Mobile: Close dropdown when clicking dropdown item
            dropdown.querySelectorAll('.dropdown-item').forEach(dropdownItem => {
                dropdownItem.addEventListener('click', () => {
                    if (window.innerWidth < 992) {
                        dropdown.classList.remove('active');
                        icon.classList.remove('rotated');
                        
                        // Close mobile menu
                        const navMenu = document.querySelector('.nav-menu');
                        const mobileToggle = document.querySelector('.mobile-toggle');
                        if (navMenu?.classList.contains('active')) {
                            navMenu.classList.remove('active');
                            mobileToggle?.classList.remove('active');
                            if (mobileToggle) {
                                mobileToggle.innerHTML = '<i class="fas fa-bars"></i>';
                            }
                            document.body.style.overflow = '';
                        }
                    }
                });
            });
        }
    });
    
    // Close dropdowns when clicking outside (mobile only)
    document.addEventListener('click', (e) => {
        if (window.innerWidth < 992) {
            if (!e.target.closest('.nav-item')) {
                document.querySelectorAll('.dropdown').forEach(dropdown => {
                    dropdown.classList.remove('active');
                });
                document.querySelectorAll('.dropdown-icon').forEach(icon => {
                    icon.classList.remove('rotated');
                });
            }
        }
    });
}