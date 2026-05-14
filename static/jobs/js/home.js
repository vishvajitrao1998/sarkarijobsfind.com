const categories = [
    { icon: "🏛️", name: "Central Govt", count: "3,200+", color: "#3b82f6" },
    { icon: "🏢", name: "State Govt", count: "4,100+", color: "#8b5cf6" },
    { icon: "🏦", name: "Banking", count: "1,800+", color: "#10b981" },
    { icon: "🚂", name: "Railway", count: "2,400+", color: "#ef4444" },
    { icon: "🛡️", name: "Defence", count: "1,600+", color: "#f59e0b" },
    { icon: "📚", name: "Teaching", count: "900+", color: "#ec4899" },
    { icon: "⚕️", name: "Medical", count: "700+", color: "#14b8a6" },
    { icon: "💻", name: "IT / Tech", count: "500+", color: "#6366f1" },
    { icon: "⚖️", name: "Judiciary", count: "350+", color: "#a855f7" },
    { icon: "🔬", name: "Research", count: "420+", color: "#0ea5e9" },
    { icon: "🏗️", name: "Engineering", count: "1,100+", color: "#f97316" },
    { icon: "📊", name: "SSC / UPSC", count: "2,800+", color: "#dc2626" }
];

const listingsData = {
    latest: [
        { id: 1, title: "UPSC Civil Services 2025", org: "Union Public Service Commission", date: "15 Jul 2025", badge: "new", vacancies: "1,000+", description: "The Union Public Service Commission invites online applications from Indian citizens for the Civil Services Examination 2025.", eligibility: "Bachelor's degree from any recognized university", qualifications: "General Knowledge, English, Mathematics", selectionProcess: "Prelims → Mains → Interview", examPattern: "2 Papers (300 marks each)", howToApply: "Apply online at www.upsc.gov.in", orgInfo: "UPSC conducts the Civil Services Examination annually.", links: [{ icon: "📋", name: "Official Notification", desc: "Download PDF", url: "#" }, { icon: "🌐", name: "Official Website", desc: "Visit UPSC", url: "#" }, { icon: "📥", name: "Download Syllabus", desc: "Get PDF", url: "#" }, { icon: "💡", name: "Preparation Tips", desc: "Read Guide", url: "#" }, { icon: "📝", name: "Previous Papers", desc: "Download", url: "#" }] },
        { id: 2, title: "SSC CGL Tier-I 2025", org: "Staff Selection Commission", date: "20 Jul 2025", badge: "hot", vacancies: "8,000+", description: "Staff Selection Commission invites applications for Combined Graduate Level Examination 2025.", eligibility: "12th Pass or equivalent", qualifications: "General Awareness, Reasoning, Quantitative Aptitude, English", selectionProcess: "Tier-I → Tier-II → Tier-III → Interview", examPattern: "Computer-based Test", howToApply: "Apply online at www.ssc.nic.in", orgInfo: "SSC conducts various recruitment examinations for government positions.", links: [{ icon: "📋", name: "Official Notification", desc: "Download PDF", url: "#" }, { icon: "🌐", name: "Official Website", desc: "Visit SSC", url: "#" }, { icon: "📥", name: "Download Syllabus", desc: "Get PDF", url: "#" }, { icon: "💡", name: "Preparation Tips", desc: "Read Guide", url: "#" }, { icon: "🎫", name: "Admit Card", desc: "Download", url: "#" }] },
        { id: 3, title: "RBI Grade B Officer", org: "Reserve Bank of India", date: "10 Jul 2025", badge: "new", vacancies: "300+", description: "RBI invites applications for Grade B Officer posts in various departments.", eligibility: "Bachelor's degree with 60% marks", qualifications: "Economics, Finance, Management", selectionProcess: "Preliminary → Mains → Interview", examPattern: "Paper-based examination", howToApply: "Apply online at www.rbi.org.in", orgInfo: "RBI is the central banking institution of India.", links: [{ icon: "📋", name: "Official Notification", desc: "Download PDF", url: "#" }, { icon: "🌐", name: "Official Website", desc: "Visit RBI", url: "#" }, { icon: "📥", name: "Download Syllabus", desc: "Get PDF", url: "#" }, { icon: "💡", name: "Preparation Tips", desc: "Read Guide", url: "#" }] },
    ],
    results: [
        { id: 4, title: "RRB NTPC Final Result 2025", org: "Railway Recruitment Board", date: "05 Jul 2025", badge: "new", links: [] },
        { id: 5, title: "SSC CHSL Tier-II Result", org: "Staff Selection Commission", date: "01 Jul 2025", badge: "hot", links: [] },
    ],
    admit: [
        { id: 6, title: "SSC MTS 2025 Admit Card", org: "Staff Selection Commission", date: "18 Jul 2025", badge: "hot", links: [] },
    ],
    answer: [
        { id: 7, title: "SSC CGL 2024 Answer Key", org: "SSC", date: "08 Jul 2025", badge: "update", links: [] },
    ],
    syllabus: [
        { id: 8, title: "SSC CGL 2025 Syllabus & Pattern", org: "Staff Selection Commission", date: "Updated", badge: "update", links: [] },
    ]
};

