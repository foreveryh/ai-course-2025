# DeeptoAI AI 实战营 - 8月2期

基于 [Slidev](https://sli.dev) 构建的完整 AI 实战课程幻灯片系统。

## 📋 项目概览

本项目是 DeeptoAI AI 实战营的官方课程材料，包含完整的幻灯片、代码示例和实践指南。

**课程信息：**
- 🎯 **目标学员**: 个人创业者、独立开发者、个体产品人
- ⏱️ **课程周期**: 4周项目制实战
- 📅 **上课时间**: 每周二、四 晚8点
- 👨‍🏫 **讲师**: 熊布朗

## 🚀 快速开始

### 前置要求

- Node.js >= 18
- npm 或 pnpm

### 本地开发

```bash
# 安装依赖
npm install

# 启动开发服务器
npm run dev

# 在浏览器中访问 http://localhost:3030
```

### 构建部署

```bash
# 构建静态文件
npm run build

# 预览构建结果
npx vite preview --outDir dist
```

### 导出 PDF

```bash
# 导出为 PDF
npm run export
```

## 📁 项目结构

```
.
├── slides.md                 # 主幻灯片入口文件
├── pages/                    # 章节幻灯片目录
│   ├── instructor-intro.md   # 讲师介绍
│   ├── course-intro.md       # 课程介绍
│   ├── 01-intro.md           # 第1章：AI能力与边界
│   └── 02-prompt.md          # 第2章：提示词工程
├── public/                   # 静态资源
│   ├── *.jpg                 # 图片资源
│   ├── *.png                 # 图片资源
│   ├── *.mp4                 # 视频资源
│   └── *.webp                # 图片资源
├── docs/                     # 文档目录
│   ├── assignment/           # 作业模板
│   ├── eval/                 # 评估报告
│   └── *.md                  # 设计指南和规范
├── pm_docs/                  # 项目管理文档
├── components.d.ts           # Vue 组件类型声明
├── slidev.config.ts          # Slidev 配置文件
├── vercel.json              # Vercel 部署配置
└── package.json             # 项目依赖配置
```

## 🎨 课程内容

### 第1章：AI 能力与边界
- LLM 基础原理
- Transformer 架构
- 能力边界分析
- 实际应用案例

### 第2章：提示词工程
- RACER 模型
- 上下文工程
- 结构化输出
- 实战练习

### 实践作业
- 📝 作业模板：`docs/assignment/`
- ✅ 评估清单：完整的验收标准
- 🎯 实战项目：从0到1的完整流程

## 🛠 技术栈

- **框架**: [Slidev](https://sli.dev) - 为开发者打造的演示框架
- **主题**: Seriph - 优雅的学术风格主题
- **语言**: Vue 3 + TypeScript + Markdown
- **样式**: UnoCSS + TailwindCSS
- **部署**: Vercel

## 🎯 特性

### 幻灯片功能
- ✨ **交互式演示**: 渐进式内容展示
- 🎨 **丰富组件**: 自定义 Vue 组件支持
- 📱 **响应式设计**: 适配多种设备
- 🎭 **多种模式**: 
  - 演讲者模式 (`/presenter`)
  - 概览模式 (`/overview`) 
  - 笔记模式 (`/notes`)

### 开发体验
- 🔥 **热重载**: 实时编辑预览
- 📝 **Markdown 优先**: 专注内容创作
- 🎯 **TypeScript 支持**: 类型安全
- 🔍 **代码高亮**: 多语言语法高亮

### 部署优化
- 📦 **静态生成**: SPA 单页应用
- 🚀 **CDN 友好**: 资源优化和缓存
- 🌐 **SEO 优化**: 开放图谱支持

## 🔧 自定义配置

### 主题配置
主要配置在 `slides.md` 顶部的 frontmatter 中：

```yaml
---
theme: seriph           # 主题选择
title: 课程标题         # 页面标题
background: 背景图      # 背景设置
class: text-center      # 全局样式
transition: slide-left  # 页面过渡
---
```

### 字体配置
针对中文优化的字体栈：
- **无衬线**: Inter, Source Han Sans CN, PingFang SC
- **等宽字体**: JetBrains Mono, Source Code Pro

### 样式系统
- 基于 UnoCSS 的实用优先 CSS
- 完整的设计系统和组件库
- 响应式断点和暗色模式支持

## 📚 相关链接

- 📖 [Slidev 官方文档](https://sli.dev)
- 🎨 [主题文档](https://github.com/slidevjs/themes)
- 💻 [课程代码仓库](https://github.com/foreveryh/ai-course-2025)
- 🔗 [在线访问](https://ai-course-2025.vercel.app)

## 👥 贡献指南

如果你发现任何问题或有改进建议：

1. 🍴 Fork 本仓库
2. 🌿 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 💾 提交更改 (`git commit -m 'Add amazing feature'`)
4. 📤 推送到分支 (`git push origin feature/amazing-feature`)
5. 🔀 开启 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 了解详情。

## 📞 联系方式

- **GitHub**: [@foreveryh](https://github.com/foreveryh)
- **X (Twitter)**: [@Stephen4171127](https://x.com/Stephen4171127)
- **项目主页**: [AI Course 2025](https://ai-course-2025.vercel.app)

---

⭐ 如果这个项目对你有帮助，请给它一个 star！
