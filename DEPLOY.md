# 🚀 AI News Hub 部署指南

本指南将帮助你将 AI News Hub 项目部署到 GitHub 和 Vercel。

## 📋 前置准备

### 1. GitHub 账号
- 访问 https://github.com 注册（如果没有账号）

### 2. Vercel 账号
- 访问 https://vercel.com 注册
- 可以使用 GitHub 账号直接登录

---

## 📤 步骤一：推送代码到 GitHub

### 方法 A：通过 GitHub 网页界面（最简单）

1. **创建新仓库**
   - 登录 GitHub
   - 点击右上角 `+` → `New repository`
   - 仓库名称：`ai-news-hub`（或其他名称）
   - 选择 `Public` 或 `Private`
   - **不要**勾选 "Initialize this repository with a README"
   - 点击 `Create repository`

2. **上传代码**
   - 在项目页面，点击 `uploading an existing file`
   - 将以下文件拖拽上传：
     - `index.html`
     - `style.css`
     - `app.js`
     - `package.json`
     - `vercel.json`
     - `README.md`
     - `LICENSE`
     - `.gitignore`
   - 填写提交信息："Initial commit"
   - 点击 `Commit changes`

### 方法 B：通过 Git 命令行（推荐）

1. **在 GitHub 创建新仓库**（同上）

2. **推送代码到 GitHub**
   ```bash
   cd /data1/cc/vide-coding/ai-news-hub

   # 添加远程仓库（替换 YOUR_USERNAME）
   git remote add origin https://github.com/YOUR_USERNAME/ai-news-hub.git

   # 推送代码
   git branch -M main
   git push -u origin main
   ```

3. **如果需要身份验证**
   - GitHub 现在使用 Personal Access Token (PAT)
   - 创建 PAT：GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
   - 勾选 `repo` 权限
   - 使用 token 作为密码

---

## 🌐 步骤二：部署到 Vercel

### 方法 A：一键部署（最简单）

1. **访问部署链接**
   - 打开：https://vercel.com/new
   - 或直接点击：[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/YOUR_USERNAME/ai-news-hub)

2. **导入仓库**
   - 选择你的 `ai-news-hub` 仓库
   - 点击 `Import`

3. **配置项目**
   - Project Name: `ai-news-hub`（自动填充）
   - Framework Preset: `Other`（静态网站）
   - Root Directory: `./`（默认）
   - 点击 `Deploy`

4. **等待部署完成**
   - 大约需要 30-60 秒
   - 完成后会获得一个 `.vercel.app` 域名

### 方法 B：通过 Vercel CLI

1. **安装 Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **登录**
   ```bash
   vercel login
   ```

3. **部署**
   ```bash
   cd /data1/cc/vide-coding/ai-news-hub
   vercel
   ```

4. **按照提示操作**
   - 选择 `Set up and deploy`
   - 选择链接到已有项目或创建新项目
   - 等待部署完成

---

## ✅ 步骤三：验证部署

1. **访问你的网站**
   - Vercel 会提供类似：`https://ai-news-hub.vercel.app`
   - 或自定义域名

2. **测试功能**
   - 检查页面加载是否正常
   - 测试筛选按钮
   - 测试响应式布局（调整浏览器宽度）
   - 测试移动端显示

---

## 🎨 步骤四：自定义（可选）

### 修改内容

编辑 `app.js` 中的 `sampleNews` 数组来添加/修改新闻：

```javascript
const sampleNews = [
    {
        id: 1,
        title: "你的标题",
        excerpt: "摘要内容...",
        category: "breaking", // breaking | research | industry | tools
        source: "来源",
        sourceUrl: "https://example.com",
        date: "2026-02-04",
        readTime: "5 分钟",
        image: "图片 URL"
    }
];
```

### 修改样式

编辑 `style.css` 中的 CSS 变量：

```css
:root {
    --primary-color: #2563eb;    /* 修改主色调 */
    --secondary-color: #7c3aed;  /* 修改次要色调 */
}
```

### 更新部署

每次修改后：
1. 提交到 GitHub：
   ```bash
   git add .
   git commit -m "Update content"
   git push
   ```
2. Vercel 会自动重新部署（约 30 秒）

---

## 🌟 步骤五：绑定自定义域名（可选）

1. **在 Vercel 项目设置中**
   - 进入项目 Settings → Domains
   - 添加你的域名（如 `ai.yourdomain.com`）

2. **配置 DNS**
   - Vercel 会提供 DNS 配置信息
   - 在你的域名提供商处添加 CNAME 记录

3. **等待 DNS 生效**
   - 通常需要 5-30 分钟

---

## 📊 项目文件说明

| 文件 | 说明 |
|-----|------|
| `index.html` | 主页面，包含网站结构 |
| `style.css` | 所有样式，支持响应式设计 |
| `app.js` | JavaScript 逻辑和数据 |
| `vercel.json` | Vercel 部署配置 |
| `package.json` | 项目信息 |
| `README.md` | 项目说明文档 |

---

## 🔧 常见问题

### Q: 为什么图片不显示？
A: 检查图片 URL 是否可访问，或使用占位图服务。

### Q: 如何添加更多新闻？
A: 编辑 `app.js` 中的 `sampleNews` 数组，添加新对象。

### Q: 如何更改网站标题？
A: 编辑 `index.html` 中的 `<title>` 标签和 `.hero-title` 内容。

### Q: 部署后页面空白？
A: 检查浏览器控制台是否有错误，确保文件路径正确。

### Q: 如何添加 Google Analytics？
A: 在 `index.html` 的 `<head>` 标签中添加 GA 代码。

---

## 📚 下一步

- ✅ 部署到 Vercel
- 🎨 自定义样式和内容
- 🔗 绑定自定义域名
- 📊 添加 Google Analytics
- 🚀 集成新闻 API（自动更新）

---

**祝你部署顺利！** 🎉

如有问题，随时询问贾维斯。
