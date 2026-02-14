
// === COURSES DATA ===
const coursesData = [
    {
        id: 1,
        title: "Full Stack Web Development",
        description: "Learn HTML, CSS, JavaScript, React, Node.js, MongoDB and become a full-stack developer. Build real-world projects and deploy them online.",
        category: "web",
        icon: "fas fa-code",
        duration: "6 Months",
        projects: "15+ Projects",
        level: "Beginner to Advanced",
        certification: "Yes",
        image: "our courses/Full Stack Web Development.png",
        modules: [
            "HTML5 & CSS3 Fundamentals",
            "JavaScript & ES6+",
            "React.js & Redux",
            "Node.js & Express.js",
            "MongoDB & Database Design",
            "RESTful APIs",
            "Git & GitHub",
            "Deployment & DevOps Basics"
        ],
        careers: ["Frontend Developer", "Backend Developer", "Full Stack Developer", "Web Application Developer"],
        prerequisites: ["Basic Computer Knowledge", "Logical Thinking"]
    },
    {
        id: 2,
        title: "Professional Graphic Design",
        description: "Master Adobe Photoshop, Illustrator, InDesign for professional graphic design. Learn branding, UI design, and print media design.",
        category: "design",
        icon: "fas fa-paint-brush",
        duration: "4 Months",
        projects: "12+ Projects",
        level: "Beginner to Intermediate",
        certification: "Yes",
        image: "our courses/Professional Graphic Design.jpg",
        modules: [
            "Adobe Photoshop Mastery",
            "Adobe Illustrator Essentials",
            "Logo & Brand Identity Design",
            "UI/UX Design Principles",
            "Print Media Design",
            "Social Media Graphics",
            "Portfolio Development"
        ],
        careers: ["Graphic Designer", "UI Designer", "Brand Designer", "Digital Artist"],
        prerequisites: ["Creative Mindset", "Basic Computer Skills"]
    },
    {
        id: 3,
        title: "Digital Marketing Mastery",
        description: "Learn SEO, Social Media Marketing, Google Ads, content marketing strategies, and analytics to become a digital marketing expert.",
        category: "marketing",
        icon: "fas fa-chart-line",
        duration: "3 Months",
        projects: "10+ Campaigns",
        level: "Beginner to Advanced",
        certification: "Yes",
        image: "our courses/Digital Marketing Mastery.jpg",
        modules: [
            "SEO Fundamentals",
            "Social Media Marketing",
            "Google Ads & PPC",
            "Content Marketing",
            "Email Marketing",
            "Analytics & Reporting",
            "E-commerce Marketing"
        ],
        careers: ["Digital Marketing Specialist", "SEO Expert", "Social Media Manager", "Content Marketer"],
        prerequisites: ["Basic Internet Knowledge", "Communication Skills"]
    },
    {
        id: 4,
        title: "Python Programming & Data Science",
        description: "Start with Python basics, then move to data analysis, automation, machine learning basics, and web development with Django.",
        category: "programming",
        icon: "fab fa-python",
        duration: "5 Months",
        projects: "20+ Projects",
        level: "Beginner to Intermediate",
        certification: "Yes",
        image: "our courses/Python Programming & Data Science.webp",
        modules: [
            "Python Fundamentals",
            "Data Structures & Algorithms",
            "Data Analysis with Pandas",
            "Data Visualization",
            "Automation Scripting",
            "Web Scraping",
            "Django Web Framework"
        ],
        careers: ["Python Developer", "Data Analyst", "Automation Engineer", "Backend Developer"],
        prerequisites: ["Logical Thinking", "Basic Math"]
    },
    {
        id: 5,
        title: "UI/UX Design Specialization",
        description: "Learn user interface and experience design with Figma, Adobe XD, prototyping, user research, and design systems.",
        category: "design",
        icon: "fas fa-object-group",
        duration: "4 Months",
        projects: "12+ Projects",
        level: "Beginner to Advanced",
        certification: "Yes",
        image: "our courses/UI-UX Design Specialization.jpg",
        modules: [
            "UI Design Principles",
            "UX Research Methods",
            "Wireframing & Prototyping",
            "Figma Mastery",
            "Design Systems",
            "Mobile App Design",
            "Portfolio Building"
        ],
        careers: ["UI Designer", "UX Designer", "Product Designer", "Interaction Designer"],
        prerequisites: ["Creative Thinking", "Basic Design Sense"]
    },
    {
        id: 6,
        title: "Freelancing Career Development",
        description: "Learn how to start and grow your freelancing career from scratch. Master client communication, pricing, and platform management.",
        category: "freelance",
        icon: "fas fa-laptop-house",
        duration: "2 Months",
        projects: "8+ Real Projects",
        level: "All Levels",
        certification: "Yes",
        image: "our courses/Freelancing Career Development.jpg",
        modules: [
            "Freelancing Platforms",
            "Client Communication",
            "Proposal Writing",
            "Pricing Strategies",
            "Time Management",
            "Contract & Legal",
            "Building Portfolio"
        ],
        careers: ["Freelance Developer", "Freelance Designer", "Digital Marketer", "Consultant"],
        prerequisites: ["Any IT Skill", "Communication Skills"]
    },
    {
        id: 7,
        title: "Microsoft Office Mastery",
        description: "Master Microsoft Word, Excel, PowerPoint, and Outlook for professional office work. Learn advanced formulas, macros, and automation.",
        category: "office",
        icon: "fas fa-file-excel",
        duration: "2 Months",
        projects: "10+ Practical Tasks",
        level: "Beginner to Advanced",
        certification: "Yes",
        image: "our courses/Microsoft Office Mastery.jpg",
        modules: [
            "Microsoft Word Advanced",
            "Excel Formulas & Functions",
            "Data Analysis in Excel",
            "PowerPoint Presentations",
            "Outlook & Email Management",
            "Office Automation",
            "Collaboration Tools"
        ],
        careers: ["Office Administrator", "Data Entry Specialist", "Executive Assistant", "Account Assistant"],
        prerequisites: ["Basic Computer Knowledge", "Typing Skills"]
    },
    {
        id: 8,
        title: "Mobile App Development",
        description: "Learn to build mobile applications for Android and iOS using React Native. Create cross-platform apps with modern JavaScript.",
        category: "web",
        icon: "fas fa-mobile-alt",
        duration: "4 Months",
        projects: "8+ Mobile Apps",
        level: "Intermediate",
        certification: "Yes",
        image: "our courses/Mobile App Development.jpg",
        modules: [
            "React Native Fundamentals",
            "Mobile UI Design",
            "Navigation & Routing",
            "API Integration",
            "State Management",
            "App Deployment",
            "Performance Optimization"
        ],
        careers: ["Mobile App Developer", "React Native Developer", "Cross-platform Developer"],
        prerequisites: ["JavaScript Basics", "React Fundamentals"]
    },
    {
        id: 9,
        title: "Data Analytics with Excel & Power BI",
        description: "Learn data analysis, visualization, and business intelligence using Excel and Microsoft Power BI for data-driven decision making.",
        category: "office",
        icon: "fas fa-chart-bar",
        duration: "3 Months",
        projects: "10+ Dashboards",
        level: "Beginner to Intermediate",
        certification: "Yes",
        image: "our courses/Data Analytics with Excel & Power BI.jpg",
        modules: [
            "Advanced Excel Analytics",
            "Power Query & Power Pivot",
            "DAX Formulas",
            "Power BI Desktop",
            "Data Visualization",
            "Dashboard Design",
            "Business Reporting"
        ],
        careers: ["Data Analyst", "Business Analyst", "Reporting Specialist", "BI Developer"],
        prerequisites: ["Basic Excel Knowledge", "Analytical Thinking"]
    }
];

