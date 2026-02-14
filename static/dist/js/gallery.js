
// === GALLERY DATA ===
const galleryData = [
    {
        id: 1,
        category: "classes",
        title: "Web Development Class",
        description: "Students learning HTML, CSS, and JavaScript in our lab",
        image: "images/classes.webp",
        date: "2023-10-15"
    },
    {
        id: 2,
        category: "events",
        title: "Annual IT Festival",
        description: "Our annual technology festival with coding competitions",
        image: "images/events.webp",
        date: "2023-08-22"
    },
    {
        id: 3,
        category: "students",
        title: "Student Project Presentation",
        description: "Students presenting their final projects to industry experts",
        image: "images/students.jpg",
        date: "2023-11-05"
    },
    {
        id: 4,
        category: "certificates",
        title: "Certificate Distribution",
        description: "Graduation ceremony for our web development batch",
        image: "images/certificates.png",
        date: "2023-09-30"
    },
    {
        id: 5,
        category: "projects",
        title: "Student Portfolio Websites",
        description: "Showcase of student-created portfolio websites",
        image: "images/classes.webp",
        date: "2023-10-28"
    },
    {
        id: 6,
        category: "classes",
        title: "Graphic Design Workshop",
        description: "Hands-on Adobe Photoshop and Illustrator training",
        image: "images/events.webp",
        date: "2023-09-12"
    },
    {
        id: 7,
        category: "events",
        title: "Industry Expert Session",
        description: "Guest lecture by senior software engineer from Google",
        image: "images/students.jpg",
        date: "2023-07-18"
    },
    {
        id: 8,
        category: "projects",
        title: "E-commerce Website Project",
        description: "Student project: fully functional e-commerce platform",
        image: "images/certificates.png",
        date: "2023-11-20"
    },
    {
        id: 9,
        category: "classes",
        title: "Python Programming Class",
        description: "Learning Python for data analysis and automation",
        image: "images/classes.webp",
        date: "2023-10-10"
    },
    {
        id: 10,
        category: "students",
        title: "Group Study Session",
        description: "Collaborative learning environment in our campus",
        image: "images/events.webp",
        date: "2023-09-05"
    },
    {
        id: 11,
        category: "certificates",
        title: "Digital Marketing Certification",
        description: "Certification ceremony for digital marketing graduates",
        image: "images/students.jpg",
        date: "2023-08-15"
    },
    {
        id: 12,
        category: "projects",
        title: "Mobile App Development",
        description: "Student projects: cross-platform mobile applications",
        image: "images/certificates.png",
        date: "2023-11-25"
    }
];

const videoData = [
    {
        id: 1,
        title: "Web Development Course Overview",
        description: "Complete overview of our 6-month web development course",
        thumbnail: "images/web development course.png",
        videoUrl: "https://example.com/videos/web-dev-overview.mp4",
        duration: "5:30"
    },
    {
        id: 2,
        title: "Student Success Stories",
        description: "Hear from our graduates about their career transformation",
        thumbnail: "images/students.jpg",
        videoUrl: "https://example.com/videos/success-stories.mp4",
        duration: "8:15"
    },
    {
        id: 3,
        title: "Graphic Design Workshop",
        description: "Highlights from our Adobe Creative Suite workshop",
        thumbnail: "images/graphic design course.avif",
        videoUrl: "https://example.com/videos/graphic-design-workshop.mp4",
        duration: "6:45"
    },
    {
        id: 4,
        title: "Campus Tour",
        description: "Virtual tour of our IT training facilities and labs",
        thumbnail: "images/classes.webp",
        videoUrl: "https://example.com/videos/campus-tour.mp4",
        duration: "4:20"
    }
];

// === INITIALIZATION ===
document.addEventListener('DOMContentLoaded', function() {
    initializeGallery();
    setupEventListeners();
    initLightbox();
    setupFilters();
    initScrollAnimations();
    
    // Hide loading screen
    setTimeout(() => {
        document.querySelector('.loading')?.classList.add('hidden');
    }, 500);
});

