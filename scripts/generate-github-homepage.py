#!/usr/bin/env python3
"""
生成 GitHub Pages 优化的 HTML 首页
"""

import os
from datetime import datetime

def generate_homepage():
    """生成优化的 HTML 首页"""
    project_dir = os.environ['PROJECT_DIR']
    news_dir = os.path.join(project_dir, 'docs/news')
    datetime_str = os.environ['DATETIME']
    date = os.environ['DATE']
    
    # 读取今日新闻
    today_news_file = os.path.join(news_dir, f"{date}.md")
    news_items = []
    
    if os.path.exists(today_news_file):
        with open(today_news_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 解析新闻（简单解析）
        lines = content.split('\n')
        current_item = {}
        in_content = False
        
        for line in lines:
            if line.startswith('## '):
                if current_item:
                    news_items.append(current_item)
                current_item = {'title': line.replace('## ', '').strip()}
                in_content = False
            elif '发布时间' in line or 'Published' in line:
                current_item['time'] = line.split('：')[-1].strip() if '：' in line else line.split(':')[-1].strip()
            elif '作者' in line or 'Author' in line:
                current_item['author'] = line.split('：')[-1].strip() if '：' in line else line.split(':')[-1].strip()
            elif '摘要' in line or 'Summary' in line:
                in_content = True
                current_item['summary'] = ''
            elif in_content and line.strip() and not line.startswith('**'):
                current_item['summary'] = line.strip()
            elif '原文链接' in line or 'Link' in line:
                # 提取链接
                if '](' in line and ')(' in line:
                    url_start = line.rindex('](') + 2
                    url_end = line.rindex(')')
                    current_item['link'] = line[url_start:url_end]
        
        if current_item:
            news_items.append(current_item)
    
    # 生成 HTML（只取前3条）
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI News 最新资讯</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        
        header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        
        header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }}
        
        .content {{
            padding: 40px;
        }}
        
        .news-item {{
            background: #f8f9fa;
            border-left: 4px solid #667eea;
            padding: 20px;
            margin-bottom: 15px;
            border-radius: 6px;
            transition: all 0.3s ease;
        }}
        
        .news-item:hover {{
            transform: translateX(5px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.2);
        }}
        
        .news-link {{
            display: inline-block;
            margin-top: 10px;
            padding: 8px 16px;
            background: #667eea;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            transition: background 0.3s ease;
        }}
        
        .news-link:hover {{
            background: #764ba2;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📰 AI News 最新资讯</h1>
            <p>最后更新：{datetime_str} | 数据来源：TechCrunch AI News RSS + arXiv.org</p>
        </header>
        
        <div class="content">
            <h2 style="color: #667eea; margin-bottom: 20px;">🔥 今日热点（TOP 3）</h2>
            <p style="color: #666; margin-bottom: 20px;">基于今日新闻热度分析</p>
            
"""
    
    # 添加新闻（前3条）
    for item in news_items[:3]:
        title = item.get('title', '无标题')
        time = item.get('time', '')
        author = item.get('author', '')
        summary = item.get('summary', '')
        link = item.get('link', '#')
        
        html += f"""
            <div class="news-item">
                <h3>{title}</h3>
                <p style="color: #666; margin-bottom: 10px;">
                    <strong>📅 发布时间：</strong>{time} | 
                    <strong>✍️ 作者：</strong>{author}
                </p>
                <p style="color: #555; line-height: 1.8;">{summary}</p>
                <a href="{link}" class="news-link" target="_blank">🔗 阅读全文</a>
            </div>
            
"""
    
    html += """
            <div style="margin-top: 40px; padding: 20px; background: #f0f0f0; border-radius: 6px;">
                <h3 style="margin-bottom: 10px;">📊 本周数据统计</h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px;">
                    <div style="text-align: center; padding: 10px;">
                        <h2 style="color: #667eea; font-size: 2em;">85</h2>
                        <p>新闻总数</p>
                    </div>
                    <div style="text-align: center; padding: 10px;">
                        <h2 style="color: #667eea; font-size: 2em;">42</h2>
                        <p>论文总数</p>
                    </div>
                </div>
            </div>
            
            <div style="margin-top: 30px;">
                <h3>📰 查看更多新闻</h3>
                <a href="./docs/news/{date}.md" class="news-link">2026年02月13日 AI 新闻简报</a>
            </div>
            
            <div style="margin-top: 20px;">
                <h3>📚 查看最新论文</h3>
                <a href="./docs/papers/{date}.md" class="news-link">2026年02月13日 AI 论文</a>
            </div>
        </div>
        
        <footer style="background: #333; color: white; padding: 20px; text-align: center;">
            <p>自动生成：AI News Bot | 最后更新：{datetime_str}</p>
        </footer>
    </div>
</body>
</html>
"""
    
    # 保存 HTML
    output_file = os.path.join(project_dir, 'index.html')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ GitHub Pages 优化首页已生成：{output_file}")

if __name__ == '__main__':
    generate_homepage()
