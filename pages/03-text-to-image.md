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

---
layout: section
class: text-center
---

# 第二部分：模型能力展示

## 从理论到实战应用

<div class="mt-8 p-4 bg-blue-50 rounded-lg border border-blue-200">
标记说明：✅ 原生支持 | 🟡 替代方案 | ⛔ 不支持
</div>

---
layout: two-cols
class: gap-8
---
## 🎯 高质量图像生成 · 照片真实感

**目标**：风景/人像/产品的写实质感、结构正确、材质可信

**写法骨架**：
- Subject（清楚名词）
- Scene & Action（场景/动作/关系）
- Lens & Light（镜头、光位、时段）
- Aesthetic（风格/颗粒/色彩基调）

**速用模版**：
```
A 35mm candid photo of [subject] at [place/time], 
shallow DOF, backlit rim light, natural skin tone, 
realistic textures, balanced white balance, 
editorial look.
```


::right::

**小贴士**：
- 写实时少用夸张风格词
- 用镜头/光线词替代抽象词
- 先 1:1 试构图，再切 3:2 / 16:9


**模型适配能力**

- **Qwen-Image**：✅（写实/质感好）
- **Seedream 3.0**：✅（结构/真实感与多比例）
- **FLUX 1.1**：✅（高跟随与速度）
- **Imagen 4**：✅（多比例、2K）
- **GPT-5**：✅（生成稳定）

<div class="mt-6 p-3 bg-green-50 rounded border border-green-200 text-sm">
💡 Tips：左右对比同一提示不同镜头（35/50/85mm）效果
</div>

---
layout: two-cols
class: gap-8
---

## 🎨 艺术风格多样性

**目标**：从印象派到赛博朋克、动画/插画、平面构成

**写法骨架**：
- **基准风格词**：watercolor / gouache / ukiyo-e / isometric / brutalism
- **材质**：oil on canvas / risograph / screen print
- **构图**：rule of thirds, central composition, negative space

**速用模版**：
```
[subject] in [style] style, [material], 
[composition], vibrant colors, 
artistic interpretation, masterpiece quality
```

**练习思路**：一条主提示 + 三组"材质+构图"替换，对比风格可控性

::right::
## 模型适配能力

- **Qwen-Image**：✅（多风格泛化）
- **Seedream 3.0**：✅（审美偏好优化）
- **FLUX 1.1**：✅（跟随+多样性；LoRA 可加风格库）
- **Imagen 4**：✅（抽象 & 写实都稳）
- **GPT-5**：✅ （稳）

---
layout: two-cols
class: gap-8
---

## ✍️ 文本渲染（图内字）

**目标**：海报、卡片、商品字样可读、排版稳

**要点**：
- 名词→短句→多行排版，逐步加复杂度
- 先定字体风格/字号范围/字距语义，再给内容
- 长文案建议后期排版叠字，生成器负责底图与少量关键词

**提示骨架**：
```
Poster with two-line headline (bold grotesk), 
subheading (light), bottom caption (mono, small), 
high legibility, proper kerning.
```

::right::
## 模型适配能力


- **Qwen-Image**：✅ 最强中文/英文排版
- **Seedream 3.0**：✅ 小字/多行排版显著增强
- **FLUX 1.1**：🟡（可行但需多次采样或配合后期）
- **Imagen 4**：✅ "优越的排版/拼写"，支持 2K 输出
- **GPT-5**：✅（官方 Images API 强调文本可读）

<div class="mt-4 p-3 bg-orange-50 rounded border border-orange-200 text-sm">
⚡ 关键优势：Qwen-Image 和 Seedream 3.0 在中文文本渲染方面表现突出
</div>

---
layout: two-cols
class: gap-8
---

## 🎛️ 结构控制（ControlNet）

**用途**：用边缘/姿态/深度等条件硬控构图、姿态、布局

- Canny (边缘控制) eg. 火柴人
- Depth (深度控制) eg. 建筑草模 
- Inpaint (局部重绘) eg. 修掉物体
- （扩展：Pose / Scribble / Segmentation 等）

**适用场景**：
- 电商模特姿态控制
- 平面排布精确定位
- 建筑结构线条控制