// === GALLERY INITIALIZATION ===
function initializeGallery() {
    generateGalleryItems('all');
    generateVideoGallery();
}

// === GENERATE GALLERY ITEMS ===
function generateGalleryItems(filter = 'all') {
    const container = document.querySelector('.gallery-grid');
    if (!container) return;

    // Filter items if needed
    const filteredItems = filter === 'all' 
        ? galleryData.slice(0, 8) // Show first 8 items initially
        : galleryData.filter(item => item.category === filter).slice(0, 8);

    container.innerHTML = '';
    
    filteredItems.forEach((item, index) => {
        const galleryItem = document.createElement('div');
        galleryItem.className = `gallery-item ${item.category}`;
        galleryItem.dataset.id = item.id;
        galleryItem.dataset.category = item.category;
        galleryItem.style.transitionDelay = `${index * 0.1}s`;
        
        // Format date
        const date = new Date(item.date);
        const formattedDate = date.toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });

        galleryItem.innerHTML = `
            <img src="${item.image}" alt="${item.title}" loading="lazy">
            <div class="gallery-overlay">
                <i class="fas fa-search-plus"></i>
                <h3>${item.title}</h3>
                <p>${item.description}</p>
                <small>${formattedDate}</small>
            </div>
        `;
        
        // Add error handling for image
        const img = galleryItem.querySelector('img');
        img.onerror = function() {
            this.src = 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="400" height="300" viewBox="0 0 400 300"><rect width="400" height="300" fill="%23f3f4f6"/><text x="200" y="150" text-anchor="middle" fill="%239ca3af" font-family="Arial" font-size="16">${item.title}</text></svg>';
        };
        
        container.appendChild(galleryItem);
    });

    // Update load more button visibility
    const loadMoreBtn = document.getElementById('loadMoreBtn');
    if (loadMoreBtn) {
        const totalItems = filter === 'all' 
            ? galleryData.length 
            : galleryData.filter(item => item.category === filter).length;
        
        if (filteredItems.length >= totalItems) {
            loadMoreBtn.style.display = 'none';
        } else {
            loadMoreBtn.style.display = 'inline-flex';
            loadMoreBtn.dataset.filter = filter;
            loadMoreBtn.dataset.currentCount = filteredItems.length;
        }
    }
}

// === GENERATE VIDEO GALLERY ===
function generateVideoGallery() {
    const container = document.querySelector('.video-grid');
    if (!container) return;

    container.innerHTML = '';
    
    videoData.forEach((video, index) => {
        const videoItem = document.createElement('div');
        videoItem.className = 'video-item';
        videoItem.dataset.id = video.id;
        videoItem.style.transitionDelay = `${index * 0.1}s`;
        
        videoItem.innerHTML = `
            <img src="${video.thumbnail}" alt="${video.title}" loading="lazy">
            <div class="video-overlay">
                <div class="play-btn">
                    <i class="fas fa-play"></i>
                </div>
            </div>
            <div class="video-info" style="display: none;">
                <h3>${video.title}</h3>
                <p>${video.description}</p>
                <p>Duration: ${video.duration}</p>
                <p class="video-url">${video.videoUrl}</p>
            </div>
        `;
        
        // Add error handling for thumbnail
        const img = videoItem.querySelector('img');
        img.onerror = function() {
            this.src = 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="400" height="300" viewBox="0 0 400 300"><rect width="400" height="300" fill="%23f3f4f6"/><text x="200" y="150" text-anchor="middle" fill="%239ca3af" font-family="Arial" font-size="16">${video.title}</text></svg>';
        };
        
        container.appendChild(videoItem);
    });
}

// === DROPDOWN FUNCTIONALITY ===

// === FILTER FUNCTIONALITY ===
function setupFilters() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const loadMoreBtn = document.getElementById('loadMoreBtn');

    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Update active button
            filterButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            
            // Apply filter
            const filter = button.dataset.filter;
            generateGalleryItems(filter);
            
            // Animate new items
            setTimeout(() => {
                initScrollAnimations();
            }, 100);
        });
    });

    // Load more functionality
    if (loadMoreBtn) {
        loadMoreBtn.addEventListener('click', loadMoreItems);
    }
}

