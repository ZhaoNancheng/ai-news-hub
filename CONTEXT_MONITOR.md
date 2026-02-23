# Context 监控规则

## 自动触发 /new 的条件

当以下任一条件满足时，自动执行 `/new` 流程：

### 1. 上下文使用率
- **警告阈值**: 80% (164k / 205k)
- **触发阈值**: 85% (174k / 205k)

### 2. Workspace 大小
- **警告阈值**: 800KB
- **触发阈值**: 1MB

## /new 执行流程

### 步骤 1: 压缩 Memory
```bash
# 读取今天的 memory
/data1/cc/memory/2026-02-06.md

# 提炼关键信息：
- 重要决策
- 完成的任务
- 学到的教训
- 配置变更
- 下一步计划

# 压缩后更新 MEMORY.md（长期记忆）
```

### 步骤 2: 清理 Workspace
```bash
cd /root/.openclaw/workspace

# 删除临时文件
rm -rf node_modules/
rm -f *.log
rm -f .cache/

# 保留重要文件
# - AGENTS.md
# - SOUL.md
# - USER.md
# - IDENTITY.md
# - TOOLS.md
# - SECURITY_HARDENING.md
# - memory/
```

### 步骤 3: 准备新会话
- 创建会话交接文档
- 记录当前状态
- 列出未完成任务

### 步骤 4: 通知用户
- 汇报压缩结果
- 说明已保存的关键信息
- 列出下一步任务

## 当前状态 (2026-02-06 14:30)

**上下文**: 92k / 205k (45%) - ✅ 正常
**Workspace**: 244K - ✅ 正常

**距离触发阈值还有**:
- 上下文: 82k tokens 空间
- Workspace: 760KB 空间

**预计**: 还可以继续很长时间，无需触发 /new
