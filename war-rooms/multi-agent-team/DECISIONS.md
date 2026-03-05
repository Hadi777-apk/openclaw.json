# 决策日志

## [D001] SYSTEM_ARCHITECTURE - 采用 War Room 多智能体架构 - 2026-03-05
决定采用 War Room 方法论构建多智能体系统，支持模块化、可扩展的 Agent 协作。

## [D002] ROLE_DEFINITION - 定义四大核心角色 - 2026-03-05
定义四大核心角色：COMMANDER (Gemini 3.0), IMAGE (Nano Banana Pro), CODER (Claude Code), COORDINATOR (Qwen)。

## [D003] COMMUNICATION_PROTOCOL - 采用文件系统通信 - 2026-03-05
决定使用共享文件系统作为 Agent 间通信机制，以零 Token 成本实现高效协作。

## [D004] CONFIGURATION_STORAGE - API Keys 环境变量方案 - 2026-03-05
决定使用环境变量存储 API Keys，确保安全性同时便于配置管理。

## [D005] ERROR_HANDLING - 降级方案设计 - 2026-03-05
设计降级方案，确保单个 Agent 故障不影响整个系统运行。

## [D006] FUTURE_EXTENSION - 预留扩展能力 - 2026-03-05
架构设计预留未来扩展能力，支持新增更多专业 Agent。