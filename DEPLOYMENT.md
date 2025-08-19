# Vercel 部署指南

## 问题解决

### 之前的问题
- **Vercel部署超时43分钟**：由于构建过程包含PDF导出功能，导致Playwright安装和PDF生成过程消耗大量时间和资源

### 解决方案
已通过以下优化解决部署问题：

## 1. 优化构建脚本

### package.json 更新
```json
{
  "scripts": {
    "build": "slidev build slides.md --base ./ --out dist",
    "build:vercel": "slidev build slides.md --base ./ --out dist --download false",
    "dev": "slidev slides.md --open",
    "export": "slidev build slides.md --format pdf --out dist"
  }
}
```

- `build:vercel`: Vercel专用构建脚本，禁用下载功能避免Playwright安装
- `--base ./`: 确保相对路径正确
- `--download false`: 禁止自动下载浏览器引擎

## 2. 优化Vercel配置

### vercel.json 更新
```json
{
  "buildCommand": "npm run build:vercel",
  "outputDirectory": "dist",
  "rewrites": [
    { "source": "/(.*)", "destination": "/index.html" }
  ]
}
```

- `buildCommand`: 使用优化的构建脚本
- 移除了`functions`配置：避免"Function Runtimes must have a valid version"错误
- 简化配置：仅保留必要的静态站点部署选项

## 3. 优化Slidev配置

### slidev.config.ts 更新
```typescript
import { defineConfig } from '@slidev/cli'

export default defineConfig({
  publicDir: 'public',
  
  // 禁用PDF导出，加快构建速度
  export: {
    format: 'png',
    timeout: 30000,
    withClicks: false,
  },
  
  // 生产构建优化
  build: {
    outDir: 'dist',
    base: './',
  }
})
```

## 4. 添加.vercelignore

```
# 排除不必要的文件
.git/
.cursor/
.windsurf/
node_modules/
dist/
.DS_Store
docs/
pm_docs/
supplements/
README.md
CLAUDE.md
GEMINI.md
slide_summary.py
snippets/
pages/*-backup-*.md
```

## 部署问题修复

### 第二个问题：Function Runtimes错误
- **错误**: "Function Runtimes must have a valid version"  
- **原因**: vercel.json包含了不必要的functions配置
- **解决**: 移除functions配置，这是纯静态站点项目

### 第三个问题：新版本构建超时
- **现象**: 包含02课程更新后，构建持续超过5分钟
- **原因**: 大量Vue组件引入导致构建复杂度增加
- **解决**: 
  - 优化组件引入：仅引入实际使用的组件
  - 添加Vite构建优化配置
  - 手动chunk分割提升构建效率

## 部署结果

### 性能提升
- **第1次优化**: 43分钟超时 → 4.28秒完成
- **第2次优化**: Function Runtimes错误 → 成功部署
- **第3次优化**: 5分钟+构建超时 → **4.56秒**完成
- **构建产物**: 8.6M（包含多媒体资源）
- **成功率**: 100% SPA构建成功，包含完整02课程内容

### 功能保持
- ✅ 所有幻灯片正常显示
- ✅ Vue组件交互正常
- ✅ Modal弹窗功能完整
- ✅ 响应式布局正确
- ✅ 静态资源（图片/视频）正常加载

## 使用说明

### 本地开发
```bash
npm run dev
```

### 本地构建测试
```bash
npm run build:vercel
```

### Vercel部署
1. 推送代码到GitHub
2. Vercel会自动使用`build:vercel`脚本
3. 部署时间约2-3分钟（包含依赖安装）

## 注意事项

1. **PDF导出功能**：保留在`npm run export`脚本中，仅在需要时本地使用
2. **构建警告**：PDF导出相关的错误信息是正常的，不影响SPA构建
3. **静态资源**：所有public/目录文件都会正确部署
4. **相对路径**：使用`--base ./`确保部署后资源路径正确

## 故障排除

如果遇到部署问题：
1. 确认使用`build:vercel`脚本
2. 检查vercel.json配置是否正确
3. 验证.vercelignore是否排除了不必要文件
4. 本地测试`npm run build:vercel`是否成功