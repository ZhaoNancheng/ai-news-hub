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
  - icon: 🤖
    title: 每日自动更新
    details: 每天早上 8 点自动获取最新 AI 新闻、arXiv 论文和行业动态
  - icon: 📚
    title: 学术论文追踪
    details: 聚焦 AI Agent、多智能体系统等前沿研究方向，精选重要论文
  - icon: 🌐
    title: 行业动态
    details: 实时追踪 OpenAI、Google、Anthropic 等顶级公司的最新动态
  - icon: 🛠️
    title: 工具与产品
    details: 发现最新的 AI 工具、框架和产品发布
  - icon: ⚡
    title: 极速加载
    details: 基于 VitePress 构建，静态生成，秒级加载体验
  - icon: 📱
    title: 完美适配
    details: 响应式设计，完美支持桌面、平板和手机

---

## 📊 今日数据

<style>
.stats-section {
  padding: 3rem 0;
  background: linear-gradient(135deg, rgba(37, 99, 235, 0.05), rgba(124, 58, 237, 0.05));
  border-radius: 16px;
  margin: 2rem 0;
}

.stats-title {
  text-align: center;
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 2rem;
  color: var(--vp-c-text-1);
}

.stats-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  max-width: 1000px;
  margin: 0 auto;
}

.stat-card {
  padding: 1.5rem;
  border-radius: 16px;
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-border);
  text-align: center;
  transition: all 0.3s ease;
  box-shadow: var(--vp-shadow-1);
}

.stat-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--vp-shadow-2);
  border-color: var(--vp-c-brand-1);
}

.stat-number {
  font-size: 2rem;
  font-weight: 700;
  background: linear-gradient(135deg, var(--vp-c-brand-1), var(--vp-c-brand-2));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 0.5rem;
  line-height: 1.2;
  word-break: break-all;
}

.stat-label {
  color: var(--vp-c-text-2);
  font-size: 0.875rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-top: 0.5rem;
}
</style>

<div class="stats-section">
  <div class="stats-title">📊 今日数据概览</div>
  <div class="stats-container">
    <div class="stat-card">
      <div class="stat-number">15+</div>
      <div class="stat-label">今日论文</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">5</div>
      <div class="stat-label">行业新闻</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">4</div>
      <div class="stat-label">产品更新</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">50+</div>
      <div class="stat-label">arXiv 论文</div>
    </div>
  </div>
</div>

---

## 🔥 热门话题

<style>
.section-title {
  text-align: center;
  font-size: 2rem;
  font-weight: 700;
  margin: 3rem 0 2rem;
  color: var(--vp-c-text-1);
}

.topic-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.topic-card {
  padding: 1.5rem;
  border-radius: 12px;
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-border);
  transition: all 0.3s ease;
}

.topic-card:hover {
  border-color: var(--vp-c-brand-1);
  transform: translateY(-2px);
  box-shadow: var(--vp-shadow-2);
}

.topic-title {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.75rem;
  color: var(--vp-c-text-1);
}

.topic-desc {
  color: var(--vp-c-text-2);
  font-size: 0.875rem;
  line-height: 1.6;
}

.topic-link {
  display: inline-block;
  margin-top: 1rem;
  color: var(--vp-c-brand-1);
  text-decoration: none;
  font-weight: 500;
}

.topic-link:hover {
  text-decoration: underline;
}
</style>

<div class="section-title">🔥 热门话题</div>

<div class="topic-grid">
  <div class="topic-card">
    <div class="topic-title">🔬 多智能体系统</div>
    <div class="topic-desc">最新研究显示 2 个多样化智能体的性能可以超过 16 个同质智能体，质量胜于数量。</div>
    <a href="/news/2026-02-05#understanding-agent-scaling" class="topic-link">了解更多 →</a>
  </div>
  <div class="topic-card">
    <div class="topic-title">⚡ 自动编排框架</div>
    <div class="topic-desc">AOrchestra 实现了 16.28% 的性能提升，通过自动化子智能体创建优化任务执行。</div>
    <a href="/news/2026-02-05#aorchestra" class="topic-link">了解更多 →</a>
  </div>
  <div class="topic-card">
    <div class="topic-title">💰 AGI 争议</div>
    <div class="topic-desc">Sam Altman 关于 "已构建 AGI" 的声明引发行业广泛讨论和争议。</div>
    <a href="/news/2026-02-05#agi-controversy" class="topic-link">了解更多 →</a>
  </div>
  <div class="topic-card">
    <div class="topic-title">🏥 医疗世界模型</div>
    <div class="topic-desc">EHRWorld 实现了长视界临床模拟的稳定性突破，优于朴素 LLM 基线。</div>
    <a href="/news/2026-02-05#ehreworld" class="topic-link">了解更多 →</a>
  </div>
