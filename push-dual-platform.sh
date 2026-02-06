#!/bin/bash

# 快速双平台推送脚本（不构建，仅推送已有代码）

PROJECT_DIR="/data1/cc/vide-coding/ai-news-hub"
cd "$PROJECT_DIR"

echo "推送到双平台..."
echo ""

# 推送到 GitHub
echo "→ 推送到 GitHub..."
git push origin main

# 推送到 Gitee
echo "→ 推送到 Gitee..."
git push gitee main

echo ""
echo "✅ 推送完成！"
echo ""
echo "Vercel: https://ai-news-hub-rosy.vercel.app/"
echo "Gitee: https://zhao-nancheng.gitee.io/ai-news-hub/"
