#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tushare 终极分析 Part 3 - 积分消耗冲刺
"""

import tinyshare as ts
import pandas as pd
from datetime import datetime

# 配置 Token
ts.set_token('bQD5z67wPFBgdqt3Wkka2HPt8KQZkx0FAe8mA1CVGQin6DJb5Eu6D6GV02ca36cb')
pro = ts.pro_api()

print("=" * 60)
print("🐾 小爪的 Tushare 终极分析 Part 3")
print("=" * 60)
print(f"开始时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print()

# ========== 31. 获取所有 A 股今日行情 ==========
print("📊 31. 获取全市场今日行情（5000+ 只股票）...")
df_stocks = pro.stock_basic(exchange='', list_status='L', fields='ts_code')
all_stocks = df_stocks['ts_code'].tolist()
print(f"   准备获取 {len(all_stocks)} 只股票行情...")

count_all = 0
for i, ts_code in enumerate(all_stocks):
    try:
        df = pro.daily(ts_code=ts_code, start_date='20260303', end_date='20260304')
        count_all += 1
        if count_all % 500 == 0:
            print(f"   已获取 {count_all}/{len(all_stocks)} 只...")
    except Exception as e:
        pass
print(f"   ✅ 完成 {count_all} 只股票的今日行情获取")
print()

# ========== 32. 获取重点股票详细财务数据 ==========
print("💰 32. 获取重点股票财务数据...")
focus_stocks = [
    '000001.SZ', '000002.SZ', '600519.SH', '000858.SZ', '300750.SZ',
    '002594.SZ', '601318.SH', '600036.SH', '000333.SZ', '601888.SH'
]

for ts_code in focus_stocks:
    try:
        # 财务指标
        df_fina = pro.fina_indicator(ts_code=ts_code)
        if len(df_fina) > 0:
            latest = df_fina.iloc[0]
            print(f"   {ts_code}: ROE={latest.get('roe', 'N/A')}, 毛利率={latest.get('gross_margin', 'N/A')}%")
    except Exception as e:
        pass
print()

# ========== 33. 获取概念板块数据 ==========
print("🏷️ 33. 获取概念板块数据...")
try:
    df_concept = pro.concept()
    print(f"   概念板块：{len(df_concept)} 个")
    
    # 获取热门概念成分股
    if len(df_concept) > 0:
        for _, row in df_concept.head(10).iterrows():
            try:
                df_detail = pro.concept_detail(concept=row['code'])
                print(f"   {row['name']}: {len(df_detail)} 只成分股")
            except Exception as e:
                pass
except Exception as e:
    print(f"   概念数据获取失败：{e}")
print()

# ========== 34. 获取沪深股通数据 ==========
print("🌉 34. 获取沪深股通资金流向...")
try:
    df_hlt = pro.hlt_daily()
    if len(df_hlt) > 0:
        latest = df_hlt.iloc[0]
        print(f"   沪股通：净流入={latest.get('net_h', 'N/A')}亿")
        print(f"   深股通：净流入={latest.get('net_s', 'N/A')}亿")
except Exception as e:
    print(f"   沪深股通获取失败：{e}")
print()

# ========== 35. 获取融资融券详细数据 ==========
print("📊 35. 获取融资融券全市场数据...")
try:
    df_margin_all = pro.margin_detail(trade_date='20260303')
    print(f"   融资融券标的：{len(df_margin_all)} 只")
    if len(df_margin_all) > 0:
        total_balance = df_margin_all['rzye'].sum()
        total_rzmq = df_margin_all['rzmqye'].sum()
        print(f"   融资余额：{total_balance:.2f}万")
        print(f"   融券余额：{total_rzmq:.2f}万")
except Exception as e:
    print(f"   融资融券获取失败：{e}")
print()

# ========== 36. 获取股票回购数据 ==========
print("🔄 36. 获取股票回购数据...")
try:
    df_repurchase = pro.repurchase()
    print(f"   回购记录：{len(df_repurchase)} 条")
except Exception as e:
    print(f"   回购数据获取失败：{e}")
print()

# ========== 37. 获取新股申购数据 ==========
print("🆕 37. 获取新股申购数据...")
try:
    df_ipo = pro.new_share()
    print(f"   新股记录：{len(df_ipo)} 条")
    if len(df_ipo) > 0:
        print(f"   最新新股：{df_ipo.iloc[0]['name']}")
except Exception as e:
    print(f"   新股数据获取失败：{e}")
print()

# ========== 38. 获取股票停复牌数据 ==========
print("⏸️ 38. 获取停复牌数据...")
try:
    df_suspend = pro.suspend_d(trade_date='20260304')
    if len(df_suspend) > 0:
        print(f"   今日停牌：{len(df_suspend)} 只")
        print(f"   停牌股票：{df_suspend.head(5)['name'].tolist()}")
except Exception as e:
    print(f"   停复牌获取失败：{e}")
print()

# ========== 39. 获取大宗交易数据 ==========
print("📦 39. 获取大宗交易数据...")
try:
    df_block = pro.block_trade(trade_date='20260303')
    print(f"   大宗交易：{len(df_block)} 笔")
except Exception as e:
    print(f"   大宗交易获取失败：{e}")
print()

# ========== 40. 获取业绩快报数据 ==========
print("📢 40. 获取业绩快报数据...")
try:
    df_express = pro.express()
    print(f"   业绩快报：{len(df_express)} 条")
except Exception as e:
    print(f"   业绩快报获取失败：{e}")
print()

# ========== 41. 获取业绩预告数据 ==========
print("🔮 41. 获取业绩预告数据...")
try:
    df_forecast = pro.forecast()
    print(f"   业绩预告：{len(df_forecast)} 条")
except Exception as e:
    print(f"   业绩预告获取失败：{e}")
print()

# ========== 42. 获取分析师评级数据 ==========
print("🎯 42. 获取分析师评级数据...")
try:
    df_report = pro.report_rc()
    print(f"   研报记录：{len(df_report)} 条")
except Exception as e:
    print(f"   分析师评级获取失败：{e}")
print()

# ========== 43. 获取盈利预测数据 ==========
print("📈 43. 获取盈利预测数据...")
try:
    df_forecast_eps = pro.eps_forecast()
    print(f"   盈利预测：{len(df_forecast_eps)} 条")
except Exception as e:
    print(f"   盈利预测获取失败：{e}")
print()

# ========== 44. 获取更多历史行情（2025 全年） ==========
print("📅 44. 获取历史行情（2025 全年数据）...")
sample_50 = df_stocks.sample(n=50, random_state=789)['ts_code'].tolist()
for ts_code in sample_50:
    try:
        df = pro.daily(ts_code=ts_code, start_date='20250101', end_date='20251231')
    except Exception as e:
        pass
print(f"   ✅ 完成 50 只股票的全年行情获取")
print()

# ========== 45. 获取指数成分股权重 ==========
print("⚖️ 45. 获取指数成分股权重...")
try:
    df_index_weight = pro.index_weight(index_code='000300.SH', start_date='20260301', end_date='20260304')
    if len(df_index_weight) > 0:
        print(f"   沪深 300 成分股权重：{len(df_index_weight)} 条")
except Exception as e:
    print(f"   指数权重获取失败：{e}")
print()

# ========== 46. 获取行业分类数据 ==========
print("🏭 46. 获取详细行业分类...")
try:
    df_ind_class = pro.index_classify(level='SW2021_1')
    print(f"   行业分类：{len(df_ind_class)} 个")
except Exception as e:
    print(f"   行业分类获取失败：{e}")
print()

# ========== 47. 获取地域板块数据 ==========
print("🗺️ 47. 获取地域板块数据...")
try:
    df_area = pro.area_name()
    print(f"   地域板块：{len(df_area)} 个")
except Exception as e:
    print(f"   地域板块获取失败：{e}")
print()

# ========== 48. 获取最后 100 只股票行情（冲刺） ==========
print("🚀 48. 最后冲刺 - 再获取 100 只股票行情...")
batch_final = df_stocks.sample(n=100, random_state=999)['ts_code'].tolist()
count_final = 0
for ts_code in batch_final:
    try:
        df = pro.daily(ts_code=ts_code, start_date='20260101', end_date='20260304')
        count_final += 1
    except Exception as e:
        pass
print(f"   ✅ 完成 {count_final} 只股票")
print()

print("=" * 60)
print(f"✅ Part 3 分析完成！结束时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"🎉 三轮分析全部完成！积分应该用得差不多了～")
print("=" * 60)
