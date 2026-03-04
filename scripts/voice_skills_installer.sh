#!/bin/bash
# 凌晨 12:00 任务：安装用户推荐的 2 个技能

echo "⏰ 凌晨 12:00 任务启动：安装 self-improving-agent 和 ontology"

# 进入工作目录
cd /Users/john/.openclaw/workspace

# 技能 1: self-improving-agent (让 AI 越用越懂你)
echo "Installing self-improving-agent..."
if [ -d "skills/self-improving-agent" ]; then
    echo "✅ self-improving-agent 已存在，跳过"
else
    npx clawhub install self-improving-agent 2>&1 || echo "self-improving-agent 安装失败或不存在"
fi

# 技能 2: ontology (给 AI 一个真正的记忆系统)
echo "Installing ontology..."
if [ -d "skills/ontology" ]; then
    echo "✅ ontology 已存在，跳过"
else
    # 尝试不同的可能名称
    npx clawhub install ontology 2>&1 || \
    npx clawhub install oswalpalash-ontology 2>&1 || \
    npx clawhub install ai-ontology 2>&1 || \
    echo "ontology 未找到，跳过"
fi

echo "✅ 凌晨 12:00 任务完成"