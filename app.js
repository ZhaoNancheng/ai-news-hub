// ===== 数据存储 =====
let newsData = [];
let currentPage = 1;
let itemsPerPage = 9;
let currentFilter = 'all';

// ===== 示例新闻数据 =====
const sampleNews = [
    {
        id: 1,
        title: "OpenAI 发布 GPT-5：推理能力大幅提升",
        excerpt: "OpenAI 正式发布 GPT-5，新模型在复杂推理、数学计算和多语言理解方面取得重大突破...",
        category: "breaking",
        source: "OpenAI Blog",
        sourceUrl: "https://openai.com",
        date: "2026-02-04",
        readTime: "5 分钟",
        image: "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&h=400&fit=crop"
    },
    {
        id: 2,
        title: "Google DeepMind 新模型 AlphaGeometry 3 解决数学难题",
        excerpt: "DeepMind 发布 AlphaGeometry 3，在国际数学奥林匹克竞赛级别的几何问题上达到人类专家水平...",
        category: "research",
        source: "Google AI Blog",
        sourceUrl: "https://blog.google/technology/ai",
        date: "2026-02-04",
        readTime: "7 分钟",
        image: "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?w=600&h=400&fit=crop"
    },
    {
        id: 3,
        title: "Anthropic 获得 20 亿美元融资",
        excerpt: "AI 安全公司 Anthropic 宣布完成新一轮融资，估值达到 400 亿美元，用于扩展 Claude AI 能力...",
        category: "industry",
        source: "TechCrunch",
        sourceUrl: "https://techcrunch.com",
        date: "2026-02-04",
        readTime: "4 分钟",
        image: "https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=600&h=400&fit=crop"
    },
    {
        id: 4,
        title: "Cursor AI 编辑器更新：智能代码重构功能",
        excerpt: "流行的 AI 代码编辑器 Cursor 发布重大更新，新增智能代码重构、自动化测试生成等功能...",
        category: "tools",
        source: "Cursor Blog",
        sourceUrl: "https://cursor.sh",
        date: "2026-02-03",
        readTime: "6 分钟",
        image: "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&h=400&fit=crop"
    },
    {
        id: 5,
        title: "斯坦福研究：多模态 AI 在医疗诊断中的应用",
        excerpt: "斯坦福大学发布最新研究，展示多模态 AI 模型在早期疾病筛查方面的突破性进展...",
        category: "research",
        source: "Stanford AI",
        sourceUrl: "https://ai.stanford.edu",
        date: "2026-02-03",
        readTime: "8 分钟",
        image: "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=600&h=400&fit=crop"
    },
    {
        id: 6,
        title: "微软推出 Copilot Pro：面向开发者的 AI 助手",
        excerpt: "微软发布 Copilot Pro 订阅服务，为开发者提供更强大的 AI 辅助编程功能...",
        category: "industry",
        source: "Microsoft Blog",
        sourceUrl: "https://blogs.microsoft.com",
        date: "2026-02-03",
        readTime: "5 分钟",
        image: "https://images.unsplash.com/photo-1633419461186-7d40a38105ec?w=600&h=400&fit=crop"
    },
    {
        id: 7,
        title: "Hugging Face 推出开源模型评估平台",
        excerpt: "Hugging Face 发布全新模型评估平台，提供标准化基准测试和性能对比工具...",
        category: "tools",
        source: "Hugging Face",
        sourceUrl: "https://huggingface.co",
        date: "2026-02-02",
        readTime: "4 分钟",
        image: "https://images.unsplash.com/photo-1617791160505-6f00504e3519?w=600&h=400&fit=crop"
    },
    {
        id: 8,
        title: "OpenAI o3 模型在编程竞赛中夺冠",
        excerpt: "OpenAI 的 o3 模型在 Codeforces 编程竞赛中达到特级大师水平，创历史新高...",
        category: "breaking",
        source: "OpenAI",
        sourceUrl: "https://openai.com",
        date: "2026-02-02",
        readTime: "6 分钟",
        image: "https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=600&h=400&fit=crop"
    },
    {
        id: 9,
        title: "Meta 发布 Llama 4：开源大语言模型新里程碑",
        excerpt: "Meta 发布 Llama 4 系列模型，性能接近顶级闭源模型，完全开源供研究和商业使用...",
        category: "industry",
        source: "Meta AI",
        sourceUrl: "https://ai.meta.com",
        date: "2026-02-01",
        readTime: "7 分钟",
        image: "https://images.unsplash.com/photo-1677433118515-7466d3a5c1f1?w=600&h=400&fit=crop"
    }
];

