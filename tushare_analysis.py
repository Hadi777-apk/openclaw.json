#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tushare 全面股票分析 - 消耗 4000 积分计划
"""

import tinyshare as ts
import pandas as pd
from datetime import datetime, timedelta

# 配置 Token
ts.set_token('bQD5z67wPFBgdqt3Wkka2HPt8KQZkx0FAe8mA1CVGQin6DJb5Eu6D6GV02ca36cb')
pro = ts.pro_api()

print("=" * 60)
print("🐾 小爪的 Tushare 全面股票分析")
print("=" * 60)
print(f"开始时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print()

# ========== 1. 获取全市场股票列表 ==========
print("📊 1. 获取全市场股票列表...")
df_stocks = pro.stock_basic(exchange='', list_status='L', 
                            fields='ts_code,symbol,name,area,industry,market,list_date')
print(f"   ✅ 获取到 {len(df_stocks)} 只股票")
print()

# ========== 2. 获取主要指数列表 ==========
print("📈 2. 获取主要指数列表...")
df_indices = pro.index_basic()
print(f"   ✅ 获取到 {len(df_indices)} 个指数")
print()

# ========== 3. 获取大盘指数行情（上证、深证、创业板） ==========
print("📉 3. 获取大盘指数近期行情...")
indices = ['000001.SH', '399001.SZ', '399006.SZ', '000016.SH', '000300.SH']
index_names = ['上证指数', '深证成指', '创业板指', '上证 50', '沪深 300']

for idx, idx_name in zip(indices, index_names):
    df = pro.index_daily(ts_code=idx, start_date='20260201', end_date='20260304')
    if len(df) > 0:
        latest = df.iloc[0]
        print(f"   {idx_name}: 最新={latest['close']:.2f}, 涨跌={latest['pct_chg']:.2f}%")
print()

# ========== 4. 获取热门行业股票 ==========
print("🏭 4. 分析热门行业股票...")
hot_industries = ['银行', '保险', '证券', '白酒', '新能源汽车', '半导体', '医药', '房地产']

for industry in hot_industries:
    df_ind = df_stocks[df_stocks['industry'] == industry]
    if len(df_ind) > 0:
        print(f"   {industry}: {len(df_ind)} 只股票")
        # 获取前 3 只股票的近期行情
        for _, row in df_ind.head(3).iterrows():
            try:
                df_daily = pro.daily(ts_code=row['ts_code'], start_date='20260228', end_date='20260304')
                if len(df_daily) > 0:
                    latest = df_daily.iloc[0]
                    print(f"      - {row['name']}: {latest['close']:.2f} ({latest['pct_chg']:.2f}%)")
            except Exception as e:
                pass
print()

# ========== 5. 获取财务指标 ==========
print("💰 5. 获取财务指标数据...")
# 获取部分股票的财务指标
sample_stocks = df_stocks.head(50)['ts_code'].tolist()
for ts_code in sample_stocks[:10]:
    try:
        df_fina = pro.fina_indicator(ts_code=ts_code)
        if len(df_fina) > 0:
            latest = df_fina.iloc[0]
            print(f"   {ts_code}: ROE={latest.get('roe', 'N/A')}, 每股收益={latest.get('basic_eps', 'N/A')}")
    except Exception as e:
        pass
print()

# ========== 6. 获取宏观经济数据 ==========
print("📊 6. 获取宏观经济数据...")
try:
    df_gdp = pro.gdp()
    if len(df_gdp) > 0:
        print(f"   GDP 数据：最新季度={df_gdp.iloc[0]['gdp_yoy']}%")
except Exception as e:
    print(f"   GDP 数据获取失败：{e}")

try:
    df_cpi = pro.cpi()
    if len(df_cpi) > 0:
        print(f"   CPI 数据：最新={df_cpi.iloc[0]['cpi_m']}%")
except Exception as e:
    print(f"   CPI 数据获取失败：{e}")
print()

# ========== 7. 获取资金流向数据 ==========
print("💸 7. 获取资金流向数据...")
try:
    df_moneyflow = pro.moneyflow(ts_code='000001.SZ', start_date='20260228', end_date='20260304')
    if len(df_moneyflow) > 0:
        print(f"   平安银行资金流向：主力净流入={df_moneyflow['net_m_in'].sum():.2f}万")
except Exception as e:
    print(f"   资金流向获取失败：{e}")
print()

# ========== 8. 获取股票技术因子 ==========
print("📐 8. 获取技术因子数据...")
try:
    df_factor = pro.stk_factor(ts_code='000001.SZ', trade_date='20260303')
    if len(df_factor) > 0:
        print(f"   技术因子数据获取成功，{len(df_factor)} 条记录")
except Exception as e:
    print(f"   技术因子获取失败：{e}")
print()

# ========== 9. 获取龙虎榜数据 ==========
print("🐉 9. 获取龙虎榜数据...")
try:
    df_top = pro.top_list(trade_date='20260303')
    if len(df_top) > 0:
        print(f"   龙虎榜：{len(df_top)} 只股票上榜")
except Exception as e:
    print(f"   龙虎榜获取失败：{e}")
print()

# ========== 10. 获取融资融券数据 ==========
print("📊 10. 获取融资融券数据...")
try:
    df_margin = pro.margin_detail(trade_date='20260303')
    if len(df_margin) > 0:
        print(f"   融资融券：{len(df_margin)} 条记录")
        total_buy = df_margin['buy_amt'].sum()
        total_repay = df_margin['repay_amt'].sum()
        print(f"   融资买入额：{total_buy:.2f}万，偿还额：{total_repay:.2f}万")
except Exception as e:
    print(f"   融资融券获取失败：{e}")
print()

# ========== 11. 获取更多股票行情（批量） ==========
print("📈 11. 批量获取股票行情（消耗积分大户）...")
batch_stocks = df_stocks.sample(n=100, random_state=42)['ts_code'].tolist()
count = 0
for ts_code in batch_stocks:
    try:
        df = pro.daily(ts_code=ts_code, start_date='20260201', end_date='20260304')
        count += 1
        if count % 20 == 0:
            print(f"   已获取 {count}/100 只股票行情...")
    except Exception as e:
        pass
print(f"   ✅ 完成 {count} 只股票的行情获取")
print()

# ========== 12. 获取周线/月线数据 ==========
print("📅 12. 获取周线/月线数据...")
try:
    df_week = pro.weekly(ts_code='000001.SZ', start_date='20260101', end_date='20260304')
    print(f"   周线数据：{len(df_week)} 条")
except Exception as e:
    print(f"   周线获取失败：{e}")

try:
    df_month = pro.monthly(ts_code='000001.SZ', start_date='20250101', end_date='20260304')
    print(f"   月线数据：{len(df_month)} 条")
except Exception as e:
    print(f"   月线获取失败：{e}")
print()

# ========== 13. 获取复权因子 ==========
print("🔄 13. 获取复权因子数据...")
try:
    df_adj = pro.adj_factor(ts_code='000001.SZ', trade_date='20260303')
    print(f"   复权因子：{df_adj['adj_factor'].values[0] if len(df_adj) > 0 else 'N/A'}")
except Exception as e:
    print(f"   复权因子获取失败：{e}")
print()

# ========== 14. 获取股票基本信息 ==========
print("📋 14. 获取重点股票详细信息...")
focus_stocks = ['000001.SZ', '000002.SZ', '600519.SH', '000858.SZ', '300750.SZ']
for ts_code in focus_stocks:
    try:
        df_info = pro.stock_basic(ts_code=ts_code, fields='ts_code,name,area,industry,market,list_date,total_shares,float_shares')
        if len(df_info) > 0:
            row = df_info.iloc[0]
            print(f"   {row['name']}: 总股本={row['total_shares']/10000:.2f}亿股，流通={row['float_shares']/10000:.2f}亿股")
    except Exception as e:
        pass
print()

# ========== 15. 获取行业分类数据 ==========
print("🏷️ 15. 获取行业分类统计...")
try:
    df_ind_class = pro.index_classify(level='SW2021_1')
    print(f"   申万一级行业：{len(df_class)} 个" if 'df_class' in dir() else "   行业分类数据获取成功")
except Exception as e:
    print(f"   行业分类获取失败：{e}")
print()

print("=" * 60)
print(f"✅ 分析完成！结束时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 60)
