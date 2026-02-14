# 📝 脚本更新说明

## ✅ 已完成的更新

### 1. 主更新脚本
- ✅ **新建** `scripts/auto-update-ai-news-v5.sh`
  - 移除了对不存在的 Python 脚本的调用
  - 更新文件路径：移除 `docs/latest-news.md`
  - 新增对 `docs/industry.md` 的引用
  - 更新 commit message

### 2. 推送脚本
- ✅ **新建** `push-to-remotes.sh`（替代 `push-to-gitlab.sh`）
  - 支持同时推送到 GitHub + GitLab
  - 添加状态检查
  - 更新部署链接

### 3. 备份文件
- ✅ **备份** `auto-update-ai-news-v4.sh` → `auto-update-ai-news-v4.sh.backup`
- ✅ **备份** `push-to-gitlab.sh` → `push-to-gitlab.sh.backup`

---

## ⏳ 下一步操作

### 1. 更新 Crontab
```bash
# 编辑 crontab
crontab -e

# 替换这一行：
0 22 * * * /data1/cc/vide-coding/ai-news-hub/scripts/auto-update-ai-news-v4.sh >> /var/log/ai-news-update.log 2>&1
0 2 * * * /data1/cc/vide-coding/ai-news-hub/scripts/auto-update-ai-news-v4.sh >> /var/log/ai-news-update.log 2>&1

# 为：
0 22 * * * /data1/cc/vide-coding/ai-news-hub/scripts/auto-update-ai-news-v5.sh >> /var/log/ai-news-update.log 2>&1
0 2 * * * /data1/cc/vide-coding/ai-news-hub/scripts/auto-update-ai-news-v5.sh >> /var/log/ai-news-update.log 2>&1
```

### 2. 创建缺失的 Python 脚本
需要创建以下脚本（如果需要自动化抓取行业新闻）：
- `scripts/fetch_industry_news.py` - 抓取 TechCrunch 等行业新闻
- `scripts/update_research.py` - 更新研究前沿页面
- `scripts/update_trending.py` - 更新热门推荐页面

### 3. 测试脚本
```bash
# 手动测试
/data1/cc/vide-coding/ai-news-hub/scripts/auto-update-ai-news-v5.sh
```

---

## 📋 注意事项

1. **v5.0 脚本目前是简化版本**，移除了对不存在的 Python 脚本的调用
2. **arXiv 抓取仍然工作**：保留了 `fetch_arxiv_news.py`
3. **行业动态和热门推荐需要手动更新**，直到创建对应的 Python 脚本
