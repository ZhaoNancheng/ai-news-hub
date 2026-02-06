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

<CountdownTimer />

<FeatureCards />

<LatestUpdates />

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
