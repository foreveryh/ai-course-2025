# W2 作业模板 · 结构化输出示例（JSON）

使用说明：根据任务自定义字段，但需满足“可被程序消费、允许未知、便于比对”的原则。

```jsonc
{
  "title": "",
  "audience": "",
  "goal": "",
  "outline": [
    { "h2": "", "bullets": ["", ""] }
  ],
  "constraints": {
    "language": "zh-CN",
    "max_chars": 800,
    "style": ["professional", "concise"],
    "forbidden": ["fabrication", "exaggeration"]
  },
  "metrics": {
    "kpis": [""],
    "unknown_allowed": true
  },
  "risks": [
    { "risk": "", "mitigation": "" }
  ],
  "notes": "允许 unknown / null，不得编造"
}
```

