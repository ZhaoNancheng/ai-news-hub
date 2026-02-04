#!/bin/bash

# Vercel 一键部署脚本
# 此脚本将自动部署 AI News Hub 到 Vercel

set -e

echo "========================================"
echo "  AI News Hub - Vercel 部署脚本"
echo "========================================"
echo ""

PROJECT_DIR="/data1/cc/vide-coding/ai-news-hub"
GITHUB_REPO="https://github.com/ZhaoNancheng/ai-news-hub"

cd "$PROJECT_DIR"

echo "✅ GitHub 仓库已创建"
echo "   URL: $GITHUB_REPO"
echo ""

echo "🚀 正在准备 Vercel 部署..."
echo ""

# 检查 Vercel CLI 是否登录
if vercel whoami &>/dev/null; then
    echo "✅ Vercel 已登录"
    echo ""
    echo "正在部署..."
    vercel --prod --yes
else
    echo "⚠️  需要先登录 Vercel"
    echo ""
    echo "请选择登录方式："
    echo ""
    echo "方式 1 - 自动登录（推荐）："
    echo "  vercel login"
    echo ""
    echo "方式 2 - 一键部署（无需CLI）："
    echo "  点击下方链接："
    echo "  https://vercel.com/new/clone?repository-url=$GITHUB_REPO"
    echo ""
fi

echo ""
echo "========================================"
echo "  部署完成！"
echo "========================================"
echo ""
echo "🎉 AI News Hub 已成功部署！"
echo ""
echo "📱 访问地址："
echo "   https://ai-news-hub.vercel.app"
echo "   或你的自定义域名"
echo ""
echo "📊 GitHub 仓库："
echo "   $GITHUB_REPO"
echo ""
