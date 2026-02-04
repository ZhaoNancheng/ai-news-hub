import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'AI News Hub',
  description: '每日 AI 新闻聚合平台',
  lang: 'zh-CN',
  base: '/',
  head: [
    ['link', { rel: 'icon', href: '/favicon.ico' }],
    ['meta', { name: 'theme-color', content: '#3c8772' }]
  ],

  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '最新', link: '/latest' },
      { text: '热门', link: '/trending' },
      { text: '研究', link: '/research' },
      { text: '工具', link: '/tools' },
    ],

    sidebar: [
      {
        text: '新闻分类',
        items: [
          { text: '最新动态', link: '/latest' },
          { text: '热门推荐', link: '/trending' },
          { text: '研究前沿', link: '/research' },
          { text: '实用工具', link: '/tools' },
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/ZhaoNancheng/ai-news-hub' }
    ],

    footer: {
      message: '基于 VitePress 构建',
      copyright: 'Copyright © 2026 AI News Hub'
    },

    search: {
      provider: 'local'
    }
  },

  markdown: {
    lineNumbers: true
  }
})
