# 技能清理记录

_2026-03-04 23:05_

---

## 🗑️ 已删除的技能（4 个）

| 技能名 | 删除原因 | 用户说明 |
|--------|---------|---------|
| **blogwatcher** | 用户没有订阅博客 | "我没有订阅博客，把这个功能也删了" |
| **todo-manager** | 与 Things 3 重复 | 统一用 things-mac |
| **apple-reminders** | 与 Things 3 重复 | 统一用 things-mac |
| **wechat-pub-auto-update** | 用户不运营公众号 | "公众号运营也删了吧" |

---

## ✅ 保留的技能（47 个）

### 股票金融类（13 个）- 全部保留
- a-stock-monitor
- finance
- financial-calculator
- finnhub-pro
- stock-analysis
- stock-info-explorer
- stock-monitor-skill
- stock-price-query
- stock-watcher
- trading-coach
- tushare-finance
- us-stock-analysis
- us-value-investing-framework

### 新闻资讯类（3 个）- 删除 1 个
- bbc-news ✅
- news-summary ✅
- ~~blogwatcher~~ ❌ 已删除

### 办公通讯类（6 个）- 全部保留
- feishu-doc
- feishu-drive
- gcalcli-calendar
- gmail
- gog
- himalaya

### 开发工具类（7 个）- 全部保留
- api-designer
- chrome-devtools-mcp
- coding-agent
- remote-desktop
- summarize
- war-room
- automation-workflows

### AI 自我进化类（4 个）- 全部保留
- agent-browser
- find-skills
- proactive-agent
- self-improving-agent

### 安全审计类（3 个）- 全部保留
- security-audit-toolkit
- security-auditor
- skill-vetter

### 笔记文档类（3 个）- 删除 2 个
- cfo ✅
- data-analysis ✅
- things-mac ✅（统一使用）
- ~~todo-manager~~ ❌ 已删除
- ~~apple-reminders~~ ❌ 已删除

### 效率工具类（5 个）- 全部保留
- cron-scheduling
- economic-calendar-fetcher
- polymarket-odds ✅（用户需要预测市场）
- tavily-search
- market-analysis-cn

### 内容创作类（2 个）- 删除 1 个
- xhs-note-creator ✅
- xiaohongshu-furniture ✅
- ~~wechat-pub-auto-update~~ ❌ 已删除

---

## 📊 技能统计

| 状态 | 数量 |
|------|------|
| 清理前 | 51 个 |
| 已删除 | 4 个 |
| **清理后** | **47 个** |

---

## 🎯 任务管理统一方案

**统一使用**: `things-mac`

**理由**:
1. 用户是 Mac 用户（MacBook Air）
2. Things 3 是 macOS 原生应用，体验最佳
3. 支持本地数据库读写，速度快
4. 支持 URL scheme，可快速添加任务

**已删除的替代方案**:
- todo-manager - 通用待办，功能重复
- apple-reminders - Apple 官方提醒事项，但与 Things 3 相比功能较弱

---

## 🌐 浏览器自动化对比

### chrome-devtools-mcp vs agent-browser

| 特性 | chrome-devtools-mcp | agent-browser |
|------|--------------------|---------------|
| **来源** | Google 官方 | Vercel Labs |
| **技术栈** | Node.js + Puppeteer | Rust + Node.js 回退 |
| **GitHub Stars** | 较新，stars 较少 | 较新，stars 较少 |
| **热度** | Google 官方背书 | Vercel Labs 支持 |
| **特点** | Chrome DevTools Protocol 原生支持 | Rust 性能优势，CLI 友好 |
| **使用场景** | 深度 Chrome 集成、性能分析 | 快速 CLI 自动化、AI 代理交互 |
| **依赖** | Chrome/Chromium | Node.js + npm |

### 详细对比

#### chrome-devtools-mcp
- **优势**:
  - Google 官方出品
  - 完整的 Chrome DevTools Protocol 支持
  - 性能追踪和分析功能强大
  - 网络请求深度检查
  - 控制台消息捕获
  
- **劣势**:
  - 依赖 Chrome 浏览器
  - 配置相对复杂
  - 需要 MCP 服务器模式运行

- **适用场景**:
  - 性能分析和优化
  - 深度网络调试
  - 需要 Chrome 特定功能的场景

#### agent-browser
- **优势**:
  - Rust 编写，性能优秀
  - CLI 设计友好，易于脚本化
  - 语义定位器（semantic locators）
  - 会话管理（多浏览器并行）
  - 状态保存/加载（认证会话复用）
  - 视频录制功能
  
- **劣势**:
  - 相对较新，社区较小
  - 功能可能不如 Puppeteer 全面

- **适用场景**:
  - AI 代理自动化
  - 快速网页交互
  - 表单填写和数据提取
  - 需要多会话并行的场景

### 建议

**两个都保留**，因为：
1. **互补而非重复**：chrome-devtools-mcp 适合深度调试和性能分析，agent-browser 适合快速自动化
2. **不同场景**：前者是 MCP 服务器模式，后者是 CLI 工具
3. **技术栈不同**：一个依赖 Chrome，一个是独立 Rust 二进制

**使用建议**:
- 日常自动化 → 优先用 `agent-browser`（CLI 简单快速）
- 性能分析/深度调试 → 用 `chrome-devtools-mcp`
- 需要视频录制 → 用 `agent-browser`
- 需要 MCP 协议集成 → 用 `chrome-devtools-mcp`

---

## ⚠️ 待办事项

### 明天需要安装
```bash
brew install ffmpeg
pip3 install openai-whisper --break-system-packages
```

### 可选优化
- 评估 `himalaya` 和 `gmail` 是否重复（建议统一用 Gmail API）
- 定期检查技能使用频率

---

_🐾 小爪整理 · 2026-03-04 23:05_
