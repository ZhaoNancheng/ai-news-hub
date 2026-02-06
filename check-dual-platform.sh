#!/bin/bash

# 双平台部署配置检查脚本

PROJECT_DIR="/data1/cc/vide-coding/ai-news-hub"
cd "$PROJECT_DIR"

echo "=========================================="
echo "  双平台部署配置检查"
echo "=========================================="
echo ""

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# 检查项1：远程仓库配置
echo -e "${BLUE}[检查 1/5] 远程仓库配置${NC}"
if git remote | grep -q "gitee"; then
    echo -e "${GREEN}✓ Gitee 远程仓库已配置${NC}"
    git remote -v | grep gitee
else
    echo -e "${RED}✗ Gitee 远程仓库未配置${NC}"
    echo -e "${YELLOW}  请运行: git remote add gitee <你的gitee仓库地址>${NC}"
fi
echo ""

# 检查项2：构建产物
echo -e "${BLUE}[检查 2/5] VitePress 构建产物${NC}"
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

# 检查项3：部署脚本
echo -e "${BLUE}[检查 3/5] 部署脚本${NC}"
if [ -x "deploy-dual-platform.sh" ]; then
    echo -e "${GREEN}✓ deploy-dual-platform.sh 可执行${NC}"
else
    echo -e "${YELLOW}⚠ deploy-dual-platform.sh 不可执行${NC}"
    echo -e "${YELLOW}  请运行: chmod +x deploy-dual-platform.sh${NC}"
fi

if [ -x "push-dual-platform.sh" ]; then
    echo -e "${GREEN}✓ push-dual-platform.sh 可执行${NC}"
else
    echo -e "${YELLOW}⚠ push-dual-platform.sh 不可执行${NC}"
    echo -e "${YELLOW}  请运行: chmod +x push-dual-platform.sh${NC}"
fi
echo ""

# 检查项4：npm 脚本
echo -e "${BLUE}[检查 4/5] npm 脚本配置${NC}"
if grep -q '"deploy:dual"' package.json; then
    echo -e "${GREEN}✓ npm run deploy:dual 已配置${NC}"
else
    echo -e "${YELLOW}⚠ npm run deploy:dual 未配置${NC}"
fi

if grep -q '"push:dual"' package.json; then
    echo -e "${GREEN}✓ npm run push:dual 已配置${NC}"
else
    echo -e "${YELLOW}⚠ npm run push:dual 未配置${NC}"
fi
echo ""

# 检查项5：Git 状态
echo -e "${BLUE}[检查 5/5] Git 工作区状态${NC}"
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
if git remote | grep -q "gitee"; then
    echo -e "${GREEN}✅ 配置完成！可以使用以下命令部署：${NC}"
    echo ""
    echo "  完整部署（构建 + 推送）："
    echo "    npm run deploy:dual"
    echo "    或"
    echo "    ./deploy-dual-platform.sh"
    echo ""
    echo "  快速推送（不构建）："
    echo "    npm run push:dual"
    echo "    或"
    echo "    ./push-dual-platform.sh"
else
    echo -e "${YELLOW}⚠️  需要先配置 Gitee 远程仓库：${NC}"
    echo ""
    echo "  步骤："
    echo "  1. 在 Gitee 创建仓库: https://gitee.com/"
    echo "  2. 添加远程仓库:"
    echo "     git remote add gitee <你的gitee仓库地址>"
    echo "  3. 推送代码:"
    echo "     git push gitee main"
    echo "  4. 启用 Gitee Pages 服务"
    echo ""
    echo "  详细说明请查看: DEPLOY_DUAL_PLATFORM.md"
fi

echo ""
