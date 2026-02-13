#!/usr/bin/env python3
"""
内容分类和标签系统
根据关键词自动分配类别和标签
"""

import re
from typing import List, Dict, Tuple

# AI 主题分类定义
TOPIC_CATEGORIES = {
    '🤖 大模型 & 基础模型': [
        'gpt', 'claude', 'gemini', 'llm', 'large language model',
        'foundation model', 'transformer', 'bert', 'diffusion',
        'stable diffusion', 'midjourney', 'dall-e'
    ],
    '🤬 智能体 & 多智能体': [
        'agent', 'multi-agent', 'autonomous', 'robotics',
        'embodied ai', 'orchestration', 'agentic'
    ],
    '🎯 企业 & 商业应用': [
        'startup', 'funding', 'investment', 'acquisition',
        'ipo', 'venture capital', 'enterprise', 'business',
        'company', 'launch', 'product', 'service'
    ],
    '🔬 研究 & 论文': [
        'paper', 'research', 'arxiv', 'study', 'experiment',
        'breakthrough', 'algorithm', 'methodology', 'benchmark',
        'conference', 'neurips', 'icml', 'iclr'
    ],
    '💻 开发工具 & 框架': [
        'framework', 'library', 'api', 'sdk', 'tool',
        'platform', 'github', 'open source', 'repository',
        'code', 'programming', 'deployment'
    ],
    '🎨 生成式 AI & 创意': [
        'generative', 'creative', 'art', 'design', 'image',
        'video', 'audio', 'music', 'content creation',
        'creative ai', 'design tool'
    ],
    '🌐 搜索 & 信息检索': [
        'search', 'retrieval', 'rag', 'embedding',
        'vector database', 'semantic search', 'information',
        'query', 'indexing'
    ],
    '🧠 推理 & 认知': [
        'reasoning', 'thinking', 'planning', 'logic',
        'inference', 'chain of thought', 'cognitive',
        'decision making', 'problem solving'
    ],
    '💬 对话 & 交互': [
        'chatbot', 'conversational', 'dialogue', 'voice',
        'nlp', 'natural language', 'understanding',
        'interaction', 'user interface'
    ],
    '🛡️ 安全 & 伦理': [
        'safety', 'ethics', 'bias', 'fairness',
        'privacy', 'security', 'regulation', 'policy',
        'alignment', 'responsible ai'
    ]
}

# 公司/产品标签
COMPANY_TAGS = {
    'openai': ['openai', 'gpt', 'chatgpt', 'dall-e', 'sora'],
    'google': ['google', 'gemini', 'bard', 'deepmind'],
    'anthropic': ['anthropic', 'claude'],
    'meta': ['meta', 'facebook', 'llama'],
    'microsoft': ['microsoft', 'copilot', 'azure'],
    'amazon': ['amazon', 'aws', 'bedrock'],
    'nvidia': ['nvidia', 'gpu', 'cuda'],
    'apple': ['apple', 'siri'],
    'tesla': ['tesla', 'spacex', 'elon musk', 'xai'],
}

def classify_content(title: str, description: str = '') -> Tuple[List[str], List[str]]:
    """
    分类内容并返回标签
    
    返回: (分类列表, 标签列表)
    """
    text = f"{title} {description}".lower()
    
    # 1. 主题分类
    matched_categories = []
    for category, keywords in TOPIC_CATEGORIES.items():
        if any(keyword in text for keyword in keywords):
            matched_categories.append(category)
    
    # 如果没有匹配到，使用默认分类
    if not matched_categories:
        matched_categories = ['📰 综合 AI 资讯']
    
    # 2. 公司/产品标签
    matched_companies = []
    for company, keywords in COMPANY_TAGS.items():
        if any(keyword in text for keyword in keywords):
            matched_companies.append(f"@{company}")
    
    # 3. 技术标签
    tech_tags = []
    
    # 模型类型
    if any(word in text for word in ['gpt-4', 'gpt4', 'gpt 4']):
        tech_tags.append('#GPT-4')
    if any(word in text for word in ['claude', 'anthropic']):
        tech_tags.append('#Claude')
    if any(word in text for word in ['gemini', 'google']):
        tech_tags.append('#Gemini')
    if any(word in text for word in ['llama', 'meta']):
        tech_tags.append('#LLaMA')
    
    # 技术方向
    if any(word in text for word in ['multimodal', 'multi-modal']):
        tech_tags.append('#多模态')
    if any(word in text for word in ['rag', 'retrieval']):
        tech_tags.append('#RAG')
    if any(word in text for word in ['agent', 'autonomous']):
        tech_tags.append('#AI智能体')
    if any(word in text for word in ['vision', 'image', 'video']):
        tech_tags.append('#计算机视觉')
    
    return matched_categories, matched_companies + tech_tags

