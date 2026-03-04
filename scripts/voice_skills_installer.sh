#!/bin/bash
# 凌晨 12:00 任务：安装语音转文字相关技能

echo "⏰ 凌晨 12:00 任务启动：安装语音转文字技能"

# 进入工作目录
cd /Users/john/.openclaw/workspace

# 安装语音转文字技能
echo "Installing tg-voice-whisper..."
npx clawhub install tg-voice-whisper 2>/dev/null || echo "tg-voice-whisper 已存在或安装失败"

echo "Installing speech-to-text..."
npx clawhub install speech-to-text 2>/dev/null || echo "speech-to-text 安装失败或已存在"

echo "Installing openai-whisper..."
npx clawhub install openai-whisper 2>/dev/null || echo "openai-whisper 安装失败或已存在"

echo "Installing telegram-offline-voice..."
npx clawhub install telegram-offline-voice 2>/dev/null || echo "telegram-offline-voice 安装失败或已存在"

echo "✅ 凌晨 12:00 任务完成"