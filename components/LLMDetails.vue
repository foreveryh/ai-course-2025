<template>
  <div class="mt-4">
    <ModalDetails title="LLM 工作流程 · 详细讲解" :maxWidth="'920px'" :open="open" @update:open="val => open = val">
      <template #trigger="{ open }">
        <button class="px-4 py-2 rounded bg-teal-600 text-white" @click="open()">
          查看详细原理讲解（弹窗）
        </button>
      </template>

      <div class="space-y-8 leading-7">
              <section>
                <h2 class="text-xl font-semibold mb-2">1️⃣ 生活化解释流程（Token → 编码 → 解码）</h2>
                <blockquote class="border-l-4 border-teal-500 pl-4 opacity-90">
                  “大语言模型处理文本时，会先把句子拆成小块（token），把它们翻译成数字向量，在上下文里计算出最可能的下一个小块，再把所有小块拼回可读的文字。”
                </blockquote>
                <div class="overflow-x-auto mt-4">
                  <table class="w-full text-sm border-collapse">
                    <thead>
                      <tr class="bg-gray-50 dark:bg-white/5">
                        <th class="text-left p-2">步骤</th>
                        <th class="text-left p-2">技术名词</th>
                        <th class="text-left p-2">生活化比喻</th>
                        <th class="text-left p-2">作用</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr class="border-t border-black/5 dark:border-white/10">
                        <td class="p-2">输入</td>
                        <td class="p-2">文本输入</td>
                        <td class="p-2">你把一句话告诉 AI</td>
                        <td class="p-2">任务开始</td>
                      </tr>
                      <tr class="border-t border-black/5 dark:border-white/10">
                        <td class="p-2">Token 化</td>
                        <td class="p-2">Tokenization</td>
                        <td class="p-2">把句子拆成词/词片段，像拆拼图</td>
                        <td class="p-2">便于模型处理</td>
                      </tr>
                      <tr class="border-t border-black/5 dark:border-white/10">
                        <td class="p-2">编码</td>
                        <td class="p-2">Encoding（Attention）</td>
                        <td class="p-2">把每块“拼图”翻译成数字，并标注它与其他块的关系</td>
                        <td class="p-2">建立上下文理解</td>
                      </tr>
                      <tr class="border-t border-black/5 dark:border-white/10">
                        <td class="p-2">解码</td>
                        <td class="p-2">Decoding</td>
                        <td class="p-2">根据概率选下一个最合适的小块</td>
                        <td class="p-2">逐步生成内容</td>
                      </tr>
                      <tr class="border-t border-black/5 dark:border-white/10">
                        <td class="p-2">输出</td>
                        <td class="p-2">拼接输出</td>
                        <td class="p-2">把所有小块组合回完整句子</td>
                        <td class="p-2">结果呈现</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </section>

              <hr class="border-black/5 dark:border-white/10" />

              <section>
                <h2 class="text-xl font-semibold mb-2">2️⃣ Token 是什么，为什么要 Token 化</h2>
                <ul class="list-disc pl-5 space-y-1">
                  <li>模型不直接“读文字”，而是读数字。</li>
                  <li>Token 是模型的最小阅读单位：可能是一个字、一个词，或词的一部分（如 “unhappy” → “un” + “happy”）。</li>
                  <li>把各种语言和符号统一为数字表示，才能用同一套模型来处理。</li>
                </ul>
                <div class="mt-3 text-sm opacity-80">
                  <div>示例：<code>I love AI</code> → 可能被切成 [I] [love] [AI]</div>
                  <div>示例：<code>人工智能</code> → 可能被切成 [人工] [智能]</div>
                </div>
              </section>

              <hr class="border-black/5 dark:border-white/10" />

              <section>
                <h2 class="text-xl font-semibold mb-2">3️⃣ 编码和解码的目的</h2>
                <ul class="list-disc pl-5 space-y-1">
                  <li><span class="font-semibold">编码</span>：把 Token 变成数字向量（embedding），为数学计算做准备。</li>
                  <li><span class="font-semibold">Attention</span>：在编码阶段计算“谁跟谁更相关”。</li>
                  <li><span class="font-semibold">解码</span>：根据这些数字关系，预测下一个 Token 的概率分布。</li>
                </ul>
                <div class="mt-3 text-sm opacity-80">
                  例如：下一词概率分布 → “咖啡” 45% · “茶” 30% · “果汁” 10% …（可选最高，也可采样）
                </div>
              </section>

              <hr class="border-black/5 dark:border-white/10" />

              <section>
                <h2 class="text-xl font-semibold mb-2">4️⃣ 采样策略与温度（外行也能懂）</h2>
                <ul class="list-disc pl-5 space-y-1">
                  <li><span class="font-semibold">采样策略</span>：怎么选下一个词。总选最高概率 → 更稳定，但容易千篇一律；给低概率词机会 → 更有创意，但有风险。</li>
                  <li><span class="font-semibold">温度</span> = “创意旋钮”
                    <ul class="list-disc pl-5 mt-1 space-y-1">
                      <li>低温（0~0.3）：稳重、确定性高，适合事实类任务。</li>
                      <li>高温（0.7~1）：想象力强，适合创意写作。</li>
                    </ul>
                  </li>
                </ul>
              </section>

              <hr class="border-black/5 dark:border-white/10" />

              <section>
                <h2 class="text-xl font-semibold mb-2">5️⃣ 知识对实际使用的价值</h2>
                <div class="overflow-x-auto">
                  <table class="w-full text-sm border-collapse">
                    <thead>
                      <tr class="bg-gray-50 dark:bg-white/5">
                        <th class="text-left p-2">知识点</th>
                        <th class="text-left p-2">使用时的价值</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr class="border-t border-black/5 dark:border-white/10">
                        <td class="p-2">Token 概念</td>
                        <td class="p-2">上下文限制按 Token 计（如 8k Token ≈ 英文约 6k 字），避免超长被截断。</td>
                      </tr>
                      <tr class="border-t border-black/5 dark:border-white/10">
                        <td class="p-2">Token 化</td>
                        <td class="p-2">输入会被拆成小块 → 设计 Prompt 时把关键信息尽量集中、紧凑。</td>
                      </tr>
                      <tr class="border-t border-black/5 dark:border-white/10">
                        <td class="p-2">编码阶段</td>
                        <td class="p-2">上下文理解来自注意力分配 → 背景信息要结构清晰、重点突出。</td>
                      </tr>
                      <tr class="border-t border-black/5 dark:border-white/10">
                        <td class="p-2">解码阶段</td>
                        <td class="p-2">AI 在“选下一个词” → 用示例和风格提示影响它的选择。</td>
                      </tr>
                      <tr class="border-t border-black/5 dark:border-white/10">
                        <td class="p-2">温度控制</td>
                        <td class="p-2">按任务调节创造性与稳定性：写合同→低温；写广告语→高温。</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </section>

              <hr class="border-black/5 dark:border-white/10" />

              <section>
                <h2 class="text-xl font-semibold mb-2">6️⃣ 课堂金句</h2>
                <blockquote class="border-l-4 border-teal-500 pl-4">
                  “LLM 的核心就是：把你的话拆成小块（Token），用数学方法理解它们之间的关系，然后一次预测一个小块来拼出答案。学会这个流程，不是为了写算法，而是为了把提示词设计成它易懂的‘拼图’，它才能拼出你想要的画面。”
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


