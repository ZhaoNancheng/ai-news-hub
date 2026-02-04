# AI News Hub 🤖

一个现代化、响应式的 AI 新闻聚合静态网站，每日展示全球 AI 行业的最新动态。

![License](https://img.shields.io/badge/license-MIT-blue)
![Static](https://img.shields.io/badge/type-static-green)
![Deploy](https://img.shields.io/badge/deploy-vercel-brightgreen)

## ✨ 特性

- 🎨 现代化渐变设计，暗色主题
- 📱 完全响应式，支持移动端
- ⚡ 纯静态 HTML/CSS/JS，无需构建工具
- 🚀 即开即用，一键部署
- 🔄 动态内容加载
- 🎯 分类筛选功能
- 💫 流畅动画效果
- ♿ 无障碍支持

## 📁 项目结构

```
ai-news-hub/
├── index.html          # 主页面
├── style.css           # 样式文件
├── app.js              # JavaScript 逻辑
├── package.json        # 项目信息
├── vercel.json         # Vercel 配置
└── README.md           # 项目说明
```

## 🚀 本地开发

### 方法 1: Python（推荐）

```bash
cd ai-news-hub
python3 -m http.server 8000
```

访问 http://localhost:8000

### 方法 2: Node.js

```bash
npx serve
```

### 方法 3: 直接打开

直接在浏览器中打开 `index.html` 文件即可。

## 📦 部署到 Vercel

### 一键部署

点击下方按钮一键部署到 Vercel：

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/yourusername/ai-news-hub)

### 手动部署

1. **Fork 本仓库到你的 GitHub 账号**

2. **在 Vercel 导入项目**
   - 登录 [Vercel Dashboard](https://vercel.com/dashboard)
   - 点击 "New Project"
   - 选择你 fork 的仓库
   - 点击 "Deploy"

3. **完成！** 🎉

   Vercel 会自动部署你的网站，并提供一个 `.vercel.app` 域名。

## 🎨 自定义

### 修改新闻数据

编辑 `app.js` 中的 `sampleNews` 数组：

```javascript
const sampleNews = [
    {
        id: 1,
        title: "你的新闻标题",
        excerpt: "新闻摘要...",
        category: "breaking", // breaking | research | industry | tools
        source: "来源名称",
        sourceUrl: "https://example.com",
        date: "2026-02-04",
        readTime: "5 分钟",
        image: "https://example.com/image.jpg"
    },
    // 添加更多...
];
```

### 修改样式

编辑 `style.css` 中的 CSS 变量：

```css
:root {
    --primary-color: #2563eb;    /* 主色调 */
    --secondary-color: #7c3aed;  /* 次要色调 */
    --dark-bg: #0f172a;          /* 背景色 */
    --card-bg: #1e293b;          /* 卡片背景 */
    /* ... */
}
```

### 修改配色主题

项目支持轻松切换配色方案，只需修改 CSS 变量即可：

- **蓝色主题**（默认）
- **紫色主题**: `--primary-color: #7c3aed`
- **绿色主题**: `--primary-color: #10b981`
- **橙色主题**: `--primary-color: #f59e0b`

## 📊 数据来源

新闻数据可以来自：

1. **静态数据**（当前方式）
   - 在 `app.js` 中手动维护

2. **API 集成**
   - News API
   - 自建后端
   - GitHub Actions 定期更新

3. **RSS 聚合**
   - 使用 rss2json 服务
   - 或自建 RSS 解析服务

## 🔧 技术栈

- **HTML5** - 语义化标签
- **CSS3** - 现代特性（Grid、Flexbox、渐变、动画）
- **Vanilla JavaScript** - 无依赖，纯原生 JS
- **Vercel** - 部署平台

## 📝 待办事项

- [ ] 添加搜索功能
- [ ] 集成真实新闻 API
- [ ] 添加暗/亮主题切换
- [ ] 添加评论系统（如 Giscus）
- [ ] 添加 RSS 订阅
- [ ] SEO 优化
- [ ] 添加 PWA 支持

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢

- 设计灵感来自 [freestylefly/ai-news-static](https://github.com/freestylefly/ai-news-static)
- 图片来自 [Unsplash](https://unsplash.com)

---

**Made with ❤️ by 贾维斯**
