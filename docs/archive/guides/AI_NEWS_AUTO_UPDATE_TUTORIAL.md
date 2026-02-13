# 🤖 用 OpenClaw 自动创建 AI 新闻网站并每日更新：完整教程

> 作者：贾维斯 (JARVIS)  
> 时间：2026-02-05  
> 阅读时长：15 分钟  
> 难度：⭐⭐⭐ (适合有基础的开发者)

---

## 📖 导读

你是否想过创建一个属于自己的 AI 新闻网站？每天自动获取最新资讯、自动更新、自动部署？今天我来教你如何用 **OpenClaw** + **VitePress** + **Vercel** 实现这个目标。

本教程将带你从零开始，一步步创建一个现代化的 AI 新闻聚合网站，并配置每天早上 8 点自动更新！

---

## 🎯 我们要做什么

### 最终效果

- ✅ 现代化静态网站（响应式设计）
- ✅ 每天早上 8 点自动获取 AI 新闻
- ✅ 自动生成 Markdown 文件
- ✅ 自动推送到 GitHub
- ✅ Vercel 自动部署（1-2 分钟）
- ✅ 包含 arXiv 论文、行业新闻、产品更新

### 技术栈

- **OpenClaw** - AI 助手框架（自动化核心）
- **VitePress** - 静态站点生成器（Vue 团队开发）
- **GitHub** - 代码托管
- **Vercel** - 自动部署平台
- **Cron** - 定时任务调度器

---

## 📋 准备工作

### 1. 环境要求

```bash
# 检查 Node.js 版本（需要 >= 18）
node --version

# 检查 Git 版本
git --version

# 检查 Python 版本（可选，用于本地预览）
python3 --version
```

### 2. 账号准备

- GitHub 账号：https://github.com
- Vercel 账号：https://vercel.com（可用 GitHub 登录）
- OpenClaw 环境（本文基于 OpenClaw 框架）

---

## 🚀 第一步：创建 VitePress 项目

### 1.1 项目初始化

```bash
# 创建项目目录
mkdir ai-news-hub
cd ai-news-hub

# 初始化 npm 项目
npm init -y

# 安装 VitePress
npm install -D vitepress
```

### 1.2 创建项目结构

```bash
# 创建文档目录
mkdir -p docs/.vitepress
```

### 1.3 配置 VitePress

创建 `docs/.vitepress/config.mjs`：

```javascript
import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'AI News Hub',
  description: '每日 AI 新闻聚合平台',
  lang: 'zh-CN',
  
  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '每日新闻', link: '/latest-news' }
    ],
    
    sidebar: [
      {
        text: '页面',
        items: [
          { text: '首页', link: '/' },
          { text: '每日新闻', link: '/latest-news' }
        ]
      }
    ],
    
    socialLinks: [
      { icon: 'github', link: 'https://github.com/YOUR_USERNAME/ai-news-hub' }
    ],
    
    search: {
      provider: 'local'
    }
  }
})
```

### 1.4 创建首页

创建 `docs/index.md`：

```markdown
---
layout: home

hero:
  name: AI News Hub
  text: 每日 AI 新闻聚合
  tagline: 自动获取最新资讯
  actions:
    - theme: brand
      text: 开始阅读
      link: /latest-news

features:
  - icon: ⚡
    title: 自动更新
    details: 每天早上 8 点自动获取最新 AI 新闻
  - icon: 🎨
    title: 现代设计
    details: 基于 VitePress 构建，响应式布局
  - icon: 🔍
    title: 全文搜索
    details: 内置搜索引擎，快速找到内容
---
```

### 1.5 更新 package.json

修改 `package.json`：

```json
{
  "scripts": {
    "docs:dev": "vitepress dev docs",
    "docs:build": "vitepress build docs",
    "docs:preview": "vitepress preview docs"
  }
}
```

### 1.6 本地预览

```bash
# 启动开发服务器
npm run docs:dev

# 访问 http://localhost:5173
```

---

## 🌐 第二步：部署到 Vercel

### 2.1 推送代码到 GitHub

```bash
# 初始化 Git 仓库
git init
git add .
git commit -m "Initial commit: VitePress site"

# 添加远程仓库（替换 YOUR_USERNAME）
git remote add origin git@github.com:YOUR_USERNAME/ai-news-hub.git
git branch -M main
git push -u origin main
```

### 2.2 配置 Vercel

#### 方法一：一键部署（推荐）

访问：https://vercel.com/new/clone?repository-url=https://github.com/YOUR_USERNAME/ai-news-hub

#### 方法二：通过 Dashboard

1. 访问 https://vercel.com/dashboard
2. 点击 "New Project"
3. 导入 GitHub 仓库
4. Vercel 自动检测 VitePress 配置
5. 点击 "Deploy"

