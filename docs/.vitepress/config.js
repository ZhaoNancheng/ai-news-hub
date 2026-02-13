module.exports = {
  title: 'AI News Hub',
  description: '每日 AI 新闻聚合平台',
  
  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '每日新闻', link: '/latest-news' },
      { text: '研究前沿', link: '/research' },
      { text: '热门推荐', link: '/trending' }
    ],

    sidebar: {
      '/': [
        {
          text: '核心板块',
          items: [
            { text: '每日新闻', link: '/latest-news' },
            { text: '研究前沿', link: '/research' },
            { text: '热门推荐', link: '/trending' }
          ]
        }
      ],
      '/news/': [
        {
          text: '历史新闻',
          items: []
        }
      ]
    },

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
  
  locales: {},
  scrollOffset: 134,
  cleanUrls: false
}
