# 双平台同步部署配置指南

## 📋 概述

本项目支持同时部署到两个平台：
- **Vercel**: 国际访问，自动部署
- **Gitee Pages**: 国内访问，自动部署

---

## 🚀 快速开始

### 方案一：首次配置（推荐）

#### 1. 在 Gitee 创建仓库

1. 访问 https://gitee.com/
2. 创建新仓库：`ai-news-hub`
3. **不要**初始化 README（因为我们已有代码）
4. 记下仓库地址

#### 2. 添加 Gitee 远程仓库

```bash
cd /data1/cc/vide-coding/ai-news-hub

# 添加 Gitee 远程仓库
git remote add gitee https://gitee.com/你的用户名/ai-news-hub.git

# 验证远程仓库
git remote -v

# 应该看到：
# origin    git@github.com:ZhaoNancheng/ai-news-hub.git (fetch)
# origin    git@github.com:ZhaoNancheng/ai-news-hub.git (push)
# gitee     https://gitee.com/你的用户名/ai-news-hub.git (fetch)
# gitee     https://gitee.com/你的用户名/ai-news-hub.git (push)
```

#### 3. 首次推送到 Gitee

```bash
# 推送代码到 Gitee
git push gitee main

# 输入 Gitee 账号密码
```

#### 4. 启用 Gitee Pages

1. 访问你的 Gitee 仓库
2. 点击 **服务** → **Gitee Pages**
3. 配置：
   - **分支**: `main`
   - **目录**: `docs/.vitepress/dist`
4. 点击 **启动**
5. 等待部署完成（1-3分钟）
6. 访问：`https://你的用户名.gitee.io/ai-news-hub`

---

### 方案二：使用自动部署脚本

#### 完整部署（构建 + 推送）

```bash
cd /data1/cc/vide-coding/ai-news-hub

# 方式1：使用脚本
./deploy-dual-platform.sh

# 方式2：使用 npm 命令
npm run deploy:dual
```

**脚本功能：**
- ✅ 检查 Git 状态
- ✅ 拉取最新代码
- ✅ 安装依赖
- ✅ 构建 VitePress
- ✅ 提交构建产物
- ✅ 推送到 GitHub（触发 Vercel）
- ✅ 推送到 Gitee（触发 Gitee Pages）

#### 快速推送（仅推送，不构建）

```bash
# 方式1：使用脚本
./push-dual-platform.sh

# 方式2：使用 npm 命令
npm run push:dual
```

**适用场景：**
- 仅推送代码更改
- 构建产物已存在
- 快速同步到双平台

---

## 🔄 自动化工作流

### 每日自动部署（推荐）

#### 方法1：修改现有 cron 脚本

编辑 `/data1/cc/vide-coding/scripts/auto-update-ai-news.sh`，在末尾添加：

```bash
# 在文件末尾添加
echo ""
echo "=========================================="
echo "  推送到双平台"
echo "=========================================="

cd "$PROJECT_DIR"

# 推送到 GitHub
git push origin main

# 推送到 Gitee
git push gitee main

echo "✅ 双平台推送完成"
```

#### 方法2：创建独立的同步脚本

```bash
#!/bin/bash
# /data1/cc/vide-coding/scripts/sync-to-dual-platform.sh

PROJECT_DIR="/data1/cc/vide-coding/ai-news-hub"
cd "$PROJECT_DIR"

# 拉取最新
git pull origin main

# 推送到双平台
git push origin main
git push gitee main

echo "$(date '+%Y-%m-%d %H:%M:%S') - Synced to dual platform" >> /var/log/dual-platform-sync.log
```

添加到 crontab：

```bash
# 每天晚上8点05分同步
5 20 * * * /data1/cc/vide-coding/scripts/sync-to-dual-platform.sh
```

---

## 🌐 访问地址对比

### 国际访问
```
https://ai-news-hub-rosy.vercel.app/
```
- ✅ 全球 CDN 加速
- ✅ 自动 HTTPS
- ⚠️  国内访问较慢（需要翻墙）

### 国内访问
```
https://zhao-nancheng.gitee.io/ai-news-hub/
```
- ✅ 国内服务器
- ✅ 访问速度快
- ✅ 自动 HTTPS
- ⚠️  国际访问较慢

---

## 🛠️ 故障排查

### 问题1：Gitee 推送失败