### 2.3 配置 Vercel 文件

创建 `vercel.json`：

```json
{
  "buildCommand": "npm run docs:build",
  "outputDirectory": "docs/.vitepress/dist",
  "installCommand": "npm install"
}
```

---

## 🤖 第三步：创建自动更新脚本

### 3.1 创建脚本目录

```bash
mkdir -p /path/to/scripts
```

### 3.2 编写自动更新脚本

创建 `auto-update-ai-news.sh`：

```bash
#!/bin/bash

# 配置
PROJECT_DIR="/path/to/ai-news-hub"
NEWS_DIR="$PROJECT_DIR/docs/news"
DATE=$(date +"%Y-%m-%d")
DATETIME=$(date +"%Y-%m-%d %H:%M:%S")

# 创建新闻目录
mkdir -p "$NEWS_DIR"

# 生成新闻文件
NEWS_FILE="$NEWS_DIR/$DATE.md"

echo "# AI News Briefing - $DATE" > "$NEWS_FILE"
echo "" >> "$NEWS_FILE"
echo "**更新时间**: $DATETIME" >> "$NEWS_FILE"
echo "" >> "$NEWS_FILE"
echo "---" >> "$NEWS_FILE"
echo "" >> "$NEWS_FILE"

# 这里调用 OpenClaw 的 daily-ai-news-skill
# 或者使用其他新闻获取方式

# 提交到 Git
cd "$PROJECT_DIR"
git add docs/news/
git commit -m "Auto-update: AI News briefing - $DATE"
git push origin main
```

### 3.3 添加执行权限

```bash
chmod +x /path/to/scripts/auto-update-ai-news.sh
```

---

## ⏰ 第四步：配置 Cron 定时任务

### 4.1 编辑 Crontab

```bash
crontab -e
```

### 4.2 添加定时任务

```bash
# 每天早上 8 点运行
0 8 * * * /path/to/scripts/auto-update-ai-news.sh >> /var/log/ai-news-update.log 2>&1
```

**Cron 时间格式说明**：

```
* * * * * 命令
│ │ │ │ │
│ │ │ │ └─ 星期几 (0-7)
│ │ │ └─── 月份 (1-12)
│ │ └───── 日期 (1-31)
│ └─────── 小时 (0-23)
└───────── 分钟 (0-59)
```

**常用时间设置**：

```bash
# 每天早上 8 点
0 8 * * *

# 每天晚上 10 点
0 22 * * *

# 每 6 小时
0 */6 * * *

# 每周一早上 9 点
0 9 * * 1
```

### 4.3 验证 Cron 配置

```bash
# 查看当前 crontab
crontab -l

# 查看 cron 服务状态
systemctl status crond

# 查看 cron 日志
tail -f /var/log/ai-news-update.log
```

---

## 🎨 第五步：创建每日新闻页面

### 5.1 创建新闻目录

```bash
mkdir -p docs/news
```

### 5.2 创建新闻索引

创建 `docs/latest-news.md`：

```markdown
# 📰 最新 AI 新闻

> 每日更新，汇聚全球 AI 行业最新动态

**最后更新**: 2026-02-05

---

## 最近更新

### [2026-02-05](/news/2026-02-05)

今日更新包含：
- 15 篇 arXiv 论文
- 5 条行业新闻
- 4 个产品更新
- 5 个研究突破

---

## 历史新闻

更多历史新闻...
```

### 5.3 创建今日新闻

创建 `docs/news/2026-02-05.md`：

```markdown
# AI News Briefing - 2026-02-05

**更新时间**: 2026-02-05 08:00:00

---

## 🎓 学术研究

### 论文标题

**摘要**: ...

**链接**: [arXiv](https://arxiv.org/abs/...)

---

## 🌟 行业新闻

### 新闻标题

**摘要**: ...

**链接**: [来源](URL)

---
```

---

## 🔄 第六步：配置 OpenClaw 自动获取新闻

### 6.1 使用 daily-ai-news-skill

OpenClaw 提供了 `daily-ai-news-skill`，可以自动获取：

- arXiv 最新论文（AI Agent 方向）
- AI 行业重大新闻
- 产品发布和更新
- 研究突破

### 6.2 集成到脚本

修改 `auto-update-ai-news.sh`，添加：

```bash
# 调用 OpenClaw 子会话获取新闻
# （具体实现取决于你的 OpenClaw 配置）
```

---

## 📊 第七步：完整自动化流程

### 自动化时间线

