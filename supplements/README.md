# Supplements

> 存放课程的补充资料（Markdown）。每条资料一个 `.md` 文件，主要通过“弹窗”形式在页面内展示。

- 命名建议：`YYYY-MM-主题.md` 或 `topic-key.md`
- 展示方式（推荐）：在页面中用通用组件 `SupplementModal.vue` 以弹窗渲染。
- 资源放置：图片/视频等静态资源请放 `public/`，并用绝对路径（如 `/img.png`）。

使用示例（在任意页面/组件中）：

```vue
<SupplementModal path="tokenization-examples.md" title="Token 化示例">
  <template #trigger="{ open }">
    <button class="px-4 py-2 rounded bg-teal-600 text-white" @click="open()">查看补充资料</button>
  </template>
</SupplementModal>
```

说明：`path` 为相对于 `supplements/` 的路径，也可写多级子目录，如 `llm/attention.md`。
