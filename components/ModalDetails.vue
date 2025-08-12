<template>
  <div class="inline-block">
    <slot name="trigger" :open="openModal">
      <button class="px-4 py-2 rounded bg-teal-600 text-white" @click="openModal">
        {{ buttonText }}
      </button>
    </slot>

    <Teleport :to="teleportTo">
      <Transition name="fade">
        <div
          v-if="isOpen"
          class="fixed inset-0 z-50 bg-black/50 grid place-items-center p-4"
          role="dialog"
          aria-modal="true"
          :aria-labelledby="titleId"
          @click.self="onOverlayClick"
        >
          <div
            class="w-full max-w-[95vw] max-h-[85vh] overflow-y-auto rounded-xl bg-white dark:bg-[#1f1f1f] text-left shadow-2xl ring-1 ring-black/5"
            :style="{ maxWidth, maxHeight }"
          >
            <div class="sticky top-0 z-10 flex items-center justify-between px-6 py-4 border-b border-black/5 dark:border-white/10 bg-white/80 dark:bg-[#1f1f1f]/80 backdrop-blur">
              <div class="min-w-0">
                <slot name="header">
                  <h2 :id="titleId" class="text-lg font-semibold truncate">{{ title }}</h2>
                </slot>
              </div>
              <button
                v-if="showClose"
                class="px-3 py-1.5 rounded bg-gray-200 dark:bg-gray-700"
                @click="closeModal"
              >
                {{ closeText }}
              </button>
            </div>

            <div class="px-6 py-5 space-y-6 leading-7">
              <div class="prose prose-zinc dark:prose-invert max-w-none">
                <slot />
              </div>
            </div>

            <div class="px-6 pb-6 pt-2 text-right">
              <slot name="footer">
                <button class="px-4 py-2 rounded bg-teal-600 text-white" @click="closeModal">{{ confirmText }}</button>
              </slot>
            </div>
          </div>
        </div>
      </Transition>
    </Teleport>
  </div>
</template>

<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref, watch } from 'vue'

interface Props {
  title?: string
  buttonText?: string
  closeText?: string
  confirmText?: string
  maxWidth?: string
  maxHeight?: string
  teleportTo?: string
  showClose?: boolean
  closeOnEsc?: boolean
  closeOnOverlay?: boolean
  /** for v-model:open */
  open?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  title: '详细说明',
  buttonText: '查看详情',
  closeText: '关闭',
  confirmText: '我学会了，收起',
  maxWidth: '920px',
  maxHeight: '85vh',
  teleportTo: 'body',
  showClose: true,
  closeOnEsc: true,
  closeOnOverlay: true,
})

const emit = defineEmits<{
  (e: 'update:open', val: boolean): void
  (e: 'opened'): void
  (e: 'closed'): void
}>()

const localOpen = ref<boolean>(false)
const isControlled = computed(() => props.open !== undefined)
const isOpen = computed<boolean>({
  get() {
    return isControlled.value ? !!props.open : localOpen.value
  },
  set(val: boolean) {
    if (isControlled.value) emit('update:open', val)
    else localOpen.value = val
  },
})

watch(
  () => isOpen.value,
  (val) => {
    if (val) emit('opened')
    else emit('closed')
  }
)

function onKeydown(e: KeyboardEvent) {
  if (!props.closeOnEsc) return
  if (e.key === 'Escape') isOpen.value = false
}

function onOverlayClick() {
  if (props.closeOnOverlay) isOpen.value = false
}

function openModal() {
  isOpen.value = true
}

function closeModal() {
  isOpen.value = false
}

onMounted(() => window.addEventListener('keydown', onKeydown))
onBeforeUnmount(() => window.removeEventListener('keydown', onKeydown))

const titleId = `modal-title-${Math.random().toString(36).slice(2, 8)}`

const { buttonText, closeText, confirmText, maxWidth, maxHeight, teleportTo, showClose, title } = props
</script>

<style scoped>
.fade-enter-active, .fade-leave-active { transition: opacity .18s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }
</style>


