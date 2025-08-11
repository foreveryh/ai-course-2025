# 我们的 AI 课程 · Slidev 使用手册（含设计语言与最佳实践）

> 面向：在本地结合 IDE / Claude Code 进行教学开发与演示
> 框架：**Slidev**（slide + dev）——开发者友好的 Web 幻灯工具，Markdown 驱动，内置交互、代码高亮、实时录制与托管能力。官网文档见“Guide”与“Built-in/Customizations”。 ([sli.dev][1])

---

## 1) 我们的库与官网

* **选型：Slidev**（MIT 开源）
  关键词：Markdown + Vue 组件、Shiki 高亮、Monaco 编辑器/Runner、演讲者模式、录制/摄像头、导出 PDF/PPTX/PNG、可托管为 SPA。 ([GitHub][2], [sli.dev][3])
* **官网（文档）入口**：Guide（入门、语法、UI、动画、主题/插件、组件、布局、导出、托管等），当前文档版本标注为 *v52.1.0*。 ([sli.dev][4])
* **创建与运行**：`pnpm create slidev` 或 `npm init slidev@latest`；常用脚本：`slidev`（开发预览）、`slidev export`（导出 PDF/PPTX/PNG/MD）、`slidev build`（构建 SPA）。 ([sli.dev][4])
* **CLI 亮点**：

  * `--remote [password]` 远程演示/控制（可设访问口令）；
  * `--base` 子路径部署；
  * `slidev theme eject` 主题拆出可二次开发。 ([sli.dev][5])

---

## 2) 课程 Slides 的信息架构与目录约定（推荐做法）

* **多文件拆分**：用每页前置 `src:` 指向外部 Markdown，亦可按编号片段导入（如 `#2,5-7`）。便于多人协作与复用。 ([sli.dev][6])
* **约定式目录**（可选但强烈建议）：

  ```
  your-slidev/
  ├─ components/    # 自定义 Vue 组件（交互 Demo、AI 组件）
  ├─ layouts/       # 自定义布局
  ├─ public/        # 静态资源（前置里用绝对路径 /img.png）
  ├─ setup/         # shiki/monaco/runner/mermaid 等配置
  ├─ snippets/      # 代码片段（配合 <<< 导入、monaco-write）
  ├─ styles/        # 全局样式、UnoCSS 扩展
  ├─ slides.md      # 入口
  └─ vite.config.ts # Vite 扩展
  ```

  注意：前置/组件内的相对资源路径在构建后会失效，需放到 `public/` 用绝对路径（如 `background: /image.png`）。 ([sli.dev][7])

---

## 3) Slidev 独有/核心用法（尽量详述）

### 3.1 Markdown + 前置（Headmatter/Frontmatter）

* 顶部 **Headmatter** 配置全局（主题、标题、字体、过渡、Monaco 类型源等）；每页 **Frontmatter** 配置布局、背景、类名等：

  ```md
  ---
  theme: seriph
  title: AI Course
  fonts: { sans: Inter, mono: "JetBrains Mono" }
  transition: slide-left
  ---
  ---
  layout: center
  background: /cover.png
  class: text-white
  ---
  ```

  详见「Slides deck configurations & Per slide configurations」与「Configure Fonts」。 ([sli.dev][3])

### 3.2 演讲者笔记与界面

* 每页末尾 `<!-- ... -->` 为**演讲者笔记**；播放时底部导航可开 **Presenter Mode**、**Quick Overview**、导出页、黑暗模式、摄像头、录制、内置编辑器等。还有 `/presenter`、`/overview` 专页。快捷键可自定义。 ([sli.dev][3])

### 3.3 动画系统（点击步进 + 过渡 + Motion）

* **点击步进**：`v-click`、`v-after`、`<v-clicks>`（含 `depth`/`every`）+ 相对/绝对位置（`at:"+1"` / `v-click="3"`），以及隐藏（`.hide`）、区间 `[enter, leave)`、`<v-switch>`。
* **过渡**：页面级 `transition: fade | slide-left | view-transition | ...`。
* **Motion**：`v-motion`（基于 @vueuse/motion），支持按点击变体 `:click-2-4`。

  > 可自定义 `.slidev-vclick-target`/`.slidev-vclick-hidden` 过渡样式。 ([sli.dev][8])