def calculate_priority_score(title: str, description: str, source: str, 
                          recency_hours: int = 24) -> float:
    """
    计算内容优先级评分
    
    评分标准：
    - 时效性（0-30分）：越新越高
    - 来源质量（0-30分）：arXiv/官方博客 > 大媒体 > 社交
    - 内容完整性（0-20分）：有摘要 > 只有标题
    - 相关性（0-20分）：直接 AI 相关 > 间接相关
    """
    score = 0.0
    text = f"{title} {description}".lower()
    
    # 1. 时效性（0-30分）
    if recency_hours <= 6:
        score += 30
    elif recency_hours <= 12:
        score += 25
    elif recency_hours <= 24:
        score += 20
    elif recency_hours <= 48:
        score += 10
    else:
        score += 5
    
    # 2. 来源质量（0-30分）
    high_quality = ['arxiv', 'mit technology review', 'nature', 'science']
    medium_quality = ['techcrunch', 'venturebeat', 'the verge', 'wired']
    
    if any(q in source.lower() for q in high_quality):
        score += 30
    elif any(q in source.lower() for q in medium_quality):
        score += 25
    elif 'hacker news' in source.lower():
        score += 20  # 质量过滤后
    elif 'github' in source.lower():
        score += 15
    else:
        score += 10
    
    # 3. 内容完整性（0-20分）
    if description and len(description) > 100:
        score += 20
    elif description:
        score += 10
    else:
        score += 5
    
    # 4. 相关性（0-20分）
    ai_keywords = ['gpt', 'llm', 'agent', 'machine learning', 'deep learning']
    if any(keyword in text for keyword in ai_keywords):
        score += 20
    elif any(word in text for word in ['ai', 'artificial intelligence', 'automation']):
        score += 15
    elif any(word in text for word in ['tech', 'startup', 'funding']):
        score += 8
    else:
        score += 3
    
    return score

def generate_summary(articles: List[Dict], top_n: int = 5) -> str:
    """
    生成每日热点总结
    """
    # 按优先级排序
    scored_articles = []
    for article in articles:
        title = article.get('title', '')
        description = article.get('description', '')
        source = article.get('source', '')
        
        score = calculate_priority_score(title, description, source)
        scored_articles.append({
            'article': article,
            'score': score
        })
    
    # 选择 top N
    top_articles = sorted(scored_articles, key=lambda x: x['score'], reverse=True)[:top_n]
    
    # 提取关键主题
    all_tags = []
    for item in top_articles:
        title = item['article'].get('title', '')
        description = item['article'].get('description', '')
        categories, tags = classify_content(title, description)
        all_tags.extend(categories)
    
    # 统计最常见主题
    from collections import Counter
    top_topics = [tag for tag, count in Counter(all_tags).most_common(5)]
    
    # 生成总结
    summary = f"""## 🔥 今日热点总结

**最热门主题：** {' • '.join(top_topics[:3])}

**今日 {top_n} 大事件：**

"""
    
    for i, item in enumerate(top_articles, 1):
        article = item['article']
        title = article.get('title', '')
        source = article.get('source', '')
        score = item['score']
        
        summary += f"""### {i}. {title}
**来源：** {source} • **优先级：** {score:.1f}/100

"""
    
    return summary

if __name__ == '__main__':
    # 测试
    test_articles = [
        {
            'title': 'OpenAI GPT-5 Announced with Revolutionary Reasoning',
            'description': 'OpenAI today announced GPT-5, featuring breakthrough reasoning capabilities...',
            'source': 'TechCrunch AI'
        },
        {
            'title': 'New Multi-Agent System Achieves Human-Level Performance',
            'description': 'Researchers from Stanford and MIT developed a multi-agent system...',
            'source': 'arXiv'
        }
    ]
    
    for article in test_articles:
        categories, tags = classify_content(
            article['title'],
            article.get('description', '')
        )
        score = calculate_priority_score(
            article['title'],
            article.get('description', ''),
            article['source']
        )
        
        print(f"\n标题：{article['title']}")
        print(f"分类：{', '.join(categories)}")
        print(f"标签：{', '.join(tags)}")
        print(f"评分：{score:.1f}/100")
