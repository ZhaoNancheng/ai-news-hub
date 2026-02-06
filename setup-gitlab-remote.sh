#!/bin/bash

# GitLab 远程仓库配置助手

echo "=========================================="
echo "  GitLab 远程仓库配置助手"
echo "=========================================="
echo ""

PROJECT_DIR="/data1/cc/vide-coding/ai-news-hub"
cd "$PROJECT_DIR"

# 检查是否已配置 gitlab
if git remote | grep -q "gitlab"; then
    echo "⚠️  GitLab 远程仓库已存在"
    echo ""
    git remote -v | grep gitlab
    echo ""
    read -p "是否删除并重新配置？(y/N): " choice
    if [ "$choice" != "y" ] && [ "$choice" != "Y" ]; then
        echo "取消配置"
        exit 0
    fi
    git remote remove gitlab
    echo "已删除旧的 GitLab 远程仓库"
    echo ""
fi

echo "请按提示输入信息："
echo ""

# 输入 GitLab 用户名
read -p "1. GitLab 用户名: " gitlab_username

# 构造仓库地址
gitlab_url="https://gitlab.com/${gitlab_username}/ai-news-hub.git"

echo ""
echo "将添加 GitLab 远程仓库："
echo "  $gitlab_url"
echo ""

read -p "确认继续？(Y/n): " confirm
if [ "$confirm" == "n" ] || [ "$confirm" == "N" ]; then
    echo "取消配置"
    exit 0
fi

# 添加远程仓库
git remote add gitlab "$gitlab_url"

echo ""
echo "✓ GitLab 远程仓库已添加"
echo ""

# 验证
echo "当前远程仓库："
git remote -v
echo ""

# 推送到 GitLab
echo "=========================================="
echo "  下一步：推送到 GitLab"
echo "=========================================="
echo ""
echo "请运行以下命令推送代码到 GitLab："
echo ""
echo "  git push gitlab main"
echo ""
echo "或使用快速部署脚本："
echo ""
echo "  ./push-dual-platform-gitlab.sh"
echo ""
echo "推送后，GitLab CI/CD 将自动部署到 GitLab Pages"
echo ""
echo "预计访问地址："
echo "  https://${gitlab_username}.gitlab.io/ai-news-hub/"
echo ""
