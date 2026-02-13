#!/usr/bin/env python3
"""
增强版多源抓取 - 集成分类和评分系统
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

# 导入分类和评分函数
exec(open('/data1/cc/vide-coding/ai-news-hub/scripts/content-classifier.py').read())
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
                if source_key == 'mit' and 'ai' not in title and 'artificial intelligence' not in description:
                    continue
                if source_key != 'mit':
                    continue
            
            # 清理 HTML
            clean_desc = clean_html(entry.get('description', ''))
            
            article = {
                'title': entry.get('title', ''),
                'link': entry.get('link', ''),
                'description': clean_desc,
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

def sort_by_priority(articles: List[Dict]) -> List[Dict]:
    """按优先级评分排序"""
    scored_articles = []
    
    for article in articles:
        score = calculate_priority_score(
            article['title'],
            article.get('description', ''),
            article['source']
        )
        article['priority_score'] = score
        scored_articles.append(article)
    
    # 按评分降序排序
    return sorted(scored_articles, key=lambda x: x['priority_score'], reverse=True)

def fetch_all_news():
    """抓取所有新闻源"""
    all_articles = []
    
    # 获取环境变量
    news_dir = os.environ.get('NEWS_DIR', '/data1/cc/vide-coding/ai-news-hub/docs/news')
    date = os.environ.get('DATE', datetime.now().strftime('%Y-%m-%d'))
    datetime_str = os.environ.get('DATETIME', datetime.now().strftime('%Y-%m-%d %H:%M'))
    output_file = os.path.join(news_dir, f"{date}.md")
    
    print(f"\n{'='*60}")
    print(f"  AI 新闻多源抓取开始（Enhanced 版）")
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
    
    # 按优先级排序
    prioritized_articles = sort_by_priority(unique_articles)
    
    # 选择前 25 条高质量新闻
    top_articles = prioritized_articles[:25]
    
    # 生成 Markdown
    content = generate_markdown_enhanced(top_articles, date, datetime_str)
    
    # 保存文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ 已保存 {len(top_articles)} 条新闻到 {output_file}")
    print(f"{'='*60}\n")

def generate_summary(articles: List[Dict], top_n: int = 5) -> str:
    """
    生成每日热点总结
    """
    from collections import Counter
    
    # 按优先级排序
    scored_articles = sorted(articles, key=lambda x: x.get('priority_score', 0), reverse=True)
    
    # 选择 top N
    top_articles = scored_articles[:top_n]
    
    # 提取关键主题
    all_tags = []
    for article in top_articles:
        categories, _ = classify_content(article['title'], article.get('description', ''))
        all_tags.extend(categories)
    
    # 统计最常见主题
    top_topics = [tag for tag, count in Counter(all_tags).most_common(5)]
    
    # 生成总结
    summary = f"""## 🔥 今日热点总结

**最热门主题：** {' • '.join(top_topics[:3])}

**今日 {top_n} 大事件：**

"""
    
    for i, article in enumerate(top_articles, 1):
        title = article.get('title', '')
        source = article.get('source', '')
        score = article.get('priority_score', 0)
        
        summary += f"""### {i}. {title}
**来源：** {source} • **优先级：** {score:.1f}/100

"""
    
    return summary

def generate_markdown_enhanced(articles: List[Dict], date: str, datetime_str: str) -> str:
    """生成增强版 Markdown 内容"""
    
    # 生成今日总结
    summary = generate_summary(articles, top_n=3)
    
    content = f"""# {datetime.strptime(date, '%Y-%m-%d').strftime('%Y年%m月%d日')} AI 新闻简报（增强版）

**来源：** TechCrunch + VentureBeat + The Verge + MIT + AI News + 机器之心
**更新时间：** {datetime_str}
**新闻数量：** {len(articles)} 条（按优先级排序）

---

{summary}

---

## 🔥 今日头条（TOP 10）

"""
    
    # 前 10 条详细展示
    for i, article in enumerate(articles[:10], 1):
        content += format_article_enhanced(article, i, detailed=True)
        content += "\n"
    
    # 其余新闻
    if len(articles) > 10:
        content += "\n## 📰 更多资讯\n\n"
        for i, article in enumerate(articles[10:], 11):
            content += format_article_enhanced(article, i, detailed=False)
            content += "\n"
    
    # 数据统计
    source_counts = {}
    category_counts = {}
    
    for article in articles:
        source = article['source']
        source_counts[source] = source_counts.get(source, 0) + 1
        
        # 统计分类
        categories, _ = classify_content(article['title'], article.get('description', ''))
        for cat in categories:
            category_counts[cat] = category_counts.get(cat, 0) + 1
    
    content += "\n## 📊 数据统计\n\n"
    content += "**新闻来源分布：**\n\n"
    for source, count in sorted(source_counts.items(), key=lambda x: x[1], reverse=True):
        content += f"- {source}: {count} 条\n"
    
    content += "\n**热门主题分布：**\n\n"
    top_categories = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)[:5]
    for cat, count in top_categories:
        content += f"- {cat}: {count} 条\n"
    
    content += f"""
---

**所有新闻按优先级评分排序（时效性+来源质量+内容完整性+相关性）**
**数据来源：** 6 个主要 AI 新闻源
**更新频率：** 每日 02:00 和 14:00
**智能功能：** 自动分类、标签、质量评分

---

*自动生成：AI News Bot (Enhanced) | 最后更新：{datetime_str}*
"""
    
    return content

def format_article_enhanced(article: Dict, index: int, detailed: bool = True) -> str:
    """格式化单篇文章（增强版）"""
    
    # 智能分类
    categories, tags = classify_content(article['title'], article.get('description', ''))
    category_str = ' | '.join(categories[:2])
    tags_str = ' '.join(tags[:4])
    
    priority_score = article.get('priority_score', 0)
    
    formatted = f"""### {index}. {article['title']}

**📊 优先级：** {priority_score:.1f}/100
**🏷️ 分类：** {category_str}
**📚 标签：** {tags_str}
**📅 发布时间：** {article['published']}
**✍️ 来源：** {article['source']}
**🔗 原文链接：** [{article['title']}]({article['link']})
"""
    
    if detailed:
        description = article.get('description', '')
        if description and len(description) > 400:
            description = description[:400] + '...'
        if description:
            formatted += f"""
**📝 内容摘要：**
{description}

"""
        else:
            formatted += "\n"
    else:
        description = article.get('description', '')
        if description and len(description) > 150:
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
