#!/bin/bash

# GitLab 部署配置检查脚本

PROJECT_DIR="/data1/cc/vide-coding/ai-news-hub"
cd "$PROJECT_DIR"

echo "=========================================="
echo "  GitLab 部署配置检查"
echo "=========================================="
echo ""

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# 检查项1：远程仓库配置
echo -e "${BLUE}[检查 1/6] 远程仓库配置${NC}"
if git remote | grep -q "gitlab"; then
    echo -e "${GREEN}✓ GitLab 远程仓库已配置${NC}"
    git remote -v | grep gitlab
else
    echo -e "${RED}✗ GitLab 远程仓库未配置${NC}"
    echo -e "${YELLOW}  请运行: git remote add gitlab <你的gitlab仓库地址>${NC}"
    echo -e "${YELLOW}  或运行: ./setup-gitlab-remote.sh${NC}"
fi
echo ""

# 检查项2：.gitlab-ci.yml 配置
echo -e "${BLUE}[检查 2/6] GitLab CI/CD 配置${NC}"
if [ -f ".gitlab-ci.yml" ]; then
    echo -e "${GREEN}✓ .gitlab-ci.yml 存在${NC}"
    if grep -q "pages:" .gitlab-ci.yml; then
        echo -e "${GREEN}  ✓ pages 任务已配置${NC}"
    else
        echo -e "${YELLOW}  ⚠ pages 任务未配置${NC}"
    fi
else
    echo -e "${RED}✗ .gitlab-ci.yml 不存在${NC}"
    echo -e "${YELLOW}  GitLab CI/CD 将不会运行${NC}"
fi
echo ""

# 检查项3：构建产物
echo -e "${BLUE}[检查 3/6] VitePress 构建产物${NC}"
if [ -d "docs/.vitepress/dist" ]; then
    FILE_COUNT=$(find docs/.vitepress/dist -type f | wc -l)
    echo -e "${GREEN}✓ 构建产物存在${NC} ($FILE_COUNT 个文件)"

    # 检查关键文件
    if [ -f "docs/.vitepress/dist/index.html" ]; then
        echo -e "${GREEN}  ✓ index.html 存在${NC}"
    else
        echo -e "${RED}  ✗ index.html 缺失${NC}"
    fi

    if [ -f "docs/.vitepress/dist/favicon.ico" ]; then
        echo -e "${GREEN}  ✓ favicon.ico 存在${NC}"
    else
        echo -e "${YELLOW}  ⚠ favicon.ico 缺失${NC}"
    fi
else
    echo -e "${RED}✗ 构建产物不存在${NC}"
    echo -e "${YELLOW}  请运行: npm run docs:build${NC}"
fi
echo ""

# 检查项4：部署脚本
echo -e "${BLUE}[检查 4/6] 部署脚本${NC}"
if [ -x "deploy-dual-platform-gitlab.sh" ]; then
    echo -e "${GREEN}✓ deploy-dual-platform-gitlab.sh 可执行${NC}"
else
    echo -e "${YELLOW}⚠ deploy-dual-platform-gitlab.sh 不可执行${NC}"
    echo -e "${YELLOW}  请运行: chmod +x deploy-dual-platform-gitlab.sh${NC}"
fi

if [ -x "push-dual-platform-gitlab.sh" ]; then
    echo -e "${GREEN}✓ push-dual-platform-gitlab.sh 可执行${NC}"
else
    echo -e "${YELLOW}⚠ push-dual-platform-gitlab.sh 不可执行${NC}"
    echo -e "${YELLOW}  请运行: chmod +x push-dual-platform-gitlab.sh${NC}"
fi
echo ""

# 检查项5：npm 脚本
echo -e "${BLUE}[检查 5/6] npm 脚本配置${NC}"
if grep -q '"deploy:gitlab"' package.json; then
    echo -e "${GREEN}✓ npm run deploy:gitlab 已配置${NC}"
else
    echo -e "${YELLOW}⚠ npm run deploy:gitlab 未配置${NC}"
fi

if grep -q '"push:gitlab"' package.json; then
    echo -e "${GREEN}✓ npm run push:gitlab 已配置${NC}"
else
    echo -e "${YELLOW}⚠ npm run push:gitlab 未配置${NC}"
fi
echo ""

# 检查项6：Git 状态
echo -e "${BLUE}[检查 6/6] Git 工作区状态${NC}"
if [ -z "$(git status --porcelain)" ]; then
    echo -e "${GREEN}✓ Git 工作区干净${NC}"
else
    echo -e "${YELLOW}⚠ 有未提交的更改${NC}"
    git status --short
fi
echo ""

# 总结
echo "=========================================="
echo "  检查完成"
echo "=========================================="
echo ""

# 提供下一步建议
if git remote | grep -q "gitlab"; then
    if [ -f ".gitlab-ci.yml" ]; then
        echo -e "${GREEN}✅ 配置完成！可以使用以下命令部署：${NC}"
        echo ""
        echo "  完整部署（构建 + 推送）："
        echo "    npm run deploy:gitlab"
        echo "    或"
        echo "    ./deploy-dual-platform-gitlab.sh"
        echo ""
        echo "  快速推送（不构建）："
        echo "    npm run push:gitlab"
        echo "    或"
        echo "    ./push-dual-platform-gitlab.sh"
    else
        echo -e "${YELLOW}⚠️  GitLab 远程仓库已配置，但缺少 CI/CD 配置${NC}"
        echo ""
        echo "  请确保 .gitlab-ci.yml 文件存在并已提交"
    fi
else
    echo -e "${YELLOW}⚠️  需要先配置 GitLab 远程仓库：${NC}"
    echo ""
    echo "  步骤："
    echo "  1. 在 GitLab 创建仓库: https://gitlab.com/"
    echo "  2. 添加远程仓库:"
    echo "     git remote add gitlab <你的gitlab仓库地址>"
    echo "     或运行: ./setup-gitlab-remote.sh"
    echo "  3. 推送代码:"
    echo "     git push gitlab main"
    echo "  4. GitLab CI/CD 将自动部署到 Pages"
    echo ""
    echo "  详细说明请查看: DEPLOY_GITLAB.md"
fi

echo ""
