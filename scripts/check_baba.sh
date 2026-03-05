#!/bin/bash
# 阿里巴巴 (BABA) 股价检查脚本
# 用于模拟炒股监控

cd /Users/john/.openclaw/workspace/skills/stock-info-explorer

# 设置 PATH 包含 uv
export PATH="$HOME/.local/bin:$PATH"

# 获取最新报价
echo "🔍 检查阿里巴巴 (BABA) 股价..."
uv run --script scripts/yf.py price BABA

# 获取技术指标摘要
echo ""
echo "📊 技术指标:"
uv run --script scripts/yf.py report BABA 1mo | grep -A 20 "Technical Signals"

# 检查持仓状态
echo ""
echo "📈 模拟持仓状态:"
echo "建仓价格: \$133.27 USD"
echo "投资金额: ¥10,000 CNY (约 10 股)"
echo "检查时间: $(date '+%Y-%m-%d %H:%M:%S Asia/Shanghai')"
