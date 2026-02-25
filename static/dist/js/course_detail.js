const courseModules = [
    {
        title: "Module 1: Web Fundamentals",
        icon: "fas fa-html5",
        duration: "4 Weeks",
        topics: [
            "HTML5 & Semantic HTML",
            "CSS3 & Modern Layouts",
            "Responsive Web Design",
            "CSS Flexbox & Grid",
            "CSS Animations & Transitions",
            "Version Control with Git & GitHub"
        ]
    },
    {
        title: "Module 2: JavaScript Mastery",
        icon: "fab fa-js",
        duration: "6 Weeks",
        topics: [
            "JavaScript Fundamentals",
            "ES6+ Modern JavaScript",
            "DOM Manipulation",
            "Async JavaScript & APIs",
            "Error Handling & Debugging",
            "JavaScript Best Practices"
        ]
    },
    {
        title: "Module 3: Frontend with React",
        icon: "fab fa-react",
        duration: "6 Weeks",
        topics: [
            "React Fundamentals",
            "Components & Props",
            "State & Lifecycle",
            "React Hooks",
            "React Router",
            "State Management with Redux",
            "Context API"
        ]
    },
    {
        title: "Module 4: Backend with Node.js",
        icon: "fab fa-node-js",
        duration: "5 Weeks",
        topics: [
            "Node.js Fundamentals",
            "Express.js Framework",
            "RESTful API Development",
            "Authentication & Authorization",
            "Middleware & Error Handling",
            "File Uploads & Processing"
        ]
    },
    {
        title: "Module 5: Database with MongoDB",
        icon: "fas fa-database",
        duration: "4 Weeks",
        topics: [
            "MongoDB Fundamentals",
            "Mongoose ODM",
            "Database Design",
            "CRUD Operations",
            "Aggregation Framework",
            "Database Optimization"
        ]
    },
    {
        title: "Module 6: Deployment & DevOps",
        icon: "fas fa-cloud-upload-alt",
        duration: "3 Weeks",
        topics: [
            "Cloud Deployment (AWS, Heroku)",
            "Docker Basics",
            "CI/CD Pipeline",
            "Performance Optimization",
            "Security Best Practices",
            "Monitoring & Debugging"
        ]
    },
    {
        title: "Module 7: Advanced Topics",
        icon: "fas fa-rocket",
        duration: "4 Weeks",
        topics: [
            "TypeScript Fundamentals",
            "Next.js Framework",
            "GraphQL API Development",
            "WebSockets & Real-time Apps",
            "Testing (Jest, React Testing Library)",
            "Progressive Web Apps"
        ]
    },
    {
        title: "Module 8: Career Development",
        icon: "fas fa-briefcase",
        duration: "2 Weeks",
        topics: [
            "Portfolio Development",
            "Resume & LinkedIn Optimization",
            "Technical Interview Preparation",
            "Freelancing & Job Search",
            "Salary Negotiation",
            "Career Roadmap Planning"
        ]
    }
];

// === INITIALIZATION ===
document.addEventListener('DOMContentLoaded', function() {
    generateCurriculum();
    initScrollAnimations();
    setupEventListeners();
    // setupDropdowns();
    setupModuleAccordions();
});

// === GENERATE CURRICULUM ===
function generateCurriculum() {
    const container = document.querySelector('.curriculum-container');
    if (!container) return;

    container.innerHTML = '';
    
    courseModules.forEach((module, index) => {
        const moduleElement = document.createElement('div');
        moduleElement.className = 'module';
        moduleElement.style.transitionDelay = `${index * 0.1}s`;
        
        moduleElement.innerHTML = `
            <div class="module-header">
                <h3>
                    <div class="module-icon">
                        <i class="${module.icon}"></i>
                    </div>
                    <span class="module-title-text">${module.title}</span>
                </h3>
                <div class="module-duration">${module.duration}</div>
            </div>
            <div class="module-content">
                <ul class="topics-list">
                    ${module.topics.map(topic => `<li><i class="fas fa-circle"></i> ${topic}</li>`).join('')}
                </ul>
            </div>
        `;
        
        container.appendChild(moduleElement);
    });
}

