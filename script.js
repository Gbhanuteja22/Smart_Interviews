// Smart Interviews Website JavaScript
class SmartInterviews {
    constructor() {
        this.problems = [];
        this.tasks = JSON.parse(localStorage.getItem('smartInterviewsTasks')) || [];
        this.currentFilter = 'all';
        this.currentTaskFilter = 'all';
        
        this.init();
    }

    init() {
        // Wait for DOM to be fully loaded
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => this.initializeApp());
        } else {
            this.initializeApp();
        }
    }

    initializeApp() {
        console.log('Initializing Smart Interviews App...');
        
        this.setupEventListeners();
        this.loadProblems();
        this.renderTasks();
        this.updateStats();
        this.updateTaskStats();
        
        // Show home section by default
        this.showSection('home');
        
        console.log('App initialized successfully!');
    }

    setupEventListeners() {
        // Navigation
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const section = link.getAttribute('data-section');
                this.showSection(section);
                this.setActiveNavLink(link);
            });
        });

        // Mobile hamburger menu
        const hamburger = document.querySelector('.hamburger');
        const navMenu = document.querySelector('.nav-menu');
        
        if (hamburger && navMenu) {
            hamburger.addEventListener('click', () => {
                hamburger.classList.toggle('active');
                navMenu.classList.toggle('active');
            });

            // Close mobile menu when clicking on a link
            navLinks.forEach(link => {
                link.addEventListener('click', () => {
                    hamburger.classList.remove('active');
                    navMenu.classList.remove('active');
                });
            });
        }

        // Search functionality
        const searchInput = document.getElementById('search-input');
        const languageFilter = document.getElementById('language-filter');
        
        if (searchInput) {
            searchInput.addEventListener('input', () => this.filterProblems());
        }
        
        if (languageFilter) {
            languageFilter.addEventListener('change', () => this.filterProblems());
        }

        // Task management
        const addTaskBtn = document.getElementById('add-task-btn');
        const taskInput = document.getElementById('task-input');
        
        if (addTaskBtn) {
            addTaskBtn.addEventListener('click', () => this.addTask());
        }
        
        if (taskInput) {
            taskInput.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') {
                    this.addTask();
                }
            });
        }

        // Task filters
        const filterBtns = document.querySelectorAll('.filter-btn');
        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const filter = btn.getAttribute('data-filter');
                this.setTaskFilter(filter);
                this.setActiveFilterBtn(btn);
            });
        });

        // Modal functionality
        const modal = document.getElementById('problem-modal');
        const closeBtn = document.querySelector('.close');
        
        if (closeBtn) {
            closeBtn.addEventListener('click', () => {
                modal.style.display = 'none';
            });
        }
        
        if (modal) {
            window.addEventListener('click', (e) => {
                if (e.target === modal) {
                    modal.style.display = 'none';
                }
            });
        }
    }

    showSection(sectionId) {
        console.log(`Showing section: ${sectionId}`);
        
        // Hide all sections
        const sections = document.querySelectorAll('.section');
        sections.forEach(section => {
            section.classList.remove('active');
        });

        // Show target section
        const targetSection = document.getElementById(sectionId);
        if (targetSection) {
            targetSection.classList.add('active');
            targetSection.classList.add('fade-in');
            
            // Remove animation class after animation completes
            setTimeout(() => {
                targetSection.classList.remove('fade-in');
            }, 500);
        }

        // Special handling for different sections
        if (sectionId === 'problems') {
            this.renderProblems();
        } else if (sectionId === 'contests') {
            this.renderContests();
        } else if (sectionId === 'tasks') {
            this.renderTasks();
        }
    }

    setActiveNavLink(activeLink) {
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(link => link.classList.remove('active'));
        activeLink.classList.add('active');
    }

    loadProblems() {
        // Since we can't dynamically read files in a static GitHub Pages site,
        // we'll create a curated list of problems based on the repository structure
        this.problems = [
            {
                name: "A Power B",
                language: "python",
                category: "Mathematics",
                description: "Calculate A raised to the power B efficiently."
            },
            {
                name: "Balanced Parentheses",
                language: "python",
                category: "Stack",
                description: "Check if parentheses in a string are balanced."
            },
            {
                name: "Binary Representation",
                language: "python",
                category: "Bit Manipulation",
                description: "Convert decimal numbers to binary representation."
            },
            {
                name: "Bubble Sort",
                language: "python",
                category: "Sorting",
                description: "Implementation of bubble sort algorithm."
            },
            {
                name: "Cabinets Partitioning",
                language: "python",
                category: "Dynamic Programming",
                description: "Partition cabinets optimally."
            },
            {
                name: "Changing Directories",
                language: "python",
                category: "Stack",
                description: "Simulate directory navigation commands."
            },
            {
                name: "Check Anagrams",
                language: "python",
                category: "Strings",
                description: "Check if two strings are anagrams."
            },
            {
                name: "CheckerBoard Pattern",
                language: "java",
                category: "Patterns",
                description: "Generate checkerboard pattern."
            },
            {
                name: "Coin Game",
                language: "python",
                category: "Game Theory",
                description: "Optimal strategy for coin game."
            },
            {
                name: "Collecting Mangoes",
                language: "python",
                category: "Stack",
                description: "Track maximum mango size in basket."
            },
            {
                name: "Count Unreachable Nodes",
                language: "python",
                category: "Graph",
                description: "Find unreachable nodes in a graph."
            },
            {
                name: "Count the Triangles",
                language: "python",
                category: "Geometry",
                description: "Count valid triangles from given sides."
            },
            {
                name: "Diagonal Traversal of Matrix",
                language: "java",
                category: "Arrays",
                description: "Traverse matrix diagonally."
            },
            {
                name: "Distinct Elements in Window",
                language: "java",
                category: "Sliding Window",
                description: "Find distinct elements in sliding window."
            },
            {
                name: "Finding CubeRoot",
                language: "java",
                category: "Mathematics",
                description: "Find cube root using binary search."
            },
            {
                name: "Hollow Diamond Pattern",
                language: "java",
                category: "Patterns",
                description: "Generate hollow diamond pattern."
            },
            {
                name: "Insertion Sort",
                language: "python",
                category: "Sorting",
                description: "Implementation of insertion sort."
            },
            {
                name: "Interleavings",
                language: "python",
                category: "Recursion",
                description: "Generate all interleavings of two strings."
            },
            {
                name: "LCM and HCF",
                language: "python",
                category: "Mathematics",
                description: "Calculate LCM and HCF of numbers."
            },
            {
                name: "Left View of Tree",
                language: "java",
                category: "Trees",
                description: "Find left view of binary tree."
            },
            {
                name: "Optimal Prime Game",
                language: "java",
                category: "Game Theory",
                description: "Game theory problem with prime numbers."
            },
            {
                name: "Product of 2 Matrices",
                language: "java",
                category: "Arrays",
                description: "Matrix multiplication algorithm."
            },
            {
                name: "Right Angled Triangle Pattern",
                language: "java",
                category: "Patterns",
                description: "Generate right angled triangle pattern."
            },
            {
                name: "Selection Sort",
                language: "python",
                category: "Sorting",
                description: "Implementation of selection sort."
            },
            {
                name: "Spiral Traversal Of Matrix",
                language: "python",
                category: "Arrays",
                description: "Traverse matrix in spiral order."
            },
            {
                name: "Stock Span",
                language: "python",
                category: "Stack",
                description: "Calculate stock span for each day."
            },
            {
                name: "Tower of Hanoi",
                language: "python",
                category: "Recursion",
                description: "Solve Tower of Hanoi puzzle."
            },
            {
                name: "Triple Trouble",
                language: "java",
                category: "Arrays",
                description: "Find unique element in array of triplets."
            }
        ];

        console.log(`Loaded ${this.problems.length} problems`);
    }

    renderProblems() {
        const problemsGrid = document.getElementById('problems-grid');
        if (!problemsGrid) return;

        const filteredProblems = this.getFilteredProblems();
        
        if (filteredProblems.length === 0) {
            problemsGrid.innerHTML = '<p class="no-results">No problems found matching your criteria.</p>';
            return;
        }

        problemsGrid.innerHTML = filteredProblems.map(problem => `
            <div class="problem-card" onclick="smartInterviews.showProblemDetails('${problem.name}')">
                <div class="problem-title">${problem.name}</div>
                <span class="problem-language">${problem.language.toUpperCase()}</span>
                <div class="problem-description">${problem.description}</div>
                <div class="problem-category">Category: ${problem.category}</div>
            </div>
        `).join('');
    }

    getFilteredProblems() {
        const searchTerm = document.getElementById('search-input')?.value.toLowerCase() || '';
        const languageFilter = document.getElementById('language-filter')?.value || '';

        return this.problems.filter(problem => {
            const matchesSearch = problem.name.toLowerCase().includes(searchTerm) ||
                                problem.description.toLowerCase().includes(searchTerm) ||
                                problem.category.toLowerCase().includes(searchTerm);
            
            const matchesLanguage = !languageFilter || problem.language === languageFilter;
            
            return matchesSearch && matchesLanguage;
        });
    }

    filterProblems() {
        this.renderProblems();
    }

    showProblemDetails(problemName) {
        const problem = this.problems.find(p => p.name === problemName);
        if (!problem) return;

        const modal = document.getElementById('problem-modal');
        const modalBody = document.getElementById('modal-body');
        
        if (modal && modalBody) {
            modalBody.innerHTML = `
                <h2>${problem.name}</h2>
                <div class="problem-meta">
                    <span class="problem-language">${problem.language.toUpperCase()}</span>
                    <span class="problem-category-badge">Category: ${problem.category}</span>
                </div>
                <div class="problem-full-description">
                    <p>${problem.description}</p>
                    <p><strong>Note:</strong> This problem is part of the Smart Interviews collection. 
                    The complete solution and problem statement can be found in the repository files.</p>
                </div>
                <div class="problem-actions">
                    <button class="btn-primary" onclick="window.open('https://github.com/Gbhanuteja22/Smart_Interviews', '_blank')">
                        View on GitHub
                    </button>
                </div>
            `;
            modal.style.display = 'block';
        }
    }

    renderContests() {
        // Render internal contests
        const internalContests = document.getElementById('internal-contests');
        if (internalContests) {
            internalContests.innerHTML = `
                <div class="contest-item">
                    <h4>Internal Contest 1</h4>
                    <p>Collection of algorithmic problems from the first internal contest.</p>
                </div>
                <div class="contest-item">
                    <h4>Internal Contest 2</h4>
                    <p>Advanced problems covering various data structures and algorithms.</p>
                </div>
                <div class="contest-item">
                    <h4>Internal Contest 3 - Smaller Elements</h4>
                    <p>Problems focusing on counting and array manipulation techniques.</p>
                </div>
                <div class="contest-item">
                    <h4>Internal Contest 4 - Ranking Books</h4>
                    <p>Problems involving sorting and ranking algorithms.</p>
                </div>
            `;
        }

        // Render final contests
        const finalContests = document.getElementById('final-contests');
        if (finalContests) {
            finalContests.innerHTML = `
                <div class="contest-item">
                    <h4>Farewell Party</h4>
                    <p>Optimization problem involving room capacity and time intervals.</p>
                </div>
                <div class="contest-item">
                    <h4>Advanced Algorithms</h4>
                    <p>Complex algorithmic challenges from the final contest round.</p>
                </div>
            `;
        }
    }

    // Task Management System
    addTask() {
        const taskInput = document.getElementById('task-input');
        const taskPriority = document.getElementById('task-priority');
        
        if (!taskInput || !taskPriority) return;
        
        const taskText = taskInput.value.trim();
        if (!taskText) {
            alert('Please enter a task!');
            return;
        }

        const task = {
            id: Date.now(),
            text: taskText,
            priority: taskPriority.value,
            completed: false,
            createdAt: new Date().toISOString()
        };

        this.tasks.push(task);
        this.saveTasks();
        
        taskInput.value = '';
        taskPriority.value = 'low';
        
        this.renderTasks();
        this.updateTaskStats();
        
        console.log('Task added:', task);
    }

    toggleTask(taskId) {
        const task = this.tasks.find(t => t.id === taskId);
        if (task) {
            task.completed = !task.completed;
            this.saveTasks();
            this.renderTasks();
            this.updateTaskStats();
            console.log('Task toggled:', task);
        }
    }

    deleteTask(taskId) {
        if (confirm('Are you sure you want to delete this task?')) {
            this.tasks = this.tasks.filter(t => t.id !== taskId);
            this.saveTasks();
            this.renderTasks();
            this.updateTaskStats();
            console.log('Task deleted:', taskId);
        }
    }

    setTaskFilter(filter) {
        this.currentTaskFilter = filter;
        this.renderTasks();
        console.log('Task filter set to:', filter);
    }

    setActiveFilterBtn(activeBtn) {
        const filterBtns = document.querySelectorAll('.filter-btn');
        filterBtns.forEach(btn => btn.classList.remove('active'));
        activeBtn.classList.add('active');
    }

    getFilteredTasks() {
        switch (this.currentTaskFilter) {
            case 'completed':
                return this.tasks.filter(task => task.completed);
            case 'pending':
                return this.tasks.filter(task => !task.completed);
            case 'high':
                return this.tasks.filter(task => task.priority === 'high');
            default:
                return this.tasks;
        }
    }

    renderTasks() {
        const taskList = document.getElementById('task-list');
        if (!taskList) return;

        const filteredTasks = this.getFilteredTasks();
        
        if (filteredTasks.length === 0) {
            taskList.innerHTML = '<p class="no-tasks">No tasks found. Add a new task to get started!</p>';
            return;
        }

        taskList.innerHTML = filteredTasks.map(task => `
            <div class="task-item ${task.completed ? 'completed' : ''} ${task.priority}-priority slide-in">
                <input type="checkbox" 
                       class="task-checkbox" 
                       ${task.completed ? 'checked' : ''} 
                       onchange="smartInterviews.toggleTask(${task.id})">
                <span class="task-text">${task.text}</span>
                <span class="task-priority-badge priority-${task.priority}">${task.priority.toUpperCase()}</span>
                <button class="task-delete" onclick="smartInterviews.deleteTask(${task.id})">Delete</button>
            </div>
        `).join('');
    }

    saveTasks() {
        localStorage.setItem('smartInterviewsTasks', JSON.stringify(this.tasks));
    }

    updateTaskStats() {
        const totalTasks = document.getElementById('total-tasks');
        const pendingTasks = document.getElementById('pending-tasks');
        const completedTasks = document.getElementById('completed-tasks');

        if (totalTasks) totalTasks.textContent = this.tasks.length;
        if (pendingTasks) pendingTasks.textContent = this.tasks.filter(t => !t.completed).length;
        if (completedTasks) completedTasks.textContent = this.tasks.filter(t => t.completed).length;
    }

    updateStats() {
        const problemCount = document.getElementById('problem-count');
        const contestCount = document.getElementById('contest-count');
        const languageCount = document.getElementById('language-count');

        if (problemCount) {
            this.animateCounter(problemCount, this.problems.length);
        }

        if (contestCount) {
            this.animateCounter(contestCount, 6); // Total contests
        }

        if (languageCount) {
            const languages = [...new Set(this.problems.map(p => p.language))];
            this.animateCounter(languageCount, languages.length);
        }
    }

    animateCounter(element, target) {
        let current = 0;
        const increment = target / 30; // Animate over 30 frames
        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }
            element.textContent = Math.floor(current);
        }, 50);
    }
}

// Initialize the application
const smartInterviews = new SmartInterviews();

// Make functions available globally for inline event handlers
window.smartInterviews = smartInterviews;

// Add some additional utility functions
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM fully loaded');
    
    // Add smooth scrolling for any anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add loading states for buttons
    document.querySelectorAll('button').forEach(button => {
        button.addEventListener('click', function() {
            if (!this.disabled) {
                this.style.opacity = '0.8';
                setTimeout(() => {
                    this.style.opacity = '1';
                }, 200);
            }
        });
    });
});

// Service Worker registration for offline functionality (optional)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        // You can add service worker registration here if needed
        console.log('Service Worker support detected');
    });
}

// Error handling
window.addEventListener('error', function(e) {
    console.error('JavaScript error:', e.error);
});

window.addEventListener('unhandledrejection', function(e) {
    console.error('Unhandled promise rejection:', e.reason);
});

console.log('Smart Interviews script loaded successfully!');