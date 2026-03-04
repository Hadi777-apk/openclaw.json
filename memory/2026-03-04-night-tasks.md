# 2026-03-04 - 语音技能和夜间学习任务

## 🎤 语音转文字技能安装

### 已安装技能
- **tg-voice-whisper** ✅ - Telegram 语音 Whisper 转录器
  - 安装时间：2026-03-04 21:52
  - 功能：自动将 Telegram 语音消息转成文字
  - 使用场景：用户发送语音 → 技能转文字 → 小爪理解并回复

### 待安装（凌晨 12 点任务）
1. speech-to-text - 通用语音转文字
2. openai-whisper - OpenAI Whisper 本地版
3. telegram-offline-voice - Telegram 离线语音处理

---

## ⏰ 定时任务设置

### 任务 1：凌晨 12:00 - 安装语音技能
- **任务 ID**: be7b4fa3-1eda-4c66-9e07-bc4d00838a7d
- **名称**: install-voice-skills
- **时间**: 每天 00:00
- **内容**: 安装 4 个语音转文字技能
- **脚本**: `scripts/voice_skills_installer.sh`
- **日志**: `data/voice_skills.log`

### 任务 2：凌晨 1:00 - 自主学习股票
- **任务 ID**: e0881dac-0f7a-4d80-af36-edb60fd32524
- **名称**: auto-stock-learning
- **时间**: 每天 01:00
- **内容**: 使用 Tushare 消耗 1 万积分学习股票知识
- **脚本**: `scripts/auto_stock_learning.sh`
- **日志**: `data/stock_learning.log`

---

## 📊 凌晨 1 点学习任务详情

### 学习内容
1. 全 A 股列表（5486 只）
2. 行业分类数据
3. 23 只重点龙头股财务数据
   - 白酒：茅台、五粮液、泸州老窖、洋河、汾酒
   - 家电：美的、格力、海尔
   - 医药：恒瑞、长春高新、华润三九
   - 食品：海天、双汇、伊利
   - 银行：招商、工商、建行
   - 保险：平安、人寿
   - 科技：海康、宁德、比亚迪

4. 股票行情数据（2025-2026 年）
5. 大盘指数数据（上证、深证、创业板等）
6. 基金数据（场内基金）
7. 宏观经济数据（GDP、CPI、PPI）
8. 资金流向数据
9. 龙虎榜数据
10. 融资融券数据
11. 批量 200 只股票行情（消耗积分大户）
12. 概念股数据（879 个概念板块）

### 预期积分消耗
- 预计消耗：~10,000 积分
- 用途：深度学习和数据收集

---

## 📁 相关文件

- `scripts/voice_skills_installer.sh` - 语音技能安装脚本
- `scripts/auto_stock_learning.sh` - 股票学习脚本
- `skills/tg-voice-whisper/` - Telegram 语音转文字技能
- `crontab.txt` - 定时任务配置

---

_🐾 小爪记录 · 2026-03-04 深夜_
