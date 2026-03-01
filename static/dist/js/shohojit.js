
const courses = [
    {
        title: "Web Development",
        description: "Learn HTML, CSS, JavaScript, React, Node.js and become a full-stack developer.",
        icon: "fas fa-code",
        duration: "6 Months",
        projects: "15 Projects",
        image: "images/web development course.png"
    },
    {
        title: "Graphic Design",
        description: "Master Adobe Photoshop, Illustrator, InDesign for professional graphic design.",
        icon: "fas fa-paint-brush",
        duration: "4 Months",
        projects: "12 Projects",
        image: "images/graphic design course.avif"
    },
    {
        title: "Digital Marketing",
        description: "Learn SEO, Social Media Marketing, Google Ads, and content marketing strategies.",
        icon: "fas fa-chart-line",
        duration: "3 Months",
        projects: "10 Projects",
        image: "images/digital marketing course.avif"
    },
    {
        title: "Python Programming",
        description: "Start with Python basics, then move to data analysis, automation, and web development.",
        icon: "fab fa-python",
        duration: "5 Months",
        projects: "20 Projects",
        image: "images/Python Programming course.png"
    },
    {
        title: "UI/UX Design",
        description: "Learn user interface and experience design with Figma, Adobe XD, and prototyping.",
        icon: "fas fa-object-group",
        duration: "4 Months",
        projects: "12 Projects",
        image: "images/UI-UX Design course.webp"
    },
    {
        title: "Freelancing",
        description: "Learn how to start and grow your freelancing career from scratch.",
        icon: "fas fa-laptop-house",
        duration: "2 Months",
        projects: "8 Projects",
        image: "images/Freelancing course.png"
    }
];

const services = [
    {
        title: "IT Training Institute",
        description: "Professional training in web development, graphic design, programming, and freelancing.",
        icon: "fas fa-graduation-cap"
    },
    {
        title: "IT Solutions Agency",
        description: "Custom software development, website creation, and IT consultancy services.",
        icon: "fas fa-briefcase"
    },
    {
        title: "Corporate Training",
        description: "Tailored IT training programs for corporate teams to enhance digital skills.",
        icon: "fas fa-users"
    },
    {
        title: "Web Development Service",
        description: "Custom website and web application development for businesses.",
        icon: "fas fa-laptop-code"
    },
    {
        title: "Digital Marketing Service",
        description: "Complete digital marketing solutions including SEO and social media marketing.",
        icon: "fas fa-bullhorn"
    },
    {
        title: "Career Counseling",
        description: "Professional guidance for career development in the IT industry.",
        icon: "fas fa-user-tie"
    }
];

const galleryImages = [
    { url: "images/classes.webp" },
    { url: "images/students.jpg" },
    { url: "images/events.webp" },
    { url: "images/certificates.png" },
    { url: "images/classes.webp" },
    { url: "images/events.webp" }
];

// === INITIALIZATION ===
document.addEventListener('DOMContentLoaded', function() {
    // generateCourses();
    // generateServices();
    // generateGallery();
    // initSlider();
    initScrollAnimations();
    setupEventListeners();
    setupForm();
    setupLightbox();
    initCounters();
    setupDropdowns();
});

// === GENERATE COURSES ===
function generateCourses() {
    const container = document.querySelector('.courses-container');
    if (!container) return;

    container.innerHTML = '';
    
    courses.forEach((course, index) => {
        const card = document.createElement('div');
        card.className = 'course-card';
        card.style.transitionDelay = `${index * 0.1}s`;
        
        // Create image with error handling
        const imgSrc = course.image || 'images/placeholder-course.jpg';
        
        card.innerHTML = `
            <div class="course-image">
                <img src="${imgSrc}" alt="${course.title}" loading="lazy">
                <div class="course-overlay">
                    <div class="course-icon">
                        <i class="${course.icon}"></i>
                    </div>
                </div>
            </div>
            <div class="course-content">
                <h3>${course.title}</h3>
                <p>${course.description}</p>
                <div class="course-meta">
                    <span><i class="far fa-clock"></i> ${course.duration}</span>
                    <span><i class="fas fa-project-diagram"></i> ${course.projects}</span>
                </div>
                <a href="#contact" class="btn btn-outline" style="margin-top: auto;">View Details</a>
            </div>
        `;
        
        // Add error handling for image
        const img = card.querySelector('img');
        img.onerror = function() {
            this.src = 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="400" height="250" viewBox="0 0 400 250"><rect width="400" height="250" fill="%23f3f4f6"/><text x="200" y="125" text-anchor="middle" fill="%239ca3af" font-family="Arial" font-size="16">${course.title}</text></svg>';
        };
        
        container.appendChild(card);
    });
}

