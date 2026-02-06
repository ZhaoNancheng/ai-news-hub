---
layout: home

hero:
  name: AI News Hub
  text: Latest Updates on AI Tools & Technology
  tagline: 每日聚合全球 AI 新闻、论文和工具，保持知识前沿
  image:
    src: /favicon.svg
    alt: AI News Hub
  actions:
    - theme: brand
      text: 开始浏览
      link: /latest-news
    - theme: alt
      text: GitHub
      link: https://github.com/ZhaoNancheng/ai-news-hub

features:
  - icon: 📰
    title: 每日新闻
    details: 每天 08:00 自动获取最新 AI 新闻、行业动态和产品更新
    link: /latest-news
    linkText: 查看新闻 →
  - icon: 🔬
    title: 研究前沿
    details: 追踪 AI Agent、多智能体系统、世界模型等前沿研究
    link: /research
    linkText: 深入研究 →
  - icon: 🔥
    title: 热门推荐
    details: 发现当前 AI 领域最热门的研究方向和讨论话题
    link: /trending
    linkText: 查看热门 →
---

<style>
.home-cards-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 2rem;
  margin: 4rem auto;
  max-width: 1200px;
  padding: 0 2rem;
}

.home-card {
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-border);
  border-radius: 16px;
  padding: 2rem;
  transition: all 0.3s ease;
  display: block;
  text-decoration: none;
  color: inherit;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.home-card:hover {
  border-color: var(--vp-c-brand-1);
  box-shadow: 0 12px 24px rgba(60, 135, 114, 0.15);
  transform: translateY(-8px);
}

.home-card-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.home-card-icon {
  font-size: 2.5rem;
  line-height: 1;
}

.home-card-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--vp-c-text-1);
  flex: 1;
}

.home-card-content {
  color: var(--vp-c-text-2);
  line-height: 1.8;
  margin-bottom: 1.5rem;
  font-size: 1rem;
}

.home-card-list {
  list-style: none;
  padding: 0;
  margin: 1.5rem 0;
}

.home-card-list li {
  padding: 0.75rem 0;
  padding-left: 2rem;
  position: relative;
  color: var(--vp-c-text-2);
  font-size: 1rem;
  line-height: 1.7;
  border-bottom: 1px solid var(--vp-c-divider-light);
}

.home-card-list li:last-child {
  border-bottom: none;
}

.home-card-list li::before {
  content: "▸";
  position: absolute;
  left: 0;
  color: var(--vp-c-brand-1);
  font-weight: 700;
  font-size: 1.25rem;
}

.home-card-link {
  display: inline-block;
  color: white;
  font-weight: 600;
  font-size: 1rem;
  margin-top: 1rem;
  padding: 0.875rem 2rem;
  background: var(--vp-c-brand-1);
  border-radius: 8px;
  transition: all 0.3s ease;
  text-align: center;
}

.home-card:hover .home-card-link {
  background: var(--vp-c-brand-2);
}

@media (max-width: 768px) {
  .home-cards-container {
    grid-template-columns: 1fr;
    padding: 0 1rem;
    gap: 1.5rem;
  }

  .home-card {
    padding: 1.5rem;
  }
}
</style>

<div class="home-cards-container">
  <a href="/latest-news" class="home-card">
    <div class="home-card-header">
      <div class="home-card-icon">📰</div>
      <div class="home-card-title">最新动态</div>
    </div>
    <div class="home-card-content">
      今日新闻 (2026-02-06)
    </div>
    <ul class="home-card-list">
      <li>🔥 OpenAI 发布 GPT-5.3 Codex，性能提升 25%</li>
      <li>🤖 Anthropic 推出 Claude Opus 4.6，竞争白热化</li>
      <li>💰 亚马逊宣布 2000 亿美元 AI 投资计划</li>
      <li>🏥 蚂蚁"阿福"健康助手日处理 1000 万问询</li>
    </ul>
    <div class="home-card-link">查看完整新闻 →</div>
  </a>

  <a href="/research" class="home-card">
    <div class="home-card-header">
      <div class="home-card-icon">🔬</div>
      <div class="home-card-title">研究前沿</div>
    </div>
    <div class="home-card-content">
      最新研究方向
    </div>
    <ul class="home-card-list">
      <li>Agentic Coding - AI 编程助手成为竞争焦点</li>
      <li>多智能体系统 - 2 个多样化智能体 > 16 个同质智能体</li>
      <li>世界模型 - 医疗、游戏等领域的长视界模拟突破</li>
      <li>垂直领域模型 - 专业化 AI 模型商业潜力凸显</li>
    </ul>
    <div class="home-card-link">深入了解 →</div>
  </a>

  <a href="/trending" class="home-card">
    <div class="home-card-header">
      <div class="home-card-icon">🔥</div>
      <div class="home-card-title">热门话题</div>
    </div>
    <div class="home-card-content">
      当前趋势 (2026年2月)
    </div>
    <ul class="home-card-list">
      <li>编程工具竞争 - OpenAI vs Anthropic</li>
      <li>基础设施投资 - 全球数千亿美元投入</li>
      <li>垂直模型崛起 - 医疗、法律、金融等专业化模型</li>
      <li>AI 治理 - 联合国成立专家组推进安全治理</li>
    </ul>
    <div class="home-card-link">查看热门推荐 →</div>
  </a>
</div>

---

<style>
.featured-section {
  background: linear-gradient(135deg, rgba(60, 135, 114, 0.08), rgba(45, 105, 88, 0.08));
  border-radius: 20px;
  padding: 4rem 3rem;
  margin: 5rem 2rem;
  text-align: center;
}

