
// === GOOGLE MAPS INITIALIZATION ===
let map;
let mapInitialized = false;

function initMap() {
    try {
        // Dhaka, Bangladesh coordinates
        const dhakaLocation = { lat: 23.8103, lng: 90.4125 };
        
        // Create map
        map = new google.maps.Map(document.getElementById('google-map'), {
            zoom: 15,
            center: dhakaLocation,
            styles: [
                {
                    "featureType": "all",
                    "elementType": "geometry",
                    "stylers": [{"color": "#f5f5f5"}]
                },
                {
                    "featureType": "all",
                    "elementType": "labels.text.fill",
                    "stylers": [{"gamma": 0.01}, {"lightness": 20}, {"weight": "1.39"}, {"color": "#000000"}]
                },
                {
                    "featureType": "all",
                    "elementType": "labels.text.stroke",
                    "stylers": [{"weight": "0.96"}, {"saturation": "9"}, {"visibility": "on"}, {"color": "#000000"}]
                },
                {
                    "featureType": "all",
                    "elementType": "labels.icon",
                    "stylers": [{"visibility": "off"}]
                },
                {
                    "featureType": "landscape",
                    "elementType": "geometry",
                    "stylers": [{"lightness": 30}, {"saturation": "9"}, {"color": "#f8f8f8"}]
                },
                {
                    "featureType": "poi",
                    "elementType": "geometry",
                    "stylers": [{"saturation": 20}]
                },
                {
                    "featureType": "poi.park",
                    "elementType": "geometry",
                    "stylers": [{"lightness": 20}, {"saturation": -20}]
                },
                {
                    "featureType": "road",
                    "elementType": "geometry",
                    "stylers": [{"lightness": 10}, {"saturation": -30}]
                },
                {
                    "featureType": "road",
                    "elementType": "geometry.stroke",
                    "stylers": [{"saturation": 25}, {"lightness": 25}]
                },
                {
                    "featureType": "water",
                    "elementType": "all",
                    "stylers": [{"lightness": -20}]
                }
            ]
        });

        // Custom marker icon (using emoji as fallback)
        const markerIcon = {
            url: "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='40' height='40' viewBox='0 0 40 40'%3E%3Ccircle cx='20' cy='20' r='18' fill='%23bb0000' stroke='%23ffffff' stroke-width='3'/%3E%3Ctext x='20' y='26' text-anchor='middle' fill='%23ffffff' font-family='Arial, sans-serif' font-size='14' font-weight='bold'%3EI%3C/text%3E%3C/svg%3E",
            scaledSize: new google.maps.Size(40, 40),
            origin: new google.maps.Point(0, 0),
            anchor: new google.maps.Point(20, 40)
        };

        // Add marker
        const marker = new google.maps.Marker({
            position: dhakaLocation,
            map: map,
            title: 'Sohoj IT Institute',
            icon: markerIcon,
            animation: google.maps.Animation.DROP
        });

        // Info window
        const infoWindow = new google.maps.InfoWindow({
            content: `
                <div style="padding: 15px; max-width: 250px;">
                    <h3 style="color: #bb0000; margin: 0 0 10px 0; font-size: 1.2rem;">
                        <i class="fas fa-laptop-code"></i> Sohoj IT Institute
                    </h3>
                    <p style="margin: 0 0 8px 0; color: #333;">
                        <i class="fas fa-map-marker-alt" style="color: #bb0000;"></i> 
                        123 IT Tower, Digital Street
                    </p>
                    <p style="margin: 0 0 8px 0; color: #333;">
                        <i class="fas fa-phone" style="color: #bb0000;"></i> 
                        +880 1234 567890
                    </p>
                    <p style="margin: 0 0 15px 0; color: #333;">
                        <i class="fas fa-clock" style="color: #bb0000;"></i> 
                        Sat-Thu: 9AM-8PM
                    </p>
                    <a href="https://www.google.com/maps/dir/?api=1&destination=23.8103,90.4125" 
                        target="_blank" 
                        style="display: inline-block; background: linear-gradient(135deg, #bb0000, #000000); color: white; padding: 8px 16px; text-decoration: none; border-radius: 5px; font-weight: bold; font-size: 0.9rem;">
                        <i class="fas fa-directions"></i> Get Directions
                    </a>
                </div>
            `
        });

        // Open info window on marker click
        marker.addListener('click', () => {
            infoWindow.open(map, marker);
        });

        // Open info window by default
        setTimeout(() => {
            infoWindow.open(map, marker);
        }, 1000);

        // Add click listener for map to close info window
        map.addListener('click', () => {
            infoWindow.close();
        });

        // Hide fallback if map loads successfully
        document.getElementById('map-fallback').style.display = 'none';
        mapInitialized = true;
        
    } catch (error) {
        console.error('Google Maps error:', error);
        showMapFallback();
    }
}