// === GENERATE SERVICES ===
function generateServices() {
    const container = document.querySelector('.services-container');
    if (!container) return;

    container.innerHTML = '';
    
    services.forEach((service, index) => {
        const card = document.createElement('div');
        card.className = 'service-card';
        card.style.transitionDelay = `${index * 0.1}s`;
        
        card.innerHTML = `
            <div class="service-icon">
                <i class="${service.icon}"></i>
            </div>
            <h3>${service.title}</h3>
            <p>${service.description}</p>
            <a href="#contact" class="btn btn-outline">Learn More</a>
        `;
        
        container.appendChild(card);
    });
}

// === GENERATE GALLERY ===
function generateGallery() {
    const container = document.querySelector('.gallery-container');
    if (!container) return;

    container.innerHTML = '';
    
    galleryImages.forEach((image, index) => {
        const item = document.createElement('div');
        item.className = 'gallery-item';
        item.style.transitionDelay = `${index * 0.1}s`;
        
        item.innerHTML = `
            <img src="${image.url}" alt="Gallery Image ${index + 1}" loading="lazy">
            <div class="gallery-overlay">
                <i class="fas fa-search-plus"></i>
            </div>
        `;
        
        // Add error handling
        const img = item.querySelector('img');
        img.onerror = function() {
            this.src = 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="400" height="300" viewBox="0 0 400 300"><rect width="400" height="300" fill="%23f3f4f6"/><text x="200" y="150" text-anchor="middle" fill="%239ca3af" font-family="Arial" font-size="16">Gallery Image</text></svg>';
        };
        
        container.appendChild(item);
    });
}

// === DROPDOWN FUNCTIONALITY ===
// function setupDropdowns() {
//     const dropdownTriggers = document.querySelectorAll('.nav-link');
    
//     dropdownTriggers.forEach(trigger => {
//         if (trigger.querySelector('.dropdown-icon')) {
//             const dropdown = trigger.parentElement.querySelector('.dropdown');
            
//             // Mobile click handler - toggle dropdown when clicking the link
//             trigger.addEventListener('click', (e) => {
//                 // Only handle dropdown toggle on mobile
//                 if (window.innerWidth < 992) {
//                     // Check if click was on the text or the icon
//                     const clickedIcon = e.target.closest('.dropdown-icon');
//                     const clickedText = e.target.closest('span');
                    
//                     // If clicking on the text (not icon), allow normal navigation
//                     if (clickedText && !clickedIcon) {
//                         return; // Allow default behavior
//                     }
                    
//                     // If clicking on icon or empty space in the link, toggle dropdown
//                     e.preventDefault();
//                     e.stopPropagation();
                    
//                     const isActive = dropdown.classList.contains('active');
                    
//                     // Close all other dropdowns
//                     document.querySelectorAll('.dropdown').forEach(d => {
//                         if (d !== dropdown) {
//                             d.classList.remove('active');
//                             d.previousElementSibling?.querySelector('.dropdown-icon')?.classList.remove('rotated');
//                         }
//                     });
                    
//                     // Toggle current dropdown
//                     dropdown.classList.toggle('active');
                    
//                     // Rotate icon
//                     const icon = trigger.querySelector('.dropdown-icon');
//                     if (isActive) {
//                         icon.classList.remove('rotated');
//                     } else {
//                         icon.classList.add('rotated');
//                     }
//                 }
//             });
            
//             // Desktop hover handler
//             trigger.parentElement.addEventListener('mouseenter', () => {
//                 if (window.innerWidth >= 992) {
//                     dropdown.classList.add('active');
//                     trigger.querySelector('.dropdown-icon')?.classList.add('rotated');
//                 }
//             });
            
//             trigger.parentElement.addEventListener('mouseleave', () => {
//                 if (window.innerWidth >= 992) {
//                     dropdown.classList.remove('active');
//                     trigger.querySelector('.dropdown-icon')?.classList.remove('rotated');
//                 }
//             });
//         }
//     });
    
//     // Close dropdowns when clicking outside (mobile only)
//     document.addEventListener('click', (e) => {
//         if (window.innerWidth < 992) {
//             if (!e.target.closest('.nav-item')) {
//                 document.querySelectorAll('.dropdown').forEach(dropdown => {
//                     dropdown.classList.remove('active');
//                 });
//                 document.querySelectorAll('.dropdown-icon').forEach(icon => {
//                     icon.classList.remove('rotated');
//                 });
//             }
//         }
//     });
// }

