---
layout: home

hero:
  name: AI News Hub
  text: 探索 AI 世界的最新动态
  tagline: 每日聚合全球 AI 新闻、论文和工具
  image:
    src: /favicon.svg
    alt: AI News Hub
  actions:
    - theme: brand
      text: 开始浏览
      link: /latest-news
    - theme: alt
      text: 查看源码
      link: https://github.com/ZhaoNancheng/ai-news-hub

features:
  - icon: 📰
    title: 每日新闻
    details: 每天 08:00 自动获取最新 AI 新闻、行业动态和产品更新
    link: /latest-news
    linkText: 查看新闻
  - icon: 🔬
    title: 研究前沿
    details: 追踪 AI Agent、多智能体系统、世界模型等前沿研究
    link: /research
    linkText: 深入研究
  - icon: 🔥
    title: 热门推荐
    details: 发现当前 AI 领域最热门的研究方向和讨论话题
    link: /trending
    linkText: 查看热门
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
  box-shadow: var(--vp-shadow-1);
}

.home-card:hover {
  border-color: var(--vp-c-brand-1);
  box-shadow: var(--vp-shadow-3);
  transform: translateY(-6px);
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
  color: var(--vp-c-brand-1);
  font-weight: 600;
  font-size: 1rem;
  margin-top: 1rem;
  padding: 0.75rem 1.5rem;
  background: var(--vp-c-brand-1);
  color: white !important;
  border-radius: 8px;
  transition: all 0.3s ease;
}

.home-card:hover .home-card-link {
  background: var(--vp-c-brand-2);
  transform: translateX(4px);
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

## 🎯 为什么选择 AI News Hub？

### ⚡ 极速性能

基于 VitePress 静态生成，CDN 全球加速，毫秒级加载响应。

### 🔄 自动化更新

每天 08:00 自动获取最新资讯，无需人工干预。

### 📱 完美体验

响应式设计，支持所有设备，内置全文搜索。

---

## 📊 数据来源

我们整合了多个权威数据源，为您提供最全面的 AI 资讯：

- **arXiv.org** - 最新学术论文
- **TechCrunch** - AI 行业新闻
- **The Verge** - 深度科技报道
- **MIT Technology Review** - 前沿技术分析
- **21世纪经济报道** - 中国 AI 动态
- **Gartner** - 市场研究数据
- **公司博客** - OpenAI、Google、Anthropic

---

## 🚀 快速开始

1. **浏览新闻** - 查看最新的 AI 论文、行业动态和产品更新
2. **深入阅读** - 点击感兴趣的文章，查看详细摘要和原文链接
3. **订阅更新** - 每天 08:00 自动更新，保持知识前沿

[开始探索 →](/latest-news)

---

## 📞 联系我们

- [GitHub 仓库](https://github.com/ZhaoNancheng/ai-news-hub)
- [Vercel 访问](https://ai-news-hub-rosy.vercel.app/)
- [GitLab 访问](https://ai-news-hub-046491.gitlab.io/)

欢迎提 Issue 和 PR 反馈建议

---

**最后更新:** 2026-02-06 | **下次更新:** 2026-02-07 08:00

Made with ❤️ using [VitePress](https://vitepress.dev) + [OpenClaw](https://docs.openclaw.ai)