</div>

---

## 📰 最新更新

<style>
.news-preview {
  background: var(--vp-c-bg);
  border-radius: 16px;
  padding: 2rem;
  margin: 2rem 0;
  border: 1px solid var(--vp-c-border);
}

.news-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
  flex-wrap: wrap;
  gap: 1rem;
}

.news-title {
  font-size: 1.75rem;
  font-weight: 700;
  color: var(--vp-c-text-1);
}

.news-date {
  color: var(--vp-c-text-2);
  font-size: 0.875rem;
  padding: 0.5rem 1rem;
  background: var(--vp-c-bg-soft);
  border-radius: 8px;
}

.news-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.news-item {
  padding: 1rem;
  border-radius: 8px;
  background: var(--vp-c-bg-soft);
  border-left: 3px solid var(--vp-c-brand-1);
  transition: all 0.3s ease;
}

.news-item:hover {
  transform: translateX(4px);
  box-shadow: var(--vp-shadow-1);
}

.news-item-title {
  font-weight: 600;
  margin-bottom: 0.25rem;
  color: var(--vp-c-text-1);
}

.news-item-meta {
  font-size: 0.75rem;
  color: var(--vp-c-text-2);
}

.news-cta {
  text-align: center;
  margin-top: 1.5rem;
}

.news-cta-btn {
  display: inline-block;
  padding: 0.875rem 2rem;
  background: var(--vp-c-brand-1);
  color: white !important;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s ease;
}

.news-cta-btn:hover {
  transform: translateY(-2px);
  box-shadow: var(--vp-shadow-2);
}
</style>

<div class="news-preview">
  <div class="news-header">
    <div class="news-title">📰 今日早报</div>
    <div class="news-date">2026-02-05</div>
  </div>
  <div class="news-list">
    <div class="news-item">
      <div class="news-item-title">🔬 15 篇 arXiv 论文发布</div>
      <div class="news-item-meta">AI Agent、多智能体系统、世界模型等前沿研究</div>
    </div>
    <div class="news-item">
      <div class="news-item-title">🌟 OpenAI 从 Anthropic 挖走安全高管</div>
      <div class="news-item-meta">AGI 准备度主管 Dylan Scandinaro 加入 OpenAI</div>
    </div>
    <div class="news-item">
      <div class="news-item-title">🚀 Anthropic 扩展 Cowork 插件功能</div>
      <div class="news-item-meta">支持销售、法律、金融等多领域专家模式</div>
    </div>
    <div class="news-item">
      <div class="news-item-title">💡 成本优化：EquiRouter 降低 17%</div>
      <div class="news-item-meta">解决路由器崩溃问题，优化模型选择策略</div>
    </div>
  </div>
  <div class="news-cta">
    <a href="/latest-news" class="news-cta-btn">查看完整日报 →</a>
  </div>
</div>

---

## 🎯 为什么选择 AI News Hub？

<style>
.feature-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin: 3rem 0;
}

.feature-box {
  padding: 2rem;
  border-radius: 16px;
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-border);
  transition: all 0.3s ease;
}

.feature-box:hover {
  border-color: var(--vp-c-brand-1);
  box-shadow: var(--vp-shadow-2);
}

.feature-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
  display: block;
}

.feature-box-title {
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: var(--vp-c-text-1);
}

.feature-box-desc {
  color: var(--vp-c-text-2);
  line-height: 1.8;
}

.feature-list {
  margin-top: 1rem;
  padding-left: 1.5rem;
}

.feature-list li {
  margin-bottom: 0.5rem;
  color: var(--vp-c-text-2);
}
</style>

<div class="section-title">🎯 为什么选择 AI News Hub？</div>

