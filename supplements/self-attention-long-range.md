# Self-Attention 如何处理“长距离依赖”

> 目标：让你直观看到模型如何“跨过很多词，准确找到相关信息”。

---

## 例子 1：主语-谓语一致（跨越干扰项）

句子：

- The keys to the old cabinet upstairs in the museum are missing.

观察点：

- 正确谓语是 are（复数），因为真正的主语是 keys；
- 中间插入了多个名词短语（cabinet, museum），容易“干扰”。

Self-Attention 的作用：

- 在预测 are 时，注意力头会“跳过”中间干扰，直接给 keys 高权重。

简化示意（高权重用箭头标注）：

```
... keys ... cabinet ... museum ... are ...
                ↑      ↑            ↖︎  主要注意力 → keys
```

---

## 例子 2：地名-国家的长距离关系（跨句指代 + 事实）

句子：

- Paris is known for its art scene. Many say it is the capital of France.

观察点：

- 第二句里的 it 指代的是 Paris；
- 预测 capital 时，需要把 France 与 Paris 关联起来。

Self-Attention 的作用：

- 预测 capital 或 France 等词时，注意力会连接到前文的 Paris，实现“跨句整合”。

简化示意：

```
Paris ... art ... it ... capital ... France
  ↑                    ↖︎———————  主要注意力回看 Paris
```

---

## 为什么 Self-Attention 更擅长长距离

- 并行地看“整段”文本，不需要一步步传递记忆；
- 多头注意力（multi-head）可同时捕捉不同类型的关联（语法/语义/指代）。

对比：

- RNN/LSTM 更像“接力棒”，信息逐步传递，长距离容易“遗忘/衰减”。

---

## 使用者的两条实用建议

1) 把关键信息写清晰、就近：例如“Paris（法国首都）以艺术闻名……”。

2) 在同一条输入里提供必要背景：减少模型跨多轮寻找线索的成本。

> 记住：Self-Attention 能“跨越很远”，但你把线索摆得越清楚，它就越稳。