### 3.4 代码与编辑：Shiki + Monaco（编辑/Runner/写回）

* **高亮**：内置 **Shiki**，支持 Magic Move、TwoSlash、行高亮/行号/最大高度、代码分组等。Magic Move 用四反引号 \`\`\` `md magic-move ` 组合多段代码，实现“逐步变形”。 ([sli.dev][9])
* **Monaco 编辑器**：代码块后加 `{monaco}` 变可编辑；`{monaco-diff}` 显示 Diff。可在 `setup/monaco.ts` 配置全局 `editorOptions` 与类型获取源（内置扫描依赖类型，或切为 `monacoTypesSource: ata`）。 ([sli.dev][10])
* **Monaco Runner**：`{monaco-run}` 一键运行代码，默认自动运行，可 `{autorun:false}`。 ([sli.dev][11])
* **可写回文件**：结合 `<<< @/snippets/foo.ts {monaco-write}` 直接在演示里编辑并保存**本地文件**（谨慎使用）。另有 `<<<` 片段导入、支持 VS Code 区域选择。 ([sli.dev][12])
* **自定义 Runner**：在 `setup/code-runners.ts` 里注册语言（如 `python`）、或把执行代理到 WebWorker/远端服务，用于教学沙箱/在线评测。Runner 可返回 text/html/Element，且可组合调用其他 runner。 ([sli.dev][13])

### 3.5 组件与布局

* **直接用 Vue 组件**（免显式导入，得益于 unplugin-vue-components）。可用：内置组件（箭头、可拖拽、TOC、视频/YouTube、链接跳转、基于点击的 VSwitch、RenderWhen 等）、主题/插件提供的组件、自定义 `components/`。 ([sli.dev][14])
* **内置布局**：`cover/default/center/end/two-cols/two-cols-header/quote/statement/fact/full/image/iframe-*` 等，多列用 `::right::` 分栏。 ([sli.dev][15])

### 3.6 图表/数学/图解

* **LaTeX**（KaTeX）、**Mermaid/PlantUML** 可直接用；分别可在 `setup/katex.ts` 与 `setup/mermaid.ts` 改主题/变量。 ([sli.dev][3])

### 3.7 全局层（Global Layers）与自定义 UI

* 在项目根创建 `global-top.vue`、`global-bottom.vue` 或 `custom-nav-controls.vue`，即可为**整场**演示挂载导航/页脚/进度条/互动控件；还支持单页 `slide-top.vue` / `slide-bottom.vue`。 ([sli.dev][16])

### 3.8 绘注/摄像头/录制/集成编辑器

* **Drawing & Annotations**：导航栏打开画笔，实时同步到各实例。
* **Camera & Recording**：内置摄像头画中画，支持位置尺寸记忆；可直接录制讲解。
* **Integrated Editor**：在播放界面侧边直接编辑 `slides.md` 并热更新。 ([sli.dev][17])

### 3.9 导出与托管

* **导出**：推荐浏览器导出 UI（/export）；CLI 结合 `playwright-chromium` 输出 PDF / PPTX（按点击导出 `--with-clicks`）/ PNG / MD。
* **托管**：`slidev build` 生成 SPA（`--base` 子路径）；提供 GitHub Pages/Netlify/Vercel/Docker 示例。 ([sli.dev][18])

---

## 4) 我们这门 AI 课的「Best Practices」

> 下列为**课程实践建议**（非官方强制），结合 Slidev 官方能力实现。

1. **信息架构**

* 入口 `slides.md` 只放章节骨架；各章放到 `pages/`，通过每页 `src:` 引用；代码放 `snippets/`；演示组件放 `components/`；全场控件（计时、反馈按钮、进度）做成 **Global Layers**。 ([sli.dev][6])

2. **代码演示**

* 只读展示：Shiki + 行高亮/编号/MaxHeight；渐进讲解用 **Magic Move**。
* 交互演示：`{monaco}` + `{monaco-run}`；需要状态对比时用 `{monaco-diff}`。
* 现场改代码并保存：`{monaco-write}` 仅对**示例仓库**文件使用，先备份/版本控制。 ([sli.dev][9])

3. **AI/LLM Demo**

* 把调用 LLM 的逻辑封装成 `components/AIDemo.vue`，通过 `fetch` 命中你本地代理或云端 API（避免在 Markdown 里直接写密钥）。
* 如需让学生在幻灯中“运行”生成：以 **Monaco Runner 自定义语言**（如 `prompt` 或 `python`）把代码/Prompt 发送到教学后端，Runner 返回渲染片段或图片/视频 URL，结果插在 Runner 输出区。 ([sli.dev][13])

4. **动效规范**

* 内容出现用 `v-clicks`，强调/对比用 Magic Move；跨页使用 `transition: slide-left` 或 `view-transition`（浏览器支持需留意）；少量 `v-motion` 做位移动画。 ([sli.dev][8])

5. **资源与构建**

* 背景/视频封面等用于前置或组件 prop 的资源放 `public/` 并用绝对路径 `/...`；导出 PDF/PPTX 前装好 `playwright-chromium`，必要时 `--wait` 保证动画完成。 ([sli.dev][19])

6. **演示流程**

* 两窗口：观众看 Play 页面，讲者用 Presenter 页面；需要远程时 `slidev --remote [password]`，绑定公网 IP 或内网穿透。 ([sli.dev][20])

---

## 5) 我们这门 AI 课程的「设计语言」

> 目标：清晰、克制、具科研感，专注内容与互动。

* **色彩**：`primary #6C63FF`、`accent #00C2A8`、`ink #111827`、`muted #6B7280`、背景浅色 `#F7F7FB` / 深色 `#0B1020`（跟随主题暗色）。
* **字体**（前置里统一）：

  ```yaml
  fonts:
    sans: Inter
    mono: JetBrains Mono
  ```

  Slidev 会从 Google Fonts 自动拉取，确保代码与正文风格一致。 ([sli.dev][21])
