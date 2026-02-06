<template>
  <div class="feature-cards-section">
    <div class="section-title">探索 AI 世界</div>
    <div class="section-subtitle">从最新动态到前沿研究，一站式追踪 AI 发展</div>

    <div class="cards-container">
      <a href="/latest-news" class="feature-card">
        <div class="card-header">
          <div class="card-icon">📰</div>
          <div class="card-title">每日新闻</div>
        </div>
        <div class="card-content">
          每天 08:00 自动更新，聚合全球 AI 新闻和行业动态
        </div>
        <div class="card-link">查看新闻 →</div>
      </a>

      <a href="/research" class="feature-card">
        <div class="card-header">
          <div class="card-icon">🔬</div>
          <div class="card-title">研究前沿</div>
        </div>
        <div class="card-content">
          追踪 AI Agent、多智能体系统、世界模型等前沿研究
        </div>
        <div class="card-link">深入研究 →</div>
      </a>

      <a href="/trending" class="feature-card">
        <div class="card-header">
          <div class="card-icon">🔥</div>
          <div class="card-title">热门推荐</div>
        </div>
        <div class="card-content">
          发现当前 AI 领域最热门的研究方向和讨论话题
        </div>
        <div class="card-link">查看热门 →</div>
      </a>
    </div>
  </div>
</template>

<script setup>
// 无需复杂逻辑，纯展示组件
</script>

<style scoped>
.feature-cards-section {
  padding: 4rem 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.section-title {
  font-size: 2rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 1rem;
  color: var(--vp-c-text-1);
}

.section-subtitle {
  font-size: 1.125rem;
  text-align: center;
  color: var(--vp-c-text-2);
  margin-bottom: 3rem;
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
}

.cards-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 2rem;
}

.feature-card {
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-border);
  border-radius: 16px;
  padding: 2rem;
  text-decoration: none;
  color: inherit;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.feature-card:hover {
  border-color: var(--vp-c-brand-1);
  box-shadow: 0 12px 24px rgba(60, 135, 114, 0.15);
  transform: translateY(-8px);
}

.card-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.card-icon {
  font-size: 2.5rem;
  line-height: 1;
}

.card-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--vp-c-text-1);
  flex: 1;
}

.card-content {
  color: var(--vp-c-text-2);
  line-height: 1.8;
  margin-bottom: 1.5rem;
  font-size: 1rem;
  flex: 1;
}

.card-link {
  color: var(--vp-c-brand-1);
  font-weight: 600;
  font-size: 1rem;
  padding: 0.875rem 2rem;
  background: var(--vp-c-brand-1);
  color: white !important;
  border-radius: 8px;
  transition: all 0.3s ease;
  text-align: center;
}

.feature-card:hover .card-link {
  background: var(--vp-c-brand-2);
}

@media (max-width: 768px) {
  .feature-cards-section {
    padding: 3rem 1.5rem;
  }

  .cards-container {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }

  .section-title {
    font-size: 1.75rem;
  }

  .feature-card {
    padding: 1.5rem;
  }
}
</style>
