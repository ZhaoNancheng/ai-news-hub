---
layout: home

hero:
  name: AI News Hub
  text: 探索 AI 世界的最新动态
  tagline: 每日聚合全球 AI 新闻、研究和工具
  image:
    src: /logo.png
    alt: AI News Hub
  actions:
    - theme: brand
      text: 开始浏览
      link: /latest
    - theme: alt
      text: 查看 GitHub
      link: https://github.com/ZhaoNancheng/ai-news-hub

features:
  - icon: 🚀
    title: 每日更新
    details: 聚合全球 AI 行业最新动态，保持你与前沿同步
  - icon: 📊
    title: 多维度分类
    details: 涵盖突发新闻、研究前沿、产业动态、实用工具等
  - icon: 🔍
    title: 全文搜索
    details: 内置搜索引擎，快速找到你感兴趣的内容
  - icon: 📱
    title: 完美适配
    details: 响应式设计，支持桌面、平板、手机等各种设备
  - icon: ⚡
    title: 极速加载
    details: 基于 VitePress 构建，秒级加载，流畅体验
  - icon: 🎨
    title: 现代设计
    details: 精美的 UI 设计，舒适的阅读体验
---

## 📈 今日数据

<div class="stats-grid">

### 📰 今日新闻
**9** 篇

### 🌐 信息源
**8** 个

### 📂 分类
**5** 个

</div>

## 🎯 快速导航

<div class="quick-nav">

### 🔥 最新动态
- OpenAI 发布 GPT-5：推理能力大幅提升
- Google DeepMind 新模型 AlphaGeometry 3
- Anthropic 获得 20 亿美元融资

### 🔬 研究前沿
- 斯坦福研究：多模态 AI 在医疗诊断中的应用
- OpenAI o3 模型在编程竞赛中夺冠

### 🛠️ 实用工具
- Cursor AI 编辑器更新：智能代码重构功能
- Hugging Face 推出开源模型评估平台

</div>

<style>
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.stats-grid div {
  padding: 1.5rem;
  border-radius: 12px;
  background: var(--vp-c-bg-soft);
  text-align: center;
}

.stats-grid div strong {
  display: block;
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--vp-c-brand-1);
}

.stats-grid div span {
  color: var(--vp-c-text-2);
  margin-top: 0.5rem;
}

.quick-nav {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.quick-nav div {
  padding: 1.5rem;
  border-radius: 12px;
  background: var(--vp-c-bg-soft);
}

.quick-nav h3 {
  margin-top: 0;
}

.quick-nav ul {
  padding-left: 1.5rem;
}

.quick-nav li {
  margin: 0.5rem 0;
}
</style>
