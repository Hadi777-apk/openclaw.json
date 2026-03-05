#!/bin/bash
# 检查多智能体系统状态

PROJECT_DIR="$(dirname "$0")/.."

echo "╔══════════════════════════════════════════════════════════╗"
echo "║           多智能体系统 - 实时状态                        ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# 显示 STATUS.md 的关键信息
if [ -f "$PROJECT_DIR/STATUS.md" ]; then
    echo "📋 系统状态:"
    grep -A 20 "## Agent 状态" "$PROJECT_DIR/STATUS.md" | head -10
    echo ""
    
    echo "📝 当前任务:"
    if grep -q "当前任务" "$PROJECT_DIR/STATUS.md"; then
        grep -A 10 "## 当前任务" "$PROJECT_DIR/STATUS.md" | tail -n +2
    else
        echo "  无活跃任务"
    fi
else
    echo "⚠️  状态文件不存在"
fi

echo ""
echo "📂 工作目录：$PROJECT_DIR"
