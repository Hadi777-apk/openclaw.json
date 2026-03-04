# 2026-03-04 - 最终定时任务安排

## ⏰ 定时任务清单

### 每天执行的任务

| 时间 | 任务名称 | 任务 ID | 内容 | 状态 |
|------|---------|--------|------|------|
| **00:00** | learning-skills-search | 467cfa97-a814-4946-a4fe-0562390442cf | 搜索和安装学习型技能 | ✅ 已设置 |
| **01:00** | auto-stock-learning | ec86c1ee-463c-4df7-aa96-39ead4a505b3 | 自主学习股票知识（消耗 1 万积分） | ✅ 已设置 |
| **07:30** | morning-weather | 1fbbcdfb-b543-403f-ae4e-187986bd6ef6 | 三天天气预报 | ✅ 已存在 |
| **08:00** | morning-news | 588c0850-0edc-4bf4-bc03-ba1c1e01127f | 热点新闻推送 | ✅ 已存在 |
| **09:00 (4 月 3 日)** | check-shanxifenjiu | 244ddbc4-d35c-4f13-a64a-1f493f15f52d | 检查山西汾酒持仓盈亏 | ✅ 已存在 |

---

## 📚 凌晨 12 点任务详情

### 目标
搜索和安装能让 AI 学习知识、变强的技能

### 搜索方向
1. **自我改进类**
   - self-improving-agent（已有）
   - autonomous-learning
   - adaptive-learning
   - learning-agent

2. **记忆与知识库类**
   - ontology
   - knowledge-graph
   - memory-architect
   - longterm-memory
   - knowledge-base
   - agent-memory

3. **学习与推理类**
   - semantic-search
   - rag-builder
   - context-enhancer
   - cognitive-architect
   - intelligent-reasoning

### 搜索渠道
1. **ClawHub** - npx clawhub search/install
2. **GitHub** - awesome-openclaw-skills
3. **VoltAgent** - 精选技能集合

### 选择标准
- 高评分（Stars）
- 高人气
- 能把知识存入知识库
- 能让 AI 自我学习和进化

---

## 📊 凌晨 1 点任务详情

### 目标
使用 Tushare 消耗 1 万积分学习股票知识

### 学习内容
1. 全 A 股列表（5486 只）
2. 行业分类数据
3. 23 只重点龙头股财务数据
4. 股票行情数据（2025-2026 年）
5. 大盘指数数据
6. 基金数据
7. 宏观经济数据（GDP/CPI/PPI）
8. 资金流向数据
9. 龙虎榜数据
10. 融资融券数据
11. 批量 200 只股票行情
12. 概念股数据（879 个概念板块）

### 脚本
`scripts/auto_stock_learning.sh`

### 日志
`data/stock_learning.log`

---

## 📝 相关脚本

1. **learning_skills_installer.sh** - 凌晨 12 点技能搜索安装
2. **auto_stock_learning.sh** - 凌晨 1 点股票学习
3. **daily-weather.sh** - 早上 7:30 天气推送
4. **daily-news.sh** - 早上 8:00 新闻推送
5. **check_portfolio.py** - 4 月 3 日持仓检查

---

## 📁 文件结构

```
/Users/john/.openclaw/workspace/
├── scripts/
│   ├── learning_skills_installer.sh    # 凌晨 12 点任务
│   ├── auto_stock_learning.sh          # 凌晨 1 点任务
│   ├── daily-weather.sh                # 7:30 天气
│   ├── daily-news.sh                   # 8:00 新闻
│   └── voice_skills_installer.sh       # 已废弃
├── memory/
│   ├── 2026-03-04-night-install.md     # 安装记录
│   └── 2026-03-04-night-tasks.md       # 任务记录
├── crontab.txt                         # 定时任务配置
└── data/
    ├── learning_skills.log             # 技能安装日志
    ├── stock_learning.log              # 股票学习日志
    ├── weather.log                     # 天气推送日志
    └── news.log                        # 新闻推送日志
```

---

## ✅ 状态总结

- ✅ 凌晨 12 点：学习型技能搜索安装
- ✅ 凌晨 1 点：股票知识学习（1 万积分）
- ✅ 早上 7:30：天气预报
- ✅ 早上 8:00：新闻推送
- ✅ 4 月 3 日：持仓盈亏检查

---

_🐾 小爪整理 · 2026-03-04 22:30_
