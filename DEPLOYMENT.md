# AI News Hub - 部署说明

## 🚀 当前部署方案

### 双平台部署

| 平台 | 地址 | 状态 |
|------|------|------|
| **Vercel** | https://ai-news-hub-rosy.vercel.app/ | ✅ 已上线 |
| **GitLab Pages** | https://ai-news-hub-046491.gitlab.io/ | ✅ 已部署 |

---

## 🌐 访问地址

### Vercel（推荐 - 国际访问）
```
https://ai-news-hub-rosy.vercel.app/
```
✅ 全球 CDN 加速
✅ 访问速度快
✅ 稳定可靠

### GitLab Pages（备用）
```
https://ai-news-hub-046491.gitlab.io/
```
✅ 免费托管
✅ 自动部署
⚠️  可能需要等待 DNS 生效

---

## 📋 部署流程

### 自动部署（已配置）

两个平台都已连接到 GitHub 仓库，每次推送代码到 `main` 分支时自动部署。

```bash
# 更新内容后推送
git add .
git commit -m "Update: news content"
git push origin main

# GitLab 推送
git push gitlab main
```

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

## 💻 日常使用

### 更新内容并部署

```bash
cd /data1/cc/vide-coding/ai-news-hub

# 推送到 GitHub（Vercel 自动部署）
git push origin main

# 推送到 GitLab（GitLab 自动部署）
./push-to-gitlab.sh

# 或同时推送到两个平台
git push origin main && git push gitlab main
```

---

## 🛠️ 故障排查

### GitLab Pages 无法访问

**问题**: 访问 https://ai-news-hub-046491.gitlab.io/ 返回认证页面

**解决方案**:
1. 确认项目是 **Public**（公开）
2. 访问 **Settings** → **Pages** 确认配置
3. 等待 5-10 分钟让 DNS 生效
4. 清除浏览器缓存后重试

### Pipeline 失败

**查看日志**:
```
https://gitlab.com/ZhaoNancheng/ai-news-hub/-/pipelines
```

点击失败的 job 查看详细错误信息。

---

## 📚 相关文档

- **VitePress 文档**: https://vitepress.dev/
- **Vercel 文档**: https://vercel.com/docs
- **GitLab Pages 文档**: https://docs.gitlab.com/ee/user/project/pages/

---

**文档更新时间**: 2026-02-06
**GitLab Pages 地址**: https://ai-news-hub-046491.gitlab.io/
**Vercel 地址**: https://ai-news-hub-rosy.vercel.app/