// Render categories
const catGrid = document.getElementById('categoriesGrid');
categories.forEach((cat, i) => {
    const div = document.createElement('div');
    div.className = 'col-6 col-sm-4 col-lg-3';
    div.innerHTML = `
        <div class="glass-card p-3 d-flex align-items-center gap-3 cursor-pointer" style="animation-delay: ${0.05 * i}s;">
          <div class="category-icon" style="background: ${cat.color}20; color: ${cat.color}; font-size: 24px;">${cat.icon}</div>
          <div>
            <div style="font-weight: 600; font-size: 14px;">${cat.name}</div>
            <div style="font-size: 12px; color: var(--text-secondary);">${cat.count} Jobs</div>
          </div>
        </div>
      `;
    catGrid.appendChild(div);
});

// Render listings
let activeTab = 'latest';
function renderListings(tab) {
    const container = document.getElementById('listingsContainer');
    container.innerHTML = '';
    const items = listingsData[tab] || [];
    items.forEach((item, i) => {
        const badgeClass = item.badge === 'new' ? 'badge-new' : item.badge === 'hot' ? 'badge-hot' : 'badge-update';
        const badgeText = item.badge.toUpperCase();
        const div = document.createElement('div');
        div.className = 'col-12 col-md-6';
        div.innerHTML = `
          <div class="glass-card p-4 cursor-pointer" style="animation-delay: ${0.05 * i}s; cursor: pointer;" onclick="viewJobDetails(${item.id})">
            <div class="d-flex align-items-start justify-content-between mb-2">
              <h6 style="font-weight: bold; font-size: 14px; margin: 0; font-family: 'Plus Jakarta Sans', sans-serif;">${item.title}</h6>
              <span class="${badgeClass}">${badgeText}</span>
            </div>
            <p style="font-size: 12px; margin: 0 0 12px 0; color: var(--text-secondary);">${item.org}</p>
            <div class="d-flex align-items-center justify-content-between">
              <div class="d-flex align-items-center gap-1" style="font-size: 12px; color: var(--text-secondary);">
                <i data-lucide="calendar" style="width: 12px; height: 12px;"></i> ${item.date}
              </div>
              ${item.vacancies ? `<div style="font-size: 12px; font-weight: 600; color: var(--accent);">Vacancies: ${item.vacancies}</div>` : `<div style="font-size: 12px; font-weight: 600; color: var(--accent);">View Details →</div>`}
            </div>
          </div>
        `;
        container.appendChild(div);
    });
    lucide.createIcons();
}
renderListings('latest');

// Tab switching
const tabBar = document.getElementById('tabBar');
['latest', 'results', 'admit', 'answer', 'syllabus'].forEach((tab, i) => {
    const icons = ['🔥', '📋', '🎫', '📝', '📚'];
    const labels = ['Latest Jobs', 'Results', 'Admit Card', 'Answer Key', 'Syllabus'];
    const btn = document.createElement('button');
    btn.className = `tab-btn ${i === 0 ? 'active' : ''}`;
    btn.setAttribute('data-tab', tab);
    btn.textContent = `${icons[i]} ${labels[i]}`;
    btn.addEventListener('click', (e) => {
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeTab = tab;
        renderListings(activeTab);
    });
    tabBar.appendChild(btn);
});

