# 多智能体系统使用示例

## 场景 1: 生成股票分析图表

### 用户请求
"帮我生成阿里巴巴股票的技术分析图表，包含 K 线、RSI 和 MACD"

### 系统处理流程
1. COORDINATOR 接收请求，创建任务文件
2. COMMANDER 分解任务:
   - 获取股票数据 (COORDINATOR)
   - 分析技术指标 (COMMANDER)
   - 生成图表 (IMAGE Agent)
3. 各 Agent 并行执行
4. COMMANDER 整合结果
5. COORDINATOR 交付用户

### 任务文件示例
```markdown
# 任务：生成股票分析图表

**提交时间**: 2026-03-05 18:00
**优先级**: NORMAL
**描述**: 生成阿里巴巴 (BABA) 股票技术分析图表

**要求**:
- 图表类型：专业金融 K 线图
- 技术指标：RSI(14), MACD(12,26,9)
- 时间范围：6 个月
- 风格：深色背景，清晰标注

**输出**: PNG 图像文件
```

---

## 场景 2: 开发股票监控脚本

### 用户请求
"帮我写一个 Python 脚本，监控 10 只股票的价格，超过 5% 涨跌幅就发通知"

### 系统处理流程
1. COORDINATOR 接收请求
2. COMMANDER 分析需求，分配给 CODER Agent
3. CODER (Claude Code) 编写代码
4. COORDINATOR 测试并交付

### 任务文件示例
```markdown
# 任务：开发股票监控脚本

**提交时间**: 2026-03-05 18:30
**优先级**: HIGH
**描述**: 开发实时股票价格监控脚本

**功能需求**:
- 监控 10 只指定股票
- 实时获取价格 (Yahoo Finance API)
- 涨跌幅超过 5% 时发送通知
- 支持配置股票代码列表
- 日志记录所有价格变动

**技术栈**: Python 3.10+
**输出**: 可执行的 Python 脚本 + 使用说明
```

---

## 场景 3: 多步骤深度分析

### 用户请求
"深度分析腾讯控股，包括基本面、技术面、舆情分析，并生成投资报告"

### 系统处理流程
1. COORDINATOR 接收复杂请求
2. COMMANDER 分解为多个子任务:
   - 基本面分析 (COMMANDER)
   - 技术面分析 (COORDINATOR + 技术指标)
   - 舆情分析 (COMMANDER + 网络搜索)
   - 生成可视化图表 (IMAGE Agent)
   - 编写分析报告 (COMMANDER)
3. 多 Agent 并行协作
4. 整合所有输出为完整报告

---

## 快速开始

1. 配置 API Keys:
   ```bash
   cd war-rooms/multi-agent-team
   cp .env.example .env
   # 编辑 .env 填入真实的 API Keys
   ```

2. 启动系统:
   ```bash
   ./scripts/start.sh
   ```

3. 提交任务:
   ```bash
   ./scripts/submit_task.sh my_task.md
   ```

4. 检查进度:
   ```bash
   ./scripts/check_status.sh
   ```