* **网格与留白**：大标题上下 96px，正文段落 16–20px 行距；左右两栏时以 `two-cols`，右栏用于代码/示例。 ([sli.dev][15])
* **图标**：使用 Iconify（vscode-icons 集合）与代码块/分组的自动图标匹配能力，统一风格。 ([sli.dev][22])
* **代码主题**：Shiki 选择 `min-dark/min-light`，并开启行高亮/行号；讲解改造选用 **Magic Move**。 ([sli.dev][9])
* **动效**：

  * 页面过渡：`slide-left`；
  * 内容出现：`v-clicks`（列表逐项）；
  * 关键术语：`v-motion` 轻微位移；
  * 复杂变更：Magic Move；
  * 控制速率：每页不超过 5 次点击。 ([sli.dev][8])
* **图解**：流程/结构图用 Mermaid，统一 `theme: 'forest'` 或自定义 themeVariables。 ([sli.dev][23])
* **全局层**：底部细进度条（全局层）、右下角 Q\&A 呼出按钮（自定义导航控件），左上角课程徽标（暗色自动切换）。 ([sli.dev][16])

---

## 6) 快速代码片段（可直接复制）

```bash
# 初始化
pnpm create slidev
pnpm dev
```

```md
<!-- slides.md：章节骨架 + 外链页面 -->
# 课程封面
副标题 / 讲师 / 时间

---

src: ./pages/01-foundation.md

---

src: ./pages/02-llm-basics.md

---

src: ./pages/03-prompting.md
```

```ts
// setup/monaco.ts：统一编辑器行为
import { defineMonacoSetup } from '@slidev/types'
export default defineMonacoSetup(() => ({
  editorOptions: { wordWrap: 'on' }
}))
```