// ===== 初始化应用 =====
function initApp() {
    // 加载新闻数据
    newsData = [...sampleNews];

    // 更新日期显示
    updateDateDisplay();

    // 更新统计数据
    updateStats();

    // 渲染新闻
    renderNews();

    // 设置事件监听器
    setupEventListeners();
}

// ===== 更新日期显示 =====
function updateDateDisplay() {
    const now = new Date();
    const options = { year: 'numeric', month: 'long', day: 'numeric', weekday: 'long' };
    const dateString = now.toLocaleDateString('zh-CN', options);
    const timeString = now.toLocaleTimeString('zh-CN', { hour: '2-digit', minute: '2-digit' });

    document.getElementById('current-date').textContent = dateString;
    document.getElementById('update-time').textContent = timeString;
}

// ===== 更新统计数据 =====
function updateStats() {
    // 动画效果
    animateNumber('total-news', newsData.length);
    animateNumber('total-sources', 18); // 更新为18个信息源
}

// ===== 数字动画 =====
function animateNumber(elementId, target) {
    const element = document.getElementById(elementId);
    let current = 0;
    const increment = target / 20;
    const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
            current = target;
            clearInterval(timer);
        }
        element.textContent = Math.floor(current);
    }, 50);
}

// ===== 渲染新闻 =====
function renderNews() {
    const container = document.getElementById('news-container');
    const filteredNews = currentFilter === 'all'
        ? newsData
        : newsData.filter(news => news.category === currentFilter);

    const paginatedNews = filteredNews.slice(0, currentPage * itemsPerPage);

    container.innerHTML = paginatedNews.map(news => createNewsCard(news)).join('');

    // 隐藏加载更多按钮（如果没有更多数据）
    const loadMoreBtn = document.getElementById('load-more-btn');
    loadMoreBtn.style.display = paginatedNews.length >= filteredNews.length ? 'none' : 'block';
}

// ===== 创建新闻卡片 =====
function createNewsCard(news) {
    const categoryLabels = {
        breaking: '突发',
        research: '研究',
        industry: '产业',
        tools: '工具'
    };

    return `
        <article class="news-card" data-id="${news.id}">
            <div class="news-card-image-wrapper">
                <img
                    src="${news.image}"
                    alt="${news.title}"
                    class="news-card-image"
                    loading="lazy"
                    onerror="this.src='https://via.placeholder.com/600x400/1e293b/64748b?text=AI+News'"
                >
            </div>
            <div class="news-card-content">
                <div class="news-card-tags">
                    <span class="tag ${news.category}">${categoryLabels[news.category]}</span>
                </div>
                <h3 class="news-card-title">
                    <a href="${news.sourceUrl}" target="_blank" rel="noopener noreferrer">
                        ${news.title}
                    </a>
                </h3>
                <p class="news-card-excerpt">${news.excerpt}</p>
                <div class="news-card-meta">
                    <div class="news-card-source">
                        <div class="source-icon"></div>
                        <span>${news.source}</span>
                    </div>
                    <div class="news-card-date">
                        <span>📅 ${news.date}</span>
                        <span>⏱️ ${news.readTime}</span>
                    </div>
                </div>
            </div>
        </article>
    `;
}

// ===== 设置事件监听器 =====
function setupEventListeners() {
    // 筛选按钮
    const filterButtons = document.querySelectorAll('.filter-btn');
    filterButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            filterButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            currentFilter = btn.dataset.filter;
            currentPage = 1;
            renderNews();
        });
    });

    // 加载更多按钮
    document.getElementById('load-more-btn').addEventListener('click', () => {
        currentPage++;
        renderNews();
    });

    // 移动端导航切换
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');

    navToggle.addEventListener('click', () => {
        navMenu.classList.toggle('active');
    });

    // 平滑滚动
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // 回到顶部按钮
    const backToTopBtn = document.getElementById('back-to-top');

    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            backToTopBtn.classList.add('visible');
        } else {
            backToTopBtn.classList.remove('visible');
        }
    });

    backToTopBtn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}

// ===== 页面加载完成后初始化 =====
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initApp);
} else {
    initApp();
}

// ===== 服务工作者注册（可选，用于离线支持）=====
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        // navigator.serviceWorker.register('/sw.js')
        //     .then(registration => console.log('SW registered'))
        //     .catch(error => console.log('SW registration failed'));
    });
}
