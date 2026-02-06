# AI News Hub - 部署说明

## 🚀 当前部署方案

### 单平台部署：Vercel

**访问地址**：https://ai-news-hub-rosy.vercel.app/

**特点**：
- ✅ 全球 CDN 加速
- ✅ 自动 HTTPS
- ✅ 自动部署（推送代码自动触发）
- ✅ 访问速度快
- ✅ 稳定可靠

---

## 📋 部署流程

### 自动部署（已配置）

Vercel 已连接到 GitHub 仓库，每次推送代码到 `main` 分支时自动部署。

```bash
# 更新内容后推送
git add .
git commit -m "Update: news content"
git push origin main

# Vercel 自动部署，2-3分钟后生效
```

### 手动部署

如需手动触发部署：

1. 访问 Vercel Dashboard
2. 选择项目 `ai-news-hub`
3. 点击 **Redeploy**

---

## 🔧 本地开发

### 安装依赖

```bash
npm install
```

### 本地预览

```bash
npm run docs:dev
```

访问：http://localhost:5173

### 构建网站

```bash
npm run docs:build
```

构建产物：`docs/.vitepress/dist/`

---

## 📊 已尝试但不适合的方案

### ❌ Gitee Pages
- **状态**：2024年已下线
- **原因**：运营成本过高、滥用问题

### ❌ GitLab Pages
- **状态**：服务正常但无法注册
- **原因**：中国手机号无法注册

### ❌ 其他国内平台
- 大多有各种限制
- 部分已停止免费服务

---

## 💡 可选的国内加速方案

如果需要提升国内访问速度，可以考虑：

### 方案1：阿里云 OSS + CDN
```
成本：约5-20元/月
速度：国内最快
适用：对国内访问要求高
```

### 方案2：Cloudflare Pages
```
成本：免费
速度：中等
适用：国际访问为主
```

### 方案3：Netlify
```
成本：免费
速度：中等
适用：备份方案
```

---

## 🎯 总结

**当前推荐**：继续使用 **Vercel** 单平台部署

**理由**：
- ✅ 配置简单
- ✅ 自动部署
- ✅ 全球访问快
- ✅ 完全免费
- ✅ 稳定可靠

**如果需要国内加速**：
- 考虑阿里云 OSS + CDN（低成本方案）
- 或等待更合适的国内平台出现

---

**文档更新时间**：2026-02-06
