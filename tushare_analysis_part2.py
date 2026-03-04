#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tushare 深度分析 Part 2 - 继续消耗积分
"""

import tinyshare as ts
import pandas as pd
from datetime import datetime

# 配置 Token
ts.set_token('bQD5z67wPFBgdqt3Wkka2HPt8KQZkx0FAe8mA1CVGQin6DJb5Eu6D6GV02ca36cb')
pro = ts.pro_api()

print("=" * 60)
print("🐾 小爪的 Tushare 深度分析 Part 2")
print("=" * 60)
print(f"开始时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print()

# ========== 16. 获取港股数据 ==========
print("🇭🇰 16. 获取港股数据...")
try:
    df_hk = pro.hk_basic()
    print(f"   港股列表：{len(df_hk)} 只")
    
    # 获取几只热门港股行情
    hk_stocks = ['00700.HK', '09988.HK', '03690.HK']  # 腾讯、阿里、美团
    for hk_code in hk_stocks:
        try:
            df = pro.hk_daily(ts_code=hk_code, start_date='20260201', end_date='20260304')
            if len(df) > 0:
                latest = df.iloc[0]
                print(f"   {hk_code}: {latest['close']:.2f} ({latest['pct_chg']:.2f}%)")
        except Exception as e:
            pass
except Exception as e:
    print(f"   港股数据获取失败：{e}")
print()

# ========== 17. 获取美股数据 ==========
print("🇺🇸 17. 获取美股数据...")
try:
    df_us = pro.us_basic()
    print(f"   美股列表：{len(df_us)} 只")
    
    # 获取热门美股行情
    us_stocks = ['AAPL.US', 'TSLA.US', 'NVDA.US', 'MSFT.US']
    for us_code in us_stocks:
        try:
            df = pro.us_daily(ts_code=us_code, start_date='20260201', end_date='20260304')
            if len(df) > 0:
                latest = df.iloc[0]
                print(f"   {us_code}: {latest['close']:.2f} ({latest['pct_chg']:.2f}%)")
        except Exception as e:
            pass
except Exception as e:
    print(f"   美股数据获取失败：{e}")
print()

# ========== 18. 获取基金数据 ==========
print("💎 18. 获取基金数据...")
try:
    df_fund = pro.fund_basic(market='E')  # 场内基金
    print(f"   场内基金：{len(df_fund)} 只")
    
    df_fund2 = pro.fund_basic(market='I')  # 场外基金
    print(f"   场外基金：{len(df_fund2)} 只")
    
    # 获取几只热门基金净值
    fund_codes = ['510300.SH', '510500.SH', '159915.SZ']  # 沪深 300ETF、中证 500ETF、创业板 ETF
    for fund_code in fund_codes:
        try:
            df = pro.fund_nav(ts_code=fund_code, start_date='20260201', end_date='20260304')
            if len(df) > 0:
                latest = df.iloc[0]
                print(f"   {fund_code}: 净值={latest['nav']:.4f}")
        except Exception as e:
            pass
except Exception as e:
    print(f"   基金数据获取失败：{e}")
print()

# ========== 19. 获取债券数据 ==========
print("📜 19. 获取债券数据...")
try:
    df_bond = pro.convert_bond()
    print(f"   可转债列表：{len(df_bond)} 只")
    
    # 获取可转债行情
    if len(df_bond) > 0:
        for _, row in df_bond.head(5).iterrows():
            try:
                df = pro.cb_daily(ts_code=row['ts_code'], trade_date='20260303')
                if len(df) > 0:
                    print(f"   {row['bond_name']}: {df.iloc[0]['close']:.2f} ({df.iloc[0]['pct_chg']:.2f}%)")
            except Exception as e:
                pass
except Exception as e:
    print(f"   债券数据获取失败：{e}")
print()

# ========== 20. 获取期货数据 ==========
print("📦 20. 获取期货数据...")
try:
    df_fut = pro.fut_basic()
    print(f"   期货合约：{len(df_fut)} 只")
except Exception as e:
    print(f"   期货数据获取失败：{e}")
print()

# ========== 21. 获取更多 A 股行情（再批量 200 只） ==========
print("📈 21. 继续批量获取 A 股行情（200 只）...")
df_stocks = pro.stock_basic(exchange='', list_status='L', fields='ts_code')
batch2 = df_stocks.sample(n=200, random_state=123)['ts_code'].tolist()
count2 = 0
for ts_code in batch2:
    try:
        df = pro.daily(ts_code=ts_code, start_date='20260101', end_date='20260304')
        count2 += 1
        if count2 % 50 == 0:
            print(f"   已获取 {count2}/200 只股票行情...")
    except Exception as e:
        pass
print(f"   ✅ 完成 {count2} 只股票的行情获取")
print()

# ========== 22. 获取利润表数据 ==========
print("💵 22. 获取利润表数据...")
sample_stocks2 = ['000001.SZ', '600519.SH', '000858.SZ', '300750.SZ', '002594.SZ']
for ts_code in sample_stocks2:
    try:
        df_income = pro.income(ts_code=ts_code, start_date='20250101', end_date='20251231')
        if len(df_income) > 0:
            latest = df_income.iloc[0]
            print(f"   {ts_code}: 营收={latest.get('total_revenue', 'N/A')}, 净利润={latest.get('net_profit', 'N/A')}")
    except Exception as e:
        pass
print()

# ========== 23. 获取资产负债表数据 ==========
print("📊 23. 获取资产负债表数据...")
for ts_code in sample_stocks2:
    try:
        df_bps = pro.balsheet(ts_code=ts_code, start_date='20250101', end_date='20251231')
        if len(df_bps) > 0:
            print(f"   {ts_code}: 资产负债表数据获取成功")
    except Exception as e:
        pass
print()

# ========== 24. 获取现金流量表数据 ==========
print("💸 24. 获取现金流量表数据...")
for ts_code in sample_stocks2:
    try:
        df_cashflow = pro.cashflow(ts_code=ts_code, start_date='20250101', end_date='20251231')
        if len(df_cashflow) > 0:
            print(f"   {ts_code}: 现金流量表数据获取成功")
    except Exception as e:
        pass
print()

# ========== 25. 获取分红数据 ==========
print("🎁 25. 获取分红数据...")
try:
    df_div = pro.dividend(ts_code='000001.SZ')
    if len(df_div) > 0:
        print(f"   平安银行分红记录：{len(df_div)} 条")
        print(f"   最新分红：每 10 股派{df_div.iloc[0]['cash_div']}元")
except Exception as e:
    print(f"   分红数据获取失败：{e}")
print()

# ========== 26. 获取股东人数 ==========
print("👥 26. 获取股东人数数据...")
try:
    df_holder = pro.top10_holders(ts_code='000001.SZ', ann_date='20251231')
    if len(df_holder) > 0:
        print(f"   前十大股东数据：{len(df_holder)} 条")
except Exception as e:
    print(f"   股东数据获取失败：{e}")
print()

# ========== 27. 获取机构调研数据 ==========
print("🏢 27. 获取机构调研数据...")
try:
    df_survey = pro.stk_surv()
    if len(df_survey) > 0:
        print(f"   机构调研记录：{len(df_survey)} 条")
except Exception as e:
    print(f"   机构调研获取失败：{e}")
print()

# ========== 28. 获取更多指数行情 ==========
print("📊 28. 获取行业指数行情...")
industry_indices = ['886007.WI', '886008.WI', '886009.WI', '886010.WI']  # 银行、保险、证券、白酒
for idx in industry_indices:
    try:
        df = pro.index_daily(ts_code=idx, start_date='20260201', end_date='20260304')
        if len(df) > 0:
            latest = df.iloc[0]
            print(f"   {idx}: {latest['close']:.2f} ({latest['pct_chg']:.2f}%)")
    except Exception as e:
        pass
print()

# ========== 29. 获取股票技术面数据 ==========
print("📐 29. 获取技术面数据...")
try:
    df_tech = pro.stk_factor(ts_code='600519.SH', trade_date='20260303')
    if len(df_tech) > 0:
        print(f"   贵州茅台技术因子：{len(df_tech)} 个指标")
except Exception as e:
    print(f"   技术面获取失败：{e}")
print()

# ========== 30. 最后再来一批股票行情（100 只） ==========
print("📈 30. 最后一批股票行情（100 只）...")
batch3 = df_stocks.sample(n=100, random_state=456)['ts_code'].tolist()
count3 = 0
for ts_code in batch3:
    try:
        df = pro.daily(ts_code=ts_code, start_date='20260215', end_date='20260304')
        count3 += 1
    except Exception as e:
        pass
print(f"   ✅ 完成 {count3} 只股票的行情获取")
print()

print("=" * 60)
print(f"✅ Part 2 分析完成！结束时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 60)
