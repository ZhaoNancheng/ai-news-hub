# GitLab Pages 部署指南

## 🚀 快速开始（3步完成）

### 第1步：添加 GitLab 远程仓库

```bash
cd /data1/cc/vide-coding/ai-news-hub

# 运行配置助手
./setup-gitlab.sh

# 或手动添加
git remote add gitlab https://gitlab.com/你的用户名/ai-news-hub.git
```

### 第2步：推送到 GitLab

```bash
# 推送代码到 GitLab
git push gitlab main

# 输入 GitLab 用户名和密码
# 或使用 Personal Access Token
```

**获取 Token**（推荐）：
1. GitLab → Settings → Access Tokens
2. Token name: `deploy-token`
3. Scopes: 勾选 `write_repository`
4. 创建后复制 token
5. 推送时用 token 作为密码

### 第3步：等待自动部署（2-5分钟）

推送成功后，GitLab CI/CD 会自动：
1. 检测到 `.gitlab-ci.yml`
2. 启动 CI/CD Pipeline
3. 构建 VitePress 项目
4. 部署到 GitLab Pages

**查看部署状态**：
```
https://gitlab.com/你的用户名/ai-news-hub/-/pipelines
```

部署完成后访问：
```
https://你的用户名.gitlab.io/ai-news-hub/
```

---

## 🌐 双平台访问

配置完成后，您的网站可在两个地址访问：

### 国际访问（Vercel）
```
https://ai-news-hub-rosy.vercel.app/
```
✅ 全球 CDN，速度快

### 国内/全球访问（GitLab Pages）
```
https://你的用户名.gitlab.io/ai-news-hub/
```
✅ 免费托管，自动部署

---

## 💻 日常使用

### 更新内容后部署

```bash
# 方式1：使用快速推送脚本
./push-to-gitlab.sh

# 方式2：手动推送
git push gitlab main

# 方式3：同时推送到 GitHub 和 GitLab
git push origin main && git push gitlab main
```

---

## 🔧 配置验证

```bash
# 查看远程仓库
git remote -v

# 应该看到：
# origin    git@github.com:ZhaoNancheng/ai-news-hub.git (fetch)
# origin    git@github.com:ZhaoNancheng/ai-news-hub.git (push)
# gitlab    https://gitlab.com/你的用户名/ai-news-hub.git (fetch)
# gitlab    https://gitlab.com/你的用户名/ai-news-hub.git (push)
```

---

## 🛠️ 故障排查

### Q1: 推送时提示权限错误？

**A**: 使用 Personal Access Token
```bash
git push gitlab main
# Username: <任意填写>
# Password: <粘贴 token>
```

### Q2: CI/CD 不运行？

**A**: 检查以下几点
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

**A**: 可能原因
1. 部署还在进行中（等待 5-10 分钟）
2. 项目不是 Public（设置为公开）
3. CI/CD 失败（查看日志）

---

## ✅ 完成检查清单

- [ ] 在 GitLab 创建了仓库 `ai-news-hub`
- [ ] 运行了 `./setup-gitlab.sh` 添加远程仓库
- [ ] 成功推送代码到 GitLab：`git push gitlab main`
- [ ] 看到 CI/CD Pipeline 在运行
- [ ] Pipeline 成功完成（绿色勾）
- [ ] 可以访问 `https://你的用户名.gitlab.io/ai-news-hub/`

---

## 📚 相关文档

- **GitLab Pages 官方文档**: https://docs.gitlab.com/ee/user/project/pages/
- **GitLab CI/CD 文档**: https://docs.gitlab.com/ee/ci/
- **VitePress 部署指南**: https://vitepress.dev/guide/deploy.html

---

**祝使用愉快！** 🚀