```
每天早上 8:00
   ↓
Cron 触发脚本
   ↓
调用 OpenClaw 获取新闻
   ↓
生成 Markdown 文件
   ↓
更新首页索引
   ↓
Git commit 并 push
   ↓
Vercel 自动部署
   ↓
网站更新完成（1-2分钟）
```

### 监控和维护

```bash
# 查看运行日志
tail -f /var/log/ai-news-update.log

# 查看最新提交
git log --oneline -1

# 查看 Vercel 部署状态
# 访问 Vercel Dashboard
```

---

## 🎨 进阶优化

### 1. 添加更多功能

#### RSS 订阅

```javascript
// 在 docs/.vitepress/config.mjs 中添加
export default defineConfig({
  head: [
    ['link', { rel: 'alternate', type: 'application/rss+xml', href: '/rss.xml' }]
  ]
})
```

#### 评论系统（Giscus）

安装 [Giscus](https://giscus.app/) 添加 GitHub Discussions 评论。

#### Google Analytics

在 `config.mjs` 中添加 GA 代码。

### 2. 自定义样式

创建 `docs/.vitepress/theme/index.css`：

```css
/* 自定义样式 */
.my-custom-card {
  padding: 1rem;
  border-radius: 8px;
  background: var(--vp-c-bg-soft);
}
```

### 3. 添加更多页面

```bash
# 创建关于页面
echo "# 关于" > docs/about.md

# 创建友链页面
echo "# 友情链接" > docs/links.md
```

---

## 🐛 常见问题

### Q1: Vercel 构建失败

**问题**: `build error: [vitepress] 1 dead link(s) found.`

**解决**: 在 `config.mjs` 中添加：

```javascript
export default defineConfig({
  ignoreDeadLinks: true
})
```

### Q2: Cron 没有运行

**检查**:

```bash
# 1. 检查 cron 服务
systemctl status crond

# 2. 查看 cron 日志
grep CRON /var/log/syslog | tail -20

# 3. 检查脚本权限
ls -lh /path/to/scripts/auto-update-ai-news.sh
```

### Q3: Git 推送失败

**检查 SSH 配置**:

```bash
# 测试 SSH 连接
ssh -T git@github.com

# 检查 remote
git remote -v
```

### Q4: 新闻文件没有生成

**检查**:

```bash
# 1. 检查脚本是否有执行权限
ls -lh /path/to/scripts/auto-update-ai-news.sh

# 2. 手动运行脚本
bash /path/to/scripts/auto-update-ai-news.sh

# 3. 查看日志
cat /var/log/ai-news-update.log
```

---

## 📚 相关资源

### 官方文档

- [VitePress 官方文档](https://vitepress.dev/)
- [Vercel 部署指南](https://vercel.com/docs)
- [OpenClaw 文档](https://docs.openclaw.ai)

### 参考项目

- [AI News Hub](https://github.com/ZhaoNancheng/ai-news-hub) - 完整示例
- [VitePress 官方示例](https://github.com/vuejs/vitepress)

### 推荐阅读

- [为什么选择 VitePress](https://vitepress.dev/guide/why-vitepress)
- [静态网站最佳实践](https://vercel.com/docs/best-practices)

---

## 💡 最佳实践

### 1. 版本控制

```bash
# 使用 .gitignore
node_modules/
docs/.vitepress/dist/
.DS_Store
```

### 2. 内容组织

```
docs/
├── .vitepress/
│   └── config.mjs
├── news/
│   ├── 2026-02-05.md
│   └── 2026-02-06.md
├── index.md
└── latest-news.md
```

### 3. 性能优化

- 使用图片懒加载
- 启用 VitePress 缓存
- 压缩静态资源

### 4. 安全建议

- 不要在代码中硬编码 API 密钥
- 使用环境变量
- 定期更新依赖

---

## 🎉 总结

通过本教程，你已经学会了：

✅ 使用 VitePress 创建静态网站  
✅ 部署到 Vercel  
✅ 配置 Cron 定时任务  
✅ 自动获取 AI 新闻  
✅ 自动更新部署  

### 下一步

- 添加更多内容分类
- 优化网站性能
- 集成更多数据源
- 添加用户互动功能

---

## 📞 获取帮助

- **GitHub Issues**: https://github.com/YOUR_USERNAME/ai-news-hub/issues
- **Vercel 文档**: https://vercel.com/docs
- **VitePress 社区**: https://github.com/vuejs/vitepress/discussions

---

**祝你成功创建自己的 AI 新闻网站！** 🎊

如果本教程对你有帮助，欢迎分享给更多人！

---

**作者**: 贾维斯 (JARVIS)  
**项目**: AI News Hub  
**在线示例**: https://ai-news-hub-rosy.vercel.app/

> 本教程基于实际项目经验编写，如有疑问欢迎交流。
