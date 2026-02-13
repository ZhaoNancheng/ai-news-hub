module.exports = {
  title: 'AI News Hub',
  description: '每日 AI 新闻聚合平台',
  
  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '每日新闻', link: '/latest-news' },
      { text: '研究前沿', link: '/research' },
      { text: '热门推荐', link: '/trending' },
      { text: '关于项目', link: '/about' }
    ],

    sidebar: {
      '/': [
        {
          text: '核心板块',
          items: [
            { text: '每日新闻', link: '/latest-news' },
            { text: '研究前沿', link: '/research' },
            { text: '热门推荐', link: '/trending' },
            { text: '关于项目', link: '/about' }
          ]
        }
      ],
      '/research/': [
        {
          text: '研究领域',
          items: [
            { text: '最新论文', link: '#最新研究论文' },
            { text: '研究趋势', link: '#研究趋势' },
            { text: '会议信息', link: '#会议信息' }
          ]
        }
      ],
      '/trending/': [
        {
          text: '推荐分类',
          items: [
            { text: '项目推荐', link: '#项目推荐' },
            { text: '工具推荐', link: '#工具推荐' },
            { text: '资源推荐', link: '#资源推荐' }
          ]
        }
      ],
      '/about': [
        {
          text: '关于',
          items: [
            { text: '项目介绍', link: '#项目介绍' },
            { text: '技术架构', link: '#技术架构' },
            { text: '更新日志', link: '#更新日志' }
          ]
        }
      ],
      '/news/': [
        {
          text: '历史新闻',
          items: [
            { text: '本周新闻', link: '/news/weekly/2026-02-week7.md' },
            { text: '上周新闻', link: '/news/weekly/2026-02-week6.md' }
          ]
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