function loadMoreItems() {
    const filter = this.dataset.filter;
    const currentCount = parseInt(this.dataset.currentCount);
    const container = document.querySelector('.gallery-grid');
    
    if (!container) return;

    // Get more items
    const allItems = filter === 'all' 
        ? galleryData 
        : galleryData.filter(item => item.category === filter);
    
    const nextItems = allItems.slice(currentCount, currentCount + 4);
    
    // Append new items
    nextItems.forEach((item, index) => {
        const galleryItem = document.createElement('div');
        galleryItem.className = `gallery-item ${item.category}`;
        galleryItem.dataset.id = item.id;
        galleryItem.dataset.category = item.category;
        galleryItem.style.transitionDelay = `${index * 0.1}s`;
        
        // Format date
        const date = new Date(item.date);
        const formattedDate = date.toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });

        galleryItem.innerHTML = `
            <img src="${item.image}" alt="${item.title}" loading="lazy">
            <div class="gallery-overlay">
                <i class="fas fa-search-plus"></i>
                <h3>${item.title}</h3>
                <p>${item.description}</p>
                <small>${formattedDate}</small>
            </div>
        `;
        
        // Add error handling for image
        const img = galleryItem.querySelector('img');
        img.onerror = function() {
            this.src = 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="400" height="300" viewBox="0 0 400 300"><rect width="400" height="300" fill="%23f3f4f6"/><text x="200" y="150" text-anchor="middle" fill="%239ca3af" font-family="Arial" font-size="16">${item.title}</text></svg>';
        };
        
        container.appendChild(galleryItem);
    });

    // Update button state
    const newCount = currentCount + nextItems.length;
    const totalItems = filter === 'all' 
        ? galleryData.length 
        : galleryData.filter(item => item.category === filter).length;
    
    this.dataset.currentCount = newCount;
    
    if (newCount >= totalItems) {
        this.style.display = 'none';
    }

    // Animate new items
    setTimeout(() => {
        initScrollAnimations();
    }, 100);
}

