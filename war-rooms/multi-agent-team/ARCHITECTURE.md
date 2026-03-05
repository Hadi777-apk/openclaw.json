# 多智能体团队系统架构

## 系统概述
本系统是一个基于 War Room 方法论的多智能体协作框架，支持多个 AI 模型协同工作。

## 架构图
```
┌─────────────────────────────────────────────────────────────┐
│                      用户界面                                │
│                   (小爪 - COORDINATOR)                       │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                   任务调度层                                  │
│                (Gemini 3.0 - COMMANDER)                      │
│  - 任务分解  - 资源分配  - 结果整合  - 质量控制               │
└────────────────────┬────────────────────────────────────────┘
                     │
        ┌────────────┼────────────┬────────────┐
        │            │            │            │
        ▼            ▼            ▼            ▼
┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐
│  IMAGE    │ │  CODER    │ │ 其他专业  │ │  未来扩展  │
│  Agent    │ │  Agent    │ │   Agent   │ │   Agent   │
│ Nano      │ │  Claude   │ │           │ │           │
│ Banana    │ │   Code    │ │           │ │           │
│    Pro    │ │           │ │           │ │           │
└───────────┘ └───────────┘ └───────────┘ └───────────┘
```

## 目录结构
```
war-rooms/multi-agent-team/
├── BRIEF.md              # 项目简报
├── DNA.md                # 团队核心协议
├── ARCHITECTURE.md       # 本文档
├── DECISIONS.md          # 决策记录
├── STATUS.md             # 实时状态
├── TASK_QUEUE.md         # 任务队列
├── RESULTS.md            # 结果汇总
├── BLOCKERS.md           # 阻塞问题
├── agents/               # 各 Agent 工作区
│   ├── commander/        # Gemini 3.0
│   ├── image/           # Nano Banana Pro
│   ├── coder/           # Claude Code
│   └── coordinator/     # 小爪
├── artifacts/            # 输出产物
├── comms/                # Agent 间通信
├── scripts/              # 自动化脚本
└── references/           # 参考资料
```

## Agent 详细职责

### 🧠 COMMANDER (Gemini 3.0)
**核心能力**:
- 复杂任务分解
- 多 Agent 调度
- 结果质量评估
- 冲突解决

**输入**: 用户任务描述
**输出**: 任务分解方案、最终整合报告

**触发条件**: 需要多步骤协作的复杂任务

### 🎨 IMAGE Agent (Nano Banana Pro)
**核心能力**:
- 文生图 (Text-to-Image)
- 图生图 (Image-to-Image)
- 图像编辑
- 风格迁移

**输入**: 图像需求描述、参考图像
**输出**: 生成的图像文件

**API 配置**:
```bash
NANO_BANANA_API_KEY=your_key_here
NANO_BANANA_MODEL=banana-pro-v1
```

### 💻 CODER Agent (Claude Code)
**核心能力**:
- 代码编写
- 代码审查
- Bug 调试
- 重构优化

**输入**: 功能需求、现有代码
**输出**: 可执行代码、测试用例

**配置**:
```bash
# Claude Code 通过 OpenClaw ACP harness 调用
# 或本地 claude 命令
```

### 🔐 VAULT Agent (小爪 - Qwen) **NEW!**
**核心能力**:
- API Key 统一管理
- 来源记录与追踪
- 余额监控与预警
- 充值指引与建议
- 使用统计与分析

**输入**: API Key、购买记录、余额信息
**输出**: API 状态报告、充值指南、费用分析

**触发条件**: 
- 需要 API Key 时
- API 余额不足时
- 需要充值时
- 查询 API 使用记录时

**特殊职责**:
- 安全存储所有 API Credentials
- 记录每个 Key 的购买渠道
- 提供详细的充值流程
- 生成费用统计报告

### 😈 CHAOS Agent (Gemini 3.0) **NEW!**
**核心能力**:
- 决策挑战与质疑
- 假设检验与验证
- 风险评估与预警
- 对立论证与反思
- 事前验尸与预案