<div class="feature-grid">
  <div class="feature-box">
    <span class="feature-icon">⚡</span>
    <div class="feature-box-title">极速性能</div>
    <div class="feature-box-desc">
      基于 VitePress 静态生成，CDN 全球加速，毫秒级加载响应。
      <ul class="feature-list">
        <li>静态 HTML，无需服务器</li>
        <li>Vercel 边缘网络加速</li>
        <li>图片懒加载优化</li>
      </ul>
    </div>
  </div>
  <div class="feature-box">
    <span class="feature-icon">🔄</span>
    <div class="feature-box-title">自动化更新</div>
    <div class="feature-box-desc">
      每天 8:00 自动获取最新资讯，无需人工干预。
      <ul class="feature-list">
        <li>Cron 定时任务</li>
        <li>自动 Git 提交</li>
        <li>Vercel 自动部署</li>
      </ul>
    </div>
  </div>
  <div class="feature-box">
    <span class="feature-icon">📱</span>
    <div class="feature-box-title">完美体验</div>
    <div class="feature-box-desc">
      响应式设计，支持所有设备，内置全文搜索。
      <ul class="feature-list">
        <li>移动端完美适配</li>
        <li>深色模式自动切换</li>
        <li>本地搜索，即时结果</li>
      </ul>
    </div>
  </div>
</div>

---

## 📊 数据来源

<style>
.sources-section {
  background: var(--vp-c-bg-soft);
  border-radius: 16px;
  padding: 2rem;
  margin: 3rem 0;
}

.sources-title {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  text-align: center;
}

.sources-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
}

.source-item {
  padding: 1rem;
  background: var(--vp-c-bg);
  border-radius: 8px;
  border: 1px solid var(--vp-c-border);
}

.source-name {
  font-weight: 600;
  color: var(--vp-c-text-1);
  margin-bottom: 0.25rem;
}

.source-desc {
  font-size: 0.875rem;
  color: var(--vp-c-text-2);
}
</style>

<div class="sources-section">
  <div class="sources-title">📚 数据来源</div>
  <div class="sources-list">
    <div class="source-item">
      <div class="source-name">📚 arXiv.org</div>
      <div class="source-desc">最新学术论文</div>
    </div>
    <div class="source-item">
      <div class="source-name">🌐 The Verge</div>
      <div class="source-desc">AI 行业新闻</div>
    </div>
    <div class="source-item">
      <div class="source-name">🔬 MIT Technology Review</div>
      <div class="source-desc">深度技术报道</div>
    </div>
    <div class="source-item">
      <div class="source-name">💼 TechCrunch</div>
      <div class="source-desc">产业和投资动态</div>
    </div>
    <div class="source-item">
      <div class="source-name">🏢 公司博客</div>
      <div class="source-desc">OpenAI、Google、Anthropic</div>
    </div>
  </div>
</div>

---

## 🚀 快速开始

<style>
.steps-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin: 3rem 0;
}

.step-card {
  position: relative;
  padding: 1.5rem;
  padding-left: 4rem;
  border-radius: 12px;
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-border);
  transition: all 0.3s ease;
}

.step-card:hover {
  border-color: var(--vp-c-brand-1);
  transform: translateY(-2px);
}

.step-number {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  width: 2rem;
  height: 2rem;
  border-radius: 50%;
  background: var(--vp-c-brand-1);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 1.25rem;
}

.step-title {
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: var(--vp-c-text-1);
}

.step-desc {
  color: var(--vp-c-text-2);
  font-size: 0.875rem;
  line-height: 1.6;
}
</style>

<div class="section-title">🚀 快速开始</div>

<div class="steps-container">
  <div class="step-card">
    <div class="step-number">1</div>
    <div class="step-title">浏览新闻</div>
    <div class="step-desc">查看最新的 AI 论文、行业动态和产品更新</div>
  </div>
  <div class="step-card">
    <div class="step-number">2</div>
    <div class="step-title">深入阅读</div>
    <div class="step-desc">点击感兴趣的文章，查看详细摘要和原文链接</div>
  </div>
  <div class="step-card">
    <div class="step-number">3</div>
    <div class="step-title">订阅更新</div>
    <div class="step-desc">每天 8:00 自动更新，保持知识前沿</div>
  </div>
  <div class="step-card">
    <div class="step-number">4</div>
    <div class="step-title">分享知识</div>
    <div class="step-desc">与同事朋友分享有价值的 AI 资讯</div>
  </div>
</div>

---

## 🎉 立即开始