// Important links
const linksContainer = document.getElementById('importantLinks');
const importantLinksData = [
    { icon: "📝", title: "Online Form", desc: "Apply for latest government jobs", color: "#3b82f6" },
    { icon: "📋", title: "Latest Result", desc: "Check exam results instantly", color: "#10b981" },
    { icon: "🎫", title: "Admit Card", desc: "Download hall tickets", color: "#f59e0b" },
    { icon: "📚", title: "Exam Syllabus", desc: "Complete syllabus & patterns", color: "#8b5cf6" },
    { icon: "📰", title: "Notifications", desc: "Official job notifications", color: "#ef4444" },
    { icon: "💡", title: "Preparation Tips", desc: "Strategy & study material", color: "#ec4899" },
];
importantLinksData.forEach((link, i) => {
    const div = document.createElement('div');
    div.className = 'col-12 col-sm-6 col-lg-4';
    div.innerHTML = `
        <div class="glass-card p-3 d-flex align-items-center gap-3 cursor-pointer" style="animation-delay: ${0.05 * i}s;">
          <div class="category-icon" style="background: ${link.color}20; font-size: 24px;">${link.icon}</div>
          <div>
            <div style="font-weight: 600; font-size: 14px;">${link.title}</div>
            <div style="font-size: 12px; color: var(--text-secondary);">${link.desc}</div>
          </div>
        </div>
      `;
    linksContainer.appendChild(div);
});

// // View Job Details
// function viewJobDetails(jobId) {
//     const job = Object.values(listingsData).flat().find(j => j.id === jobId);
//     if (!job) return;

//     document.getElementById('homePage').classList.remove('page-visible');
//     document.getElementById('homePage').classList.add('page-hidden');
//     document.getElementById('jobDetailsPage').classList.remove('page-hidden');
//     document.getElementById('jobDetailsPage').classList.add('page-visible');
//     document.getElementById('app-root').scrollTop = 0;

//     // Populate job details
//     document.getElementById('jobTitle').textContent = job.title;
//     document.getElementById('jobOrg').textContent = job.org;
//     document.getElementById('jobBreadcrumb').textContent = job.title;
//     document.getElementById('postedDate').textContent = job.date;
//     document.getElementById('vacancies').textContent = job.vacancies || 'N/A';

//     const badgeClass = job.badge === 'new' ? 'badge-new' : job.badge === 'hot' ? 'badge-hot' : 'badge-update';
//     document.getElementById('jobBadge').className = badgeClass;
//     document.getElementById('jobBadge').textContent = job.badge.toUpperCase();

//     document.getElementById('jobDescription').textContent = job.description || 'Job description not available.';

//     // Important Dates
//     const datesHTML = `
//         <div class="requirement-item"><strong>Application Start Date:</strong> ${job.date}</div>
//         <div class="requirement-item"><strong>Application End Date:</strong> ${new Date(Date.now() + 30 * 24 * 60 * 60 * 1000).toLocaleDateString()}</div>
//         <div class="requirement-item"><strong>Exam Date:</strong> ${new Date(Date.now() + 60 * 24 * 60 * 60 * 1000).toLocaleDateString()}</div>
//         <div class="requirement-item"><strong>Result Date:</strong> ${new Date(Date.now() + 90 * 24 * 60 * 60 * 1000).toLocaleDateString()}</div>
//       `;
//     document.getElementById('importantDates').innerHTML = datesHTML;
//     document.getElementById('keyDatesSidebar').innerHTML = datesHTML;

