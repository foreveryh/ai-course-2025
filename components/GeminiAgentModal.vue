<template>
  <div class="mt-4">
    <ModalDetails title="Gemini Agent 实战演示" :maxWidth="'1000px'" :open="open" @update:open="val => open = val">
      <template #trigger="{ open }">
        <button class="px-6 py-3 rounded-lg bg-blue-600 text-white hover:bg-blue-700 transition-colors text-lg font-semibold" @click="open()">
          🚀 查看 Gemini ReAct 演示
        </button>
      </template>

      <div class="space-y-6 leading-7">
        <section>
          <h2 class="text-xl font-semibold mb-4">📋 任务：智能研究助手</h2>
          <div class="bg-blue-50 rounded-lg p-4 border-l-4 border-blue-400">
            <p class="font-semibold">用户请求：</p>
            <p class="mt-2 italic">"帮我研究一下2024年AI领域的重大突破，并分析对未来的影响"</p>
          </div>
        </section>

        <hr class="border-gray-200" />

        <section>
          <h2 class="text-xl font-semibold mb-4">🔄 ReAct 执行过程</h2>
          
          <div class="space-y-4">
            <!-- Round 1 -->
            <div class="border rounded-lg p-4 bg-yellow-50">
              <div class="flex items-start gap-3">
                <span class="bg-yellow-500 text-white px-2 py-1 rounded text-sm font-semibold">Thought 1</span>
                <div class="flex-1">
                  <p>用户要求研究2024年AI重大突破，我需要搜索最新的AI发展信息，然后分析影响。让我先搜索相关信息。</p>
                </div>
              </div>
            </div>

            <div class="border rounded-lg p-4 bg-green-50">
              <div class="flex items-start gap-3">
                <span class="bg-green-500 text-white px-2 py-1 rounded text-sm font-semibold">Action 1</span>
                <div class="flex-1">
                  <p><code>search_web("2024年AI人工智能重大突破 最新发展")</code></p>
                </div>
              </div>
            </div>

            <div class="border rounded-lg p-4 bg-blue-50">
              <div class="flex items-start gap-3">
                <span class="bg-blue-500 text-white px-2 py-1 rounded text-sm font-semibold">Observation 1</span>
                <div class="flex-1">
                  <p>搜索到以下关键信息：</p>
                  <ul class="mt-2 list-disc pl-5 space-y-1">
                    <li>GPT-4o 和 Claude 3.5 Sonnet 发布</li>
                    <li>Sora 文生视频模型突破</li>
                    <li>Google Gemini 2.0 多模态能力</li>
                    <li>AI Agent 和工作流自动化普及</li>
                    <li>开源模型 Llama 3.1 达到商业级水平</li>
                  </ul>
                </div>
              </div>
            </div>

            <!-- Round 2 -->
            <div class="border rounded-lg p-4 bg-yellow-50">
              <div class="flex items-start gap-3">
                <span class="bg-yellow-500 text-white px-2 py-1 rounded text-sm font-semibold">Thought 2</span>
                <div class="flex-1">
                  <p>获得了基础信息，但需要更深入了解每个突破的技术细节和商业影响。让我搜索更具体的分析报告。</p>
                </div>
              </div>
            </div>

            <div class="border rounded-lg p-4 bg-green-50">
              <div class="flex items-start gap-3">
                <span class="bg-green-500 text-white px-2 py-1 rounded text-sm font-semibold">Action 2</span>
                <div class="flex-1">
                  <p><code>search_web("2024 AI breakthrough impact analysis report GPT-4o Sora Claude")</code></p>
                </div>
              </div>
            </div>

            <div class="border rounded-lg p-4 bg-blue-50">
              <div class="flex items-start gap-3">
                <span class="bg-blue-500 text-white px-2 py-1 rounded text-sm font-semibold">Observation 2</span>
                <div class="flex-1">
                  <p>找到了详细的影响分析：</p>
                  <ul class="mt-2 list-disc pl-5 space-y-1">
                    <li>多模态AI大幅降低内容创作门槛</li>
                    <li>AI编程助手提高开发效率50%+</li>
                    <li>企业AI采用率从15%增长到45%</li>
                    <li>AI安全和监管政策加速制定</li>
                  </ul>
                </div>
              </div>
            </div>

            <!-- Round 3 -->
            <div class="border rounded-lg p-4 bg-yellow-50">
              <div class="flex items-start gap-3">
                <span class="bg-yellow-500 text-white px-2 py-1 rounded text-sm font-semibold">Thought 3</span>
                <div class="flex-1">
                  <p>现在我有了足够的信息来分析未来影响。让我整理一个结构化的分析报告，包括技术突破、商业影响和未来趋势。</p>
                </div>
              </div>
            </div>

            <div class="border rounded-lg p-4 bg-green-50">
              <div class="flex items-start gap-3">
                <span class="bg-green-500 text-white px-2 py-1 rounded text-sm font-semibold">Final Action</span>
                <div class="flex-1">
                  <p><code>generate_structured_report(技术突破, 商业影响, 未来趋势)</code></p>
                </div>
              </div>
            </div>
          </div>
        </section>

        <hr class="border-gray-200" />

        <section>
          <h2 class="text-xl font-semibold mb-4">📊 最终输出示例</h2>
          <div class="bg-gray-50 rounded-lg p-4 text-sm">
            <h3 class="font-semibold mb-2">2024年AI领域重大突破分析报告</h3>
            
            <div class="space-y-3">
              <div>
                <h4 class="font-semibold text-blue-600">🚀 技术突破</h4>
                <ul class="list-disc pl-5 mt-1 space-y-1">
                  <li><strong>多模态统一</strong>：GPT-4o实现文本、图像、音频的无缝集成</li>
                  <li><strong>视频生成</strong>：Sora达到接近专业制作的视频质量</li>
                  <li><strong>推理能力</strong>：o1系列模型在复杂推理任务上突破人类水平</li>
                </ul>
              </div>
              
              <div>
                <h4 class="font-semibold text-green-600">💼 商业影响</h4>
                <ul class="list-disc pl-5 mt-1 space-y-1">
                  <li><strong>内容产业</strong>：AI生成内容占比达到30%，创作成本下降70%</li>
                  <li><strong>软件开发</strong>：AI编程助手普及，开发效率提升显著</li>
                  <li><strong>客户服务</strong>：智能客服解决率达到90%，人工成本大幅降低</li>
                </ul>
              </div>
              
              <div>
                <h4 class="font-semibold text-purple-600">🔮 未来趋势</h4>
                <ul class="list-disc pl-5 mt-1 space-y-1">
                  <li><strong>个人AI助手</strong>：每个人都将拥有专属的AI工作伙伴</li>
                  <li><strong>AI+机器人</strong>：物理世界的AI应用将快速普及</li>
                  <li><strong>监管框架</strong>：AI治理和伦理标准将更加完善</li>
                </ul>
              </div>
            </div>
          </div>
        </section>

        <section class="mt-6">
          <div class="bg-green-50 rounded-lg p-4 border-l-4 border-green-400">
            <h3 class="font-semibold text-green-800 mb-2">🎯 ReAct 模式的优势体现</h3>
            <ul class="text-green-700 space-y-1">
              <li>✅ <strong>信息获取</strong>：通过搜索获得最新、准确的信息</li>
              <li>✅ <strong>动态调整</strong>：根据搜索结果调整后续的查询策略</li>
              <li>✅ <strong>结构化输出</strong>：将信息整理成用户易理解的格式</li>
              <li>✅ <strong>质量保证</strong>：多轮验证确保信息的全面性和准确性</li>
            </ul>
          </div>
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