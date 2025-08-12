<template>
  <div class="mt-4">
    <ModalDetails title="Self-Attention 如何处理长距离依赖" :maxWidth="'920px'" :open="open" @update:open="val => open = val">
      <template #trigger="{ open }">
        <button class="px-4 py-2 rounded bg-teal-600 text-white" @click="open()">
          查看“长距离依赖”补充示例
        </button>
      </template>

      <div class="space-y-8 leading-7">
        <section>
          <h2 class="text-xl font-semibold mb-2">例子 1：主语-谓语一致（跨越干扰项）</h2>
          <div class="opacity-90">句子：</div>
          <ul class="list-disc pl-5">
            <li>The keys to the old cabinet upstairs in the museum are missing.</li>
          </ul>
          <div class="mt-3 opacity-90">观察点：</div>
          <ul class="list-disc pl-5 space-y-1">
            <li>正确谓语是 <code>are</code>（复数），因为真正的主语是 <code>keys</code>。</li>
            <li>中间插入了多个名词短语（cabinet, museum），容易“干扰”。</li>
          </ul>
          <div class="mt-3 opacity-90">Self-Attention 的作用：</div>
          <ul class="list-disc pl-5 space-y-1">
            <li>在预测 <code>are</code> 时，注意力头会“跳过”中间干扰，直接给 <code>keys</code> 高权重。</li>
          </ul>
          <pre class="mt-3 text-sm overflow-x-auto"><code>... keys ... cabinet ... museum ... are ...
                ↑      ↑            ↖︎  主要注意力 → keys</code></pre>
        </section>

        <hr class="border-black/5 dark:border-white/10" />

        <section>
          <h2 class="text-xl font-semibold mb-2">例子 2：地名-国家的长距离关系（跨句指代 + 事实）</h2>
          <div class="opacity-90">句子：</div>
          <ul class="list-disc pl-5">
            <li>Paris is known for its art scene. Many say it is the capital of France.</li>
          </ul>
          <div class="mt-3 opacity-90">观察点：</div>
          <ul class="list-disc pl-5 space-y-1">
            <li>第二句里的 <code>it</code> 指代的是 <code>Paris</code>。</li>
            <li>预测 <code>capital</code> 时，需要把 <code>France</code> 与 <code>Paris</code> 关联起来。</li>
          </ul>
          <div class="mt-3 opacity-90">Self-Attention 的作用：</div>
          <ul class="list-disc pl-5 space-y-1">
            <li>预测 <code>capital</code> 或 <code>France</code> 等词时，注意力会连接到前文的 <code>Paris</code>，实现“跨句整合”。</li>
          </ul>
          <pre class="mt-3 text-sm overflow-x-auto"><code>Paris ... art ... it ... capital ... France
  ↑                    ↖︎———————  主要注意力回看 Paris</code></pre>
        </section>

        <hr class="border-black/5 dark:border-white/10" />

        <section>
          <h2 class="text-xl font-semibold mb-2">为什么 Self-Attention 更擅长长距离</h2>
          <ul class="list-disc pl-5 space-y-1">
            <li>并行地看“整段”文本，不需要一步步传递记忆。</li>
            <li>多头注意力（multi-head）可同时捕捉不同类型的关联（语法/语义/指代）。</li>
          </ul>
          <div class="mt-3 opacity-90">对比：</div>
          <ul class="list-disc pl-5">
            <li>RNN/LSTM 更像“接力棒”，信息逐步传递，长距离容易“遗忘/衰减”。</li>
          </ul>
        </section>

        <section>
          <h2 class="text-xl font-semibold mb-2">使用者的两条实用建议</h2>
          <ol class="list-decimal pl-5 space-y-1">
            <li>把关键信息写清晰、就近：例如“Paris（法国首都）以艺术闻名……”。</li>
            <li>在同一条输入里提供必要背景：减少模型跨多轮寻找线索的成本。</li>
          </ol>
          <blockquote class="mt-3 border-l-4 border-teal-500 pl-4">
            记住：Self-Attention 能“跨越很远”，但你把线索摆得越清楚，它就越稳。
          </blockquote>
        </section>

        
      </div>
    </ModalDetails>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import ModalDetails from './ModalDetails.vue'
const open = ref(false)
</script>

<style scoped></style>