// === SCROLL ANIMATIONS ===
function initScrollAnimations() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animated');
                
                // Animate child elements with delays
                if (entry.target.classList.contains('service-card')) {
                    const h3 = entry.target.querySelector('h3');
                    const p = entry.target.querySelector('p');
                    if (h3) h3.classList.add('animated');
                    if (p) p.classList.add('animated');
                }
                
                if (entry.target.classList.contains('course-card')) {
                    const content = entry.target.querySelector('.course-content');
                    const meta = entry.target.querySelector('.course-meta');
                    if (content) content.classList.add('animated');
                    if (meta) meta.classList.add('animated');
                }
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });

    // Observe all animatable elements
    document.querySelectorAll('.section-title, .course-card, .service-card, .gallery-item, .testimonial, .client-logo, .about-image, .about-content, .feature-item, .contact-item, .contact-form, .form-group, .footer-column, .stat-item').forEach(el => {
        observer.observe(el);
    });
}

// === COUNTER ANIMATION ===
function initCounters() {
    const counters = document.querySelectorAll('.stat-number');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                counters.forEach(counter => {
                    const target = +counter.getAttribute('data-count');
                    let count = 0;
                    const increment = target / 100;
                    
                    const update = () => {
                        if (count < target) {
                            count += increment;
                            counter.innerText = Math.ceil(count);
                            setTimeout(update, 20);
                        } else {
                            counter.innerText = target;
                        }
                    };
                    update();
                });
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(c => observer.observe(c));
}

// === EVENT LISTENERS ===
function setupEventListeners() {
    // Navbar scroll effect - transparent in hero section
    window.addEventListener('scroll', () => {
        const navbar = document.querySelector('.navbar');
        const logo = document.querySelector('.logo');
        const mobileToggle = document.querySelector('.mobile-toggle');
        const heroSection = document.querySelector('.hero-section');
        
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
        
        // Update active nav link
        updateActiveNavLink();
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
    
    // Update active nav link on scroll
    function updateActiveNavLink() {
        const sections = document.querySelectorAll('section[id]');
        const navLinks = document.querySelectorAll('.nav-link');
        
        let current = '';
        const scrollPosition = window.scrollY + 100;
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            const sectionId = section.getAttribute('id');
            
            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                current = sectionId;
            }
        });
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    }
}

// === FORM HANDLING ===
function setupForm() {
    const contactForm = document.getElementById('contactForm');
    if (!contactForm) return;
    
    contactForm.addEventListener('submit', e => {
        e.preventDefault();
        
        const submitBtn = contactForm.querySelector('button[type="submit"]');
        const originalText = submitBtn.innerHTML;
        
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
        submitBtn.disabled = true;
        
        // Simulate form submission
        setTimeout(() => {
            submitBtn.innerHTML = '<i class="fas fa-check"></i> Sent Successfully!';
            submitBtn.style.background = 'linear-gradient(135deg, #00b300, #008000)';
            
            contactForm.reset();
            
            setTimeout(() => {
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
                submitBtn.style.background = '';
            }, 3000);
        }, 1500);
    });
}

// === LIGHTBOX SETUP ===
function setupLightbox() {
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const closeBtn = document.querySelector('.close');
    
    if (!lightbox || !lightboxImg || !closeBtn) return;
    
    document.querySelectorAll('.gallery-item').forEach(item => {
        item.addEventListener('click', () => {
            const img = item.querySelector('img');
            if (img) {
                lightboxImg.src = img.src;
                lightboxImg.alt = img.alt;
                lightbox.style.display = 'flex';
                document.body.style.overflow = 'hidden';
            }
        });
    });
    
    closeBtn.addEventListener('click', () => {
        lightbox.style.display = 'none';
        document.body.style.overflow = '';
    });
    
    lightbox.addEventListener('click', (e) => {
        if (e.target === lightbox) {
            lightbox.style.display = 'none';
            document.body.style.overflow = '';
        }
    });
    
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && lightbox.style.display === 'flex') {
            lightbox.style.display = 'none';
            document.body.style.overflow = '';
        }
    });
}

// === LOADING SCREEN ===
window.addEventListener('load', () => {
    setTimeout(() => {
        document.querySelector('.loading')?.classList.add('hidden');
    }, 500);
});