```ts
// setup/code-runners.ts：把 “prompt” 作为可运行语言，调用你本地教学后端
import { defineCodeRunnersSetup } from '@slidev/types'
export default defineCodeRunnersSetup(() => ({
  async prompt(code, ctx) {
    const res = await fetch('/api/generate', {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({ prompt: code })
    }).then(r => r.json())
    return { html: `<div class="prose">${res.html ?? res.text}</div>` }
  }
}))
```

> Runner 机制与 Monaco 配置详见官方文档。 ([sli.dev][13])

---

## 7) 参考索引（便于查回）

* 入门与语法：Getting Started / Syntax Guide。([sli.dev][4])
* 动画与 Motion：Animations。([sli.dev][8])
* 组件与布局（内置清单）：Built-in Components / Layouts。([sli.dev][24])
* 编辑器与代码：Monaco Editor / Runner / Magic Move / Import Snippet。([sli.dev][10])
* 全局层与 UI：Global Layers / User Interface。([sli.dev][16])
* 录制/摄像头/侧边编辑器：Recording / Integrated Editor。([sli.dev][25])
* 导出与托管：Exporting / Hosting。([sli.dev][18])
* CLI：Slidev CLI。([sli.dev][5])
* 目录结构/资源处理：Directory Structure / FAQ-Assets。([sli.dev][7])

---

### 最后提示

* **交互导出限制**：PDF/PPTX 仅为静态渲染，交互需部署为 SPA。 ([sli.dev][18])
* **浏览器兼容**：View Transitions、录制/摄像头等在不同环境兼容性不同，演前实机检查。 ([sli.dev][8])

如果你愿意，我可以基于上面的设计语言，直接帮你把一个「课程模板仓库」骨架生成出来（包含分章、全局层、Runner 示例与主题预设）。

[1]: https://sli.dev/guide/?utm_source=chatgpt.com "Getting Started"
[2]: https://github.com/slidevjs/slidev?utm_source=chatgpt.com "slidevjs/slidev: Presentation Slides for Developers"
[3]: https://sli.dev/guide/syntax "Syntax Guide | Slidev"
[4]: https://sli.dev/guide/ "Getting Started | Slidev"
[5]: https://sli.dev/builtin/cli "Slidev CLI | Slidev"
[6]: https://sli.dev/features/importing-slides.html?utm_source=chatgpt.com "Importing Slides"
[7]: https://sli.dev/custom/directory-structure "Directory Structure | Slidev"
[8]: https://sli.dev/guide/animations "Animation | Slidev"
[9]: https://sli.dev/custom/config-highlighter?utm_source=chatgpt.com "Configure Highlighter"
[10]: https://sli.dev/features/monaco-editor?utm_source=chatgpt.com "Monaco Editor"
[11]: https://sli.dev/features/monaco-run?utm_source=chatgpt.com "Monaco Runner"
[12]: https://sli.dev/features/monaco-write?utm_source=chatgpt.com "Writable Monaco Editor"
[13]: https://sli.dev/custom/config-code-runners "Configure Code Runners | Slidev"
[14]: https://sli.dev/guide/component "Components in Slides | Slidev"
[15]: https://sli.dev/builtin/layouts "Layouts | Slidev"
[16]: https://sli.dev/features/global-layers?utm_source=chatgpt.com "Global Layers"
[17]: https://sli.dev/features/drawing?utm_source=chatgpt.com "Drawing & Annotations"
[18]: https://sli.dev/guide/exporting "Exporting | Slidev"
[19]: https://sli.dev/guide/faq?utm_source=chatgpt.com "FAQ"
[20]: https://sli.dev/guide/ui "User Interface | Slidev"
[21]: https://sli.dev/custom/config-fonts "Configure Fonts | Slidev"
[22]: https://sli.dev/features/code-groups?utm_source=chatgpt.com "Code Groups"
[23]: https://sli.dev/custom/config-mermaid "Configure Mermaid | Slidev"
[24]: https://sli.dev/builtin/components "Components | Slidev"
[25]: https://sli.dev/features/recording?utm_source=chatgpt.com "Recording"