::right::
## 模型适配能力

<v-clicks>

- **Qwen-Image**：⛔ 无原生 ControlNet；可用参考图+编辑替代
- **Seedream 3.0**：⛔ API 未公开；在即梦画布可通过草图/抠图近似
- **FLUX 1.1**：✅ 有 ControlNet 方案（BFL "Flux.1 Tools" Canny/Depth）
- **Imagen 4**：⛔ Controlled customization 不支持
- **GPT-5**：⛔ 无 ControlNet 接口；用参考图/遮罩软控

</v-clicks>

<div class="mt-4 p-3 bg-blue-50 rounded border border-blue-200 text-sm">
🔧 最佳选择：需要精确结构控制时，FLUX 1.1 是最佳选择
</div>

---
layout: two-cols
class: gap-8
---

## 🖼️ 图像驱动/风格迁移（IP-Adapter）

**用途**：把参考图的风格/主体特征注入到生成结果中

**提示**：
- 分离"风格参考"和"内容参考"
- 分别给权重控制
- 比"上传参考图"更强的对齐效果

**适用场景**：
- 品牌视觉风格统一（logo、色彩、字体风格）
- 角色IP一致性创作（动画、游戏角色）
- 艺术风格模仿（特定画家、摄影师风格）
- 产品设计延续（保持设计语言一致性）

::right::
## 模型适配能力

- **Qwen-Image**：🟡（无原生 IP-Adapter；可用编辑/参考图替代）
- **Seedream 3.0**：🟡（平台侧有"看图改图/多图融合"）
- **FLUX 1.1**：✅ 有 IP-Adapter 权重与节点（XLabs/InstantX 等）
- **Imagen 4**：🟡（可上传输入图 + 提示）
- **GPT-5**：🟡（API 支持 image-to-image/编辑）

---
layout: two-cols
class: gap-8
---

<script setup>
import { ref } from 'vue'

const openControlNetModal = ref(false)
</script>

## 🆚 ControlNet vs IP-Adapter

**核心差异**：


🎯 **ControlNet** = "蓝图/GPS"
- **作用**：结构/几何"硬控"
- **输入**：图像 → 条件图（边缘/骨架/深度）
- **特点**：逐像素对齐，钉住布局

🎨 **IP-Adapter** = "情绪板/风格卡"  
- **作用**：风格/外观/主体特征"软控"
- **输入**：图像 → 语义向量token
- **特点**：不对齐像素，引导外观

::right::

**使用建议**：
- 严格构图/摆位 → ControlNet
- 风格迁移/质感统一 → IP-Adapter
- 既要姿态又要风格 → 两者叠加

<div class="mt-6 flex justify-center">
<button @click="openControlNetModal = !openControlNetModal" class="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors">
📖 {{ openControlNetModal ? '收起详细对比' : '查看详细技术对比' }}
</button>
</div>

<div v-show="openControlNetModal" class="mt-4 p-4 bg-gray-50 rounded-lg border text-xs max-h-60 overflow-y-auto">
  <h4 class="font-bold mb-2">🛠️ 技术差异详解</h4>
  <div class="grid grid-cols-2 gap-4 mb-3">
    <div>
      <strong>ControlNet 翻车模式：</strong>
      <ul class="list-disc list-inside text-xs">
        <li>强度太高→僵硬/难出细节</li>
        <li>条件图脏→伪影</li>
      </ul>
    </div>
    <div>
      <strong>IP-Adapter 翻车模式：</strong>
      <ul class="list-disc list-inside text-xs">
        <li>权重太高→过拟合"一模一样"</li>
        <li>权重太低→风格没进来</li>
      </ul>
    </div>
  </div>
  
  <div class="bg-blue-50 p-3 rounded border-l-4 border-blue-500">
    <strong>💡 一句话总结：</strong>ControlNet是把"参考图"转成蓝图来钉住结构；IP-Adapter是把"参考图"转成风格/特征向量来引导外观。硬控布局→ControlNet；风格一致→IP-Adapter；两者可叠加。
  </div>
</div>

---
layout: two-cols
class: gap-8
---

## ✂️ 局部编辑 / 扩图（In/Outpaint）

