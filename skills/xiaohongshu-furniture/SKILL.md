---
name: xiaohongshu-furniture
description: 全屋定制装修效果图生成。用于将毛坯房照片转换为装修效果图，适合小红书种草、给客户展示方案。触发条件：用户需要生成装修效果图、渲染图、全屋定制方案图
---

# 全屋定制效果图生成

## 技能说明

这个技能可以将毛坯房照片通过AI转换为装修效果图，适用于：
- 小红书种草笔记
- 客户方案展示
- 全屋定制案例分享

## 使用方法

1. **用户提供照片**：让用户发送毛坯房照片
2. **选择装修风格**：现代简约/北欧/新中式/奶油风/轻奢等
3. **生成图片**：调用 Nano Banana (Gemini 2.5 Flash Image) 生成效果图
4. **返回结果**：将生成的效果图发送给用户

## 图片生成命令

使用 curl 调用 Nano Banana API：

```bash
curl -X POST "https://new.suxi.ai/v1/images/generations" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $NANO_BANANA_API_KEY" \
  -d '{
    "prompt": "A beautiful modern living room interior design, minimalist style, bright and spacious, with soft lighting, high-quality furniture, floor-to-ceiling windows, cozy atmosphere, 3D rendering, architectural visualization",
    "model": "gemini-2.5-flash-image",
    "size": "1024x1024"
  }'
```

## 风格关键词

| 风格 | 英文关键词 |
|------|------------|
| 现代简约 | modern minimalist, clean lines, simple |
| 北欧风 | Scandinavian, light wood, white walls |
| 新中式 | modern Chinese, traditional elements, elegant |
| 奶油风 | cream color palette, soft, warm |
| 轻奢 | luxury, gold accents, elegant |
| 工业风 | industrial, exposed brick, metal |

## 输出格式

将生成的 base64 图片解码后发送给用户。

如果用户需要保存到文件：
```bash
echo "$base64_image" | base64 -d > output.png
```