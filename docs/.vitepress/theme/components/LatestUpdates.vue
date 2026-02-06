<template>
  <div class="latest-updates-section">
    <div class="section-header">
      <div class="section-title">📰 最新更新</div>
      <div class="section-date">{{ currentDate }}</div>
    </div>

    <div class="updates-list">
      <a :href="item.link" class="update-item" v-for="(item, index) in newsItems" :key="index">
        <div class="update-number">{{ index + 1 }}</div>
        <div class="update-content">
          <div class="update-title">{{ item.title }}</div>
          <div class="update-meta">
            <span class="update-source">{{ item.source }}</span>
            <span class="update-time">{{ item.time }}</span>
          </div>
          <div class="update-summary">{{ item.summary }}</div>
        </div>
        <div class="update-arrow">→</div>
      </a>
    </div>

    <div class="view-all-link">
      <a href="/latest-news">查看全部新闻 →</a>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const currentDate = ref('')

const newsItems = ref([
  {
    title: 'OpenAI 发布 GPT-5.3 Codex 编程模型',
    source: 'TechCrunch',
    time: '2026-02-05',
    summary: '比上一代快 25%，首个能"帮助构建自己"的模型，可在几天内创建复杂应用',
    link: '/latest-news#1-openai-发布-gpt-53-codex-编程模型'
  },
  {
    title: 'Anthropic 发布 Claude Opus 4.6',
    source: 'TechCrunch',
    time: '2026-02-05',
    summary: '最新 agentic coding model，与 OpenAI 竞争白热化，提前 15 分钟发布',
    link: '/latest-news#2-anthropic-发布-claude-opus-46'
  },
  {
    title: '亚马逊宣布 2000 亿美元 AI 投资计划',
    source: 'The New York Times',
    time: '2026-02-05',
    summary: '巨额投资用于数据中心和 AI 基础设施，显示科技巨头在 AI 军备竞赛中的决心',
    link: '/latest-news#3-亚马逊宣布-2000-亿美元-ai-投资计划'
  }
])

onMounted(() => {
  const now = new Date()
  currentDate.value = now.toLocaleDateString('zh-CN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    weekday: 'long'
  })
})
</script>

<style scoped>
.latest-updates-section {
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-border);
  border-radius: 16px;
  padding: 2.5rem;
  max-width: 900px;
  margin: 3rem auto;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  flex-wrap: wrap;
  gap: 1rem;
}

.section-title {
  font-size: 1.75rem;
  font-weight: 700;
  color: var(--vp-c-text-1);
}

.section-date {
  font-size: 0.9375rem;
  color: var(--vp-c-text-2);
  font-weight: 500;
}

.updates-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.update-item {
  display: flex;
  align-items: flex-start;
  gap: 1.25rem;
  padding: 1.5rem;
  background: var(--vp-c-bg-soft);
  border-radius: 12px;
  text-decoration: none;
  color: inherit;
  transition: all 0.3s ease;
  border: 1px solid transparent;
}

.update-item:hover {
  border-color: var(--vp-c-brand-1);
  background: var(--vp-c-bg);
  box-shadow: 0 4px 12px rgba(60, 135, 114, 0.15);
  transform: translateX(4px);
}

.update-number {
  font-size: 1.5rem;
  font-weight: 800;
  background: linear-gradient(135deg, var(--vp-c-brand-1), var(--vp-c-brand-2));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  min-width: 2rem;
  text-align: center;
}

.update-content {
  flex: 1;
}

.update-title {
  font-size: 1.125rem;
  font-weight: 600;
  color: var(--vp-c-text-1);
  margin-bottom: 0.5rem;
  line-height: 1.5;
}

.update-meta {
  display: flex;
  gap: 1rem;
  margin-bottom: 0.75rem;
  flex-wrap: wrap;
}

.update-source {
  font-size: 0.875rem;
  color: var(--vp-c-brand-1);
  font-weight: 600;
}

.update-time {
  font-size: 0.875rem;
  color: var(--vp-c-text-2);
}

.update-summary {
  font-size: 0.9375rem;
  color: var(--vp-c-text-2);
  line-height: 1.6;
}

.update-arrow {
  font-size: 1.5rem;
  color: var(--vp-c-brand-1);
  font-weight: 700;
  transition: transform 0.3s ease;
}

.update-item:hover .update-arrow {
  transform: translateX(4px);
}

.view-all-link {
  margin-top: 2rem;
  text-align: center;
}

.view-all-link a {
  display: inline-block;
  padding: 0.875rem 2.5rem;
  background: var(--vp-c-brand-1);
  color: white;
  text-decoration: none;
  border-radius: 8px;
  font-weight: 600;
  transition: all 0.3s ease;
}

.view-all-link a:hover {
  background: var(--vp-c-brand-2);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(60, 135, 114, 0.3);
}

@media (max-width: 768px) {
  .latest-updates-section {
    padding: 1.5rem;
    margin: 2rem 1rem;
  }

  .section-header {
    flex-direction: column;
    align-items: flex-start;
  }

  .update-item {
    padding: 1rem;
  }

  .update-title {
    font-size: 1rem;
  }
}
</style>
