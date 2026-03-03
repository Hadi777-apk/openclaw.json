# 每日天气预报脚本
# 使用 Open-Meteo API（免费，无需密钥）

# 读取配置
$configPath = "$env:USERPROFILE\.openclaw\workspace\config\weather.json"
if (Test-Path $configPath) {
    $config = Get-Content $configPath -Raw | ConvertFrom-Json
} else {
    $config = @{
        city = "江苏扬中"
        latitude = 32.24
        longitude = 119.82
    }
}

$displayName = "扬中市"

$telegramToken = "8442923841:AAEGc5tRAecTaA4-gLuOlRTeltX81hnCugY"
$telegramChatId = if ($config.telegram.chatId) { $config.telegram.chatId } else { "7732316704" }

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
        Write-Host "Send failed: $_" -ForegroundColor Red
    }
}

function Get-WeatherText($code) {
    $map = @{
        0 = "☀️ 晴朗"; 1 = "🌤️ 主要晴朗"; 2 = "⛅ 多云"; 3 = "☁️ 阴天"
        45 = "🌫️ 雾"; 48 = "🌫️ 雾"; 51 = "🌦️ 毛毛雨"; 53 = "🌧️ 中雨"; 55 = "🌧️ 大雨"
        61 = "🌧️ 小雨"; 63 = "🌧️ 中雨"; 65 = "🌧️ 大雨"
        71 = "🌨️ 小雪"; 73 = "🌨️ 中雪"; 75 = "🌨️ 大雪"
        95 = "⛈️ 雷雨"; 96 = "⛈️ 雷阵雨"; 99 = "⛈️ 大雷雨"
    }
    if ($map.ContainsKey($code)) { return $map[$code] } else { return "🌡️ 未知" }
}

Write-Host "Getting weather for $displayName..."

try {
    $url = "https://api.open-meteo.com/v1/forecast?latitude=$($config.latitude)&longitude=$($config.longitude)&current_weather=true&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,weathercode&timezone=Asia%2FShanghai"
    $response = Invoke-RestMethod -Uri $url -UseBasicParsing
    
    $current = $response.current_weather
    $temp = $current.temperature
    $wind = $current.windspeed
    $daily = $response.daily
    
    $message = "🌤️ *$displayName 天气预报*`n"
    $message += "📅 更新时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')`n`n"
    $message += "━━━━━━━━━━━━━━━━━━`n"
    $message += "📍 *当前天气*`n"
    $message += "🌡️ 温度：$temp°C`n"
    $message += "💨 风速：$wind km/h`n`n"
    
    $message += "━━━━━━━━━━━━━━━━━━`n"
    $message += "📅 *三天天气预报*`n`n"
    
    for ($i = 0; $i -lt 3; $i++) {
        $date = (Get-Date).AddDays($i)
        $dateStr = $date.ToString('MM-dd')
        if ($i -eq 0) { $dayName = "今天" }
        elseif ($i -eq 1) { $dayName = "明天" }
        else { $dayName = "后天" }
        
        $maxTemp = $daily.temperature_2m_max[$i]
        $minTemp = $daily.temperature_2m_min[$i]
        $precip = $daily.precipitation_sum[$i]
        $weatherText = Get-WeatherText($daily.weathercode[$i])
        
        $message += "*$dayName ($dateStr)*`n"
        $message += "📈 最高：$maxTemp°C | 📉 最低：$minTemp°C`n"
        $message += "🌦️ $weatherText`n"
        if ($precip -gt 0) { $message += "💧 降水：$precip mm`n" }
        $message += "`n"
    }
    
    $message += "━━━━━━━━━━━━━━━━━━`n"
    if ($temp -lt 5) { $message += "*👔 穿衣建议：*❄️ 寒冷，请穿厚外套/羽绒服`n" }
    elseif ($temp -lt 15) { $message += "*👔 穿衣建议：*🍂 凉爽，建议穿夹克/风衣`n" }
    elseif ($temp -lt 25) { $message += "*👔 穿衣建议：*😊 舒适，穿长袖 T 恤即可`n" }
    else { $message += "*👔 穿衣建议：*☀️ 炎热，建议穿短袖/裙子`n" }
    
    $maxPrecip = 0
    for ($i = 0; $i -lt 3; $i++) { if ($daily.precipitation_sum[$i] -gt $maxPrecip) { $maxPrecip = $daily.precipitation_sum[$i] } }
    
    if ($maxPrecip -gt 10) { $message += "*☂️ 出门建议：*🌧️ 有大雨，记得带伞！`n" }
    elseif ($maxPrecip -gt 1) { $message += "*☂️ 出门建议：*🌦️ 有小雨，建议带伞`n" }
    else { $message += "*☀️ 出门建议：*😊 天气不错，适合外出`n" }
    
    $message += "━━━━━━━━━━━━━━━━━━`n"
    
    Write-Host $message
    Send-TelegramMessage -message $message
    
} catch {
    $errorMsg = "❌ 获取天气失败：$_"
    Write-Host $errorMsg -ForegroundColor Red
    Send-TelegramMessage -message $errorMsg
}
