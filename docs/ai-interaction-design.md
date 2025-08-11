# 我们的 AI 课程 · 交互设计语言（基于 Slidev 官方主题）

> 目标：在不改动官方主题（seriph）与默认交互机制的前提下，统一我们课程的用法与风格，做到“简洁、稳定、可直播演示”。

## 基础设定
- 主题: `seriph`（保留官方默认排版与色彩，减少视觉负担）
- 过渡: 全局 `transition: slide-left`；必要时页内可用 `fade-out/slide-up`
- 字体: 使用官方默认；如需覆盖，在 headmatter 里统一配置 `fonts`
- 布局: 首选 `default/center/two-cols`；避免复杂自定义，确保直播稳定
- 资源: 所有图片/视频走 `public/` 绝对路径，占位内容用“占位”文字说明

## 信息密度与节奏
- 每页尽量只放一个核心观点；配合口头扩展
- 列表最多 5 条；更细内容分到下一页
- 整场每页点击步进不超过 5 次

## 动效与步进
- 内容渐进：优先使用 `<v-clicks>` 或 `v-click`
- 强调/对比：优先使用 Magic Move（四反引号 + `md magic-move`）
- 位置动效：少量 `v-motion`，避免大范围平移与旋转

## 代码演示
- 只读讲解：Shiki 高亮 + 行高亮/编号；尽量配合 Magic Move
- 交互编辑：代码块标注 `{monaco}`；对比用 `{monaco-diff}`
- 直接运行：`{monaco-run}`；默认自动运行，必要时 `autorun:false`
- 外部片段：用 `<<< @/snippets/...` 导入，便于复用与维护

## 现场 Demo（LLM/多模态）
- 将 API 调用逻辑封装在 `components/`，避免在 Markdown 中出现密钥
- 需要“可运行”的演示，用 Runner 机制（`setup/code-runners.ts`），或用占位并在直播展示真实效果
- 对“失败案例/边界”保留真实截图或短视频；当前先用“占位”提示

## 演讲者笔记
- 每页末尾 `<!-- ... -->` 加讲者提示：关键点、故事、节奏
- 直播时使用 Presenter 模式查看笔记与下一页预览

## 结构约定
- 入口：`slides.md` 只保留封面、目录与 `src:` 引入章节
- 章节：放在 `pages/`，命名 `01-intro.md`、`02-...` 等
- 片段：放在 `snippets/`；组件/交互 Demo 放在 `components/`

## 直播与导出
- 本期以本地运行 + 直播为主：`pnpm dev`
- 如需导出 PDF/PPTX：先安装 `playwright-chromium`；动画较多的页可增加 `--wait`
- Vercel 托管配置已在 `vercel.json`，无需子路径；构建命令 `npm run build`

## 命名与文风
- 中文为主，术语首次出现附英文括注：如“思维链（Chain of Thought, CoT）”
- 标题短、句子短；避免大段段落
- 图标、表格等按需引用官方内置/示例，减少自定义

---

如需在主题上做二次开发，可后续将主题 `eject` 到本仓库进行小幅调整；当前阶段以复用官方默认为主，优先保证演示稳定性与可维护性。

---

## Headmatter 与 Frontmatter（样式与结构的核心）

> 说明：本节示例与字段来源于官方参考文件 `docs/slides_design_reference.md`，并结合本课程实际使用做了精简与注解。

### 全局 Headmatter（放在 `slides.md` 顶部，仅一次）
用于设置全场主题、背景、标题、字体、全局过渡与能力开关等：

```yaml
---
# You can also start simply with 'default'
theme: seriph
# random image from a curated Unsplash collection by Anthony
background: https://cover.sli.dev
# some information about your slides (markdown enabled)
title: 我们的 AI 课程 · 第一课入口
info: |
  统一风格用于直播授课
class: text-center                  # 全局 UNO 原子类
drawings:
  persist: false                    # 画笔标注是否在页面间保留
transition: slide-left              # 全局页面过渡
mdc: true                           # 开启 MDC 语法（更丰富的 Markdown 组件能力）
seoMeta:
  ogImage: auto
---
```

常用字段说明（节选自官方示例）：
- `theme`: 使用的主题（官方常见 `default`/`seriph`）
- `background`: 全局背景（建议放到 `public/` 后用绝对路径 `/...`）
- `title`/`info`: 页面标题与简介（支持 Markdown）
- `class`: 全局样式原子类
- `drawings.persist`: 画笔标注是否跨页持久
- `transition`: 全局页面切换动效
- `mdc`: 是否启用 MDC 语法
- `seoMeta.ogImage`: 开放图配置（默认自动）

