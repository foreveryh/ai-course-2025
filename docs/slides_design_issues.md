# Slides 设计常见问题与解决方案（含可复制配置）

> 目标：在保持 Slidev 官方主题（seriph）与默认交互的前提下，提供一份“能直接落地”的设计改进手册。涵盖全局 Headmatter 与每页 Frontmatter 的配置模板，并附实施清单。

---

## 一、常见问题与改进方案

### 1) 层级冲突（多个大标题同屏）
- 症状：同页出现两个大标题（主副标题不清晰）。
- 方案：仅保留一个 H1 主标题；副标题使用小字或页眉/封面展示。
- 每页 Frontmatter 与正文范式：
```yaml
---
layout: center
class: text-left max-w-4xl mx-auto leading-8
---
# 01 AI 能力与边界
<p class="text-gray-500 text-2xl mt-2">开场与引入</p>
```

### 2) 行长过长（横向阅读压力大）
- 症状：中文段落或列表单行跨全屏，难以扫读。
- 方案：限制内容宽度（容器 max-w）、或使用两栏布局分流内容。
```yaml
---
layout: two-cols
layoutClass: gap-12
class: max-w-6xl mx-auto
---
# 课程目标
- 理解 LLM 工作原理
- 掌握能力圈与边界
::right::
<ul class="list-disc ml-6 space-y-3 text-xl leading-8">…</ul>
```

### 3) 留白不足、节奏单调
- 症状：标题与正文/列表间距过小；各项过密；一次性出现所有信息。
- 方案：增大段前段后与行距；列表项加入 `space-y-*`；使用 `<v-clicks>` 分步出现。
```md
<v-clicks>
<ul class="list-disc ml-6 space-y-3 text-2xl leading-8">
  <li>本课聚焦 <b>大语言模型（LLM）</b></li>
  <li>目标：理解 <b>原理</b>、<b>能力圈</b> 与 <b>边界</b></li>
  <li>输出：判断任务是否在 AI 能力范围</li>
</ul>
</v-clicks>
```

### 4) 字号与对比过强
- 症状：标题过大、正文也很大，视觉压迫；整行着色影响可读性。
- 方案：标题降一级；正文统一为易读大小（`text-xl` 或 `text-2xl`）；仅对关键词加粗/标记（`v-mark`）。

### 5) 项目符号过“重”
- 症状：黑色方块项目符号影响节奏。
- 方案：使用圆点列表并增加左缩进。
```md
<ul class="list-disc ml-6 space-y-3">…</ul>
```

### 6) 目录与层级不一致
- 症状：目录层级与实际标题级别不匹配。
- 方案：对需要控制的页在 Frontmatter 指定 `title` 与 `level`；或者对某页 `hideInToc: true`。
```yaml
---
level: 1
title: 开场与引入
hideInToc: false
---
```

### 7) 代码块过高或难以对比
- 症状：代码块占满屏、难滚动；对比讲解不连贯。
- 方案：限制高度并允许滚动；或使用 Magic Move/分组代码块对比讲解；交互演示时改用 `{monaco}` / `{monaco-run}`。
示例容器：
```html
<div class="max-h-96 overflow-auto">
  <!-- 放置代码块 -->
</div>
```
示例代码块：
```ts {lines:true}
// 你的代码…
```

### 8) 资源路径导致构建后失效
- 症状：相对路径图片/视频在导出或托管后丢失。
- 方案：静态资源放 `public/`，以绝对路径使用：`/covers/lesson-01.png`；背景图走 Frontmatter：
```yaml
---
background: /covers/lesson-01.png
---
```

### 9) 动效过多影响理解
- 症状：频繁的 motion/大幅度位移、旋转分散注意。
- 方案：全局过渡用 `slide-left`；页内主要用 `v-clicks`；少量 `v-motion` 用于轻微强调；Magic Move 用于代码/结构演进。

### 10) 可访问性与可读性
- 建议：文本与背景对比充足（深灰正文 `text-gray-800`，弱化说明 `text-gray-500`）；图片加 `alt`；控制点击步进（每页 ≤ 5 次）。

---

## 二、可复制的全局 Headmatter（推荐）
将以下片段放在 `slides.md` 顶部（Headmatter）统一样式与能力：
```yaml
---
theme: seriph
background: https://cover.sli.dev
title: 我们的 AI 课程 · 第一课入口
info: |
  使用 Slidev 官方主题与交互能力，统一风格用于直播授课
class: text-center
transition: slide-left
mdc: true
presenter: true
monaco: true
monacoTypesSource: local
fonts: { sans: Inter, mono: 'JetBrains Mono' }
colorSchema: auto
routerMode: history
aspectRatio: 16/9
canvasWidth: 980
# 默认给所有页面一个基础版式
defaults:
  layout: default
  class: text-left leading-8
seoMeta: { ogImage: auto }
---
```

---

## 三、每页 Frontmatter 范式（常用模板）

### A) 居中+受控行长（单栏讲解）
```yaml
---
layout: center
class: text-left max-w-4xl mx-auto leading-8
transition: fade-out
level: 1
---
# 页标题
<p class="text-gray-500 text-2xl mt-2">副标题或说明</p>
```

### B) 两栏布局（左文右码/图）
```yaml
---
layout: two-cols
layoutClass: gap-12
class: max-w-6xl mx-auto
---
# 要点
- 关键点 A
- 关键点 B
::right::
```
```ts {monaco}
console.log('demo')
```

### C) 外部页导入（章节拆分）
```yaml
---
src: ./pages/01-intro.md
hide: false
---
```

### D) 控制目录显示
```yaml
---
level: 2
title: 模块标题
hideInToc: false
---
```

---

## 四、实施清单（本仓库）
- 统一全局设置：更新 `slides.md` 头部为“二、全局 Headmatter（推荐）”。
- 每页逐步套用范式：
  - `pages/01-intro.md`：采用“居中+受控行长”模板；列表使用 `list-disc ml-6 space-y-3`；关键术语用 `<b>` 或 `v-mark`；使用 `<v-clicks>` 控制节奏。
  - 需要对比/代码演示的页：换成“两栏布局”模板，右侧放代码或示意图。
- 静态资源迁移至 `public/`，以绝对路径引用。
- 点击步进控制：每页不超过 5 次；必要时拆页。

如需，我可以按上述清单直接对现有 `slides.md` 与 `pages/01-intro.md` 应用这些设定并提交编辑。