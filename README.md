# 🤖 AI News Hub

> 基于 VitePress 构建的现代化 AI 新闻聚合平台

[![VitePress](https://img.shields.io/badge/VitePress-1.0-blue)](https://vitepress.dev/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Deploy](https://img.shields.io/badge/deploy-vercel-brightgreen)](https://vercel.com)

## ✨ 特性

- 🎨 **现代化设计** - 基于 VitePress，美观且响应式
- 📱 **完美适配** - 支持桌面、平板、手机等各种设备
- ⚡ **极速加载** - 静态生成，秒级加载
- 🔍 **全文搜索** - 内置搜索引擎，快速查找内容
- 📝 **Markdown 驱动** - 内容用 Markdown 编写，易于维护
- 🎯 **多维度分类** - 最新/热门/研究/工具四大板块
- 🌙 **深色模式** - 自动适配系统主题

## 📁 项目结构

```
ai-news-hub/
├── docs/                      # 文档目录
│   ├── .vitepress/            # VitePress 配置
│   │   ├── config.mjs         # 站点配置
│   │   └── dist/              # 构建输出
│   ├── index.md               # 首页
│   ├── latest.md              # 最新动态
│   ├── trending.md            # 热门推荐
│   ├── research.md            # 研究前沿
│   └── tools.md               # 实用工具
├── package.json               # 项目配置
├── vercel.json                # Vercel 部署配置
└── README.md                  # 项目说明
```

## 🚀 本地开发

### 环境要求

- Node.js >= 18
- npm 或 pnpm

### 安装依赖

```bash
npm install
```

### 启动开发服务器

```bash
npm run docs:dev
```

访问 http://localhost:5173

### 构建生产版本

```bash
npm run docs:build
```

### 预览生产构建

```bash
npm run docs:preview
```

## 📦 部署到 Vercel

### 一键部署

点击下方按钮一键部署：

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/ZhaoNancheng/ai-news-hub)

### 手动部署

1. **Fork 本仓库到你的 GitHub 账号**

2. **在 Vercel 导入项目**
   - 访问 [Vercel Dashboard](https://vercel.com/dashboard)
   - 点击 "New Project"
   - 选择你 fork 的仓库
   - Vercel 会自动检测 VitePress 配置
   - 点击 "Deploy"

3. **完成！** 🎉

   Vercel 会自动：
   - 安装依赖 (`npm install`)
   - 构建项目 (`npm run docs:build`)
   - 部署到 CDN
   - 提供一个 `.vercel.app` 域名

## 📝 内容管理

### 添加新闻

编辑 `docs/` 目录下的 Markdown 文件，例如 `docs/latest.md`：

```markdown
### 新闻标题

新闻内容描述...

**发布时间**：2026-02-04
**阅读时长**：5 分钟
**来源**：[链接](https://example.com)

---

<NewsList category="breaking" />
```

### 修改导航

编辑 `docs/.vitepress/config.mjs`：

```javascript
themeConfig: {
  nav: [
    { text: '首页', link: '/' },
    { text: '最新', link: '/latest' },
    // 添加更多导航项...
  ]
}
```

### 自定义样式

在 Markdown 文件中使用 `<style>` 标签：

```markdown
<style>
.my-class {
  color: var(--vp-c-brand-1);
}
</style>
```

## 🎨 技术栈

- **VitePress** - 静态站点生成器
- **Vue 3** - 前端框架
- **Vite** - 构建工具
- **Markdown** - 内容格式
- **Vercel** - 部署平台

## 🌟 与原版对比

| 特性 | 原 HTML 版本 | VitePress 版本 |
|------|-------------|---------------|
| 加载速度 | 快 | ⚡ 极快 |
| 内容管理 | 手动编辑 HTML | ✅ Markdown |
| 搜索功能 | 需自己实现 | ✅ 内置 |
| 响应式 | 手动 CSS | ✅ 自动适配 |
| 深色模式 | 需自己实现 | ✅ 内置 |
| 维护成本 | 中等 | ✅ 低 |

## 📚 扩展功能

可以轻松添加：

- [ ] RSS 订阅
- [ ] 评论系统 (Giscus)
- [ ] 分析统计
- [ ] 自动化内容抓取
- [ ] 多语言支持

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

## 🙏 致谢

- [VitePress](https://vitepress.dev/) - 强大的静态站点生成器
- [Vue.js](https://vuejs.org/) - 渐进式 JavaScript 框架
- [freestylefly/ai-news-static](https://github.com/freestylefly/ai-news-static) - 设计灵感

---

**Made with ❤️ by 贾维斯 (JARVIS)**

**在线访问**: https://ai-news-hub.vercel.app
