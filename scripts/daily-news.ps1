# 每日科技新闻摘要脚本
# 获取三个网站的 RSS 并总结

# Telegram 配置
$telegramToken = "8442923841:AAEGc5tRAecTaA4-gLuOlRTeltX81hnCugY"
$telegramChatId = "7732316704"

function Send-TelegramMessage {
    param([string]$message)
    try {
        $url = "https://api.telegram.org/bot$telegramToken/sendMessage"
        $body = @{
            chat_id = $telegramChatId
            text = $message
            parse_mode = "Markdown"
        } | ConvertTo-Json
        Invoke-RestMethod -Uri $url -Method Post -Body $body -ContentType "application/json; charset=utf-8"
    } catch {
        Write-Host "❌ 发送 Telegram 失败：$_" -ForegroundColor Red
    }
}

$urls = @{
    "少数派" = "https://sspai.com/feed"
    "IT 之家" = "https://www.ithome.com/rss/"
}

$news = @()

foreach ($name in $urls.Keys) {
    $url = $urls[$name]
    try {
        $response = Invoke-WebRequest -Uri $url -UseBasicParsing -TimeoutSec 15
        $xml = [xml]$response.Content
        $items = $xml.rss.channel.item | Select-Object -First 5
        foreach ($item in $items) {
            $news += [PSCustomObject]@{
                Source = $name
                Title = $item.title
                Link = $item.link
                Date = $item.pubDate
            }
        }
    } catch {
        Write-Host "❌ $name 获取失败：$_"
    }
}

if ($news.Count -eq 0) {
    $errorMsg = "❌ 未能获取到任何新闻，请稍后再试"
    Write-Host $errorMsg -ForegroundColor Red
    Send-TelegramMessage -message $errorMsg
    exit
}

# 生成摘要消息
$message = "📰 *每日科技新闻摘要*`n"
$message += "📅 $(Get-Date -Format 'yyyy-MM-dd')`n`n"

# 选 5 条最重要的
$top5 = $news | Select-Object -First 5
for ($i = 0; $i -lt $top5.Count; $i++) {
    $item = $top5[$i]
    $message += "$($i+1). *$($item.Title)*`n"
    $message += "   来源：$($item.Source)`n"
    $message += "   🔗 $($item.Link)`n`n"
}

$message += "---`n"
$message += "_🤖 由 OpenClaw 自动推送_"

Write-Host $message

# 发送到 Telegram
Send-TelegramMessage -message $message