<style>
.cta-section {
  padding: 4rem 2rem;
  background: linear-gradient(135deg, rgba(37, 99, 235, 0.1), rgba(124, 58, 237, 0.1));
  border-radius: 20px;
  margin: 4rem 0;
  text-align: center;
}

.cta-title {
  font-size: 2.25rem;
  font-weight: 700;
  margin-bottom: 1rem;
  color: var(--vp-c-text-1);
}

.cta-desc {
  color: var(--vp-c-text-2);
  margin-bottom: 2.5rem;
  font-size: 1.125rem;
  line-height: 1.6;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.cta-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

.cta-btn {
  padding: 1rem 2.5rem;
  border-radius: 10px;
  text-decoration: none;
  font-weight: 600;
  font-size: 1.1rem;
  transition: all 0.3s ease;
  display: inline-block;
}

.cta-btn-primary {
  background: var(--vp-c-brand-1);
  color: white !important;
  border: 2px solid var(--vp-c-brand-1);
}

.cta-btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: var(--vp-shadow-3);
  background: var(--vp-c-brand-2);
  border-color: var(--vp-c-brand-2);
}

.cta-btn-secondary {
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1) !important;
  border: 2px solid var(--vp-c-border);
}

.cta-btn-secondary:hover {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1) !important;
}
</style>

<div class="cta-section">
  <div class="cta-title">🎉 准备好探索 AI 世界了吗？</div>
  <div class="cta-desc">加入我们，每天获取最新的 AI 新闻、论文和工具更新，保持技术前沿</div>
  <div class="cta-buttons">
    <a href="/latest-news" class="cta-btn cta-btn-primary">开始阅读 →</a>
    <a href="https://github.com/ZhaoNancheng/ai-news-hub" class="cta-btn cta-btn-secondary">GitHub ⭐</a>
  </div>
</div>

---

## 📞 联系我们

<style>
.contact-section {
  background: var(--vp-c-bg-soft);
  border-radius: 16px;
  padding: 2rem;
  margin: 3rem 0;
  text-align: center;
}

.contact-links {
  display: flex;
  gap: 2rem;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 1.5rem;
}

.contact-link {
  color: var(--vp-c-brand-1);
  text-decoration: none;
  font-weight: 500;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  transition: all 0.3s ease;
}

.contact-link:hover {
  background: var(--vp-c-bg);
  text-decoration: underline;
}
</style>

<div class="contact-section">
  <div>📞 联系我们</div>
  <div class="contact-links">
    <a href="https://github.com/ZhaoNancheng/ai-news-hub" class="contact-link">GitHub 仓库</a>
    <a href="https://ai-news-hub-rosy.vercel.app/" class="contact-link">Vercel 访问</a>
    <a href="https://ai-news-hub-046491.gitlab.io/" class="contact-link">GitLab 访问</a>
  </div>
  <div style="margin-top: 1.5rem; font-size: 0.875rem; color: var(--vp-c-text-2);">
    欢迎提 Issue 和 PR 反馈建议
  </div>
</div>

---

<style>
.footer-section {
  text-align: center;
  padding: 3rem 1rem;
  border-top: 1px solid var(--vp-c-divider);
  margin-top: 4rem;
  color: var(--vp-c-text-2);
  font-size: 0.875rem;
}

.footer-update {
  margin-bottom: 1rem;
}

.footer-links a {
  color: var(--vp-c-brand-1);
  text-decoration: none;
  margin: 0 0.5rem;
}

.footer-links a:hover {
  text-decoration: underline;
}
</style>

<div class="footer-section">
  <div class="footer-update">
    <strong>最后更新</strong>: 2026-02-06 08:00 | 
    <strong>下次更新</strong>: 2026-02-07 08:00
  </div>
  <div class="footer-links">
    <a href="https://github.com/ZhaoNancheng/ai-news-hub">GitHub</a> •
    <a href="https://docs.openclaw.ai">OpenClaw</a> •
    <a href="https://vitepress.dev">VitePress</a>
  </div>
  <div style="margin-top: 1.5rem;">
    Made with ❤️ using <a href="https://vitepress.dev">VitePress</a> + <a href="https://docs.openclaw.ai">OpenClaw</a>
    <br>
    Powered by <a href="https://github.com/ZhaoNancheng">贾维斯 (JARVIS)</a>
  </div>
</div>