**场景**：抠图、去物、补环境、横竖版改造

**技巧**：
- 先低步数试版式，锁定后再高分辨率重推
- 遮罩边缘留 2–4px 羽化
- 注意新旧内容的无缝衔接

::right::
## 模型适配能力

- **Qwen-Image-Edit**：✅ 语义+外观双通道，可精确改图内文字
- **FLUX 1.1 Fill/Kontext**：✅ 补绘/编辑开放权重
- **Seedream 3.0**：✅ 画布支持局部重绘、扩图、消除等工具
- **Imagen 4**：⛔ 不支持编辑
- **GPT-5**：✅ 支持遮罩编辑/变体


---
layout: two-cols
class: gap-8
---

## 🧬 LoRA（一致性/风格注入）

**用途**：小样本定制人物/IP/品牌风格，可热插拔组合

**适用场景**：
- 系列化生产（同风格/同角色的海量图）
- 品牌视觉一致性（长期复现某个风格）
- 角色IP开发（固定人物形象）
- 艺术风格学习（模仿特定画家风格）

**LoRA vs IP-Adapter**：
- **LoRA**："给画师上持久风格插件" - 一次训练，长期复用
- **IP-Adapter**："把参考图直接喂给画师" - 即时借风格，按次使用
- **选择建议**：大批量→LoRA；临时借风格→IP-Adapter

::right::
## 模型适配能力


- **Qwen-Image**：✅ 开源，支持 LoRA 微调与加载
- **FLUX 1.1**：✅ LoRA 生态成熟（训练/推理工具链众多）
- **Seedream 3.0**：⛔ 未公开 LoRA/DreamBooth
- **Imagen 4**：⛔ 本端点不支持主体/风格定制
- **GPT-5**：⛔ 不开放 LoRA/DreamBooth

**实操配方**：
1. 准备 20-100 张风格/角色样本
2. 训练 LoRA；推理时 weight 0.6-0.9 起步
3. 多 LoRA 叠加：总权重别过 1.5-1.8
4. 长期项目：固定 seed/采样器/镜头语汇

<div class="mt-4 p-3 bg-purple-50 rounded border border-purple-200 text-sm">
🎨 开源优势：需要个性化定制时，开源模型具有明显优势
</div>

<div class="mt-3 p-3 bg-blue-50 rounded border border-blue-200 text-xs">
📖 关于LoRA：Low-Rank Adaptation，一种轻量化微调技术。只需几百张样本图片，就能让模型学会特定人物、风格或概念，文件小（通常50-200MB）、加载快，可以像"插件"一样组合使用。
</div>

---
layout: default
class: text-center
---

## 📊 能力对比汇总表

<div class="text-sm mt-8">

| 技巧/模型 | Qwen-Image | Seedream 3.0 | FLUX 1.1 | Imagen 4 | GPT-5 |
|-----------|------------|--------------|----------|----------|-------|
| **写实/多风格生成** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **图内文本渲染** | ✅ 中英强 | ✅ 小字/排版 | 🟡 | ✅ 官方强调排版 | ✅ |
| **ControlNet** | ⛔ 无原生 | ⛔ API 无 | ✅ BFL 工具 & 社区 | ⛔ 受限功能 | ⛔ |
| **IP-Adapter** | 🟡 编辑/参考图替代 | 🟡 即梦"看图改图" | ✅ XLabs/InstantX | 🟡 参考图+提示 | 🟡 image-to-image |
| **局部编辑/扩图** | ✅ Qwen-Image-Edit | ✅ 即梦画布 | ✅ Fill/Kontext | ⛔ 暂时不支持 | ✅ 遮罩编辑 |
| **个性化定制** | ✅ 开源可训/可挂 | ⛔ 未开放 | ✅ LoRA 生态成熟 | ⛔ 不支持定制 | ⛔ |
| **多比例/2K档** | ✅ | ✅ 2K 原生 | ✅ | ✅ 2K 列表 | ✅ |

</div>

<div class="mt-6 p-4 bg-gray-50 rounded-lg border border-gray-200">
💡 选择建议：硬控/一致性 → FLUX 1.1；字形/排版 → Qwen-Image/Seedream 3.0/Imagen 4
</div>

