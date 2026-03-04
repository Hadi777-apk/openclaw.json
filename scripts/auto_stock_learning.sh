#!/bin/bash
# 凌晨 1:00 任务：自主学习股票知识

echo "⏰ 凌晨 1:00 任务启动：自主学习股票知识"

# 进入工作目录
cd /Users/john/.openclaw/workspace

# Step 1: 搜索并安装"自主学习"技能
echo "Searching for autonomous learning skills..."
npx clawhub search "autonomous learning" --limit 5
npx clawhub search "self-learning" --limit 5
npx clawhub search "auto-learn" --limit 5

# 尝试安装找到的技能
echo "Installing autonomous learning skill..."
npx clawhub install autonomous-learning 2>/dev/null || echo "autonomous-learning 未找到"
npx clawhub install self-learning 2>/dev/null || echo "self-learning 未找到"
npx clawhub install auto-learn 2>/dev/null || echo "auto-learn 未找到"

# Step 2: 使用 Tushare 学习股票知识（消耗 1 万积分）
echo "Starting Tushare stock analysis..."

python3 << 'PYTHON_EOF'
import tinyshare as ts
import pandas as pd
from datetime import datetime

# 配置 Token
ts.set_token('aOeJ3e56GkDkt3Kg1a2mWt0e0n95E4vdg8vS6h6iRH1JFcUbPRvrFbnX0f72d050')
pro = ts.pro_api()

print(f"开始时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("🚀 开始消耗 Tushare 积分学习股票知识...")

# 1. 获取全 A 股列表
print("\n1. 获取全 A 股列表...")
df_stocks = pro.stock_basic(exchange='', list_status='L')
print(f"   获取到 {len(df_stocks)} 只股票")

# 2. 获取行业分类
print("\n2. 获取行业分类...")
df_industry = pro.index_classify(level='SW2021_1')
print(f"   获取到 {len(df_industry)} 个行业分类")

# 3. 批量获取股票财务数据（重点行业龙头）
focus_stocks = [
    '600519.SH', '000858.SZ', '000568.SZ', '002304.SZ', '600809.SH',  # 白酒
    '000333.SZ', '000651.SZ', '600690.SH',  # 家电
    '600276.SH', '000661.SZ', '000999.SZ',  # 医药
    '603288.SH', '000895.SZ', '600887.SH',  # 食品
    '600036.SH', '601398.SH', '601939.SH',  # 银行
    '601318.SH', '601628.SH',  # 保险
    '002415.SZ', '300750.SZ', '002594.SZ',  # 科技/新能源
]

print("\n3. 获取重点股票财务数据...")
for ts_code in focus_stocks:
    try:
        df_fina = pro.fina_indicator(ts_code=ts_code)
        df_income = pro.income(ts_code=ts_code, start_date='20230101', end_date='20260304')
        df_balance = pro.balsheet(ts_code=ts_code, start_date='20230101', end_date='20260304')
        df_cashflow = pro.cashflow(ts_code=ts_code, start_date='20230101', end_date='20260304')
        print(f"   ✅ {ts_code}: 财务数据获取成功")
    except Exception as e:
        print(f"   ⚠️ {ts_code}: {str(e)}")

# 4. 获取日线行情数据（批量）
print("\n4. 获取股票行情数据...")
for ts_code in focus_stocks[:15]:  # 前 15 只
    try:
        df_daily = pro.daily(ts_code=ts_code, start_date='20250101', end_date='20260304')
        print(f"   ✅ {ts_code}: 行情数据获取成功 ({len(df_daily)} 条)")
    except Exception as e:
        print(f"   ⚠️ {ts_code}: {str(e)}")

# 5. 获取指数数据
print("\n5. 获取大盘指数数据...")
indices = ['000001.SH', '399001.SZ', '399006.SZ', '000016.SH', '000300.SH']
for idx in indices:
    try:
        df_idx = pro.index_daily(ts_code=idx, start_date='20250101', end_date='20260304')
        print(f"   ✅ {idx}: 指数数据获取成功 ({len(df_idx)} 条)")
    except Exception as e:
        print(f"   ⚠️ {idx}: {str(e)}")

# 6. 获取基金数据
print("\n6. 获取基金数据...")
df_fund = pro.fund_basic(market='E')
print(f"   获取到 {len(df_fund)} 只场内基金")

# 7. 获取宏观经济数据
print("\n7. 获取宏观经济数据...")
try:
    df_gdp = pro.gdp()
    df_cpi = pro.cpi()
    df_ppi = pro.ppi()
    print(f"   ✅ GDP/CPI/PPI 数据获取成功")
except Exception as e:
    print(f"   ⚠️ 宏观数据：{str(e)}")

# 8. 获取资金流向数据
print("\n8. 获取资金流向数据...")
try:
    df_moneyflow = pro.moneyflow(ts_code='600519.SH', start_date='20260301', end_date='20260304')
    print(f"   ✅ 资金流向数据获取成功")
except Exception as e:
    print(f"   ⚠️ 资金流向：{str(e)}")

# 9. 获取龙虎榜数据
print("\n9. 获取龙虎榜数据...")
try:
    df_top = pro.top_list(trade_date='20260303')
    print(f"   ✅ 龙虎榜数据获取成功 ({len(df_top)} 条)")
except Exception as e:
    print(f"   ⚠️ 龙虎榜：{str(e)}")

# 10. 获取融资融券数据
print("\n10. 获取融资融券数据...")
try:
    df_margin = pro.margin_detail(trade_date='20260303')
    print(f"   ✅ 融资融券数据获取成功 ({len(df_margin)} 条)")
except Exception as e:
    print(f"   ⚠️ 融资融券：{str(e)}")

# 11. 批量获取更多股票行情（消耗积分大户）
print("\n11. 批量获取 200 只股票行情（消耗积分）...")
sample_stocks = df_stocks.sample(n=200, random_state=42)['ts_code'].tolist()
count = 0
for ts_code in sample_stocks:
    try:
        df = pro.daily(ts_code=ts_code, start_date='20260101', end_date='20260304')
        count += 1
        if count % 50 == 0:
            print(f"   已获取 {count}/200 只...")
    except:
        pass
print(f"   ✅ 完成 {count} 只股票行情获取")

# 12. 获取概念股数据
print("\n12. 获取概念股数据...")
try:
    df_concept = pro.concept()
    print(f"   获取到 {len(df_concept)} 个概念板块")
    
    # 获取前 10 个概念的成分股
    for _, row in df_concept.head(10).iterrows():
        try:
            df_detail = pro.concept_detail(concept=row['code'])
            print(f"   ✅ {row['name']}: {len(df_detail)} 只成分股")
        except:
            pass
except Exception as e:
    print(f"   ⚠️ 概念股：{str(e)}")

print("\n" + "="*60)
print(f"✅ 学习任务完成！结束时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("="*60)
PYTHON_EOF

echo "✅ 凌晨 1:00 任务完成"
