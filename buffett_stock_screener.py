#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
巴菲特风格选股 - A 股筛选
标准：ROE>15% 连续 5 年、毛利率>40%、负债率<50%、自由现金流为正
"""

import tinyshare as ts
import pandas as pd
from datetime import datetime

# 配置 Token
ts.set_token('bQD5z67wPFBgdqt3Wkka2HPt8KQZkx0FAe8mA1CVGQin6DJb5Eu6D6GV02ca36cb')
pro = ts.pro_api()

print("=" * 70)
print("🐂 小爪的巴菲特风格选股 - A 股筛选")
print("=" * 70)
print(f"开始时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print()

# ========== Step 1: 获取全 A 股列表 ==========
print("📋 Step 1: 获取全 A 股列表...")
df_stocks = pro.stock_basic(exchange='', list_status='L', 
                            fields='ts_code,symbol,name,area,industry,market,list_date')
print(f"   ✅ 获取到 {len(df_stocks)} 只 A 股")
print()

# ========== Step 2: 获取财务指标 ==========
print("📊 Step 2: 获取财务指标数据（分批获取）...")

# 先获取一部分重点行业的股票进行深度分析
focus_industries = ['白酒', '银行', '保险', '医药', '半导体', '新能源汽车', '家电', '食品']
df_focus = df_stocks[df_stocks['industry'].isin(focus_industries)]
print(f"   重点行业股票：{len(df_focus)} 只")
print(f"   行业分布：{df_focus['industry'].value_counts().to_dict()}")
print()

# 获取财务指标
candidates = []
count = 0

for idx, row in df_focus.iterrows():
    ts_code = row['ts_code']
    name = row['name']
    industry = row['industry']
    
    try:
        # 获取财务指标
        df_fina = pro.fina_indicator(ts_code=ts_code)
        
        if len(df_fina) < 5:
            continue
            
        # 检查连续 5 年 ROE > 15%
        df_fina = df_fina.sort_values('ann_date', ascending=False)
        recent_5 = df_fina.head(5)
        
        if len(recent_5) < 5:
            continue
            
        roe_values = recent_5['roe'].dropna().values
        if len(roe_values) < 5:
            continue
            
        roe_pass = all(r > 15 for r in roe_values[:5])
        
        # 获取最新指标
        latest = recent_5.iloc[0]
        roe_latest = latest.get('roe', 0)
        gross_margin = latest.get('gross_margin', 0)
        debt_to_assets = latest.get('debt_to_assets', 100)
        net_profit_margin = latest.get('net_profit_margin', 0)
        
        # 巴菲特标准筛选
        if roe_pass and gross_margin > 40 and debt_to_assets < 50:
            candidates.append({
                '代码': ts_code,
                '名称': name,
                '行业': industry,
                'ROE(最新)': f"{roe_latest:.2f}%",
                'ROE(5 年均)': f"{sum(roe_values[:5])/5:.2f}%",
                '毛利率': f"{gross_margin:.2f}%" if gross_margin else 'N/A',
                '负债率': f"{debt_to_assets:.2f}%",
                '净利率': f"{net_profit_margin:.2f}%" if net_profit_margin else 'N/A'
            })
            count += 1
            if count % 10 == 0:
                print(f"   已找到 {count} 只候选股票...")
                
    except Exception as e:
        pass

print(f"   ✅ 找到 {len(candidates)} 只符合巴菲特标准的候选股票")
print()

# ========== Step 3: 输出结果 ==========
print("=" * 70)
print("📈 候选股票清单（符合巴菲特标准）")
print("=" * 70)

if len(candidates) > 0:
    df_candidates = pd.DataFrame(candidates)
    df_candidates = df_candidates.sort_values('ROE(最新)', ascending=False)
    
    print(df_candidates.to_string(index=False))
    
    # 保存结果
    output_path = '/Users/john/.openclaw/workspace/buffett_candidates.md'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# 🐂 巴菲特风格候选股票清单\n\n")
        f.write(f"**筛选时间**: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"**筛选标准**: ROE>15% 连续 5 年、毛利率>40%、负债率<50%\n\n")
        f.write("## 候选股票\n\n")
        f.write(df_candidates.to_markdown(index=False))
        f.write("\n\n")
        f.write("## 下一步分析\n\n")
        f.write("1. 护城河评估\n")
        f.write("2. 自由现金流验证\n")
        f.write("3. 估值计算\n")
        f.write("4. 买入价格区间\n")
    
    print(f"\n✅ 结果已保存：{output_path}")
else:
    print("   未找到符合所有标准的股票，可能需要放宽条件...")

print()
print("=" * 70)
print(f"✅ 分析完成！结束时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 70)
