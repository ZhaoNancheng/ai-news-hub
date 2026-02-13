#!/usr/bin/env python3
"""
社区平台抓取脚本 - Hacker News + GitHub Trending
不需要 VPN，使用公开 API
"""

import requests
import json
from datetime import datetime
import os
from typing import List, Dict, Any

# 配置
HACKERNEWS_API = "https://hacker-news.firebaseio.com/v0"
GITHUB_API = "https://api.github.com"

def fetch_hacker_news(limit: int = 15, min_points: int = 50) -> List[Dict[str, Any]]:
    """抓取 Hacker News 热门故事"""
    try:
        print("📊 正在抓取 Hacker News...")
        url = f"{HACKERNEWS_API}/topstories.json"
        response = requests.get(url, timeout=10)
        story_ids = response.json()[:limit*3]  # 获取更多以过滤

        stories = []
        for story_id in story_ids:
            detail_url = f"{HACKERNEWS_API}/item/{story_id}.json"
            detail_response = requests.get(detail_url, timeout=5)
            story = detail_response.json()

            if not story:
                continue

            # 质量过滤：最低点赞数
            points = story.get('score', 0)
            if points < min_points:
                continue

            # AI/ML 相关性过滤
            title = story.get('title', '').lower()
            url = story.get('url', '')

            ai_keywords = ['ai', 'machine learning', 'deep learning', 'llm', 'gpt',
                         'claude', 'gemini', 'neural', 'robot', 'automation',
                         'model', 'training', 'inference', 'agent']

            if not any(keyword in title for keyword in ai_keywords):
                continue

            story_data = {
                'title': story.get('title', ''),
                'url': url,
                'points': points,
                'comments': story.get('descendants', 0),
                'time': datetime.fromtimestamp(story.get('time', 0)).strftime('%Y-%m-%d %H:%M:%S'),
                'source': 'Hacker News',
                'hn_id': story_id
            }
            stories.append(story_data)

            if len(stories) >= limit:
                break

        print(f"  ✅ 获取 {len(stories)} 条 Hacker News（过滤后）")
        return stories

    except Exception as e:
        print(f"  ❌ Hacker News 抓取失败: {e}")
        return []

def fetch_github_trending(limit: int = 10, min_stars: int = 100) -> List[Dict[str, Any]]:
    """抓取 GitHub Trending AI/ML 仓库"""
    try:
        print("🚀 正在抓取 GitHub Trending...")
        # 使用搜索 API 按最近更新排序
        query = "topic:ai language:python OR language:javascript OR language:typescript"
        url = f"{GITHUB_API}/search/repositories"
        params = {
            'q': query,
            'sort': 'updated',
            'order': 'desc',
            'per_page': limit * 2
        }

        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        repos = []
        for item in data.get('items', []):
            repo = item.get('repository', item)

            # 质量过滤：最低 star 数
            stars = repo.get('stargazers_count', 0)
            if stars < min_stars:
                continue

            # AI/ML 相关性过滤
            description = repo.get('description', '').lower()
            topics = [t.lower() for t in repo.get('topics', [])]

            ai_keywords = ['ai', 'machine-learning', 'deep-learning', 'llm',
                         'gpt', 'neural-network', 'transformer', 'agent']

            if not any(keyword in description or keyword in str(topics)
                     for keyword in ai_keywords):
                continue

            repo_data = {
                'title': repo.get('full_name', ''),
                'description': repo.get('description', ''),
                'url': repo.get('html_url', ''),
                'stars': stars,
                'language': repo.get('language', 'Unknown'),
                'updated': datetime.strptime(repo.get('updated_at', ''),
                                      '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M:%S'),
                'source': 'GitHub Trending',
                'topics': repo.get('topics', [])
            }
            repos.append(repo_data)

            if len(repos) >= limit:
                break

        print(f"  ✅ 获取 {len(repos)} 个 GitHub 仓库（过滤后）")
        return repos

    except Exception as e:
        print(f"  ❌ GitHub Trending 抓取失败: {e}")
        return []

def save_to_file(hn_stories: List[Dict], gh_repos: List[Dict]) -> str:
    """保存到文件"""
    # 获取环境变量
    news_dir = os.environ.get('NEWS_DIR', '/data1/cc/vide-coding/ai-news-hub/docs/news')
    date = os.environ.get('DATE', datetime.now().strftime('%Y-%m-%d'))
    datetime_str = os.environ.get('DATETIME', datetime.now().strftime('%Y-%m-%d %H:%M'))
    output_file = os.path.join(news_dir, f"community-{date}.md")

    # 生成 Markdown
    content = f"""# {datetime.strptime(date, '%Y-%m-%d').strftime('%Y年%m月%d日')} AI 社区热点

**来源：** Hacker News + GitHub Trending
**更新时间：** {datetime_str}
**数据统计：** {len(hn_stories)} 条讨论 + {len(gh_repos)} 个项目

---

## 💬 Hacker News 热门讨论（点赞 >{min_points if hn_stories else 50}）

"""

    # Hacker News 故事
    for i, story in enumerate(hn_stories, 1):
        content += f"""### {i}. {story['title']}

**💬 点赞：** {story['points']} • **💭 评论：** {story['comments']}
**🔗 链接：** [{story['title']}]({story['url']}) • [Hacker News 讨论](https://news.ycombinator.com/item?id={story['hn_id']})
**⏰ 时间：** {story['time']}

---
"""

    # GitHub Trending
    content += """
## 🚀 GitHub Trending AI 项目（Star >100）

"""

    for i, repo in enumerate(gh_repos, 1):
        topics_str = ', '.join(repo['topics'][:5]) if repo['topics'] else 'N/A'
        content += f"""### {i}. {repo['title']}

**⭐ Stars：** {repo['stars']} • **💻 语言：** {repo['language']}
**📝 描述：** {repo['description']}
**🏷️ 话题：** {topics_str}
**🔗 链接：** [{repo['title']}]({repo['url']})
**⏰ 更新：** {repo['updated']}

---
"""

    content += f"""
---

**所有数据经过 AI 相关性过滤和质理筛选**
**数据来源：**
- Hacker News API: https://news.ycombinator.com/
- GitHub API: https://github.com/trending

---

*自动生成：AI News Bot | 最后更新：{datetime_str}*
"""

    # 保存文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n✅ 已保存社区热点到 {output_file}")
    return output_file

if __name__ == '__main__':
    print(f"\n{'='*60}")
    print("  社区平台抓取开始（Hacker News + GitHub）")
    print(f"{'='*60}\n")

    # 抓取数据
    hn_stories = fetch_hacker_news(limit=10, min_points=50)
    gh_repos = fetch_github_trending(limit=8, min_stars=100)

    # 保存文件
    if hn_stories or gh_repos:
        save_to_file(hn_stories, gh_repos)
        print(f"{'='*60}\n")
    else:
        print("\n⚠️  未能抓取到任何数据")
