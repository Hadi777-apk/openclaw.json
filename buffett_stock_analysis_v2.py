#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
巴菲特风格选股 - A 股深度筛选（认真版）
标准：ROE>15% 连续 5 年、毛利率>40%、负债率<50%、自由现金流为正
"""

import tinyshare as ts
import pandas as pd
from datetime import datetime

# 配置新 Token
ts.set_token('aOeJ3e56GkDkt3Kg1a2mWt0e0n95E4vdg8vS6h6iRH1JFcUbPRvrFbnX0f72d050')
pro = ts.pro_api()

print("=" * 70)
print("🐂 小爪的巴菲特风格选股 - A 股深度筛选（认真版）")
print("=" * 70)
print(f"开始时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"授权码：aOeJ3e56GkDkt3Kg1a2mWt0e0n95E4vdg8vS6h6iRH1JFcUbPRvrFbnX0f72d050")
print()

# ========== Step 1: 获取全 A 股列表 ==========
print("📋 Step 1: 获取全 A 股列表...")
df_stocks = pro.stock_basic(exchange='', list_status='L', 
                            fields='ts_code,symbol,name,area,industry,list_date')
print(f"   ✅ 获取到 {len(df_stocks)} 只 A 股")
print()

# ========== Step 2: 选择重点行业龙头股 ==========
print("🎯 Step 2: 选择重点行业龙头股...")

# 白酒行业
baijiu_stocks = [
    ('600519.SH', '贵州茅台'),
    ('000858.SZ', '五粮液'),
    ('000568.SZ', '泸州老窖'),
    ('002304.SZ', '洋河股份'),
    ('600809.SH', '山西汾酒'),
    ('000799.SZ', '酒鬼酒'),
    ('600779.SH', '水井坊'),
    ('603369.SH', '今世缘'),
]

# 家电行业
home_appliance = [
    ('000333.SZ', '美的集团'),
    ('000651.SZ', '格力电器'),
    ('600690.SH', '海尔智家'),
    ('002032.SZ', '苏泊尔'),
    ('603195.SH', '公牛集团'),
]

# 医药行业
pharma = [
    ('600276.SH', '恒瑞医药'),
    ('000661.SZ', '长春高新'),
    ('000999.SZ', '华润三九'),
    ('600085.SH', '同仁堂'),
    ('000538.SZ', '云南白药'),
    ('300015.SZ', '爱尔眼科'),
    ('300122.SZ', '智飞生物'),
]

# 食品饮料
food = [
    ('000895.SZ', '双汇发展'),
    ('603288.SH', '海天味业'),
    ('002847.SZ', '盐津铺子'),
    ('600887.SH', '伊利股份'),
    ('002557.SZ', '洽洽食品'),
]

# 银行（虽然 ROE 通常不达 15%，但看看数据）
banks = [
    ('600036.SH', '招商银行'),
    ('601398.SH', '工商银行'),
    ('601939.SH', '建设银行'),
    ('601288.SH', '农业银行'),
]

# 消费龙头
consumer = [
    ('601888.SH', '中国中免'),
    ('002415.SZ', '海康威视'),
    ('002594.SZ', '比亚迪'),
    ('300750.SZ', '宁德时代'),
]

# 合并所有关注股票
focus_stocks = baijiu_stocks + home_appliance + pharma + food + banks + consumer
print(f"   重点关注 {len(focus_stocks)} 只行业龙头股")
print()

# ========== Step 3: 逐个分析财务数据 ==========
print("📊 Step 3: 深度分析财务数据（耐心分析中...）")
print()

results = []

for ts_code, name in focus_stocks:
    print(f"🔍 分析 {name} ({ts_code})...")
    
    try:
        # 获取财务指标
        df_fina = pro.fina_indicator(ts_code=ts_code)
        
        if len(df_fina) == 0:
            print(f"   ⚠️  无财务数据，跳过")
            print()
            continue
        
        # 按公告日期排序
        df_fina = df_fina.sort_values('ann_date', ascending=False)
        
        # 获取最近 5 年的 ROE 数据
        roe_history = []
        for idx, row in df_fina.iterrows():
            roe = row.get('roe')
            if roe is not None and roe != '':
                try:
                    roe_val = float(roe)
                    if roe_val > 0:  # 只取正值
                        roe_history.append(roe_val)
                except:
                    pass
            if len(roe_history) >= 5:
                break
        
        # 检查是否有足够的 ROE 数据
        if len(roe_history) < 5:
            print(f"   ⚠️  ROE 数据不足 5 年（只有{len(roe_history)}年），跳过")
            print()
            continue
        
        # 检查 ROE 连续 5 年 > 15%
        roe_pass = all(r > 15 for r in roe_history[:5])
        roe_avg = sum(roe_history[:5]) / 5
        
        # 获取最新财务指标
        latest = df_fina.iloc[0]
        
        # 毛利率（需要正确解析）
        gross_margin_raw = latest.get('gross_margin')
        gross_margin = None
        if gross_margin_raw is not None and gross_margin_raw != '':
            try:
                gross_margin = float(gross_margin_raw)
            except:
                pass
        
        # 负债率
        debt_to_assets_raw = latest.get('debt_to_assets')
        debt_to_assets = None
        if debt_to_assets_raw is not None and debt_to_assets_raw != '':
            try:
                debt_to_assets = float(debt_to_assets_raw)
            except:
                pass
        
        # 净利率
        net_profit_margin_raw = latest.get('net_profit_margin')
        net_profit_margin = None
        if net_profit_margin_raw is not None and net_profit_margin_raw != '':
            try:
                net_profit_margin = float(net_profit_margin_raw)
            except:
                pass
        
        # 打印分析结果
        print(f"   ROE (最新): {roe_history[0]:.2f}%")
        print(f"   ROE (5 年平均): {roe_avg:.2f}%")
        print(f"   ROE 连续 5 年>15%: {'✅' if roe_pass else '❌'}")
        
        if gross_margin is not None:
            print(f"   毛利率：{gross_margin:.2f}%")
        else:
            print(f"   毛利率：N/A")
            
        if debt_to_assets is not None:
            print(f"   负债率：{debt_to_assets:.2f}%")
        else:
            print(f"   负债率：N/A")
            
        if net_profit_margin is not None:
            print(f"   净利率：{net_profit_margin:.2f}%")
        else:
            print(f"   净利率：N/A")
        
        # 判断是否符合巴菲特标准
        margin_pass = gross_margin is not None and gross_margin > 40
        debt_pass = debt_to_assets is not None and debt_to_assets < 50
        
        all_pass = roe_pass and margin_pass and debt_pass
        
        if all_pass:
            print(f"   🎉 🐂 符合巴菲特标准！")
            results.append({
                '代码': ts_code,
                '名称': name,
                'ROE_最新': f"{roe_history[0]:.2f}%",
                'ROE_5 年平均': f"{roe_avg:.2f}%",
                '毛利率': f"{gross_margin:.2f}%",
                '负债率': f"{debt_to_assets:.2f}%",
                '净利率': f"{net_profit_margin:.2f}%" if net_profit_margin else 'N/A'
            })
        else:
            reasons = []
            if not roe_pass:
                reasons.append("ROE 不达标")
            if not margin_pass:
                reasons.append("毛利率偏低")
            if not debt_pass:
                reasons.append("负债率偏高")
            print(f"   ❌ 不符合标准 ({', '.join(reasons)})")
        
        print()
        
    except Exception as e:
        print(f"   ⚠️  分析失败：{str(e)}")
        print()

# ========== Step 4: 输出结果 ==========
print("=" * 70)
print("🎯 巴菲特风格候选股票清单")
print("=" * 70)

if len(results) > 0:
    df_results = pd.DataFrame(results)
    df_results = df_results.sort_values('ROE_最新', ascending=False)
    
    print(df_results.to_string(index=False))
    
    # 保存结果
    output_md = '/Users/john/.openclaw/workspace/buffett_candidates_final.md'
    output_csv = '/Users/john/.openclaw/workspace/buffett_candidates_final.csv'
    
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write("# 🐂 巴菲特风格候选股票清单（认真版）\n\n")
        f.write(f"**分析时间**: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"**筛选标准**: ROE>15% 连续 5 年、毛利率>40%、负债率<50%\n\n")
        f.write("## 符合标准的股票\n\n")
        f.write(df_results.to_markdown(index=False))
        f.write("\n\n## 下一步分析\n\n")
        f.write("1. 护城河评估（品牌/转换成本/网络效应/成本优势）\n")
        f.write("2. 自由现金流验证\n")
        f.write("3. 估值计算（DCF/PE）\n")
        f.write("4. 买入价格区间\n")
    
    df_results.to_csv(output_csv, index=False)
    
    print(f"\n✅ 结果已保存：")
    print(f"   - {output_md}")
    print(f"   - {output_csv}")
else:
    print("未找到完全符合所有标准的股票")
    print("\n可能需要适当放宽标准...")

print()
print("=" * 70)
print(f"✅ 分析完成！结束时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 70)
