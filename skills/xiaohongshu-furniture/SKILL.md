---
name: 拍照
description: AI修图技能。用于将任何照片通过AI进行处理，如将毛坯房照片转换为装修效果图、换背景、修复画质等。触发条件：用户发送照片并要求处理、修图、变效果图
---

# AI拍照修图技能

## 技能说明

这个技能可以将照片通过AI进行处理，适用于：
- 毛坯房 → 装修效果图
- 换背景
- 画质修复
- 风格迁移
- 物体去除/替换

## 使用方法

1. **用户提供照片**：让用户发送需要处理的照片
2. **说明需求**：告诉我想怎么修（可选）
3. **生成图片**：调用 AI API 生成处理后的图片
4. **返回结果**：将生成的效果图发送给用户

## 图片生成命令

使用 curl 调用 Nano Banana API（免费模型）：

```bash
curl -X POST "https://new.suxi.ai/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $NANO_BANANA_API_KEY" \
  -d '{
    "model": "gemini-2.5-flash-free",
    "messages": [{"role": "user", "content": "Generate an image: [你的提示词]"}]
  }'
```

## 常见场景提示词

### 装修效果图（毛坯→效果）
```
A beautiful modern living room interior design after renovation, minimalist style, bright and spacious, with soft lighting, high-quality furniture, floor-to-ceiling windows, cozy atmosphere, 3D rendering, architectural visualization
```

### 换背景
```
Professional product photo, white background, clean and simple, studio lighting
```

### 画质修复
```
High quality photo, restored, sharp details, professional editing
```

## 输出格式

将生成的 base64 图片解码后发送给用户。

如果用户需要保存到文件：
```bash
echo "$base64_image" | base64 -d > output.png
```

## 注意事项

1. 目前使用 Nano Banana 免费模型 (gemini-2.5-flash-free)
2. 免费模型可能有并发限制
3. 图片生成可能需要几十秒时间