// === LIGHTBOX FUNCTIONALITY ===
function initLightbox() {
    const lightbox = document.getElementById('lightbox');
    const videoLightbox = document.getElementById('video-lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const lightboxVideo = document.getElementById('lightbox-video');
    const closeButtons = document.querySelectorAll('.close');
    const prevBtn = document.querySelector('.lightbox .prev-btn');
    const nextBtn = document.querySelector('.lightbox .next-btn');
    
    let currentGalleryItems = [];
    let currentIndex = 0;

    // Photo gallery lightbox
    document.addEventListener('click', (e) => {
        const galleryItem = e.target.closest('.gallery-item');
        if (galleryItem) {
            e.preventDefault();
            
            const category = galleryItem.dataset.category;
            const filter = document.querySelector('.filter-btn.active').dataset.filter;
            
            // Get all visible items
            currentGalleryItems = filter === 'all' 
                ? Array.from(document.querySelectorAll('.gallery-item'))
                : Array.from(document.querySelectorAll(`.gallery-item.${filter}`));
            
            currentIndex = currentGalleryItems.indexOf(galleryItem);
            
            openLightbox(galleryItem);
        }

        // Video gallery lightbox
        const videoItem = e.target.closest('.video-item');
        if (videoItem) {
            e.preventDefault();
            openVideoLightbox(videoItem);
        }
    });

    // Navigation in lightbox
    if (prevBtn && nextBtn) {
        prevBtn.addEventListener('click', showPrevItem);
        nextBtn.addEventListener('click', showNextItem);
        
        // Keyboard navigation
        document.addEventListener('keydown', (e) => {
            if (lightbox.style.display === 'flex') {
                if (e.key === 'ArrowLeft') showPrevItem();
                if (e.key === 'ArrowRight') showNextItem();
            }
        });
    }

    // Close lightboxes
    closeButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            lightbox.style.display = 'none';
            videoLightbox.style.display = 'none';
            document.body.style.overflow = '';
            
            // Pause video
            if (lightboxVideo) {
                lightboxVideo.pause();
                lightboxVideo.currentTime = 0;
            }
        });
    });

    // Close when clicking outside
    [lightbox, videoLightbox].forEach(lb => {
        lb.addEventListener('click', (e) => {
            if (e.target === lb) {
                lb.style.display = 'none';
                document.body.style.overflow = '';
                
                // Pause video
                if (lightboxVideo) {
                    lightboxVideo.pause();
                    lightboxVideo.currentTime = 0;
                }
            }
        });
    });

    // Escape key to close
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            lightbox.style.display = 'none';
            videoLightbox.style.display = 'none';
            document.body.style.overflow = '';
            
            // Pause video
            if (lightboxVideo) {
                lightboxVideo.pause();
                lightboxVideo.currentTime = 0;
            }
        }
    });

    function openLightbox(item) {
        const img = item.querySelector('img');
        const title = item.querySelector('h3')?.textContent || '';
        const description = item.querySelector('p')?.textContent || '';
        const date = item.querySelector('small')?.textContent || '';

        if (img) {
            lightboxImg.src = img.src;
            lightboxImg.alt = img.alt;
            
            document.getElementById('lightbox-title').textContent = title;
            document.getElementById('lightbox-desc').textContent = `${description} • ${date}`;
            
            lightbox.style.display = 'flex';
            document.body.style.overflow = 'hidden';
        }
    }

    function openVideoLightbox(item) {
        const thumbnail = item.querySelector('img');
        const title = item.querySelector('h3')?.textContent || '';
        const description = item.querySelector('p')?.textContent || '';
        const videoUrl = item.querySelector('.video-url')?.textContent || '';

        if (thumbnail && videoUrl) {
            lightboxVideo.src = videoUrl;
            lightboxVideo.poster = thumbnail.src;
            
            document.getElementById('video-lightbox-title').textContent = title;
            document.getElementById('video-lightbox-desc').textContent = description;
            
            videoLightbox.style.display = 'flex';
            document.body.style.overflow = 'hidden';
            
            // Play video automatically
            setTimeout(() => {
                lightboxVideo.play().catch(e => console.log("Autoplay prevented:", e));
            }, 300);
        }
    }

    function showPrevItem() {
        if (currentGalleryItems.length === 0) return;
        
        currentIndex = (currentIndex - 1 + currentGalleryItems.length) % currentGalleryItems.length;
        openLightbox(currentGalleryItems[currentIndex]);
    }

    function showNextItem() {
        if (currentGalleryItems.length === 0) return;
        
        currentIndex = (currentIndex + 1) % currentGalleryItems.length;
        openLightbox(currentGalleryItems[currentIndex]);
    }
}

// === SCROLL ANIMATIONS ===
function initScrollAnimations() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animated');
                
                // Animate child elements with delays
                if (entry.target.classList.contains('gallery-item') || 
                    entry.target.classList.contains('video-item')) {
                    const overlay = entry.target.querySelector('.gallery-overlay, .video-overlay');
                    if (overlay) {
                        const h3 = overlay.querySelector('h3');
                        const p = overlay.querySelector('p');
                        if (h3) h3.style.transitionDelay = '0.1s';
                        if (p) p.style.transitionDelay = '0.2s';
                    }
                }
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });

    // Observe all animatable elements
    document.querySelectorAll('.section-title, .gallery-item, .video-item, .footer-column').forEach(el => {
        observer.observe(el);
    });
}

// === EVENT LISTENERS ===
function setupEventListeners() {
    // Navbar scroll effect - transparent in hero section
    window.addEventListener('scroll', () => {
        const navbar = document.querySelector('.navbar');
        const logo = document.querySelector('.logo');
        const mobileToggle = document.querySelector('.mobile-toggle');
        const heroSection = document.querySelector('.gallery-hero');
        
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