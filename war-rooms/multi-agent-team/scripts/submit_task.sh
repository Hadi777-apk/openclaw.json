#!/bin/bash
# 提交任务到多智能体系统

TASK_FILE="$1"
if [ -z "$TASK_FILE" ]; then
    echo "用法：$0 <任务文件.md>"
    exit 1
fi

if [ ! -f "$TASK_FILE" ]; then
    echo "错误：任务文件不存在：$TASK_FILE"
    exit 1
fi

PROJECT_DIR="$(dirname "$0")/.."
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
TASK_ID="TASK-$TIMESTAMP"

echo "📝 提交任务：$TASK_ID"
echo "📄 任务文件：$TASK_FILE"

# 复制任务文件到任务队列
cp "$TASK_FILE" "$PROJECT_DIR/TASK_QUEUE.md"

# 更新状态
echo "" >> "$PROJECT_DIR/STATUS.md"
echo "## [$TIMESTAMP] 新任务提交" >> "$PROJECT_DIR/STATUS.md"
echo "- 任务 ID: $TASK_ID" >> "$PROJECT_DIR/STATUS.md"
echo "- 状态：PENDING" >> "$PROJECT_DIR/STATUS.md"

echo "✅ 任务已提交！"
echo "💡 提示：运行 ./scripts/check_status.sh 查看进度"
