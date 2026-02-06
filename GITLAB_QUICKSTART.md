# GitLab Pages - 快速开始

## 🎯 3分钟完成配置

### 前置说明

由于 **Gitee Pages 已下线**，我们改用 **GitLab Pages** 作为国内/全球访问的替代方案。

---

## 🚀 配置步骤

### 第1步：在 GitLab 创建仓库（1分钟）

1. 访问 https://gitlab.com/
2. 点击 **New Project** → **Create blank project**
3. 项目名称：`ai-news-hub`
4. **不要** 勾选 "Initialize repository"
5. 点击 **Create project**

### 第2步：运行配置助手（30秒）

```bash
cd /data1/cc/vide-coding/ai-news-hub
./setup-gitlab-remote.sh
```

按提示输入 GitLab 用户名即可。

或手动添加：
```bash
git remote add gitlab https://gitlab.com/你的用户名/ai-news-hub.git
```

### 第3步：推送到 GitLab（1分钟）

```bash
# 推送代码
git push gitlab main

# 如果提示输入密码：
# 用户名：任意填写或留空
# 密码：使用 GitLab Personal Access Token
```

**如何获取 Token**：
1. GitLab → Settings → Access Tokens
2. Token name: `deploy-token`
3. Scopes: 勾选 `write_repository`
4. 创建后复制 token
5. 推送时用 token 作为密码

### 第4步：等待自动部署（2分钟）

推送成功后，GitLab CI/CD 会自动：
- 检测到 `.gitlab-ci.yml` 配置
- 启动 CI/CD Pipeline
- 构建 VitePress 项目
- 部署到 GitLab Pages

**查看部署状态**：
```
https://gitlab.com/你的用户名/ai-news-hub/-/pipelines
```

### 第5步：访问网站（1分钟）

部署完成后（约 2-5 分钟），访问：
```
https://你的用户名.gitlab.io/ai-news-hub/
```

---

## ✅ 完成！

现在您的网站已部署到两个平台：

### 🌍 国际访问（推荐）
```
https://ai-news-hub-rosy.vercel.app/
```
✅ 全球 CDN，速度快

### 🌐 全球/国内访问
```
https://你的用户名.gitlab.io/ai-news-hub/
```
✅ 免费托管，自动部署

---

## 💻 日常使用

### 更新网站后部署

```bash
cd /data1/cc/vide-coding/ai-news-hub

# 完整部署（构建 + 推送）
npm run deploy:gitlab

# 快速推送（不构建）
npm run push:gitlab
```

---

## 🔧 验证配置

```bash
# 运行检查脚本
./check-gitlab-platform.sh
```

---

## 🛠️ 常见问题

### Q1: 推送时提示权限错误？

**A**: 使用 Personal Access Token：
```bash
# 1. 创建 Token（见上文说明）
# 2. 推送时使用 token 作为密码
git push gitlab main
# Username: <任意填写>
# Password: <粘贴 token>
```

### Q2: GitLab CI/CD 不运行？

**A**: 检查以下几点：
```bash
# 1. 确认 .gitlab-ci.yml 存在
ls -la .gitlab-ci.yml

# 2. 确认已推送到 main 分支
git branch
git push gitlab main

# 3. 查看 CI/CD 页面
# https://gitlab.com/你的用户名/ai-news-hub/-/pipelines
```

### Q3: GitLab Pages 404？

**A**: 可能的原因：
1. 部署还在进行中（等待 5-10 分钟）
2. 项目不是 Public（设置为公开）
3. CI/CD 失败（查看日志）

---

## 📚 快速命令参考

```bash
# 查看远程仓库
git remote -v

# 添加 GitLab 远程仓库
git remote add gitlab <gitlab仓库地址>
git remote add gitlab https://gitlab.com/你的用户名/ai-news-hub.git

# 删除 GitLab 远程仓库
git remote remove gitlab

# 完整部署（构建 + 推送）
npm run deploy:gitlab
./deploy-dual-platform-gitlab.sh

# 快速推送（不构建）
npm run push:gitlab
./push-dual-platform-gitlab.sh

# 仅推送到 GitHub
git push origin main

# 仅推送到 GitLab
git push gitlab main

# 同时推送到双平台
git push origin main && git push gitlab main

# 本地预览
npm run docs:dev
```

---

## 🎉 享受免费托管！

现在您拥有：

✅ **Vercel** - 国际访问快速
✅ **GitLab Pages** - 免费托管、自动部署
✅ **自动 CI/CD** - 推送代码自动更新
✅ **完全免费** - 无任何费用
✅ **全球访问** - 两个平台都可访问

---

**详细文档**: 查看 `DEPLOY_GITLAB.md`

**祝使用愉快！** 🚀
