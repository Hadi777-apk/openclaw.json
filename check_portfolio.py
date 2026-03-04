#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
山西汾酒持仓检查脚本
检查当前持仓盈亏情况
"""

import tinyshare as ts
import json
from datetime import datetime

# 配置 Token
ts.set_token('aOeJ3e56GkDkt3Kg1a2mWt0e0n95E4vdg8vS6h6iRH1JFcUbPRvrFbnX0f72d050')
pro = ts.pro_api()

print("=" * 60)
print("🐂 山西汾酒持仓盈亏检查")
print("=" * 60)
print()

# 读取持仓记录
portfolio_path = '/Users/john/.openclaw/workspace/portfolio_shanxifenjiu.json'
try:
    with open(portfolio_path, 'r', encoding='utf-8') as f:
        portfolio = json.load(f)
except FileNotFoundError:
    print("❌ 未找到持仓记录！请先建立持仓。")
    exit(1)

print(f"📊 股票：{portfolio['stock_name']} ({portfolio['stock_code']})")
print(f"📅 建仓日期：{portfolio['buy_date']}")
print(f"💰 建仓价：¥{portfolio['buy_price']:.2f}")
print(f"📈 持仓：{portfolio['shares']} 股")
print(f"💵 总投资：¥{portfolio['actual_cost']:.2f}")
print()

# 获取当前股价
df = pro.daily(ts_code=portfolio['stock_code'], 
               start_date=datetime.now().strftime('%Y%m01'), 
               end_date=datetime.now().strftime('%Y%m%d'))

if len(df) == 0:
    print("⚠️ 无法获取当前股价数据")
    exit(1)

df = df.sort_values('trade_date', ascending=False)
latest = df.iloc[0]
current_price = latest['close']
current_date = latest['trade_date']

print(f"📅 当前日期：{current_date}")
print(f"📊 当前股价：¥{current_price:.2f}")
print()

# 计算盈亏
current_value = portfolio['shares'] * current_price
profit_loss = current_value - portfolio['actual_cost']
profit_loss_pct = (profit_loss / portfolio['actual_cost']) * 100

print("=" * 60)
print("📈 盈亏情况")
print("=" * 60)
print(f"当前市值：¥{current_value:.2f}")
print(f"盈亏金额：¥{profit_loss:.2f}")
print(f"盈亏比例：{profit_loss_pct:+.2f}%")
print()

# 判断涨跌
if profit_loss > 0:
    status = "🎉 赚钱了！"
    emoji = "📈"
elif profit_loss < 0:
    status = "😢 亏钱了..."
    emoji = "📉"
else:
    status = "😐 不赚不亏"
    emoji = "➖"

print(f"状态：{emoji} {status}")
print("=" * 60)
print()

# 计算如果现在卖出的总资金（包含剩余现金）
total_cash = current_value + portfolio['remaining_cash']
total_profit_loss = total_cash - portfolio['initial_capital']
total_profit_loss_pct = (total_profit_loss / portfolio['initial_capital']) * 100

print("=" * 60)
print("💰 总体收益（含剩余现金）")
print("=" * 60)
print(f"初始资金：¥{portfolio['initial_capital']:.2f}")
print(f"剩余现金：¥{portfolio['remaining_cash']:.2f}")
print(f"当前市值：¥{current_value:.2f}")
print(f"总资金：¥{total_cash:.2f}")
print(f"总盈亏：¥{total_profit_loss:.2f} ({total_profit_loss_pct:+.2f}%)")
print("=" * 60)
print()

# 生成报告
report = f"""
# 🐂 山西汾酒持仓盈亏报告

**检查时间**: {datetime.now().strftime('%Y-%m-%d %H:%M')}

## 持仓信息
- **股票**: {portfolio['stock_name']} ({portfolio['stock_code']})
- **建仓日期**: {portfolio['buy_date']}
- **建仓价**: ¥{portfolio['buy_price']:.2f}
- **持仓**: {portfolio['shares']} 股
- **总投资**: ¥{portfolio['actual_cost']:.2f}

## 当前情况
- **检查日期**: {current_date}
- **当前股价**: ¥{current_price:.2f}
- **当前市值**: ¥{current_value:.2f}

## 盈亏情况
- **盈亏金额**: ¥{profit_loss:.2f}
- **盈亏比例**: {profit_loss_pct:+.2f}%
- **状态**: {status}

## 总体收益
- **初始资金**: ¥{portfolio['initial_capital']:.2f}
- **剩余现金**: ¥{portfolio['remaining_cash']:.2f}
- **总资金**: ¥{total_cash:.2f}
- **总盈亏**: ¥{total_profit_loss:.2f} ({total_profit_loss_pct:+.2f}%)

---
_🐾 小爪自动生成 · 投资有风险，入市需谨慎_
"""

# 保存报告
report_path = '/Users/john/.openclaw/workspace/portfolio_report.md'
with open(report_path, 'w', encoding='utf-8') as f:
    f.write(report)

print(f"✅ 报告已保存：{report_path}")
print()

# 更新持仓状态
portfolio['current_price'] = float(current_price)
portfolio['current_value'] = float(current_value)
portfolio['profit_loss'] = float(profit_loss)
portfolio['profit_loss_pct'] = float(profit_loss_pct)
portfolio['last_check'] = datetime.now().strftime('%Y-%m-%d %H:%M')
portfolio['status'] = 'checked'

with open(portfolio_path, 'w', encoding='utf-8') as f:
    json.dump(portfolio, f, indent=2, ensure_ascii=False)

print("✅ 持仓记录已更新")