// === INITIALIZATION ===
document.addEventListener('DOMContentLoaded', function() {
    generateCourses();
    initScrollAnimations();
    setupEventListeners();
    setupDropdowns();
    setupCategoryFilters();
    setupModal();
});

// === GENERATE COURSES ===
function generateCourses(filterCategory = 'all') {
    const container = document.querySelector('.courses-container');
    if (!container) return;

    container.innerHTML = '';
    
    const filteredCourses = filterCategory === 'all' 
        ? coursesData 
        : coursesData.filter(course => course.category === filterCategory);
    
    if (filteredCourses.length === 0) {
        container.innerHTML = `
            <div style="grid-column: 1/-1; text-align: center; padding: 40px;">
                <i class="fas fa-search" style="font-size: 3rem; color: var(--primary); margin-bottom: 20px;"></i>
                <h3>No courses found in this category</h3>
                <p>Please select another category or check back soon for new courses.</p>
            </div>
        `;
        return;
    }
    
    filteredCourses.forEach((course, index) => {
        const card = document.createElement('div');
        card.className = 'course-card';
        card.dataset.category = course.category;
        card.dataset.id = course.id;
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
                <span style="display: inline-block; background: rgba(187, 0, 0, 0.1); color: var(--primary); padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; margin-bottom: 10px; font-weight: 600;">${getCategoryName(course.category)}</span>
                <h3>${course.title}</h3>
                <p>${course.description}</p>
                <div class="course-meta">
                    <span><i class="far fa-clock"></i> ${course.duration}</span>
                    <span><i class="fas fa-project-diagram"></i> ${course.projects}</span>
                    <span><i class="fas fa-signal"></i> ${course.level}</span>
                </div>
                <ul class="course-features">
                    ${course.modules.slice(0, 3).map(module => `<li><i class="fas fa-check-circle"></i> ${module}</li>`).join('')}
                </ul>
                <div style="display: flex; gap: 10px; margin-top: auto;">
                    <button class="btn btn-primary view-details-btn" style="flex: 1;">View Details</button>
                    <a href="#contact" class="btn btn-outline" style="flex: 1;">Enroll Now</a>
                </div>
            </div>
        `;
        
        // Add error handling for image
        const img = card.querySelector('img');
        img.onerror = function() {
            this.src = 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="400" height="250" viewBox="0 0 400 250"><rect width="400" height="250" fill="%23f3f4f6"/><text x="200" y="125" text-anchor="middle" fill="%239ca3af" font-family="Arial" font-size="16">${course.title}</text></svg>';
        };
        
        container.appendChild(card);
    });
    
    // Add event listeners to view details buttons
    document.querySelectorAll('.view-details-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const courseId = this.closest('.course-card').dataset.id;
            showCourseDetails(courseId);
        });
    });
}

function getCategoryName(category) {
    const categories = {
        'web': 'Web Development',
        'design': 'Graphic Design',
        'marketing': 'Digital Marketing',
        'programming': 'Programming',
        'freelance': 'Freelancing',
        'office': 'Office Applications'
    };
    return categories[category] || category;
}

// === CATEGORY FILTERS ===
function setupCategoryFilters() {
    const categoryButtons = document.querySelectorAll('.category-btn');
    
    categoryButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove active class from all buttons
            categoryButtons.forEach(btn => btn.classList.remove('active'));
            
            // Add active class to clicked button
            this.classList.add('active');
            
            // Filter courses
            const category = this.dataset.category;
            generateCourses(category);
            
            // Scroll to courses section
            document.getElementById('courses-list').scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        });
    });
}

// === COURSE DETAILS MODAL ===
function setupModal() {
    const modal = document.getElementById('courseModal');
    const closeModal = document.querySelector('.close-modal');
    
    if (!modal || !closeModal) return;
    
    // Close modal when clicking close button
    closeModal.addEventListener('click', () => {
        modal.classList.remove('active');
        document.body.style.overflow = '';
    });
    
    // Close modal when clicking outside
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.classList.remove('active');
            document.body.style.overflow = '';
        }
    });
    
    // Close modal with Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('active')) {
            modal.classList.remove('active');
            document.body.style.overflow = '';
        }
    });
}

function showCourseDetails(courseId) {
    const course = coursesData.find(c => c.id == courseId);
    if (!course) return;
    
    const modal = document.getElementById('courseModal');
    
    // Update modal content
    document.getElementById('modalCourseTitle').textContent = course.title;
    document.getElementById('modalCourseCategory').textContent = getCategoryName(course.category);
    document.getElementById('modalCourseDuration').textContent = course.duration;
    document.getElementById('modalCourseProjects').textContent = course.projects;
    document.getElementById('modalCourseLevel').textContent = course.level;
    document.getElementById('modalCourseCertification').textContent = course.certification;
    document.getElementById('modalCourseDescription').textContent = course.description;
    
    // Update modules
    const modulesList = document.getElementById('modalCourseModules');
    modulesList.innerHTML = '';
    course.modules.forEach(module => {
        const li = document.createElement('li');
        li.textContent = module;
        modulesList.appendChild(li);
    });
    
    // Update careers
    const careersList = document.getElementById('modalCourseCareers');
    careersList.innerHTML = '';
    course.careers.forEach(career => {
        const li = document.createElement('li');
        li.textContent = career;
        careersList.appendChild(li);
    });
    
    // Update prerequisites
    const prereqList = document.getElementById('modalCoursePrerequisites');
    prereqList.innerHTML = '';
    course.prerequisites.forEach(prereq => {
        const li = document.createElement('li');
        li.textContent = prereq;
        prereqList.appendChild(li);
    });
    
    // Show modal
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
}


// === SCROLL ANIMATIONS ===
function initScrollAnimations() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animated');
                
                // Animate child elements with delays
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
    document.querySelectorAll('.section-title, .course-card, .footer-column').forEach(el => {
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

// === LOADING SCREEN ===
window.addEventListener('load', () => {
    setTimeout(() => {
        document.querySelector('.loading')?.classList.add('hidden');
    }, 500);
});