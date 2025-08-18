# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个基于 Slidev 构建的 AI 实战营课程幻灯片项目，包含完整的课程内容、交互式演示和多媒体资源。

## 常用命令

### 开发环境
```bash
# 启动开发服务器（支持热重载）
npm run dev

# 访问地址：http://localhost:3030
```

### 构建和部署
```bash
# 构建 SPA 静态文件
npm run build

# 预览构建结果
npx vite preview --outDir dist

# 导出 PDF（需要 Playwright，生产环境通常禁用）
npm run export
```

### 项目维护
```bash
# 清理构建缓存
rm -rf dist node_modules/.vite

# 重新安装依赖
npm install

# 验证构建输出
tree dist/
```

## 核心架构

### 文件结构
- **slides.md**: 主入口文件，包含课程配置和目录
- **pages/**: 章节幻灯片文件，每个章节一个独立 .md 文件
  - `instructor-intro.md`: 讲师介绍
  - `course-intro.md`: 课程介绍  
  - `01-intro.md`: 第1章 AI能力与边界
  - `02-prompt.md`: 第2章 提示词工程
- **components/**: Vue 组件目录（交互式演示组件）
- **public/**: 静态资源（图片、视频、多媒体文件）
- **docs/**: 文档和指南
  - `slides_design_reference.md`: 严格参考的样式和交互语法
  - `slides_guideline.md`: 制作指南
  - `assignment/`: 作业模板
  - `eval/`: 评估标准

### Slidev 配置
- **主题**: seriph（学术风格）
- **字体**: 针对中文优化的字体栈
- **功能**: 支持演讲者模式、绘图、Monaco 编辑器、TwoSlash
- **SEO**: 包含开放图谱和 Twitter Card 配置

### 课程内容架构
采用模块化结构，通过 `src: ./pages/filename.md` 引入子模块：
- 每个章节独立的 .md 文件
- 渐进式内容展示（`v-click`）
- 交互式 Vue 组件集成
- 多媒体资源支持

## 开发规范

### Cursor 规则集成
根据 `.cursor/rules/slidescreate.mdc`：
1. 主要任务是制作内容、设计和交互完整的 Slides
2. 严格遵循 `docs/slides_design_reference.md` 的语法规范
3. 注重课程内容的交互形式设计
4. 图片和视频使用占位符，后续替换实际资源

### 内容开发最佳实践
- **模块化**: 长幻灯片拆分为多个文件
- **交互性**: 使用 `<v-clicks>`、`<!-- v-click -->` 实现渐进展示
- **资源管理**: 所有静态资源放置在 `public/` 目录
- **组件使用**: 复杂交互通过自定义 Vue 组件实现

### 部署配置
- **Vercel**: 使用 `vercel.json` SPA 路由配置
- **构建输出**: 禁用 PDF 导出以避免 Playwright 依赖问题
- **静态资源**: 通过 `slidev.config.ts` 配置 `publicDir: 'public'`

## 故障排除

### 常见问题
1. **白屏**: 检查 SPA 路由配置和静态资源加载
2. **构建失败**: 通常与 PDF 导出相关，在 slides.md 中设置 `export: false`
3. **资源 404**: 确认 `public/` 目录结构和相对路径引用

### 调试步骤
1. 验证本地构建：`npm run build`
2. 检查构建输出：`ls -la dist/`
3. 本地预览：`npx vite preview --outDir dist`
4. 查看浏览器开发者工具的 Console 和 Network 面板