**输入**: 所有决策、计划、假设
**输出**: 挑战报告、风险清单、改进建议

**触发条件**: 
- 重大决策制定时
- 系统架构设计时
- 新功能上线前
- 任何时候需要质疑

**特殊职责**:
- 挑战每个决策的合理性
- 寻找每个方案的漏洞
- 预见潜在风险
- 防止群体思维

### 🐾 COORDINATOR (小爪 - Qwen)
**核心能力**:
- 用户交互
- 文件管理
- API 路由
- 状态跟踪
- 错误处理

**输入**: 用户请求、Agent 输出
**输出**: 最终交付物

**特殊职责**:
- 维护共享文件系统
- 监控 Agent 健康状态
- 处理超时和重试
- 记录决策日志

## 通信机制

### 1. 文件系统通信
所有 Agent 通过共享文件系统交换信息，零 Token 成本。

**共享文件**:
- `STATUS.md` - 各 Agent 当前状态
- `TASK_QUEUE.md` - 待处理任务
- `comms/*.md` - 点对点消息

### 2. 消息格式
```markdown
## [MSG-001] COMMANDER → IMAGE
**类型**: TASK
**优先级**: HIGH
**任务 ID**: IMG-20260305-001
**描述**: 生成阿里巴巴股票分析图表
**要求**: 
- 风格：专业金融图表
- 包含：K 线、成交量、RSI 指标
**截止时间**: 10 分钟
```

### 3. 状态更新
每个 Agent 完成任务后更新 `STATUS.md`:
```markdown
## IMAGE Agent
- 状态：IDLE | WORKING | BLOCKED | ERROR
- 当前任务：IMG-20260305-001
- 进度：0% | 25% | 50% | 75% | 100%
- 预计完成：2026-03-05 18:00
```

## 工作流示例

### 场景：生成股票分析报告 + 可视化图表

1. **用户请求** → COORDINATOR 接收
2. **任务分析** → COMMANDER 分解为：
   - 任务 A: 获取股票数据 (COORDINATOR)
   - 任务 B: 技术分析报告 (COMMANDER)
   - 任务 C: 生成 K 线图 (IMAGE)
   - 任务 D: 编写分析脚本 (CODER)
3. **并行执行** → 各 Agent 同时工作
4. **结果整合** → COMMANDER 整合所有输出
5. **交付用户** → COORDINATOR 呈现最终报告

## 配置管理

### API Keys 存储
**推荐**: 使用环境变量或加密配置文件
```bash
# ~/.openclaw/workspace/.env (加入.gitignore)
GEMINI_API_KEY=...
NANO_BANANA_API_KEY=...
ANTHROPIC_API_KEY=...
```

### 模型配置
```yaml
# config/models.yaml
commander:
  model: gemini-3.0-pro
  max_tokens: 32000
  temperature: 0.7

image:
  provider: nano-banana
  model: banana-pro-v1
  resolution: 1024x1024

coder:
  provider: claude-code
  model: claude-3-5-sonnet
  max_iterations: 10
```

## 错误处理

### 重试策略
- 网络错误：重试 3 次，指数退避
- API 限流：等待后重试
- 超时：切换备用方案

### 降级方案
- IMAGE Agent 不可用 → 使用 ASCII 图表
- CODER Agent 不可用 → 小爪尝试简单代码
- COMMANDER 不可用 → 小爪临时接管调度

## 监控与日志

### 关键指标
- 任务完成时间
- Agent 响应延迟
- API 调用成功率
- 用户满意度

### 日志位置
- `logs/YYYY-MM-DD.md` - 每日日志
- `metrics/` - 性能指标
- `errors/` - 错误记录

## 扩展指南

### 添加新 Agent
1. 在 `agents/` 创建新目录
2. 定义角色职责
3. 更新 DNA.md
4. 测试通信协议

### 支持新模型
1. 添加模型配置
2. 实现适配器
3. 更新路由逻辑

---
*本文档随系统演进持续更新*