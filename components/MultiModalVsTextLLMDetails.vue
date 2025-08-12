<template>
  <div class="mt-4">
    <ModalDetails
      title="多模态实现 vs 文本 LLM · 扩展阅读"
      :maxWidth="'980px'"
      :open="open"
      @update:open="val => (open = val)"
    >
      <template #trigger="{ open }">
        <button class="px-4 py-2 rounded bg-indigo-600 text-white" @click="open()">
          查看扩展阅读（弹窗）
        </button>
      </template>

      <div class="space-y-8 leading-7">
        <section>
          <h2 class="text-xl font-semibold mb-2">1️⃣ 核心差异对照表</h2>
          <div class="overflow-x-auto">
            <table class="w-full text-sm border-collapse">
              <thead>
                <tr class="bg-gray-50 dark:bg-white/5">
                  <th class="text-left p-2">维度</th>
                  <th class="text-left p-2">文本 LLM</th>
                  <th class="text-left p-2">多模态 LLM</th>
                </tr>
              </thead>
              <tbody>
                <tr class="border-t border-black/5 dark:border-white/10">
                  <td class="p-2">输入表示</td>
                  <td class="p-2">离散子词 Token</td>
                  <td class="p-2">连续特征（图像 patch、音频帧、视频时空 patch）</td>
                </tr>
                <tr class="border-t border-black/5 dark:border-white/10">
                  <td class="p-2">编码/对齐</td>
                  <td class="p-2">直接嵌入到语言空间</td>
                  <td class="p-2">专用编码器（ViT/CLIP/Whisper/Video）→ 投影/Connector/Q-Former 对齐到语言空间</td>
                </tr>
                <tr class="border-t border-black/5 dark:border-white/10">
                  <td class="p-2">注意力</td>
                  <td class="p-2">自注意力（1D 位置）</td>
                  <td class="p-2">自注意 + 跨模态注意/门控（含 2D/时间位置编码）</td>
                </tr>
                <tr class="border-t border-black/5 dark:border-white/10">
                  <td class="p-2">训练目标</td>
                  <td class="p-2">下一个 Token 预测 + 指令微调 + RLHF</td>
                  <td class="p-2">加 ITC/ITM/Caption/VQA、多模态指令微调、RLAIF</td>
                </tr>
                <tr class="border-t border-black/5 dark:border-white/10">
                  <td class="p-2">推理与输出</td>
                  <td class="p-2">直接输出文本</td>
                  <td class="p-2">多模态→对齐后进入 LLM，多数输出文本；需要图片/视频时由 LLM 规划提示→交扩散/Flow 模型渲染</td>
                </tr>
                <tr class="border-t border-black/5 dark:border-white/10">
                  <td class="p-2">上下文与成本</td>
                  <td class="p-2">受文本 Token 数限制</td>
                  <td class="p-2">还受特征 Token（分辨率、张数、帧数）影响；显存/延迟显著上升</td>
                </tr>
                <tr class="border-t border-black/5 dark:border-white/10">
                  <td class="p-2">易错与规避</td>
                  <td class="p-2">事实幻觉、长链推理不稳</td>
                  <td class="p-2">小字/计数/几何关系/跨页一致性易错；用“先描述再作答”、裁剪 ROI、提高分辨率、分步提问、检索/工具校验</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <hr class="border-black/5 dark:border-white/10" />

        <section>
          <h2 class="text-xl font-semibold mb-2">2️⃣ 处理流程对照</h2>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <h3 class="font-semibold">文本 LLM</h3>
              <ol class="list-decimal ml-5 mt-2 space-y-1 text-sm">
                <li>Token 化（子词）</li>
                <li>编码（自注意力建模上下文）</li>
                <li>解码（下一个 Token 概率 → 采样）</li>
                <li>输出文本</li>
              </ol>
            </div>
            <div>
              <h3 class="font-semibold">多模态 LLM（识别/理解）</h3>
              <ol class="list-decimal ml-5 mt-2 space-y-1 text-sm">
                <li>模态编码（图像/音频/视频 → 向量）</li>
                <li>对齐/投影（Connector/Q-Former → 伪 Token）</li>
                <li>LLM 融合（自注意 + 跨模态注意/门控）</li>
                <li>输出文本答案</li>
              </ol>
            </div>
          </div>
          <div class="mt-4">
            <h3 class="font-semibold">多模态“生成像素”的协作范式</h3>
            <ol class="list-decimal ml-5 mt-2 space-y-1 text-sm">
              <li>LLM 产出结构化提示（镜头/主体/光线/风格/约束）</li>
              <li>视觉生成模型（扩散/Flow）据此渲染像素</li>
              <li>可选：IP-Adapter/ControlNet/参考图/分镜进一步控制一致性</li>
            </ol>
          </div>
        </section>

        <hr class="border-black/5 dark:border-white/10" />

        <section>
          <h2 class="text-xl font-semibold mb-2">3️⃣ 训练目标与数据</h2>
          <ul class="list-disc pl-5 space-y-1 text-sm">
            <li>文本：因果语言建模 + 指令微调 + RLHF（对话偏好）</li>
            <li>多模态：加 ITC/ITM（对比/匹配）、Caption/VQA、指令微调、RLAIF（人/模型反馈）</li>
            <li>数据：图文/视听-文本配对数据、任务标注数据；质量与覆盖度决定上限</li>
          </ul>
        </section>

        <hr class="border-black/5 dark:border-white/10" />

        <section>
          <h2 class="text-xl font-semibold mb-2">4️⃣ 上下文与成本优化</h2>
          <ul class="list-disc pl-5 space-y-1 text-sm">
            <li>控制特征 Token：降分辨率/抽帧/裁剪 ROI/分页上传</li>
            <li>先文本化后多模态：把关键信息抽取为文本再推理</li>
            <li>缓存编码器特征：复用静态图/帧的向量，减少重复开销</li>
          </ul>
        </section>

        <hr class="border-black/5 dark:border-white/10" />

        <section>
          <h2 class="text-xl font-semibold mb-2">5️⃣ 易错点与规避策略</h2>
          <div class="overflow-x-auto">
            <table class="w-full text-sm border-collapse">
              <thead>
                <tr class="bg-gray-50 dark:bg-white/5">
                  <th class="text-left p-2">常见问题</th>
                  <th class="text-left p-2">原因</th>
                  <th class="text-left p-2">缓解策略</th>
                </tr>
              </thead>
              <tbody>
                <tr class="border-t border-black/5 dark:border-white/10">
                  <td class="p-2">小字/OCR 错误、计数不准</td>
                  <td class="p-2">分辨率不足、区域不聚焦</td>
                  <td class="p-2">提高分辨率/放大 ROI、先描述再作答、分步提问</td>
                </tr>
                <tr class="border-t border-black/5 dark:border-white/10">
                  <td class="p-2">跨页/跨帧一致性差</td>
                  <td class="p-2">上下文窗口被压缩、时序建模弱</td>
                  <td class="p-2">分页摘要 + 关键帧、限制上下文长度、显式对齐规则</td>
                </tr>
                <tr class="border-t border-black/5 dark:border-white/10">
                  <td class="p-2">事实类错误（幻觉）</td>
                  <td class="p-2">概率生成非数据库</td>
                  <td class="p-2">检索增强、工具校验、给定权威来源</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <hr class="border-black/5 dark:border-white/10" />

        <section>
          <h2 class="text-xl font-semibold mb-2">6️⃣ 工程落地自检清单</h2>
          <ul class="list-disc pl-5 space-y-1 text-sm">
            <li>是否能先文本化再多模态？</li>
            <li>是否控制了分辨率/帧率/张数并裁剪 ROI？</li>
            <li>是否缓存了静态特征、复用推理结果？</li>
            <li>是否输出中间可验证步骤（先描述再作答/结构化提示）？</li>
            <li>是否在需要生成像素时，采用“LLM 规划 + 视觉生成渲染”的协作？</li>
          </ul>
        </section>

        <hr class="border-black/5 dark:border-white/10" />

        <section>
          <h2 class="text-xl font-semibold mb-2">7️⃣ 课堂金句</h2>
          <blockquote class="border-l-4 border-indigo-500 pl-4">
            “文本 LLM 是离散 Token 的语言引擎；多模态 LLM 先把世界变成向量，再让语言大脑来‘讲清楚’它看见了什么、要做什么。”
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


