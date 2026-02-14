#!/bin/bash

# 快速推送到 GitHub + GitLab

PROJECT_DIR="/data1/cc/vide-coding/ai-news-hub"
cd "$PROJECT_DIR"

echo "=========================================="
echo "  快速推送脚本 v2.0"
echo "=========================================="
echo "时间: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# 检查是否有未提交的更改
if [[ -z $(git status --porcelain) ]]; then
    echo "⚠️  没有未提交的更改"
    echo ""
    exit 0
fi

echo "📝 未提交的更改："
git status --short
echo ""

# 推送到 GitHub
echo "→ 推送到 GitHub (Vercel 自动触发)..."
git push origin main || echo "⚠️  GitHub 推送失败"

echo ""
echo "→ 推送到 GitLab (GitLab CI/CD 自动触发)..."
git push gitlab main || echo "⚠️  GitLab 推送失败"

echo ""
echo "✅ 推送完成！"
echo ""
echo "🌐 查看部署状态:"
echo "   Vercel:  https://vercel.com/zhao-nancheng/ai-news-hub"
echo "   GitLab: https://gitlab.com/ZhaoNancheng/ai-news-hub/-/pipelines"
echo ""
echo "🌐 访问地址:"
echo "   https://ai-news-hub.vercel.app"
echo ""
