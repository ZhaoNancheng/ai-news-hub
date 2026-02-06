#!/bin/bash

# 一键配置 Gitee 远程仓库的辅助脚本

echo "=========================================="
echo "  Gitee 远程仓库配置助手"
echo "=========================================="
echo ""

PROJECT_DIR="/data1/cc/vide-coding/ai-news-hub"
cd "$PROJECT_DIR"

# 检查是否已配置 gitee
if git remote | grep -q "gitee"; then
    echo "⚠️  Gitee 远程仓库已存在"
    echo ""
    git remote -v | grep gitee
    echo ""
    read -p "是否删除并重新配置？(y/N): " choice
    if [ "$choice" != "y" ] && [ "$choice" != "Y" ]; then
        echo "取消配置"
        exit 0
    fi
    git remote remove gitee
    echo "已删除旧的 Gitee 远程仓库"
    echo ""
fi

echo "请按提示输入信息："
echo ""

# 输入 Gitee 用户名
read -p "1. Gitee 用户名: " gitee_username

# 构造仓库地址
gitee_url="https://gitee.com/${gitee_username}/ai-news-hub.git"

echo ""
echo "将添加 Gitee 远程仓库："
echo "  $gitee_url"
echo ""

read -p "确认继续？(Y/n): " confirm
if [ "$confirm" == "n" ] || [ "$confirm" == "N" ]; then
    echo "取消配置"
    exit 0
fi

# 添加远程仓库
git remote add gitee "$gitee_url"

echo ""
echo "✓ Gitee 远程仓库已添加"
echo ""

# 验证
echo "当前远程仓库："
git remote -v
echo ""

# 推送到 Gitee
echo "=========================================="
echo "  下一步：推送到 Gitee"
echo "=========================================="
echo ""
echo "请运行以下命令推送代码到 Gitee："
echo ""
echo "  git push gitee main"
echo ""
echo "或使用快速部署脚本："
echo ""
echo "  ./push-dual-platform.sh"
echo ""
echo "推送后，请访问 Gitee 启用 Pages 服务："
echo "  1. 打开: $gitee_url"
echo "  2. 点击: 服务 → Gitee Pages"
echo "  3. 分支选择: main"
echo "  4. 目录填写: docs/.vitepress/dist"
echo "  5. 点击: 启动"
echo ""
