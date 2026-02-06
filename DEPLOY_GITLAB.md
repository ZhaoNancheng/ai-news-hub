# GitLab Pages 双平台部署配置指南

## 📋 概述

由于 **Gitee Pages 已于 2024 年下线**，本指南将帮您配置 **Vercel + GitLab Pages** 双平台部署。

### 为什么选择 GitLab Pages？

| 特性 | GitLab Pages | 其他方案 |
|------|-------------|---------|
| **完全免费** | ✅ 公开项目永久免费 | ❌ 部分收费 |
| **持续维护** | ✅ 活跃开发 | ⚠️  维护状态不确定 |
| **自动 HTTPS** | ✅ 自动配置 | ✅ 支持 |
| **CI/CD 集成** | ✅ 内置强大 CI/CD | ⚠️  需要额外配置 |
| **国内访问** | ⚠️  中等速度 | ⚠️  取决于平台 |
| **部署方式** | ✅ 自动部署 | ✅ 支持 |

---

## 🚀 快速开始（5分钟配置）

### 第1步：在 GitLab 创建仓库（1分钟）

1. 访问 https://gitlab.com/
2. 点击右上角 **New Project** → **Create blank project**
3. 项目名称：`ai-news-hub`
4. **取消勾选**"Initialize repository with a README"
5. 点击 **Create project**

### 第2步：添加 GitLab 远程仓库（30秒）

```bash
cd /data1/cc/vide-coding/ai-news-hub

# 方式1：使用配置助手（推荐）
./setup-gitlab-remote.sh

# 方式2：手动添加
git remote add gitlab https://gitlab.com/你的用户名/ai-news-hub.git
```

### 第3步：推送到 GitLab（2分钟）

```bash
# 推送代码到 GitLab
git push gitlab main

# 输入 GitLab 用户名和密码（或 Personal Access Token）
```

**提示**：如果推送失败，可能需要使用 Personal Access Token：
1. GitLab → Settings → Access Tokens
2. 创建 token，权限：`write_repository`
3. 推送时用 token 作为密码

### 第4步：等待自动部署（2分钟）

推送成功后，GitLab CI/CD 会自动：
1. 检测到 `.gitlab-ci.yml` 配置文件
2. 启动 CI/CD Pipeline
3. 构建 VitePress 项目
4. 自动部署到 GitLab Pages

访问 CI/CD 状态：
```
https://gitlab.com/你的用户名/ai-news-hub/-/pipelines
```

### 第5步：访问网站（1分钟）

部署完成后（约 2-5 分钟），访问：
```
https://你的用户名.gitlab.io/ai-news-hub/
```

---

## 🌐 双平台访问地址

配置完成后，您的网站可以在两个地址访问：

### 国际访问（推荐）
```
https://ai-news-hub-rosy.vercel.app/
```
- ✅ 全球 CDN 加速
- ✅ 访问速度快
- ✅ 自动 HTTPS

### 国内/全球访问
```
https://你的用户名.gitlab.io/ai-news-hub/
```
- ✅ 免费托管
- ✅ 自动 HTTPS
- ⚠️  国内访问速度中等

---

## 📁 项目结构说明

```
ai-news-hub/
├── .gitlab-ci.yml                  # GitLab CI/CD 配置（核心）
├── deploy-dual-platform-gitlab.sh  # 完整部署脚本
├── push-dual-platform-gitlab.sh    # 快速推送脚本
├── check-gitlab-platform.sh        # 配置检查脚本
└── setup-gitlab-remote.sh          # 配置助手
```

---

## 🔧 GitLab CI/CD 工作流程

### .gitlab-ci.yml 解析

```yaml
# 使用 Node.js 18 镜像
image: node:18

# 定义构建阶段
stages:
  - build    # 构建阶段
  - deploy   # 部署阶段

# 构建任务
build:
  stage: build
  script:
    - npm install
    - npm run docs:build
    - cp -r docs/.vitepress/dist/* public/
  artifacts:
    paths:
      - public

# 部署到 Pages
pages:
  stage: deploy
  dependencies:
    - build
  script:
    - echo "部署到 GitLab Pages"
  artifacts:
    paths:
      - public
  only:
    - main  # 仅在 main 分支触发
```

