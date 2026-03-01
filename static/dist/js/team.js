
// === TEAM DATA ===
const teamMembers = [
    {
        id: 1,
        name: "Md. Shariful Islam",
        position: "CEO & Founder",
        department: "management",
        description: "10+ years experience in software development and IT education. Passionate about bridging the digital skills gap.",
        image: "about/Md. Shariful Islam.jpg",
        social: {
            linkedin: "#",
            twitter: "#",
            facebook: "#"
        }
    },
    {
        id: 2,
        name: "Sumon Sarker",
        position: "Lead Instructor",
        department: "training",
        description: "Hardware engineer with 6 years of experience. Specializes in computer hardware assembly, maintenance, and troubleshooting.",
        image: "about/Sumon Sarker.jpg",
        social: {
            linkedin: "#",
            twitter: "#",
            facebook: "#"
        }
    },
    {
        id: 3,
        name: "Md. Kamrul Islam",
        position: "Design Lead",
        department: "design",
        description: "Graphic and UI/UX designer with 7 years of experience. Expert in Adobe Creative Suite and Figma.",
        image: "about/Kamrul Islam.jpg",
        social: {
            linkedin: "#",
            twitter: "#",
            facebook: "#"
        }
    },
    {
        id: 4,
        name: "Golam Robbany",
        position: "Marketing Head",
        department: "marketing",
        description: "Digital marketing specialist with expertise in SEO, social media marketing, and content strategy.",
        image: "about/Golam Robbany.jpg",
        social: {
            linkedin: "#",
            twitter: "#",
            facebook: "#"
        }
    },
    {
        id: 5,
        name: "Dipro Saha",
        position: "Senior Web Developer",
        department: "development",
        description: "Full-stack developer specializing in MERN stack with 6 years of industry experience.",
        image: "about/Dipro Saha.PNG",
        social: {
            linkedin: "#",
            twitter: "#",
            facebook: "#"
        }
    },
    {
        id: 6,
        name: "Anup Mondal",
        position: "Python Instructor",
        department: "training",
        description: "Data scientist and Python expert with 9+ years of teaching experience and industry projects.",
        image: "https://images.unsplash.com/photo-1573496359322-0173103696b1?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80",
        social: {
            linkedin: "#",
            twitter: "#",
            facebook: "#"
        }
    },
    {
        id: 7,
        name: "Sadman Sadik",
        position: "Operations Manager",
        department: "management",
        description: "Expert in project management and operations with 8 years of experience in IT education.",
        image: "about/Sadman Sadik.jpg",
        social: {
            linkedin: "#",
            twitter: "#",
            facebook: "#"
        }
    },
    
];

// === INITIALIZATION ===
document.addEventListener('DOMContentLoaded', function() {
    // generateTeamMembers();
    initScrollAnimations();
    setupEventListeners();
    setupDropdowns();
    // setupTeamFilter();
});

// === TEAM FILTER ===
function setupTeamFilter() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const teamMembers = document.querySelectorAll('.team-member');
    
    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Update active button
            filterButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            
            const filter = button.dataset.filter;
            
            // Filter team members
            teamMembers.forEach(member => {
                if (filter === 'all' || member.dataset.department === filter) {
                    member.style.display = 'flex';
                    member.style.animation = 'none';
                    setTimeout(() => {
                        member.style.animation = '';
                    }, 10);
                } else {
                    member.style.display = 'none';
                }
            });
        });
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
    document.querySelectorAll('.section-title, .team-member, .expertise-card, .footer-column, .join-team-section').forEach(el => {
        observer.observe(el);
    });
}

// === DROPDOWN FUNCTIONALITY ===

// === EVENT LISTENERS ===
function setupEventListeners() {
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
            
            if (window.innerWidth < 992 && this.classList.contains('dropdown-item')) {
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
            if (link.getAttribute('href') === `#${current}` || 
                (current === '' && link.getAttribute('href') === 'team.html')) {
                link.classList.add('active');
            }
        });
    }
    
    window.addEventListener('scroll', updateActiveNavLink);
}