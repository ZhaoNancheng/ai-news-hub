#!/usr/bin/env python3
"""
多源 AI 新闻抓取脚本 - All-in-One
支持 6 个主要 AI 新闻源：
- TechCrunch AI
- VentureBeat AI
- The Verge AI
- MIT Technology Review
- AI News
- 机器之心
"""

import feedparser
import requests
from datetime import datetime, timedelta
import os
import re
from typing import List, Dict, Any

# 配置
NEWS_SOURCES = {
    'techcrunch': {
        'name': 'TechCrunch AI',
        'url': 'https://techcrunch.com/category/artificial-intelligence/feed/',
        'limit': 10,
        'enabled': True
    },
    'venturebeat': {
        'name': 'VentureBeat AI',
        'url': 'https://venturebeat.com/category/ai/feed/',
        'limit': 8,
        'enabled': True
    },
    'theverge': {
        'name': 'The Verge AI',
        'url': 'https://www.theverge.com/ai-artificial-intelligence/rss/index.xml',
        'limit': 6,
        'enabled': True
    },
    'mit': {
        'name': 'MIT Technology Review',
        'url': 'https://www.technologyreview.com/topnews.rss',
        'limit': 5,
        'enabled': True,
        'filter': 'ai'
    },
    'ainews': {
        'name': 'AI News',
        'url': 'https://artificialintelligence-news.com/feed/',
        'limit': 8,
        'enabled': True
    },
    'jiqizhixin': {
        'name': '机器之心',
        'url': 'https://www.jiqizhixin.com/rss',
        'limit': 8,
        'enabled': True
    }
}

def clean_html(text):
    """清理 HTML 标签"""
    if not text:
        return ''
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

def fetch_rss_feed(source_key: str, source_config: Dict) -> List[Dict[str, Any]]:
    """抓取单个 RSS feed"""
    try:
        print(f"📡 正在抓取 {source_config['name']}...")
        feed = feedparser.parse(source_config['url'])
        entries = feed.entries[:source_config['limit']]
        
        articles = []
        for entry in entries:
            # AI 相关性过滤
            title = entry.get('title', '').lower()
            description = entry.get('description', '').lower()
            
            # AI 关键词检查
            ai_keywords = ['ai', 'artificial intelligence', 'machine learning', 
                          'deep learning', 'llm', 'gpt', 'claude', 'gemini',
                          'neural network', 'robot', 'automation', 'agent']
            
            if not any(keyword in title or keyword in description for keyword in ai_keywords):
                # MIT 需要特别处理，因为它不是纯 AI 源
                if source_key == 'mit' and 'ai' not in title and 'artificial intelligence' not in description:
                    continue
                # 非 MIT 源，如果没有 AI 关键词就跳过
                if source_key != 'mit':
                    continue
            
            article = {
                'title': entry.get('title', ''),
                'link': entry.get('link', ''),
                'description': clean_html(entry.get('description', '')),
                'published': entry.get('published', datetime.now().strftime('%a, %d %b %Y %H:%M:%S %z')),
                'author': entry.get('author', source_config['name']),
                'source': source_config['name']
            }
            articles.append(article)
        
        print(f"  ✅ 获取 {len(articles)} 条新闻")
        return articles
        
    except Exception as e:
        print(f"  ❌ 抓取失败: {e}")
        return []

def deduplicate_articles(all_articles: List[Dict]) -> List[Dict]:
    """去重 - 基于标题相似度"""
    seen = set()
    unique_articles = []
    
    for article in all_articles:
        # 使用标题的前 50 个字符作为去重依据
        title_key = article['title'][:50].lower().strip()
        if title_key not in seen:
            seen.add(title_key)
            unique_articles.append(article)
    
    return unique_articles

def sort_by_recency(articles: List[Dict]) -> List[Dict]:
    """按发布时间排序"""
    def parse_date(date_str):
        try:
            from dateutil import parser
            return parser.parse(date_str)
        except:
            return datetime.min
    
    return sorted(articles, key=lambda x: parse_date(x['published']), reverse=True)