### 部署流程

```
推送代码到 GitLab
       ↓
GitLab 检测到 .gitlab-ci.yml
       ↓
启动 CI/CD Pipeline
       ↓
┌──────────────┐
│  Build 阶段  │
│  - npm install  │
│  - npm run build │
└──────────────┘
       ↓
┌──────────────┐
│  Deploy 阶段 │
│  - 复制到 public │
│  - 部署到 Pages  │
└──────────────┘
       ↓
✅ 网站上线
```

---

## 💻 日常使用

### 方式1：使用 npm 命令（推荐）

```bash
# 完整部署（构建 + 推送）
npm run deploy:gitlab

# 快速推送（不构建）
npm run push:gitlab
```

### 方式2：使用部署脚本

```bash
# 完整部署
./deploy-dual-platform-gitlab.sh

# 快速推送
./push-dual-platform-gitlab.sh
```

### 方式3：手动 Git 命令

```bash
# 推送到 GitHub（触发 Vercel）
git push origin main

# 推送到 GitLab（触发 GitLab CI/CD）
git push gitlab main

# 同时推送到双平台
git push origin main && git push gitlab main
```

---

## 🛠️ 故障排查

### 问题1：GitLab CI/CD 不运行

**可能原因**：
- `.gitlab-ci.yml` 文件不存在
- 语法错误
- 分支名称不是 `main`

**解决方案**：
```bash
# 1. 检查文件是否存在
ls -la .gitlab-ci.yml

# 2. 验证语法
cat .gitlab-ci.yml

# 3. 检查分支名称
git branch

# 4. 确保已推送到 main 分支
git push gitlab main

# 5. 查看 CI/CD 日志
# 访问: https://gitlab.com/你的用户名/ai-news-hub/-/pipelines
```

---

### 问题2：CI/CD 构建失败

**可能原因**：
- Node.js 版本不兼容
- 依赖安装失败
- 构建命令错误

**解决方案**：
```bash
# 本地测试构建
npm run docs:build

# 检查 Node 版本
node -v  # 应该是 18 或更高

# 清理缓存
rm -rf node_modules package-lock.json
npm install

# 重新推送
git push gitlab main
```

---

### 问题3：GitLab Pages 404 错误

**可能原因**：
- 部署还在进行中
- 项目设置问题
- 权限问题

**解决方案**：
```bash
# 1. 等待 5-10 分钟（首次部署需要时间）
# 2. 检查 CI/CD Pipeline 状态
# 3. 确认项目是 Public（公开）
# 4. 访问 Settings → Pages → 确认配置
```

---

### 问题4：推送时提示权限错误

**解决方案**：

#### 使用 Personal Access Token（推荐）

1. **创建 Token**：
   ```
   GitLab → Settings → Access Tokens
   Token name: deploy-token
   Scopes: write_repository
   创建后复制 token
   ```

2. **使用 Token 推送**：
   ```bash
   # 推送时会提示输入用户名和密码
   # 用户名：任意填写（或留空）
   # 密码：粘贴刚才的 token

   git push gitlab main
   ```

#### 使用 SSH 密钥（更安全）

```bash
# 1. 生成 SSH 密钥
ssh-keygen -t ed25519 -C "your_email@example.com"

# 2. 复制公钥
cat ~/.ssh/id_ed25519.pub

# 3. 添加到 GitLab
# GitLab → Settings → SSH Keys → Add new key

# 4. 修改远程仓库为 SSH
git remote set-url gitlab git@gitlab.com:你的用户名/ai-news-hub.git

# 5. 测试连接
ssh -T git@gitlab.com

# 6. 推送
git push gitlab main
```

---

## 📊 监控部署状态

### 查看 CI/CD Pipeline

