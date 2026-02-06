<template>
  <div class="countdown-timer">
    <div class="countdown-icon">⏰</div>
    <div class="countdown-title">距离下次更新</div>
    <div class="countdown-time">{{ timeRemaining }}</div>
    <div class="countdown-label">{{ nextUpdate }}</div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const timeRemaining = ref('')
const nextUpdate = ref('')
let timer = null

const getNextUpdate = () => {
  const now = new Date()
  const tomorrow = new Date(now)
  tomorrow.setDate(tomorrow.getDate() + 1)
  tomorrow.setHours(8, 0, 0, 0)

  const timeDiff = tomorrow - now
  const hours = Math.floor(timeDiff / (1000 * 60 * 60))
  const minutes = Math.floor((timeDiff % (1000 * 60 * 60)) / (1000 * 60))
  const seconds = Math.floor((timeDiff % (1000 * 60)) / 1000)

  const formattedTime = `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`
  timeRemaining.value = formattedTime

  const monthNames = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
  const month = monthNames[tomorrow.getMonth()]
  const day = tomorrow.getDate()
  const hour = String(tomorrow.getHours()).padStart(2, '0')
  const minute = String(tomorrow.getMinutes()).padStart(2, '0')

  nextUpdate.value = `更新时间: ${month}${day}日 ${hour}:${minute}`
}

const updateTimer = () => {
  getNextUpdate()
}

onMounted(() => {
  updateTimer()
  timer = setInterval(updateTimer, 1000)
})

onUnmounted(() => {
  if (timer) {
    clearInterval(timer)
  }
})
</script>

<style scoped>
.countdown-timer {
  background: linear-gradient(135deg, rgba(60, 135, 114, 0.1), rgba(45, 105, 88, 0.1));
  border: 1px solid var(--vp-c-brand-1);
  border-radius: 16px;
  padding: 2rem;
  text-align: center;
  max-width: 600px;
  margin: 3rem auto;
  transition: all 0.3s ease;
}

.countdown-timer:hover {
  box-shadow: 0 8px 24px rgba(60, 135, 114, 0.2);
  transform: translateY(-4px);
}

.countdown-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
  animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.1);
  }
}

.countdown-title {
  font-size: 1.125rem;
  font-weight: 600;
  color: var(--vp-c-text-2);
  margin-bottom: 0.5rem;
}

.countdown-time {
  font-size: 3rem;
  font-weight: 800;
  font-family: 'Courier New', monospace;
  background: linear-gradient(135deg, var(--vp-c-brand-1), var(--vp-c-brand-2));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin: 1rem 0;
  letter-spacing: 0.05em;
  line-height: 1.2;
  word-break: break-all;
}

.countdown-label {
  font-size: 0.9375rem;
  color: var(--vp-c-text-2);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

@media (max-width: 768px) {
  .countdown-timer {
    padding: 1.5rem;
    margin: 2rem 1rem;
  }

  .countdown-time {
    font-size: 2.5rem;
  }

  .countdown-label {
    font-size: 0.875rem;
  }
}
</style>
