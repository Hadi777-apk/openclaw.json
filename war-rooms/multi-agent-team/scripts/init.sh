#!/bin/bash
# 多智能体团队系统 - 初始化脚本
# 用于快速启动和配置多 Agent 协作环境

set -e

PROJECT_DIR="/Users/john/.openclaw/workspace/war-rooms/multi-agent-team"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "╔══════════════════════════════════════════════════════════╗"
echo "║       多智能体团队系统 - 初始化工具                      ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# 检查目录结构
echo "📁 检查目录结构..."
for dir in agents/{commander,image,coder,coordinator} artifacts comms lessons scripts references logs; do
    mkdir -p "$PROJECT_DIR/$dir"
done
echo "✅ 目录结构就绪"

# 创建环境变量模板
echo ""
echo "📝 创建环境变量模板..."
ENV_TEMPLATE="$PROJECT_DIR/.env.example"
cat > "$ENV_TEMPLATE" << 'EOF'
# 多智能体系统 API 配置
# 复制此文件为 .env 并填入真实的 API Keys

# Gemini 3.0 (总指挥)
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-3.0-pro

# Nano Banana Pro (图像生成)
NANO_BANANA_API_KEY=your_nano_banana_api_key_here
NANO_BANANA_MODEL=banana-pro-v1
NANO_BANANA_BASE_URL=https://api.nanobanana.pro/v1

# Claude Code (代码 Agent)
# 如使用本地 Claude Code，此项可为空
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# 系统配置
LOG_LEVEL=INFO
MAX_RETRIES=3
TIMEOUT_SECONDS=300
EOF
echo "✅ 环境变量模板已创建：$ENV_TEMPLATE"

# 创建快速启动脚本
echo ""
echo "🚀 创建快速启动脚本..."
STARTUP_SCRIPT="$PROJECT_DIR/scripts/start.sh"
cat > "$STARTUP_SCRIPT" << 'EOF'
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
EOF
chmod +x "$STARTUP_SCRIPT"
echo "✅ 启动脚本已创建：$STARTUP_SCRIPT"

# 创建任务提交脚本
echo ""
echo "📋 创建任务提交脚本..."
TASK_SCRIPT="$PROJECT_DIR/scripts/submit_task.sh"
cat > "$TASK_SCRIPT" << 'EOF'
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
EOF
chmod +x "$TASK_SCRIPT"
echo "✅ 任务提交脚本已创建：$TASK_SCRIPT"

# 创建状态检查脚本
echo ""
echo "📊 创建状态检查脚本..."
STATUS_SCRIPT="$PROJECT_DIR/scripts/check_status.sh"
cat > "$STATUS_SCRIPT" << 'EOF'
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
EOF
chmod +x "$STATUS_SCRIPT"
echo "✅ 状态检查脚本已创建：$STATUS_SCRIPT"

# 创建使用示例
echo ""
echo "📚 创建使用示例..."
EXAMPLE_FILE="$PROJECT_DIR/references/usage-example.md"
cat > "$EXAMPLE_FILE" << 'EOF'
# 多智能体系统使用示例

## 场景 1: 生成股票分析图表

### 用户请求
"帮我生成阿里巴巴股票的技术分析图表，包含 K 线、RSI 和 MACD"

### 系统处理流程
1. COORDINATOR 接收请求，创建任务文件
2. COMMANDER 分解任务:
   - 获取股票数据 (COORDINATOR)
   - 分析技术指标 (COMMANDER)
   - 生成图表 (IMAGE Agent)
3. 各 Agent 并行执行
4. COMMANDER 整合结果
5. COORDINATOR 交付用户

### 任务文件示例
```markdown
# 任务：生成股票分析图表

**提交时间**: 2026-03-05 18:00
**优先级**: NORMAL
**描述**: 生成阿里巴巴 (BABA) 股票技术分析图表

**要求**:
- 图表类型：专业金融 K 线图
- 技术指标：RSI(14), MACD(12,26,9)
- 时间范围：6 个月
- 风格：深色背景，清晰标注

**输出**: PNG 图像文件
```

---

## 场景 2: 开发股票监控脚本

### 用户请求
"帮我写一个 Python 脚本，监控 10 只股票的价格，超过 5% 涨跌幅就发通知"

### 系统处理流程
1. COORDINATOR 接收请求
2. COMMANDER 分析需求，分配给 CODER Agent
3. CODER (Claude Code) 编写代码
4. COORDINATOR 测试并交付

### 任务文件示例
```markdown
# 任务：开发股票监控脚本

**提交时间**: 2026-03-05 18:30
**优先级**: HIGH
**描述**: 开发实时股票价格监控脚本

**功能需求**:
- 监控 10 只指定股票
- 实时获取价格 (Yahoo Finance API)
- 涨跌幅超过 5% 时发送通知
- 支持配置股票代码列表
- 日志记录所有价格变动

**技术栈**: Python 3.10+
**输出**: 可执行的 Python 脚本 + 使用说明
```

---

## 场景 3: 多步骤深度分析

### 用户请求
"深度分析腾讯控股，包括基本面、技术面、舆情分析，并生成投资报告"

### 系统处理流程
1. COORDINATOR 接收复杂请求
2. COMMANDER 分解为多个子任务:
   - 基本面分析 (COMMANDER)
   - 技术面分析 (COORDINATOR + 技术指标)
   - 舆情分析 (COMMANDER + 网络搜索)
   - 生成可视化图表 (IMAGE Agent)
   - 编写分析报告 (COMMANDER)
3. 多 Agent 并行协作
4. 整合所有输出为完整报告

---

## 快速开始

1. 配置 API Keys:
   ```bash
   cd war-rooms/multi-agent-team
   cp .env.example .env
   # 编辑 .env 填入真实的 API Keys
   ```

2. 启动系统:
   ```bash
   ./scripts/start.sh
   ```

3. 提交任务:
   ```bash
   ./scripts/submit_task.sh my_task.md
   ```

4. 检查进度:
   ```bash
   ./scripts/check_status.sh
   ```
EOF
echo "✅ 使用示例已创建：$EXAMPLE_FILE"

echo ""
echo "╔══════════════════════════════════════════════════════════╗"
echo "║                  ✅ 初始化完成！                         ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""
echo "📂 项目目录：$PROJECT_DIR"
echo ""
echo "📋 下一步操作:"
echo "  1. 复制配置文件:"
echo "     cp $PROJECT_DIR/.env.example $PROJECT_DIR/.env"
echo ""
echo "  2. 编辑 .env 文件，填入 API Keys"
echo ""
echo "  3. 启动系统:"
echo "     $PROJECT_DIR/scripts/start.sh"
echo ""
echo "  4. 查看使用示例:"
echo "     cat $EXAMPLE_FILE"
echo ""
echo "🎉 多智能体团队系统搭建完成！"