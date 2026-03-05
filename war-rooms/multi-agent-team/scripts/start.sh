#!/bin/bash
# 启动多智能体系统

source "$(dirname "$0")/../.env" 2>/dev/null || true

echo "🤖 多智能体系统启动中..."
echo ""
echo "检查 API 配置..."

if [ -n "$GEMINI_API_KEY" ] && [ "$GEMINI_API_KEY" != "your_gemini_api_key_here" ]; then
    echo "✅ COMMANDER (Gemini 3.0) - 已配置"
else
    echo "⚠️  COMMANDER (Gemini 3.0) - 未配置"
fi

if [ -n "$NANO_BANANA_API_KEY" ] && [ "$NANO_BANANA_API_KEY" != "your_nano_banana_api_key_here" ]; then
    echo "✅ IMAGE (Nano Banana Pro) - 已配置"
else
    echo "⚠️  IMAGE (Nano Banana Pro) - 未配置"
fi

if [ -n "$ANTHROPIC_API_KEY" ] && [ "$ANTHROPIC_API_KEY" != "your_anthropic_api_key_here" ]; then
    echo "✅ CODER (Claude Code) - 已配置"
else
    echo "ℹ️  CODER (Claude Code) - 使用本地模式"
fi

echo ""
echo "🐾 COORDINATOR (小爪) - 运行中"
echo ""
echo "系统就绪！等待任务..."
