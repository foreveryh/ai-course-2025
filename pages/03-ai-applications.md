---
layout: cover
---

# 第三课 · 文生图 & 文生视频
从想法到成片：工作流 × 提示词 × 选型 × 排错

---
layout: image-right
image: /03_01.jpeg
---

## 我们本周要做出来的
- 一张 **2K 竖版海报**（清晰可读）
- （可选）**40s 短片**：3–6 镜头，风格延续
- 你将会掌握：
  - 结构化提示词写法
  - 构图与文本渲染的稳妥方案

---
layout: default
class: text-left max-w-[60ch] mx-auto leading-8 space-y-6
---

## 📋 课程目录

<v-clicks>

1. **扩散模型的介绍和发展**  
   <span class="text-sm opacity-75">了解一点 Diffusion 模型</span>

2. **文生图模型的各类能力展示**  
   <span class="text-sm opacity-75">从写实到艺术，从人物到场景的全方位展示</span>

3. **提示词技巧（通用 + 模型/场景特定）**  
   <span class="text-sm opacity-75">结构化提示词与精细化控制技巧</span>

4. **常用图像生成工具推荐**  
   <span class="text-sm opacity-75">主流工具对比与选型指南</span>

</v-clicks>

<div class="mt-8 pt-4 border-t border-gray-200">
附：常见坑与排错、小抄模板、合规要点、一致性与后期小流程
</div>

---

---
layout: image-right
image: /diffusion-model-building.gif
backgroundSize: contain
---

## 🎨 扩散模型：当前主流技术

<v-clicks>

**扩散模型（DDPM/SDXL/SD3/FLUX等）**

- **作用**：学会去噪 - 从噪声一步步把图"擦"出来
- **长处**：训练稳定、质量和多样性都高，也是当下主流
- **短板**：推理要多步（慢）。但可以用少步、蒸馏、加速采样等技巧提速

</v-clicks>

<div class="mt-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
💡 现在几乎所有流行的文生图都是扩散路线，之所以能在家用显卡上跑，是因为它常在"潜在空间"里作画。
</div>

---
layout: default
class: text-left max-w-[65ch] mx-auto leading-8 space-y-6
---

## 🔧 关键技术术语解析

<v-clicks>

- **扩散模型**：像"从雪花噪点里逐步显影"的数码冲印
- **潜在空间（Latent）**：模型在"缩小版世界"里先画好，再放大到真实尺寸
- **CLIP/多模态对齐**：像双语词典，把文字和图像放进同一个语义坐标系里
- **ControlNet**：给模型一张"线稿/骨架/深度图"，就像填色本先定轮廓再上色
- **DreamBooth/LoRA**：像给模型安装"新词条/风格插件"，小成本记住某个人/风格
- **Seed**：随机数种子 = "复现场景的钥匙"

</v-clicks>

## ⚙️ 核心参数解析

<v-clicks>

- **CFG（提示遵循强度）**：太低跑偏、太高死板/出现噪点
- **Steps（迭代步数）**：适中即可，过高收益递减
- **分辨率**：尽量一开始就接近目标尺寸，需要的话再做无损放大

</v-clicks>

---
layout: default
class: text-center
---

## 🎯 我们只需要选好模型，写好提示词


<div class="flex flex-wrap justify-center gap-3 mt-6">

<div class="flex flex-col items-center">
<img src="/text-to-image/qwen-image.png" class="rounded-lg shadow-md w-28 h-28 object-cover" />
<div class="text-xs text-gray-600 mt-1 text-center">Qwen-Image</div>
</div>

<div class="flex flex-col items-center">
<img src="/text-to-image/gpt5.png" class="rounded-lg shadow-md w-28 h-28 object-cover" />
<div class="text-xs text-gray-600 mt-1 text-center">GPT-5</div>
</div>

<div class="flex flex-col items-center">
<img src="/text-to-image/flux1.1_ultra.png" class="rounded-lg shadow-md w-28 h-28 object-cover" />
<div class="text-xs text-gray-600 mt-1 text-center">FLUX 1.1</div>
</div>

<div class="flex flex-col items-center">
<img src="/text-to-image/seedream.jpeg" class="rounded-lg shadow-md w-28 h-28 object-cover" />
<div class="text-xs text-gray-600 mt-1 text-center">即梦 3.0</div>
</div>

</div>

<div class="flex justify-center mt-4">
<div class="flex flex-col items-center">
<img src="/text-to-image/Imagen4_ultra.png" class="rounded-lg shadow-lg w-36 h-36 object-cover border-2 border-blue-300" />
<div class="text-sm font-semibold text-blue-600 mt-2">Imagen 4 Ultra（当前最强）</div>
</div>
</div>

> ### 提示词："I'm rich!" in the style of a propaganda poster

---
layout: default
class: text-left max-w-[65ch] mx-auto leading-8
---

## 📅 文生图模型发展时间线

<v-clicks>

<div class="space-y-4">

**2022年**
- **Stable Diffusion v1.5** - 2022.10
  <span class="text-sm opacity-75">开源模型普及化的重要里程碑</span>

**2023年**  
- **Midjourney v5** - 2023年3月
  <span class="text-sm opacity-75">商业模型的重大突破，图像质量显著提升</span>
- **SDXL 1.0** - 2023年7月  
  <span class="text-sm opacity-75">更高分辨率，更精细的图像生成</span>

**2024年**
- **FLUX.1** - 2024年8月
  <span class="text-sm opacity-75">新一代开源模型，性能大幅提升</span>

**2025年**
- **即梦 3.0** - 2025年4月
  <span class="text-sm opacity-75">中文原生模型的重大进展</span>
- **Imagen 4** - 2025年6月
  <span class="text-sm opacity-75">Google的最新力作，多模态能力强化</span>

</div>

</v-clicks>

<div class="mt-6 p-4 bg-gray-50 rounded-lg border border-gray-200 text-sm">
🚀 从开源普及到商业突破，再到多模态融合，文生图技术正在快速发展
</div>

