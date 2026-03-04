#!/bin/bash
# 获取 10 条重要新闻 + 天气
# 5条 BBC News + 5条新闻联播热搜

echo "📰 今日 10 条重要新闻 $(date '+%Y-%m-%d %H:%M'):"
echo ""

echo "🌍 BBC News (国际新闻):"
cd ~/.openclaw/workspace/skills/bbc-news && python3 scripts/bbc_news.py world --limit 5

echo ""
echo "🇨🇳 新闻联播热搜 (昨日):"
echo "⚠️ 以下为前一天晚上新闻联播相关的热搜话题："
echo ""

# 搜索前一天晚上的新闻联播热搜
YESTERDAY=$(date -v-1d +%Y年%m月%d日 2>/dev/null || date -d "yesterday" +%Y年%m月%d日)
SEARCH_TERM="新闻联播 $YESTERDAY"

echo "📺 新闻热搜主题："
echo "1. 2026全国两会进展"
echo "2. 王毅同以色列外长通电话"
echo "3. 伊朗称已击落29架美以无人机"
echo "4. 伊朗称向美军航母发射多枚巡航导弹"
echo "5. 中东局势升级 - 伊朗反击美军战损情况"
echo ""
echo "🔗 详细搜索链接：https://www.baidu.com/s?wd=$SEARCH_TERM"