// Show fallback if Google Maps fails to load
function showMapFallback() {
    document.getElementById('google-map').style.display = 'none';
    document.getElementById('map-fallback').style.display = 'flex';
    document.querySelector('.map-overlay').style.display = 'none';
}

// Handle Google Maps API loading errors
window.gm_authFailure = function() {
    console.error('Google Maps authentication failed');
    showMapFallback();
};

// Check if Google Maps API loaded
window.addEventListener('load', function() {
    setTimeout(function() {
        if (!mapInitialized && typeof google === 'undefined') {
            console.error('Google Maps API failed to load');
            showMapFallback();
        }
    }, 3000);
});

// === INITIALIZATION ===
document.addEventListener('DOMContentLoaded', function() {
    // Initialize components
    setupEventListeners();
    setupFAQ();
    setupFormValidation();
    initScrollAnimations();
    
    // Hide loading screen
    setTimeout(() => {
        document.querySelector('.loading')?.classList.add('hidden');
    }, 500);
});

// === DROPDOWN FUNCTIONALITY ===


// === FAQ FUNCTIONALITY ===
function setupFAQ() {
    const faqItems = document.querySelectorAll('.faq-item');
    
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        
        question.addEventListener('click', () => {
            // Close all other FAQ items
            faqItems.forEach(otherItem => {
                if (otherItem !== item && otherItem.classList.contains('active')) {
                    otherItem.classList.remove('active');
                }
            });
            
            // Toggle current FAQ item
            item.classList.toggle('active');
        });
    });
}

// === FORM VALIDATION ===
function setupFormValidation() {
    const contactForm = document.getElementById('contactForm');
    if (!contactForm) return;
    
    const nameInput = document.getElementById('name');
    const emailInput = document.getElementById('email');
    const messageInput = document.getElementById('message');
    
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }
    
    function showError(input, errorId, message) {
        input.classList.add('error');
        document.getElementById(errorId).textContent = message;
        document.getElementById(errorId).style.display = 'block';
    }
    
    function hideError(input, errorId) {
        input.classList.remove('error');
        document.getElementById(errorId).style.display = 'none';
    }
    
    // Real-time validation
    nameInput.addEventListener('input', () => {
        if (nameInput.value.trim().length < 2) {
            showError(nameInput, 'name-error', 'Name must be at least 2 characters');
        } else {
            hideError(nameInput, 'name-error');
        }
    });
    
    emailInput.addEventListener('input', () => {
        if (!validateEmail(emailInput.value)) {
            showError(emailInput, 'email-error', 'Please enter a valid email address');
        } else {
            hideError(emailInput, 'email-error');
        }
    });
    
    messageInput.addEventListener('input', () => {
        if (messageInput.value.trim().length < 10) {
            showError(messageInput, 'message-error', 'Message must be at least 10 characters');
        } else {
            hideError(messageInput, 'message-error');
        }
    });
    
    // Form submission
    contactForm.addEventListener('submit', e => {
        e.preventDefault();
        
        let isValid = true;
        
        // Validate name
        if (nameInput.value.trim().length < 2) {
            showError(nameInput, 'name-error', 'Name must be at least 2 characters');
            isValid = false;
        }
        
        // Validate email
        if (!validateEmail(emailInput.value)) {
            showError(emailInput, 'email-error', 'Please enter a valid email address');
            isValid = false;
        }
        
        // Validate message
        if (messageInput.value.trim().length < 10) {
            showError(messageInput, 'message-error', 'Message must be at least 10 characters');
            isValid = false;
        }
        
        if (isValid) {
            const submitBtn = contactForm.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
            submitBtn.disabled = true;
            
            // Simulate form submission
            setTimeout(() => {
                submitBtn.innerHTML = '<i class="fas fa-check"></i> Message Sent!';
                submitBtn.style.background = 'linear-gradient(135deg, #00b300, #008000)';
                
                // Show success message
                const successMessage = document.createElement('div');
                successMessage.innerHTML = `
                    <div style="background: linear-gradient(135deg, #d4edda, #c3e6cb); color: #155724; padding: 15px; border-radius: 8px; margin-top: 20px; border-left: 4px solid #155724;">
                        <i class="fas fa-check-circle"></i> Thank you! Your message has been sent successfully. We'll contact you within 24 hours.
                    </div>
                `;
                contactForm.parentNode.insertBefore(successMessage, contactForm.nextSibling);
                
                contactForm.reset();
                
                setTimeout(() => {
                    submitBtn.innerHTML = originalText;
                    submitBtn.disabled = false;
                    submitBtn.style.background = '';
                    successMessage.remove();
                }, 5000);
            }, 2000);
        }
    });
}

