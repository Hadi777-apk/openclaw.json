# 📦 OpenClaw 技能安装计划

_根据用户推荐的技能清单整理_

## 🎯 用户推荐的技能清单

### ⚡️ 新手入门必装
- [ ] **Skill-Vetter** - 安全扫描工具（"数字安全卫士"）
- [ ] **ClawHub** - 技能商店（`clawhub` CLI）
- [ ] **Tavily-Search** - AI 优化联网搜索
- [ ] **Agent-Browser** - 浏览器自动化

### ✨ 高效生产力套装
- [ ] **gog** - Google Workspace 集成
- [ ] **work-report** - Git 驱动周报生成器
- [ ] **focus-timer** - 番茄钟工作法
- [ ] **workflow-automation** - 工作流自动化

### 🎨 创意与内容创作
- [ ] **xhs-note-creator** - 小红书笔记生成器
- [ ] **pw-redbook-image** - 小红书配图生成
- [ ] **remotion-best-practices** - 视频生成

### 🛠️ 开发者专属工具
- [ ] **code-review-pro** - 代码审查专家
- [ ] **git-master** - Git 仓库管理大师
- [ ] **api-designer** - API 设计助手

---

## 📊 当前已安装技能（43 个）

### ✅ 已就绪（Ready）
- apple-reminders
- blogwatcher
- coding-agent
- cron-scheduling
- data-analysis
- economic-calendar-fetcher
- feishu-doc
- feishu-drive
- finance
- financial-calculator
- find-skills
- finnhub-pro
- gcalcli-calendar
- gmail
- himalaya
- market-analysis-cn
- market-environment-analysis
- news-summary
- polymarket-odds
- proactive-agent
- remote-desktop
- security-audit-toolkit
- security-auditor
- self-improving-agent
- stock-analysis
- stock-info-explorer
- stock-monitor-skill
- stock-price-query
- stock-watcher
- summarize
- things-mac
- todo-manager
- trading-coach
- tushare-finance
- us-stock-analysis
- us-value-investing-framework
- war-room
- wechat-pub-auto-update
- xiaohongshu-furniture
- bbc-news
- cfo
- chrome-devtools-mcp
- automation-workflows

### ⚠️ 缺少依赖（Missing）
- clawhub（需要安装 `clawhub` CLI）
- 其他 40+ 个技能缺少二进制文件或配置

---

## 🔧 安装步骤

### Step 1: 安装 ClawHub CLI（技能商店）
```bash
npm install -g clawhub
# 或
npx clawhub --version
```

### Step 2: 使用 ClawHub 搜索和安装技能
```bash
# 搜索技能
npx clawhub search skill-vetter
npx clawhub search tavily-search
npx clawhub search agent-browser

# 安装技能
npx clawhub install skill-vetter
npx clawhub install tavily-search
npx clawhub install agent-browser
```

### Step 3: 验证安装
```bash
openclaw skills check
```

---

## 📝 安装优先级

### 第一优先级（安全 + 基础）
1. **clawhub** - 先装这个才能装其他
2. **skill-vetter** - 安全扫描

### 第二优先级（搜索 + 浏览器）
3. **tavily-search** - 联网搜索
4. **agent-browser** - 浏览器自动化

### 第三优先级（生产力）
5. **gog** - Google 集成
6. **work-report** - 周报生成
7. **focus-timer** - 番茄钟
8. **workflow-automation** - 自动化

### 第四优先级（创意 + 开发）
9. **xhs-note-creator** - 小红书
10. **pw-redbook-image** - 配图
11. **code-review-pro** - 代码审查
12. **git-master** - Git 管理

---

## ⚠️ 注意事项

1. **安全第一** - 安装前用 skill-vetter 扫描
2. **按需安装** - 不要盲目安装一堆
3. **检查依赖** - 有些技能需要 API Key 或配置
4. **本地优先** - 尽量选择本地运行的技能

---

_🐾 小爪整理 · 2026-03-04_
