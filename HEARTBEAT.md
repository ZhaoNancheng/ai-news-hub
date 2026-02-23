# HEARTBEAT.md

## Token Usage (every hour)
Update token usage to /data1/cc/dashboard/token-status.md

## AI News Auto-Update (daily check)

**规则文档：** `/data1/cc/ai-news/README.md`

### 检查 Cron 任务状态
Every heartbeat, verify:
1. Cron service is running: `systemctl status crond`
2. Crontab exists: `crontab -l | grep ai-news`
3. Last run status: Check `/var/log/ai-news-update.log`

### 检查最新新闻
1. **⭐ CRITICAL**: 调用 `daily-ai-news-allinone` skill 执行完整抓取
   - arXiv 论文（cs.AI + cs.LG）
   - AI 新闻网站（VentureBeat, TechCrunch, MIT Tech Review 等）
   - 社交平台（Hacker News, GitHub, Product Hunt, 36Kr 等）
   - Web 搜索（Brave API）
2. Check today's news file: `/data1/cc/vide-coding/ai-news-hub/docs/news/$(date +%Y-%m-%d).md`
3. If missing or empty → Execute skill: "给我今天的全球AI资讯"
4. If exists → Show summary: "✅ 今日 AI 新闻已更新"
5. Verify research page exists: `/data1/cc/vide-coding/ai-news-hub/docs/research.md`
6. Verify trending page exists: `/data1/cc/vide-coding/ai-news-hub/docs/trending.md`
7. Verify latest-news page updated within 24h

### 检查 Git 同步状态
1. Check for uncommitted changes: `cd /data1/cc/vide-coding/ai-news-hub && git status`
2. Check last commit: `git log --oneline -1`
3. Verify remote is up to date: `git status -sb`
4. Check both remotes (origin + gitlab)

### 检查 Vercel 部署状态
If news was updated today, check:
1. Latest deployment on Vercel Dashboard
2. Deployment status (success/error)
3. Deployment time

### Alert Conditions
Alert user if:
- ❌ Cron service not running
- ❌ Crontab missing or incorrect
- ⚠️  Today's news file missing (before 23:00) → **立即调用 `daily-ai-news-allinone` skill**
- ❌ Last Git push failed (either origin or gitlab)
- ❌ Vercel deployment error

### ⭐ 重要：调用 daily-ai-news-allinone Skill

**何时调用**：
- 每日心跳检查时（如果今日新闻文件缺失或内容不足）
- 用户主动请求："给我今天的AI资讯"、"daily AI news"
- 定期补充（每日 08:00, 12:00, 18:00）

**调用方式**：
```bash
# 方式1：直接执行（推荐）
cd /data1/cc/skills/daily-ai-news-allinone/scripts
python3 fetch_social_platforms.py --source all --limit 15 --deep

# 方式2：通过对话（如果已加载 skill）
"给我今天的全球AI资讯"
```

**完整流程**：
1. 读取 skill 文档：`/data1/cc/skills/daily-ai-news-allinone/SKILL.md`
2. 执行 Phase 1：抓取 arXiv 论文（web_fetch arxiv.org）
3. 执行 Phase 2：抓取社交平台（fetch_social_platforms.py）
4. 执行 Phase 3：Web 搜索（web_search，需要配置 API key）
5. 执行 Phase 4：智能过滤和去重
6. 生成报告并保存到：`/data1/cc/dashboard/ai-news-briefing-YYYY-MM-DD.md`

### Report Format (every heartbeat)
```
📰 AI News System Status:
- Cron: ✅ Running / ❌ Stopped
- Today's News: ✅ Updated / ⚠️ Not yet
- Last Update: [timestamp]
- Git Status: ✅ Clean / ⚠️ Uncommitted
- Git Push: ✅ GitHub + GitLab / ⚠️ Partial / ❌ Failed
- Vercel: ✅ Deployed / ⏳ Processing / ❌ Error
```
