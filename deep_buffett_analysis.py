#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
深入分析符合巴菲特标准的股票
"""

import tinyshare as ts
import pandas as pd
from datetime import datetime

# 配置 Token
ts.set_token('bQD5z67wPFBgdqt3Wkka2HPt8KQZkx0FAe8mA1CVGQin6DJb5Eu6D6GV02ca36cb')
pro = ts.pro_api()

print("=" * 70)
print("🔍 深入分析潜在的巴菲特风格股票")
print("=" * 70)
print(f"开始时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print()

# 关注的重点股票 - 白酒、家电、医药等行业龙头企业
focus_stocks = [
    ('600519.SH', '贵州茅台', '白酒'),
    ('000858.SZ', '五粮液', '白酒'),
    ('000568.SZ', '泸州老窖', '白酒'),
    ('000860.SZ', '顺鑫农业', '白酒'),  # 牛栏山
    ('002304.SZ', '洋河股份', '白酒'),
    ('600809.SH', '山西汾酒', '白酒'),
    
    # 家电
    ('000333.SZ', '美的集团', '家电'),
    ('000651.SZ', '格力电器', '家电'),
    ('600690.SH', '海尔智家', '家电'),
    
    # 医药
    ('000661.SZ', '长春高新', '医药'),
    ('000999.SZ', '华润三九', '医药'),
    ('600276.SH', '恒瑞医药', '医药'),
    ('000963.SZ', '华东医药', '医药'),
    
    # 银行
    ('601398.SH', '工商银行', '银行'),
    ('601939.SH', '建设银行', '银行'),
    ('601288.SH', '农业银行', '银行'),
    ('601988.SH', '中国银行', '银行'),
    ('000001.SZ', '平安银行', '银行'),
    ('600036.SH', '招商银行', '银行'),
    ('601328.SH', '交通银行', '银行'),
    ('601998.SH', '中信银行', '银行'),
    
    # 其他消费品
    ('000895.SZ', '双汇发展', '食品'),
    ('002847.SZ', '盐津铺子', '食品'),
    ('002329.SZ', '皇氏集团', '食品'),
    ('000876.SZ', '新希望', '农牧'),
    ('002714.SZ', '牧原股份', '农牧'),
    
    # 保险
    ('601318.SH', '中国平安', '保险'),
    ('601628.SH', '中国人寿', '保险'),
    ('601336.SH', '新华保险', '保险'),
    
    # 汽车
    ('000625.SZ', '长安汽车', '汽车'),
    ('002594.SZ', '比亚迪', '汽车'),
    
    # 电池
    ('300750.SZ', '宁德时代', '电池'),
    ('002074.SZ', '国轩高科', '电池'),
]

print(f"🔍 分析 {len(focus_stocks)} 只重点股票...")
print()

results = []

for ts_code, name, industry in focus_stocks:
    try:
        print(f"📊 分析 {name} ({ts_code}) - {industry}")
        
        # 获取最近5年的财务指标
        df_fina = pro.fina_indicator(ts_code=ts_code)
        if len(df_fina) < 5:
            print(f"   ⚠️  财务数据少于5年，跳过")
            print()
            continue
            
        # 按公告日期排序，取最新的5条
        df_recent = df_fina.sort_values('ann_date', ascending=False).head(5)
        
        # 检查 ROE 连续5年 > 15%
        roe_values = []
        for idx, row in df_recent.iterrows():
            roe = row.get('roe', 0)
            if roe > 0:  # 只取有效的 ROE 值
                roe_values.append(roe)
        
        # 需要有至少5年的有效ROE数据，且都>15%
        roe_pass = len(roe_values) >= 5 and all(r > 15 for r in roe_values[:5])
        
        # 获取最新指标
        latest = df_recent.iloc[0]
        roe_latest = latest.get('roe', 0)
        gross_margin = latest.get('gross_margin', 0)
        debt_to_assets = latest.get('debt_to_assets', 100)
        net_profit_margin = latest.get('net_profit_margin', 0)
        current_ratio = latest.get('current_ratio', 0)  # 流动比率
        quick_ratio = latest.get('quick_ratio', 0)      # 速动比率
        
        print(f"   ROE (最新): {roe_latest:.2f}%")
        print(f"   ROE 连续5年 >15%: {'✅' if roe_pass else '❌'}")
        print(f"   毛利率: {gross_margin:.2f}%")
        print(f"   负债率: {debt_to_assets:.2f}%")
        print(f"   净利率: {net_profit_margin:.2f}%")
        
        # 巴菲特标准筛选
        margin_pass = gross_margin > 40 if gross_margin > 0 else False
        debt_pass = debt_to_assets < 50
        all_pass = roe_pass and margin_pass and debt_pass
        
        if all_pass:
            print(f"   🎉 🐂 符合巴菲特标准！")
            results.append({
                '代码': ts_code,
                '名称': name,
                '行业': industry,
                'ROE_最新': f"{roe_latest:.2f}%",
                'ROE_连续达标': '✅' if roe_pass else '❌',
                '毛利率': f"{gross_margin:.2f}%",
                '负债率': f"{debt_to_assets:.2f}%",
                '净利率': f"{net_profit_margin:.2f}%",
                '流动比率': f"{current_ratio:.2f}" if current_ratio > 0 else 'N/A',
                '速动比率': f"{quick_ratio:.2f}" if quick_ratio > 0 else 'N/A'
            })
        else:
            print(f"   ❌ 不符合标准")
        print()
        
    except Exception as e:
        print(f"   ⚠️  数据获取失败: {str(e)}")
        print()

print("=" * 70)
print("🎯 巴菲特风格候选股票清单")
print("=" * 70)

if len(results) > 0:
    df_results = pd.DataFrame(results)
    print(df_results.to_string(index=False))
    
    # 保存结果
    output_path = '/Users/john/.openclaw/workspace/buffett_deep_analysis.md'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# 🐂 巴菲特风格深度分析结果\n\n")
        f.write(f"**分析时间**: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write("## 符合标准的股票\n\n")
        f.write(df_results.to_markdown(index=False))
        f.write("\n\n## 筛选标准\n\n")
        f.write("- ROE 连续 5 年 > 15%\n")
        f.write("- 毛利率 > 40%\n")
        f.write("- 负债率 < 50%\n\n")
        f.write("## 后续分析\n\n")
        f.write("1. 护城河评估\n")
        f.write("2. 自由现金流验证\n")
        f.write("3. 估值计算\n")
        f.write("4. 买入时机判断\n")
    
    print(f"\n✅ 结果已保存：{output_path}")
    
    # 也保存 CSV
    df_results.to_csv('/Users/john/.openclaw/workspace/buffett_deep_analysis.csv', index=False)
    print("✅ CSV 已保存：buffett_deep_analysis.csv")
    
else:
    print("未找到完全符合所有标准的股票")
    print("\n可能需要适当放宽标准，例如：")
    print("- ROE > 12% 连续 5 年")
    print("- 毛利率 > 30%") 
    print("- 负债率 < 60%")

print()
print("=" * 70)
print(f"完成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 70)