#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
巴菲特风格选股 - 手动计算毛利率（准确版）
毛利率 = (营业收入 - 营业成本) / 营业收入 * 100
"""

import tinyshare as ts
import pandas as pd
from datetime import datetime

# 配置 Token
ts.set_token('aOeJ3e56GkDkt3Kg1a2mWt0e0n95E4vdg8vS6h6iRH1JFcUbPRvrFbnX0f72d050')
pro = ts.pro_api()

print("=" * 70)
print("🐂 小爪的巴菲特风格选股 - 手动计算毛利率（准确版）")
print("=" * 70)
print(f"开始时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print()

# 重点关注的行业龙头股
focus_stocks = [
    # 白酒
    ('600519.SH', '贵州茅台'),
    ('000858.SZ', '五粮液'),
    ('000568.SZ', '泸州老窖'),
    ('002304.SZ', '洋河股份'),
    ('600809.SH', '山西汾酒'),
    ('000799.SZ', '酒鬼酒'),
    ('600779.SH', '水井坊'),
    ('603369.SH', '今世缘'),
    # 家电
    ('000333.SZ', '美的集团'),
    ('000651.SZ', '格力电器'),
    ('600690.SH', '海尔智家'),
    ('002032.SZ', '苏泊尔'),
    ('603195.SH', '公牛集团'),
    # 医药
    ('600276.SH', '恒瑞医药'),
    ('000661.SZ', '长春高新'),
    ('000999.SZ', '华润三九'),
    ('600085.SH', '同仁堂'),
    ('000538.SZ', '云南白药'),
    ('300015.SZ', '爱尔眼科'),
    # 食品
    ('000895.SZ', '双汇发展'),
    ('603288.SH', '海天味业'),
    ('002847.SZ', '盐津铺子'),
    ('600887.SH', '伊利股份'),
    ('002557.SZ', '洽洽食品'),
    # 消费龙头
    ('601888.SH', '中国中免'),
    ('002415.SZ', '海康威视'),
    ('002594.SZ', '比亚迪'),
    ('300750.SZ', '宁德时代'),
]

print(f"🔍 分析 {len(focus_stocks)} 只行业龙头股...")
print()

results = []

for ts_code, name in focus_stocks:
    print(f"📊 分析 {name} ({ts_code})...")
    
    try:
        # ========== 1. 获取利润表数据（手动计算毛利率）==========
        df_income = pro.income(ts_code=ts_code, start_date='20190101', end_date='20260304')
        
        if len(df_income) == 0:
            print(f"   ⚠️  无利润表数据，跳过")
            print()
            continue
        
        # 按公告日期排序，取最近 5 年
        df_income = df_income.sort_values('ann_date', ascending=False)
        recent_income = df_income.head(5)
        
        # 手动计算毛利率
        gross_margin_history = []
        for idx, row in recent_income.iterrows():
            revenue = row.get('total_revenue')
            cost = row.get('total_cost')
            
            if revenue and cost and revenue > 0:
                gross_margin = ((revenue - cost) / revenue) * 100
                gross_margin_history.append(gross_margin)
        
        # 获取最新毛利率
        latest_gross_margin = gross_margin_history[0] if len(gross_margin_history) > 0 else None
        
        # ========== 2. 获取财务指标（ROE、负债率）==========
        df_fina = pro.fina_indicator(ts_code=ts_code)
        
        if len(df_fina) == 0:
            print(f"   ⚠️  无财务指标数据，跳过")
            print()
            continue
        
        df_fina = df_fina.sort_values('ann_date', ascending=False)
        
        # 获取 ROE 历史数据
        roe_history = []
        for idx, row in df_fina.iterrows():
            roe = row.get('roe')
            if roe is not None and roe != '':
                try:
                    roe_val = float(roe)
                    if roe_val > 0:
                        roe_history.append(roe_val)
                except:
                    pass
            if len(roe_history) >= 5:
                break
        
        if len(roe_history) < 5:
            print(f"   ⚠️  ROE 数据不足 5 年（只有{len(roe_history)}年），跳过")
            print()
            continue
        
        # 检查 ROE 连续 5 年 > 15%
        roe_pass = all(r > 15 for r in roe_history[:5])
        roe_latest = roe_history[0]
        roe_avg = sum(roe_history[:5]) / 5
        
        # 获取负债率
        latest_fina = df_fina.iloc[0]
        debt_to_assets_raw = latest_fina.get('debt_to_assets')
        debt_to_assets = None
        if debt_to_assets_raw is not None and debt_to_assets_raw != '':
            try:
                debt_to_assets = float(debt_to_assets_raw)
            except:
                pass
        
        # ========== 3. 打印分析结果 ==========
        print(f"   ROE (最新): {roe_latest:.2f}%")
        print(f"   ROE (5 年平均): {roe_avg:.2f}%")
        print(f"   ROE 连续 5 年>15%: {'✅' if roe_pass else '❌'}")
        
        if latest_gross_margin is not None:
            print(f"   毛利率 (手动计算): {latest_gross_margin:.2f}%")
        else:
            print(f"   毛利率：N/A")
            
        if debt_to_assets is not None:
            print(f"   负债率：{debt_to_assets:.2f}%")
        else:
            print(f"   负债率：N/A")
        
        # ========== 4. 判断是否符合巴菲特标准 ==========
        margin_pass = latest_gross_margin is not None and latest_gross_margin > 40
        debt_pass = debt_to_assets is not None and debt_to_assets < 50
        
        all_pass = roe_pass and margin_pass and debt_pass
        
        if all_pass:
            print(f"   🎉 🐂 符合巴菲特标准！")
            results.append({
                '代码': ts_code,
                '名称': name,
                'ROE_最新': f"{roe_latest:.2f}%",
                'ROE_5 年平均': f"{roe_avg:.2f}%",
                '毛利率': f"{latest_gross_margin:.2f}%",
                '负债率': f"{debt_to_assets:.2f}%",
                '状态': '✅ 符合'
            })
        else:
            reasons = []
            if not roe_pass:
                reasons.append("ROE 不达标")
            if not margin_pass:
                reasons.append(f"毛利率{latest_gross_margin:.1f}%" if latest_gross_margin else "毛利率 N/A")
            if not debt_pass:
                reasons.append(f"负债率{debt_to_assets:.1f}%" if debt_to_assets else "负债率 N/A")
            print(f"   ❌ 不符合 ({', '.join(reasons)})")
        
        print()
        
    except Exception as e:
        print(f"   ⚠️  分析失败：{str(e)}")
        print()

# ========== 输出结果 ==========
print("=" * 70)
print("🎯 巴菲特风格候选股票清单（手动计算毛利率）")
print("=" * 70)

if len(results) > 0:
    df_results = pd.DataFrame(results)
    df_results = df_results.sort_values('ROE_最新', ascending=False)
    
    print(df_results.to_string(index=False))
    
    # 保存结果
    output_md = '/Users/john/.openclaw/workspace/buffett_candidates_accurate.md'
    output_csv = '/Users/john/.openclaw/workspace/buffett_candidates_accurate.csv'
    
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write("# 🐂 巴菲特风格候选股票清单（准确版）\n\n")
        f.write(f"**分析时间**: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"**数据来源**: Tushare Pro (tinyshare 代理)\n")
        f.write(f"**毛利率计算**: 手动计算 = (营收 - 成本) / 营收 × 100\n\n")
        f.write("## 筛选标准\n\n")
        f.write("- ROE > 15% 连续 5 年\n")
        f.write("- 毛利率 > 40%\n")
        f.write("- 负债率 < 50%\n\n")
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
    print("\n建议放宽标准或进一步分析接近标准的企业")

print()
print("=" * 70)
print(f"✅ 分析完成！结束时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 70)
