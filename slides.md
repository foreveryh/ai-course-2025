---
# 主题设置 - 使用官方 seriph 主题
theme: seriph
# 背景图片 - 建议替换为自定义背景
background: https://cover.sli.dev
backgroundSize: cover
# 课程元信息
title: DeeptoAI AI 实战营 · 8月2期
titleTemplate: '%s - DeeptoAI'
info: |
  ## AI 能力与边界（第一堂课）
  
  本课程面向个人创业者、独立开发者、个体产品人，
  通过 Google AI Studio 等工具，实现 AI 产品从 0 到 1。

  🚀 运行：`pnpm dev`  
  📦 构建：`pnpm build`  
  📄 导出：`pnpm export`

# 全局样式类 - 遵循设计规范
class: text-center
# 绘图功能配置
drawings:
  persist: false
  presenterOnly: false
  syncAll: true
# 页面过渡动画
transition: slide-left
# MDC 语法支持
mdc: true
# SEO 和开放图谱
seoMeta:
  ogImage: auto
  ogTitle: DeeptoAI AI 实战营
  ogDescription: 4周内，从想法到产品发布的完整 AI 项目实战
  twitterCard: summary_large_image

# 功能开关
presenter: true              # 演讲者模式
monaco: true                 # Monaco 编辑器
monacoTypesSource: local     # 类型源
twoslash: true              # TwoSlash 支持
lineNumbers: false          # 代码行号

# 字体配置 - 优化中文显示
fonts:
  sans: 'Inter, Source Han Sans CN, Noto Sans CJK SC, PingFang SC, Microsoft YaHei'
  mono: 'JetBrains Mono, Source Code Pro, Consolas'
  
# 视觉与行为
colorSchema: auto           # 颜色方案
routerMode: history         # 路由模式
aspectRatio: 16/9          # 宽高比
# canvasWidth: 980           # 画布宽度

  
# 其他配置
remoteAssets: true         # 远程资源
selectable: true           # 文本可选
record: dev               # 录制模式
contextMenu: true         # 右键菜单
wakeLock: true           # 防止休眠
---

# DeeptoAI AI 实战营

<div class="mt-8">
  <div class="text-4xl font-bold text-primary mb-4">
    🚀 8月2期 C班
  </div>
  
  <div class="text-2xl text-gray-600 space-y-2">
    <p>👨‍🏫 讲师：熊布朗</p>
    <p>📅 时间：每周二、四 晚8点</p>
    <p>⏱️ 周期：4周项目制实战</p>
  </div>
</div>

<div class="absolute bottom-10 left-0 right-0">
  <div @click="$slidev.nav.next" class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-primary/10 hover:bg-primary/20 transition-colors cursor-pointer">
    <span class="text-lg">开始学习</span>
    <carbon:arrow-right class="text-xl" />
  </div>
  
  <p class="mt-4 text-sm text-gray-500">
    按 <kbd class="px-2 py-1 rounded bg-gray-200">空格</kbd> 或点击继续
  </p>
</div>

<!--
演讲者笔记：
- 欢迎学员，营造轻松氛围
- 简单介绍课程安排
- 确认大家能看到画面和听到声音
-->

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

# 🙏 感谢参与

<div class="mt-8 space-y-4">
  <p class="text-2xl text-gray-600">期待在课程中与大家一起成长</p>
  
  <div class="flex justify-center gap-8 mt-12">
    <a href="https://github.com/foreveryh" target="_blank" class="flex items-center gap-2 text-gray-600 hover:text-primary transition-colors">
      <carbon:logo-github class="text-2xl" />
      <span>GitHub</span>
    </a>
    <a href="https://x.com/Stephen4171127" target="_blank" class="flex items-center gap-2 text-gray-600 hover:text-primary transition-colors">
      <carbon:logo-x class="text-2xl" />
      <span>我的 X（联系我）</span>
    </a>
  </div>
</div>

<PoweredBySlidev class="absolute bottom-10" />

<!--
演讲者笔记：
- 感谢大家的参与
- 提醒课后作业
- 预告下次课程内容
-->