// === MODULE ACCORDIONS ===
function setupModuleAccordions() {
    const moduleHeaders = document.querySelectorAll('.module-header');
    
    moduleHeaders.forEach(header => {
        header.addEventListener('click', function() {
            const module = this.parentElement;
            const content = this.nextElementSibling;
            
            // Toggle active class
            module.classList.toggle('active');
            
            // Toggle content visibility
            if (content.classList.contains('active')) {
                content.classList.remove('active');
                content.style.maxHeight = null;
            } else {
                content.classList.add('active');
                content.style.maxHeight = content.scrollHeight + "px";
            }
        });
    });
}

// === DROPDOWN FUNCTIONALITY ===
function setupDropdowns() {
    const dropdownTriggers = document.querySelectorAll('.nav-link');
    
    dropdownTriggers.forEach(trigger => {
        if (trigger.querySelector('.dropdown-icon')) {
            const dropdown = trigger.parentElement.querySelector('.dropdown');
            
            // Mobile click handler - toggle dropdown when clicking the link
            trigger.addEventListener('click', (e) => {
                // Only handle dropdown toggle on mobile
                if (window.innerWidth < 992) {
                    // Check if click was on the text or the icon
                    const clickedIcon = e.target.closest('.dropdown-icon');
                    const clickedText = e.target.closest('span');
                    
                    // If clicking on the text (not icon), allow normal navigation
                    if (clickedText && !clickedIcon) {
                        return; // Allow default behavior
                    }
                    
                    // If clicking on icon or empty space in the link, toggle dropdown
                    e.preventDefault();
                    e.stopPropagation();
                    
                    const isActive = dropdown.classList.contains('active');
                    
                    // Close all other dropdowns
                    document.querySelectorAll('.dropdown').forEach(d => {
                        if (d !== dropdown) {
                            d.classList.remove('active');
                            d.previousElementSibling?.querySelector('.dropdown-icon')?.classList.remove('rotated');
                        }
                    });
                    
                    // Toggle current dropdown
                    dropdown.classList.toggle('active');
                    
                    // Rotate icon
                    const icon = trigger.querySelector('.dropdown-icon');
                    if (isActive) {
                        icon.classList.remove('rotated');
                    } else {
                        icon.classList.add('rotated');
                    }
                }
            });
            
            // Desktop hover handler
            trigger.parentElement.addEventListener('mouseenter', () => {
                if (window.innerWidth >= 992) {
                    dropdown.classList.add('active');
                    trigger.querySelector('.dropdown-icon')?.classList.add('rotated');
                }
            });
            
            trigger.parentElement.addEventListener('mouseleave', () => {
                if (window.innerWidth >= 992) {
                    dropdown.classList.remove('active');
                    trigger.querySelector('.dropdown-icon')?.classList.remove('rotated');
                }
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

// === SCROLL ANIMATIONS ===
function initScrollAnimations() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animated');
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });

    // Observe all animatable elements
    document.querySelectorAll('.section-title, .overview-content, .overview-image, .stat-card, .module, .project-card, .career-card, .instructor-image, .instructor-info, .enrollment-content, .footer-column').forEach(el => {
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
        
        if (window.scrollY > 100) {
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
            
            // Prevent body scroll when menu is open
            if (navMenu.classList.contains('active')) {
                document.body.style.overflow = 'hidden';
                document.documentElement.style.overflow = 'hidden';
            } else {
                document.body.style.overflow = '';
                document.documentElement.style.overflow = '';
            }
            
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
                document.documentElement.style.overflow = '';
                
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
                    top: targetElement.offsetTop - 100,
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
                        document.documentElement.style.overflow = '';
                    }
                }
            }
        });
    });
}

// === LOADING SCREEN ===
window.addEventListener('load', () => {
    setTimeout(() => {
        document.querySelector('.loading')?.classList.add('hidden');
    }, 500);
});