```bash
# 方式1：网页查看
https://gitlab.com/你的用户名/ai-news-hub/-/pipelines

# 方式2：使用 GitLab CLI
# 需要先安装 glab
glab ci list

# 方式3：使用 API
curl "https://gitlab.com/api/v4/projects/你的用户名%2Fai-news-hub/pipelines"
```

### 查看部署日志

```bash
# 在 Pipeline 页面
# 点击具体的 job → 查看实时日志
```

---

## 🔄 自动化部署

### 方式1：修改 cron 脚本

编辑 `/data1/cc/vide-coding/scripts/auto-update-ai-news.sh`：

```bash
# 在文件末尾添加
echo ""
echo "=========================================="
echo "  推送到双平台 (GitHub + GitLab)"
echo "=========================================="

cd "$PROJECT_DIR"

# 推送到 GitHub (Vercel)
git push origin main

# 推送到 GitLab (GitLab Pages)
git push gitlab main

echo "✅ 双平台推送完成"
```

### 方式2：创建独立的同步脚本

```bash
#!/bin/bash
# /data1/cc/vide-coding/scripts/sync-to-gitlab.sh

PROJECT_DIR="/data1/cc/vide-coding/ai-news-hub"
cd "$PROJECT_DIR"

# 拉取最新
git pull origin main

# 推送到双平台
git push origin main
git push gitlab main

echo "$(date '+%Y-%m-%d %H:%M:%S') - Synced to dual platform (GitHub + GitLab)" >> /var/gitlab-sync.log
```

添加到 crontab：
```bash
# 每天晚上8点05分同步
5 20 * * * /data1/cc/vide-coding/scripts/sync-to-gitlab.sh
```

---

## 🎯 最佳实践

### 1. 分支策略

```bash
main          # 生产环境（自动部署）
  ↓
develop       # 开发环境（手动部署）
  ↓
feature/*     # 功能分支
```

### 2. 更新流程

```bash
# 1. 编辑内容
vim docs/news/2026-02-06.md

# 2. 本地预览
npm run docs:dev

# 3. 构建并部署到双平台
npm run deploy:gitlab

# 4. 验证
# Vercel: https://ai-news-hub-rosy.vercel.app/
# GitLab: https://你的用户名.gitlab.io/ai-news-hub/
```

### 3. 环境变量（如需要）

在 GitLab 项目设置中：
```
Settings → CI/CD → Variables
```

可以添加敏感信息（API Keys等）

---

## 📚 相关文档

- **GitLab Pages 官方文档**: https://docs.gitlab.com/ee/user/project/pages/
- **GitLab CI/CD 文档**: https://docs.gitlab.com/ee/ci/
- **VitePress 部署指南**: https://vitepress.dev/guide/deploy.html

---

## ✅ 配置检查清单

部署前运行检查脚本：

```bash
./check-gitlab-platform.sh
```

会检查：
- ✅ GitLab 远程仓库配置
- ✅ .gitlab-ci.yml 文件
- ✅ 构建产物
- ✅ 部署脚本
- ✅ npm 命令配置
- ✅ Git 工作区状态

---

## 🎉 完成！

现在您的项目已配置为 **Vercel + GitLab Pages** 双平台部署：

✅ **Vercel** - 国际访问快速
✅ **GitLab Pages** - 免费托管、自动部署
✅ **自动 CI/CD** - 推送代码自动触发
✅ **零成本** - 两个平台都免费

---

## 💡 优化建议

### 提升国内访问速度

如果 GitLab Pages 国内访问较慢，可以考虑：

1. **使用国内 CDN**（如 Cloudflare）
2. **添加国内镜像站点**（阿里云 OSS + CDN）
3. **优化静态资源**（压缩、懒加载）

### 性能优化

```yaml
# 在 .gitlab-ci.yml 中添加缓存
cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - node_modules/
    - .npm/
```

---

**祝使用愉快！** 🚀

如有问题，请查看 GitLab CI/CD 日志或运行 `./check-gitlab-platform.sh` 检查配置。
