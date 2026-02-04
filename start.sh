#!/bin/bash

# AI News Hub 启动脚本

echo "🚀 启动 AI News Hub 本地服务器..."
echo ""
echo "================================"
echo "  🤖 AI News Hub
echo "================================"
echo ""
echo "服务器地址: http://localhost:8000"
echo "按 Ctrl+C 停止服务器"
echo ""
echo "================================"
echo ""

# 启动 Python HTTP 服务器
python3 -m http.server 8000