**错误信息：**
```
fatal: 'gitee' does not appear to be a git repository
```

**解决方案：**
```bash
# 添加 Gitee 远程仓库
git remote add gitee https://gitee.com/你的用户名/ai-news-hub.git

# 验证
git remote -v
```

---

### 问题2：Gitee Pages 部署失败

**可能原因：**
1. 构建目录不正确
2. 分支名称不匹配
3. 仓库包含过大文件

**解决方案：**

#### 检查构建目录
```bash
# 确认 dist 目录存在
ls -la docs/.vitepress/dist/

# 应该看到 index.html 等文件
```

#### 重新配置 Gitee Pages
1. 进入 Gitee 仓库
2. 服务 → Gitee Pages
3. 点击 **更新**（重新部署）
4. 等待 1-3 分钟

---

### 问题3：双平台内容不一致

**可能原因：**
- 构建时间不同步
- 推送顺序问题

**解决方案：**
```bash
# 使用完整部署脚本
./deploy-dual-platform.sh

# 或手动构建后推送
npm run docs:build
git add docs/.vitepress/dist/
git commit -m "Build: update"
git push origin main
git push gitee main
```

---

## 📊 部署状态检查

### Vercel 部署状态
```bash
# 访问 Vercel Dashboard
https://vercel.com/zhao-nancheng-s-projects

# 或使用 CLI
vercel list
```

### Gitee Pages 部署状态
```bash
# 访问 Gitee Pages 服务页面
https://gitee.com/zhao-nancheng/ai-news-hub/pages

# 查看部署日志和状态
```

---

## 💡 最佳实践

### 1. 日常开发流程

```bash
# 1. 编辑代码
vim docs/news/2026-02-06.md

# 2. 本地预览
npm run docs:dev

# 3. 构建并部署到双平台
npm run deploy:dual

# 4. 访问验证
# Vercel: https://ai-news-hub-rosy.vercel.app/
# Gitee: https://zhao-nancheng.gitee.io/ai-news-hub/
```

### 2. 自动化建议

#### 在 crontab 中添加：
```bash
# 每天早上8点05分自动同步
5 8 * * * cd /data1/cc/vide-coding/ai-news-hub && npm run deploy:dual >> /var/log/dual-platform-deploy.log 2>&1
```

### 3. 监控日志

```bash
# 查看部署日志
tail -f /var/log/dual-platform-deploy.log

# 查看同步日志
tail -f /var/log/dual-platform-sync.log
```

---

## 🔐 配置 Git 凭证（避免每次输入密码）

### 方法1：使用 SSH 密钥（推荐）

```bash
# 生成 SSH 密钥
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

# 复制公钥
cat ~/.ssh/id_rsa.pub

# 添加到 GitHub
# Settings → SSH and GPG keys → New SSH key

# 添加到 Gitee
# 设置 → SSH 公钥 → 添加公钥

# 修改远程仓库为 SSH
git remote set-url origin git@github.com:ZhaoNancheng/ai-news-hub.git
git remote set-url gitee git@gitee.com:你的用户名/ai-news-hub.git
```

### 方法2：使用 Git 凭证存储

```bash
# 安装 git-credential-helper
sudo yum install git-credential-libsecret

# 配置凭证存储
git config --global credential.helper store

# 首次推送时输入密码后会保存
git push gitee main
```

---

## 📝 快速命令参考

```bash
# 查看远程仓库
git remote -v

# 添加 Gitee 远程仓库
git remote add gitee <gitee仓库地址>

# 删除远程仓库
git remote remove gitee

# 完整部署（构建 + 推送）
npm run deploy:dual

# 快速推送（不构建）
npm run push:dual

# 仅推送到 GitHub
git push origin main

# 仅推送到 Gitee
git push gitee main

# 同时推送到双平台
git push origin main && git push gitee main
```

---

## 🎉 完成！

现在您的项目已经配置为双平台同步部署：

✅ **Vercel** - 国际访问快速
✅ **Gitee Pages** - 国内访问快速
✅ **自动部署** - 推送代码自动触发
✅ **零成本** - 两个平台都免费

---

## 📞 需要帮助？

如果遇到问题，请检查：
1. Gitee 远程仓库是否正确添加
2. 推送权限是否正确
3. Gitee Pages 服务是否已启动
4. 构建目录路径是否正确

---

**祝您使用愉快！** 🚀
