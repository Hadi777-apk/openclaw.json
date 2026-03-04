#!/bin/bash
# 凌晨 12:00 任务：搜索和安装学习型技能

echo "⏰ 凌晨 12:00 任务启动：搜索和安装学习型技能"

# 进入工作目录
cd /Users/john/.openclaw/workspace

# 定义高评分学习型技能列表
learning_skills=(
    "self-improving-agent"      # 已有
    "ontology"                  # 尝试安装
    "knowledge-graph"           # 知识图谱
    "memory-architect"          # 记忆架构师
    "longterm-memory"           # 长期记忆
    "semantic-search"           # 语义搜索
    "rag-builder"               # RAG 构建器
    "agent-memory"              # 智能体记忆
    "knowledge-base"            # 知识库
    "adaptive-learning"         # 自适应学习
    "context-enhancer"          # 上下文增强
    "memory-consolidation"      # 记忆巩固
    "learning-agent"            # 学习智能体
    "cognitive-architect"       # 认知架构
    "intelligent-reasoning"     # 智能推理
)

echo "🔍 开始搜索高评分学习型技能..."

# 逐个尝试安装
for skill in "${learning_skills[@]}"; do
    echo "  检查 $skill..."
    
    # 检查是否已安装
    if [ -d "skills/$skill" ]; then
        echo "  ✅ $skill 已存在，跳过"
    else
        echo "  尝试安装 $skill..."
        npx clawhub install "$skill" 2>/dev/null
        
        if [ $? -eq 0 ]; then
            echo "  ✅ $skill 安装成功"
        else
            echo "  ❌ $skill 未找到或安装失败"
        fi
    fi
    
    # 短暂延迟避免速率限制
    sleep 5
done

# 额外搜索一些自学习相关的技能
echo "🔍 搜索其他自学习相关技能..."
npx clawhub search "self learning" --limit 5
npx clawhub search "autonomous learning" --limit 5
npx clawhub search "knowledge retention" --limit 5

echo "✅ 凌晨 12:00 任务完成"