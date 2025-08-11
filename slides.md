---
# You can also start simply with 'default'
theme: seriph
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
background: https://cover.sli.dev
# some information about your slides (markdown enabled)
title: 我们的 AI 课程 · 第一课入口
info: |
  ## AI 能力与边界（第一堂课）
  使用 Slidev 官方主题与交互能力，统一风格用于直播授课。

  运行：pnpm dev · 构建：pnpm build
# apply unocss classes to the current slide
class: text-left max-w-[56ch] mx-auto leading-10 space-y-10
# https://sli.dev/features/drawing
drawings:
  persist: false
# slide transition: https://sli.dev/guide/animations.html#slide-transitions
transition: slide-left
# enable MDC Syntax: https://sli.dev/features/mdc
mdc: true
# open graph
seoMeta:
  # By default, Slidev will use ./og-image.png if it exists,
  # or generate one from the first slide if not found.
  ogImage: auto
  # ogImage: https://cover.sli.dev
# presenter mode
presenter: true
# monaco editor
monaco: true
monacoTypesSource: local
# fonts - 使用思源黑体优化中文显示
fonts: { sans: 'Source Han Sans CN', 'Source Han Sans', 'Noto Sans CJK SC', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', Inter, mono: 'JetBrains Mono' }
# color schema
colorSchema: auto
# router mode
routerMode: history
# aspect ratio
---

# DeeptoAI AI实战营
8 月 2 期 C 班 / 讲师：熊布朗 / 每周 2、4 晚上 8 点

<div @click="$slidev.nav.next" class="mt-12 py-1" hover:bg="white op-10">
  空格进入下一页 <carbon:arrow-right />
</div>

---
src: ./pages/instructor-intro.md
---

---
src: ./pages/course-intro.md
---

---
src: ./pages/01-intro.md
---

---
layout: center
class: text-center
---

# 谢谢观看

<PoweredBySlidev mt-10 />

