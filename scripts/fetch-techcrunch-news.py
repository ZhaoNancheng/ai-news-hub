#!/usr/bin/env python3
"""
抓取 TechCrunch AI 新闻并保存为 Markdown
优化格式：显示更丰富的内容
"""

import feedparser
import requests
from datetime import datetime
import os
import re

# 配置
RSS_URL = "https://techcrunch.com/category/artificial-intelligence/feed/"

def clean_html(text):
    """清理 HTML 标签"""
    text = re.sub(r'<[^>]+>', '', text)
    text = text.replace('&nbsp;', ' ')
    text = text.replace('&lt;', '<')
    text = text.replace('&gt;', '>')
    text = text.replace('&amp;', '&')
    text = text.replace('&#8217;', "'")
    text = text.replace('&#8216;', "'")
    text = text.replace('&#8220;', '"')
    text = text.replace('&#8221;', '"')
    text = text.replace('&#8230;', '...')
    text = text.replace('&quot;', '"')
    return text.strip()

def fetch_techcrunch_news():
    """抓取 TechCrunch AI 新闻"""
    try:
        feed = feedparser.parse(RSS_URL)
        entries = feed.entries[:15]  # 取前15条
        
        # 获取环境变量
        news_dir = os.environ['NEWS_DIR']
        date = os.environ['DATE']
        datetime_str = os.environ['DATETIME']
        output_file = os.path.join(news_dir, f"{date}.md")
        
        # 生成内容
        content = f"""# {datetime.strptime(date, '%Y-%m-%d').strftime('%Y年%m月%d日')} AI 新闻简报

**来源：** TechCrunch AI News RSS
**更新时间：** {datetime_str}
**新闻数量：** {len(entries)} 条

---

## 🔥 今日头条

"""
        
        # 前3条新闻作为头条
        for i, entry in enumerate(entries[:3], 1):
            title = entry.get('title', '无标题')
            link = entry.get('link', '')
            description = entry.get('description', '')
            published = entry.get('published', datetime.now().strftime('%a, %d %b %Y %H:%M:%S %z'))
            author = entry.get('author', 'TechCrunch')
            
            # 清理 HTML
            description = clean_html(description)
            if len(description) > 400:
                description = description[:400] + '...'
            
            content += f"""
### {i}. {title}

**📅 发布时间：** {published}
**✍️ 作者：** {author}
**🔗 原文链接：** [{title}]({link})

**📝 内容摘要：**
{description}

---
"""
        
        # 其余新闻
        content += """
## 📰 更多资讯

"""
        
        for i, entry in enumerate(entries[3:], 4):
            title = entry.get('title', '无标题')
            link = entry.get('link', '')
            description = entry.get('description', '')
            published = entry.get('published', datetime.now().strftime('%a, %d %b %Y %H:%M:%S %z'))
            
            # 清理 HTML
            description = clean_html(description)
            if len(description) > 150:
                description = description[:150] + '...'
            
            content += f"""
### {i}. {title}

**📅 时间：** {published}
**🔗 链接：** [{title}]({link})

{description}

---
"""
        
        content += f"""
## 📊 数据统计

- **新闻来源：** TechCrunch AI News
- **更新频率：** 每日 22:00 和 02:00
- **RSS 地址：** https://techcrunch.com/category/artificial-intelligence/feed/

---

*自动生成：AI News Bot | 最后更新：{datetime_str}*
"""
        
        # 保存文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ 已保存 {len(entries)} 条新闻到 {output_file}")
        
    except Exception as e:
        print(f"❌ 抓取新闻失败: {e}")
        exit(1)

if __name__ == '__main__':
    fetch_techcrunch_news()