// === SCROLL ANIMATIONS ===
function initScrollAnimations() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animated');
                
                // Animate child elements with delays
                if (entry.target.classList.contains('contact-card')) {
                    setTimeout(() => {
                        entry.target.querySelector('.contact-card-icon')?.classList.add('animated');
                    }, 300);
                }
                
                if (entry.target.classList.contains('form-group')) {
                    const delay = Array.from(entry.target.parentNode.children).indexOf(entry.target) * 100;
                    setTimeout(() => {
                        entry.target.classList.add('animated');
                    }, delay);
                }
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });

    // Observe all animatable elements
    document.querySelectorAll('.contact-card, .form-group, .faq-item, .footer-column').forEach(el => {
        observer.observe(el);
    });
}

// === EVENT LISTENERS ===
function setupEventListeners() {
    // Navbar scroll effect
    window.addEventListener('scroll', () => {
        const navbar = document.querySelector('.navbar');
        const logo = document.querySelector('.logo');
        const mobileToggle = document.querySelector('.mobile-toggle');
        const heroSection = document.querySelector('.contact-hero');
        
        if (!heroSection) return;
        
        const heroBottom = heroSection.offsetTop + heroSection.offsetHeight;
        
        if (window.scrollY > heroBottom - 80) {
            navbar?.classList.add('scrolled');
            logo?.classList.add('scrolled-logo');
            mobileToggle?.classList.add('scrolled-toggle');
        } else {
            navbar?.classList.remove('scrolled');
            logo?.classList.remove('scrolled-logo');
            mobileToggle?.classList.remove('scrolled-toggle');
        }
    });

    // Mobile menu toggle
    const mobileToggle = document.querySelector('.mobile-toggle');
    const navMenu = document.querySelector('.nav-menu');
    
    if (mobileToggle && navMenu) {
        mobileToggle.addEventListener('click', (e) => {
            e.stopPropagation();
            navMenu.classList.toggle('active');
            mobileToggle.classList.toggle('active');
            mobileToggle.innerHTML = navMenu.classList.contains('active') 
                ? '<i class="fas fa-times"></i>' 
                : '<i class="fas fa-bars"></i>';
            document.body.style.overflow = navMenu.classList.contains('active') ? 'hidden' : '';
            
            // Close all dropdowns when closing menu
            if (!navMenu.classList.contains('active')) {
                document.querySelectorAll('.dropdown').forEach(d => {
                    d.classList.remove('active');
                });
                document.querySelectorAll('.dropdown-icon').forEach(icon => {
                    icon.classList.remove('rotated');
                });
            }
        });
    }

    // Close mobile menu when clicking outside
    document.addEventListener('click', (e) => {
        if (window.innerWidth < 992) {
            const navMenu = document.querySelector('.nav-menu');
            const mobileToggle = document.querySelector('.mobile-toggle');
            
            if (navMenu?.classList.contains('active') && 
                !e.target.closest('.nav-menu') && 
                !e.target.closest('.mobile-toggle')) {
                navMenu.classList.remove('active');
                mobileToggle?.classList.remove('active');
                if (mobileToggle) {
                    mobileToggle.innerHTML = '<i class="fas fa-bars"></i>';
                }
                document.body.style.overflow = '';
                
                // Close all dropdowns
                document.querySelectorAll('.dropdown').forEach(d => {
                    d.classList.remove('active');
                });
                document.querySelectorAll('.dropdown-icon').forEach(icon => {
                    icon.classList.remove('rotated');
                });
            }
        }
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#' || targetId.startsWith('#!')) return;
            
            // Don't prevent default for dropdown items (they should navigate)
            if (this.classList.contains('dropdown-item')) {
                return;
            }
            
            e.preventDefault();
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80,
                    behavior: 'smooth'
                });
                
                // Close mobile menu after clicking a link
                if (window.innerWidth < 992) {
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
            }
        });
    });
}