//     document.getElementById('eligibility').innerHTML = `<div class="requirement-item">${job.eligibility || 'Bachelor\'s degree or equivalent'}</div><div class="requirement-item">Age: 18-35 years (relaxation applicable)</div>`;
//     document.getElementById('qualifications').innerHTML = `<div class="requirement-item">${job.qualifications || 'Subject specific qualifications required'}</div>`;
//     document.getElementById('selectionProcess').innerHTML = `<div class="requirement-item">${job.selectionProcess || 'Written Exam → Interview → Document Verification'}</div>`;
//     document.getElementById('examPattern').innerHTML = `<div class="requirement-item">${job.examPattern || 'Computer-based or Paper-based examination'}</div>`;
//     document.getElementById('howToApply').innerHTML = `<div class="requirement-item">${job.howToApply || 'Apply online through official website'}</div>`;
//     document.getElementById('orgInfo').textContent = job.orgInfo || `${job.org} is a prestigious government organization.`;

//     // Populate Important Links Table
//     const linksTableHTML = (job.links || []).map(link => `
//         <tr class="links-table-row">
//           <td style="width: 40px;">
//             <span class="link-icon">${link.icon}</span>
//           </td>
//           <td>
//             <div class="link-name">${link.name}</div>
//             <div class="link-desc">${link.desc}</div>
//           </td>
//           <td class="link-action">
//             <button class="link-btn" onclick="window.open('${link.url}', '_blank')">Open</button>
//           </td>
//         </tr>
//       `).join('');
//     document.getElementById('importantLinksTable').innerHTML = linksTableHTML || '<tr><td colspan="3" style="text-align: center; padding: 16px; color: var(--text-secondary);">No important links available</td></tr>';

//     lucide.createIcons();
// }

function goToHome() {
    document.getElementById('jobDetailsPage').classList.remove('page-visible');
    document.getElementById('jobDetailsPage').classList.add('page-hidden');
    document.getElementById('homePage').classList.remove('page-hidden');
    document.getElementById('homePage').classList.add('page-visible');
    document.getElementById('app-root').scrollTop = 0;
}

// Search filter
document.getElementById('searchInput').addEventListener('input', function () {
    const q = this.value.toLowerCase();
    if (!q) { renderListings(activeTab); return; }
    const container = document.getElementById('listingsContainer');
    container.innerHTML = '';
    const allItems = Object.values(listingsData).flat().filter(item =>
        item.title.toLowerCase().includes(q) || item.org.toLowerCase().includes(q)
    );
    allItems.forEach((item, i) => {
        const badgeClass = item.badge === 'new' ? 'badge-new' : item.badge === 'hot' ? 'badge-hot' : 'badge-update';
        const div = document.createElement('div');
        div.className = 'col-12 col-md-6';
        div.innerHTML = `
          <div class="glass-card p-4 cursor-pointer" style="animation-delay: ${0.05 * i}s;" onclick="viewJobDetails(${item.id})">
            <div class="d-flex align-items-start justify-content-between mb-2">
              <h6 style="font-weight: bold; font-size: 14px; margin: 0; font-family: 'Plus Jakarta Sans', sans-serif;">${item.title}</h6>
              <span class="${badgeClass}">${item.badge.toUpperCase()}</span>
            </div>
            <p style="font-size: 12px; margin: 0 0 12px 0; color: var(--text-secondary);">${item.org}</p>
            <div class="d-flex align-items-center justify-content-between">
              <div class="d-flex align-items-center gap-1" style="font-size: 12px; color: var(--text-secondary);">
                <i data-lucide="calendar" style="width: 12px; height: 12px;"></i> ${item.date}
              </div>
              <div style="font-size: 12px; font-weight: 600; color: var(--accent);">View Details →</div>
            </div>
          </div>
        `;
        container.appendChild(div);
    });
    lucide.createIcons();
});

// Element SDK
const defaultConfig = {
    site_title: 'SarkariJobsHub',
    hero_heading: 'Find Your Dream Sarkari Job',
    hero_subtext: 'Get instant updates on government job vacancies, exam results, admit cards, and answer keys — all in one place.',
};

function applyConfig(config) {
    const c = { ...defaultConfig, ...config };
    document.getElementById('nav-title').textContent = c.site_title;
    const heroH = document.getElementById('hero-heading');
    heroH.innerHTML = c.hero_heading.replace(/(Sarkari Job)/i, '<span style="color: #fbbf24;">$1</span>');
    document.getElementById('hero-subtext').textContent = c.hero_subtext;
}

lucide.createIcons();