def fetch_all_news():
    """抓取所有新闻源"""
    all_articles = []
    
    # 获取环境变量
    news_dir = os.environ.get('NEWS_DIR', '/data1/cc/vide-coding/ai-news-hub/docs/news')
    date = os.environ.get('DATE', datetime.now().strftime('%Y-%m-%d'))
    datetime_str = os.environ.get('DATETIME', datetime.now().strftime('%Y-%m-%d %H:%M'))
    output_file = os.path.join(news_dir, f"{date}.md")
    
    print(f"\n{'='*60}")
    print(f"  AI 新闻多源抓取开始（All-in-One 版）")
    print(f"{'='*60}")
    print(f"📅 日期：{date}")
    print(f"🕐 时间：{datetime_str}")
    print(f"{'='*60}\n")
    
    # 抓取各个源
    for source_key, config in NEWS_SOURCES.items():
        if config.get('enabled', True):
            articles = fetch_rss_feed(source_key, config)
            all_articles.extend(articles)
    
    print(f"\n{'='*60}")
    print(f"📊 总计获取 {len(all_articles)} 条新闻")
    print(f"{'='*60}")
    
    # 去重
    unique_articles = deduplicate_articles(all_articles)
    print(f"🔄 去重后剩余 {len(unique_articles)} 条")
    
    # 排序
    sorted_articles = sort_by_recency(unique_articles)
    
    # 选择前 20 条最新新闻
    top_articles = sorted_articles[:20]
    
    # 生成 Markdown
    content = generate_markdown(top_articles, date, datetime_str)
    
    # 保存文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ 已保存 {len(top_articles)} 条新闻到 {output_file}")
    print(f"{'='*60}\n")

def generate_markdown(articles: List[Dict], date: str, datetime_str: str) -> str:
    """生成 Markdown 内容"""
    content = f"""# {datetime.strptime(date, '%Y-%m-%d').strftime('%Y年%m月%d日')} AI 新闻简报（多源版）

**来源：** TechCrunch + VentureBeat + The Verge + MIT + AI News + 机器之心
**更新时间：** {datetime_str}
**新闻数量：** {len(articles)} 条

---

## 🔥 今日头条（TOP 5）

"""
    
    # 前 5 条作为头条
    for i, article in enumerate(articles[:5], 1):
        content += format_article(article, i, detailed=True)
        content += "\n"
    
    # 其余新闻
    if len(articles) > 5:
        content += "\n## 📰 更多资讯\n\n"
        for i, article in enumerate(articles[5:], 6):
            content += format_article(article, i, detailed=False)
            content += "\n"
    
    # 数据统计
    source_counts = {}
    for article in articles:
        source = article['source']
        source_counts[source] = source_counts.get(source, 0) + 1
    
    content += "\n## 📊 数据统计\n\n"
    content += "**新闻来源分布：**\n\n"
    for source, count in source_counts.items():
        content += f"- {source}: {count} 条\n"
    
    content += f"""
---

**所有新闻按发布时间排序**
**数据来源：** 6 个主要 AI 新闻源
**更新频率：** 每日 02:00 和 14:00

---

*自动生成：AI News Bot (All-in-One) | 最后更新：{datetime_str}*
"""
    
    return content

def format_article(article: Dict, index: int, detailed: bool = True) -> str:
    """格式化单篇文章"""
    formatted = f"""### {index}. {article['title']}

**📅 发布时间：** {article['published']}
**✍️ 来源：** {article['source']}
**🔗 原文链接：** [{article['title']}]({article['link']})
"""
    
    if detailed:
        description = article['description']
        if len(description) > 400:
            description = description[:400] + '...'
        formatted += f"""
**📝 内容摘要：**
{description}

"""
    else:
        description = article['description']
        if len(description) > 150:
            description = description[:150] + '...'
        if description:
            formatted += f"""
{description}

"""
        else:
            formatted += "\n"
    
    formatted += "---\n"
    return formatted

if __name__ == '__main__':
    fetch_all_news()
