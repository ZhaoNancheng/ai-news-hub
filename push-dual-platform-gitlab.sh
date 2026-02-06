#!/bin/bash

# 快速双平台推送脚本（Vercel + GitLab）
# 不构建，仅推送已有代码

PROJECT_DIR="/data1/cc/vide-coding/ai-news-hub"
cd "$PROJECT_DIR"

echo "推送到双平台 (GitHub + GitLab)..."
echo ""

# 推送到 GitHub (Vercel)
echo "→ 推送到 GitHub (Vercel 自动触发)..."
git push origin main

# 推送到 GitLab (GitLab Pages)
echo "→ 推送到 GitLab (GitLab CI/CD 自动触发)..."
git push gitlab main

echo ""
echo "✅ 推送完成！"
echo ""
echo "Vercel: https://ai-news-hub-rosy.vercel.app/"
echo "GitLab: https://你的用户名.gitlab.io/ai-news-hub/"
