# 2026-03-04 - 夜间技能安装任务

## 📋 用户推荐的 4 个技能

### 已存在 ✅
1. **self-improving-agent** - 已安装 (`skills/self-improving-agent/`)
   - 让 AI 越用越懂你
   - 来源：clawhub.ai/pskoett/self-improving-agent

2. **Find Skills** - 已安装
   - 把 ClawHub 变成工具助手
   - 来源：clawhub.ai/JimLiuxinghai/find-skills

3. **Agent Browser** - 已安装
   - 给 AI 一双手
   - 来源：clawhub.ai/TheSethRose/agent-browser

### 未找到 ❌
4. **Ontology** - 未找到 exact match
   - 给 AI 一个真正的记忆系统
   - 来源：clawhub.ai/oswalpalash/ontology
   - ClawHub 搜索结果：只有 `obsidian-ontology-sync`（相似，已跳过）
   - GitHub awesome-openclaw-skills：未找到
   - **策略**：凌晨 12 点任务会再次尝试安装，找不到就跳过

---

## ⏰ 定时任务设置

### 凌晨 12:00 - 安装 Ontology 技能
- **任务 ID**: be7b4fa3-1eda-4c66-9e07-bc4d00838a7d
- **名称**: install-voice-skills（已重命名用途）
- **时间**: 每天 00:00
- **内容**: 
  1. 检查 self-improving-agent（已有，跳过）
  2. 尝试安装 ontology（多种名称尝试）
  3. 找不到就跳过
- **脚本**: `scripts/voice_skills_installer.sh`
- **日志**: `data/voice_skills.log`

### 已取消的任务
- ~~凌晨 1:00 自主学习股票（消耗 1 万积分）~~ ❌ 已取消
- ~~凌晨 12:00 安装语音技能~~ ❌ 已取消（用户说明天手动安装）

---

## 🎤 语音转文字技能

### 当前状态
- **tg-voice-whisper** ✅ 已安装
- **依赖**: ffmpeg 和 whisper 未安装
- **计划**: 用户明天到公司后手动安装

```bash
# 明天需要执行的命令
brew install ffmpeg
pip3 install openai-whisper --break-system-packages
```

---

## 📁 相关文件

- `scripts/voice_skills_installer.sh` - 凌晨 12 点技能安装脚本（已更新）
- `skills/self-improving-agent/` - 自我改进技能
- `skills/tg-voice-whisper/` - 语音转文字技能
- `crontab.txt` - 定时任务配置（已更新）

---

## 🔍 搜索结果总结

| 渠道 | self-improving-agent | ontology |
|------|---------------------|----------|
| **ClawHub** | ✅ 已安装 | ❌ 未找到 |
| **GitHub awesome** | ✅ 已存在 | ❌ 未找到 |
| **备注** | 早就装好了 | 只有 obsidian-ontology-sync（跳过） |

---

_🐾 小爪记录 · 2026-03-04 晚上_