.featured-title {
  font-size: 2.25rem;
  font-weight: 700;
  margin-bottom: 1rem;
  color: var(--vp-c-text-1);
}

.featured-subtitle {
  font-size: 1.125rem;
  color: var(--vp-c-text-2);
  margin-bottom: 3rem;
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
  line-height: 1.8;
}

.featured-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 2rem;
  margin: 3rem 0;
}

.featured-stat {
  padding: 1.5rem;
}

.stat-number {
  font-size: 3rem;
  font-weight: 700;
  background: linear-gradient(135deg, var(--vp-c-brand-1), var(--vp-c-brand-2));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 0.5rem;
}

.stat-label {
  color: var(--vp-c-text-2);
  font-size: 1rem;
  font-weight: 500;
}

@media (max-width: 768px) {
  .featured-section {
    padding: 3rem 2rem;
    margin: 3rem 1rem;
  }

  .featured-title {
    font-size: 1.75rem;
  }

  .stat-number {
    font-size: 2.5rem;
  }
}
</style>

<div class="featured-section">
  <div class="featured-title">探索 AI 的无限可能</div>
  <div class="featured-subtitle">
    保持对最新 AI 发展的敏锐洞察，从学术论文到行业动态，
    我们帮您追踪人工智能领域的每一个重要突破。
  </div>
  
  <div class="featured-stats">
    <div class="featured-stat">
      <div class="stat-number">100+</div>
      <div class="stat-label">每日更新新闻</div>
    </div>
    <div class="featured-stat">
      <div class="stat-number">50+</div>
      <div class="stat-label">arXiv 论文</div>
    </div>
    <div class="featured-stat">
      <div class="stat-number">8+</div>
      <div class="stat-label">权威数据源</div>
    </div>
  </div>
</div>

---

<style>
.info-section {
  max-width: 900px;
  margin: 4rem auto;
  padding: 0 2rem;
}

.info-title {
  font-size: 2rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 3rem;
  color: var(--vp-c-text-1);
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
}

.info-item {
  padding: 2rem;
  background: var(--vp-c-bg-soft);
  border-radius: 12px;
  text-align: center;
}

.info-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
  display: block;
}

.info-item-title {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.75rem;
  color: var(--vp-c-text-1);
}

.info-item-content {
  color: var(--vp-c-text-2);
  line-height: 1.7;
  font-size: 0.9375rem;
}

@media (max-width: 768px) {
  .info-section {
    padding: 0 1rem;
  }

  .info-grid {
    grid-template-columns: 1fr;
  }
}
</style>

<div class="info-section">
  <div class="info-title">为什么选择 AI News Hub？</div>
  
  <div class="info-grid">
    <div class="info-item">
      <span class="info-icon">⚡</span>
      <div class="info-item-title">极速性能</div>
      <div class="info-item-content">
        基于 VitePress 静态生成，CDN 全球加速，毫秒级加载响应
      </div>
    </div>
    
    <div class="info-item">
      <span class="info-icon">🔄</span>
      <div class="info-item-title">自动化更新</div>
      <div class="info-item-content">
        每天 08:00 自动获取最新资讯，无需人工干预，保持知识前沿
      </div>
    </div>
    
    <div class="info-item">
      <span class="info-icon">📱</span>
      <div class="info-item-title">完美体验</div>
      <div class="info-item-content">
        响应式设计，支持所有设备，内置全文搜索，快速找到所需内容
      </div>
    </div>
  </div>
</div>

---

<style>
.data-sources {
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-border);
  border-radius: 16px;
  padding: 3rem 2rem;
  margin: 4rem auto;
  max-width: 1000px;
}

.data-sources-title {
  font-size: 1.75rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 2rem;
  color: var(--vp-c-text-1);
}

.data-sources-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}

.data-source-item {
  padding: 1rem;
  background: var(--vp-c-bg-soft);
  border-radius: 8px;
  text-align: center;
}

.data-source-name {
  font-weight: 600;
  margin-bottom: 0.25rem;
  color: var(--vp-c-text-1);
}

.data-source-desc {
  font-size: 0.875rem;
  color: var(--vp-c-text-2);
}
</style>

<div class="data-sources">
  <div class="data-sources-title">📊 数据来源</div>
  <div class="data-sources-list">
    <div class="data-source-item">
      <div class="data-source-name">📚 arXiv.org</div>
      <div class="data-source-desc">最新学术论文</div>
    </div>
    <div class="data-source-item">
      <div class="data-source-name">🌐 TechCrunch</div>
      <div class="data-source-desc">AI 行业新闻</div>
    </div>
    <div class="data-source-item">
      <div class="data-source-name">🔬 MIT Tech Review</div>
      <div class="data-source-desc">深度技术报道</div>
    </div>
    <div class="data-source-item">
      <div class="data-source-name">💼 The Verge</div>
      <div class="data-source-desc">产业动态</div>
    </div>
    <div class="data-source-item">
      <div class="data-source-name">🏢 公司博客</div>
      <div class="data-source-desc">OpenAI、Google、Anthropic</div>
    </div>
    <div class="data-source-item">
      <div class="data-source-name">📈 Gartner</div>
      <div class="data-source-desc">市场研究数据</div>
    </div>
  </div>
</div>

---

**最后更新:** 2026-02-06 | **下次更新:** 2026-02-07 08:00

Made with ❤️ using [VitePress](https://vitepress.dev) + [OpenClaw](https://docs.openclaw.ai)