> 可选：如需统一字体，在 Headmatter 增加
> ```yaml
> fonts: { sans: Inter, mono: 'JetBrains Mono' }
> ```

> 可选：Monaco 类型源（来自官方配置，可选 local/cdn/none），推荐默认：
> ```yaml
> monacoTypesSource: local
> ```

### 每页 Frontmatter（页内，位于两条 `---` 之间）
每页可覆盖布局、背景、类名、动效等，仅作用于当前页：

1) 覆盖当页过渡（来自官方示例）
```yaml
---
transition: fade-out
---
```

2) 设置目录层级（来自官方示例）
```yaml
---
transition: slide-up
level: 2
---
```

3) 两栏布局与间距（来自官方示例）
```yaml
---
layout: two-cols
layoutClass: gap-16
---
```

4) 右图布局与图片（来自官方示例）
```yaml
---
layout: image-right
image: https://cover.sli.dev
---
```

5) 覆盖当页样式类（来自官方示例）
```yaml
---
class: px-20
---
```

6) 从外部 Markdown 导入页面（官方示例用法，适配本项目）
```yaml
---
src: ./pages/01-intro.md
hide: false
---
```

7) 居中布局并设置当页类（来自官方示例）
```yaml
---
layout: center
class: text-center
---
```

使用建议：
- 全局样式优先在 Headmatter 配置；个别页面差异再用 Frontmatter 覆盖。
- 图片/视频等资源放 `public/`，Frontmatter 中用绝对路径 `/...`，便于导出与托管。
- 页面布局优先用内置 `default/center/two-cols/image-right` 等，减少自定义以保证直播稳定。

---

## 全局配置清单（精简版，来源于 config_guide.md）

> 以下为与本课程强相关的头部配置，完整清单见 `docs/config_guide.md`。

```yaml
---
# 主题与插件
theme: seriph
addons: []

# 元信息与显示
title: 我们的 AI 课程 · 第一课入口
titleTemplate: '%s - 我们的 AI 课程'
info: | 
  使用 Slidev 官方主题与交互能力，统一风格用于直播授课
author: 讲师姓名
keywords: AI,LLM,Agent

# 运行与导出
presenter: true              # 开启演讲者模式（dev/build 均可）
browserExporter: dev         # 启用浏览器导出入口
download: false              # SPA 下载 PDF 开关
exportFilename: ai-course
export:
  format: pdf
  timeout: 30000
  dark: false
  withClicks: false

# 代码与编辑
twoslash: true
lineNumbers: false
monaco: true
monacoTypesSource: local      # 或 cdn/none
monacoTypesAdditionalPackages: []

# 行为与体验
remoteAssets: false
selectable: true
record: dev
contextMenu: true
wakeLock: true
overviewSnapshots: false

# 视觉与布局
colorSchema: auto
routerMode: history
aspectRatio: 16/9
canvasWidth: 980
themeConfig: { primary: '#6C63FF' }   # 对齐课程“设计语言”的主色
favicon: /favicon.png
fonts: { sans: Inter, mono: 'JetBrains Mono' }

# 默认 Frontmatter（可选，给所有页一个默认布局）
defaults:
  layout: default

# 绘注与多语言
drawings:
  enabled: true
  persist: false
  presenterOnly: false
  syncAll: true
htmlAttrs: { lang: zh-CN }

# SEO
seoMeta:
  ogTitle: 我们的 AI 课程
  ogDescription: 课程 Slides
  ogImage: https://cover.sli.dev
  twitterCard: summary_large_image
---
```

推荐实践：
- 直播教学建议开启 `presenter: true`、`monaco: true`、`twoslash: true`。
- 非必要不改 `aspectRatio` 与 `routerMode`，保持 16/9 与 history。
- 出于稳定性考虑，`monacoTypesSource` 优先 `local`。

## 每页配置清单（精简版，来源于 config_guide.md）

> 放在每一页的 Frontmatter 中，以下为常用项（完整见 `docs/config_guide.md`）。

```yaml
---
clicks: 0                 # 自定义点击总数
clicksStart: 0            # 起始点击数
disabled: false           # 完全禁用并隐藏该页
hide: false               # 同上，别名
hideInToc: false          # 从目录组件中隐藏
layout: default           # 当页布局（如 center/two-cols/image-right）
level: 1                  # 目录层级（配合 title 生效）
preload: true             # 进入前预加载该页
routeAlias:               # 路由别名，用于直达链接
src:                      # 引入外部 Markdown（如 ./pages/01-intro.md）
title:                    # 覆盖当页标题
transition:               # 覆盖当页过渡（如 fade-out）
zoom: 1                   # 当页缩放
dragPos: {}               # 可拖拽元素位置
---
```

