#!/usr/bin/env python3
"""
AI News 论文抓取脚本
抓取 arXiv 最新论文，按研究方向分类
"""

import feedparser
import requests
from datetime import datetime, timedelta
import json
import re
from pathlib import Path

# 配置
ARXIV_FEEDS = {
    'cs.AI': 'http://export.arxiv.org/rss/cs.AI',
    'cs.CL': 'http://export.arxiv.org/rss/cs.CL',
    'cs.CV': 'http://export.arxiv.org/rss/cs.CV',
    'cs.LG': 'http://export.arxiv.org/rss/cs.LG',
}

OUTPUT_DIR = Path('/data1/cc/vide-coding/ai-news-hub/docs/papers')
DAYS_TO_FETCH = 7  # 抓取最近7天的论文

def fetch_papers(category='cs.AI', max_papers=20):
    """抓取指定分类的最新论文"""
    feed_url = ARXIV_FEEDS.get(category)
    if not feed_url:
        return []
    
    try:
        feed = feedparser.parse(feed_url)
        papers = []
        
        for entry in feed.entries[:max_papers]:
            # 提取论文信息
            paper = {
                'id': entry.id.split('/abs/')[-1],
                'title': entry.title,
                'authors': [author.name for author in entry.get('authors', [])],
                'summary': entry.get('summary', ''),
                'published': entry.get('published', ''),
                'link': entry.link,
                'pdf_url': entry.link.replace('/abs/', '/pdf/') + '.pdf',
                'category': category,
            }
            papers.append(paper)
        
        return papers
    except Exception as e:
        print(f"Error fetching papers from {category}: {e}")
        return []

def categorize_paper(paper):
    """根据论文标题和摘要分类研究方向"""
    title = paper['title'].lower()
    summary = paper['summary'].lower()
    
    # 计算机视觉 (CV)
    if any(keyword in title or summary for keyword in [
        'vision', 'image', 'visual', 'detection', 'segmentation',
        'recognition', 'generative', 'diffusion', 'gan'
    ]):
        return '🖼️ 计算机视觉 (CV)'
    
    # 强化学习 (RL)
    if any(keyword in title or summary for keyword in [
        'reinforcement', 'rl', 'policy', 'agent', 'reward',
        'offline rl', 'multi-agent'
    ]):
        return '🤖 强化学习 (RL)'
    
    # 大语言模型 (LLM)
    if any(keyword in title or summary for keyword in [
        'language model', 'llm', 'gpt', 'transformer', 'attention',
        'scaling law', 'inference', 'token', 'embedding'
    ]):
        return '📝 大语言模型 (LLM)'
    
    # 多模态
    if any(keyword in title or summary for keyword in [
        'multimodal', 'vision-language', 'vlm', 'clip',
        'cross-modal', 'fusion'
    ]):
        return '🔀 多模态'
    
    # 默认分类
    return paper['category']

def format_paper_markdown(paper):
    """格式化论文为 Markdown"""
    # 提取日期
    try:
        pub_date = datetime.strptime(paper['published'], '%a, %d %b %Y %H:%M:%S %z')
        date_str = pub_date.strftime('%Y-%m-%d')
    except:
        date_str = paper['published'][:10]
    
    # 分类
    category_tag = categorize_paper(paper)
    
    # 提取作者（最多显示3个）
    authors_str = ', '.join(paper['authors'][:3])
    if len(paper['authors']) > 3:
        authors_str += f" et al. ({len(paper['authors'])} authors)"
    
    markdown = f"""### {paper['title']}

**作者：** {authors_str}  
**时间：** {date_str}  
**分类：** {category_tag}

**摘要：** {paper['summary'][:200]}...

**原文链接：** [{paper['id']}]({paper['link']})

**PDF：** [下载]({paper['pdf_url']})

---

"""
    return markdown

def save_papers_by_date(papers, date_str):
    """保存论文到指定日期的文件"""
    output_file = OUTPUT_DIR / f"{date_str}.md"
    
    # 按分类组织
    papers_by_category = {}
    for paper in papers:
        category = categorize_paper(paper)
        if category not in papers_by_category:
            papers_by_category[category] = []
        papers_by_category[category].append(paper)
    
    # 生成 Markdown
    markdown_content = f"""# {date_str} 年{datetime.strptime(date_str, '%Y-%m-%d').strftime('%m月%d日')} AI 论文

**来源：** arXiv.org  
**更新时间：** {datetime.now().strftime('%Y-%m-%d %H:%M')}

---

"""
    
    # 添加各分类的论文
    for category in sorted(papers_by_category.keys()):
        markdown_content += f"\n## {category}\n\n"
        
        category_papers = papers_by_category[category]
        for i, paper in enumerate(category_papers, 1):
            markdown_content += format_paper_markdown(paper)
            markdown_content += "\n"
    
    # 保存文件
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"✅ 已保存 {len(papers)} 篇论文到 {output_file}")
    return output_file

def main():
    """主函数"""
    date_str = (datetime.now() - timedelta(days=0)).strftime('%Y-%m-%d')
    
    print(f"📚 开始抓取 arXiv 论文...")
    print(f"📅 日期：{date_str}")
    
    # 抓取各分类论文
    all_papers = []
    for category in ARXIV_FEEDS.keys():
        print(f"🔍 抓取 {category} 论文...")
        papers = fetch_papers(category, max_papers=10)
        all_papers.extend(papers)
        print(f"  ✅ 获取 {len(papers)} 篇")
    
    # 去重（基于 ID）
    seen_ids = set()
    unique_papers = []
    for paper in all_papers:
        if paper['id'] not in seen_ids:
            unique_papers.append(paper)
            seen_ids.add(paper['id'])
    
    print(f"\n📊 总计获取 {len(unique_papers)} 篇唯一论文")
    
    # 保存到文件
    if unique_papers:
        output_file = save_papers_by_date(unique_papers, date_str)
        print(f"\n✅ 论文抓取完成！")
        print(f"📄 文件：{output_file}")
    else:
        print("\n⚠️  没有获取到论文")

if __name__ == '__main__':
    main()
