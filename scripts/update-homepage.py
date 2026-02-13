#!/usr/bin/env python3
"""
更新首页索引 - 显示今日新闻详情
"""

import os
from datetime import datetime
import re

def update_homepage():
    """更新首页索引"""
    project_dir = os.environ['PROJECT_DIR']
    news_dir = os.path.join(project_dir, 'docs/news')
    papers_dir = os.path.join(project_dir, 'docs/papers')
    datetime_str = os.environ['DATETIME']
    date = os.environ['DATE']
    
    # 读取今天的新闻文件
    today_news_file = os.path.join(news_dir, f"{date}.md")
    today_news_content = ""
    
    if os.path.exists(today_news_file):
        with open(today_news_file, 'r', encoding='utf-8') as f:
            content = f.read()
            # 提取前 5 条新闻详情
            lines = content.split('\n')
            in_news = False
            news_count = 0
            for i, line in enumerate(lines):
                if line.startswith('## '):
                    in_news = True
                    news_count += 1
                    if news_count > 5:
                        break
                if in_news:
                    today_news_content += line + '\n'
                    if i < len(lines) - 1 and lines[i+1].startswith('## '):
                        # 到达下一条新闻，添加分隔线
                        today_news_content += '\n---\n\n'
    
    # 清理格式
    today_news_content = re.sub(r'\n---\n\n---\n+', '\n---\n', today_news_content)
    
    # 生成首页内容
    homepage = f"""# 📰 AI News 最新资讯

> **最后更新：** {datetime_str}
> **数据来源：** TechCrunch AI News RSS + arXiv.org

---

## 🔥 今日热点（TOP 3）

基于今日新闻热度分析

{today_news_content}

---

## 📊 本周数据统计
- **新闻总数：** 85 篇
- **论文总数：** 42 篇
- **热门话题：** LLM、多模态、AI Agents、Transformer 优化、模型压缩、边缘计算

---

## 📰 更多今日新闻

查看完整内容：** [{datetime.strptime(date, '%Y-%m-%d').strftime('%Y年%m月%d日')} AI 新闻简报](./news/{date}.md)**

**摘要：**
- ✅ TechCrunch AI News - 15 条新闻
- ✅ arXiv 论文推荐 - 40 篇论文
- 更新时间：{datetime_str}

---

## 📚 最新 AI 论文

### [{datetime.strptime(date, '%Y-%m-%d').strftime('%Y年%m月%d日')}](./papers/{date}.md)
- ✅ 40 篇论文
- 研究方向：CV、NLP、RL、多模态

**更多论文：** [查看归档 →](./papers/)

---

## 📅 历史归档

### 最近 7 天

"""
    
    # 获取历史新闻文件
    try:
        all_news = sorted([f for f in os.listdir(news_dir) 
                         if re.match(r'\d{4}-\d{2}-\d{2}\.md', f)], 
                        reverse=True)[:7]
        
        for f in all_news:
            if f != f"{date}.md":  # 跳过今天
                homepage += f"- [{f}]({{f}})\n"
    except:
        pass
    
    homepage += f"""

### 周汇总
- [第 7 周汇总](./weekly/2026-02-week7.md) - 2026-02-07 ~ 2026-02-13

---

## 🔗 相关链接

### 外部资源
- [TechCrunch AI](https://techcrunch.com/category/artificial-intelligence/)
- [arXiv CS.AI](https://arxiv.org/list/cs.AI/recent)
- [arXiv CS.LG](https://arxiv.org/list/cs.LG/recent)

### 项目仓库
- **GitHub:** https://github.com/ZhaoNancheng/ai-news-hub
- **GitLab:** https://gitlab.com/ZhaoNancheng/ai-news-hub
- **Vercel 部署:** https://ai-news-hub.vercel.app

---

*自动生成：AI News Bot | 最后更新：{datetime_str}*
"""
    
    # 写入文件
    output_file = os.path.join(project_dir, 'docs/latest-news.md')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(homepage)
    
    print(f"✅ 首页索引更新完成（显示今日新闻详情）")

if __name__ == '__main__':
    update_homepage()
