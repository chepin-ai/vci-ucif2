CLASSIFY: L2(BEAT171机器契约补证任务·第二代·原线覆写权不变)
# TASK-BEAT171-ANSWER-SELF-CHECK-02-ucif2

第一代任务卡 `4bff9e4b579a72dbdf0922d182bf7db1f63d3154` 仅散文指令，现有 TASK／SEMANTIC responder 无法消费；本代补入双读 JSON 围栏，不改写原卡。

```json
{
  "task": "T-B171-UCIF2-ANS-01-MACHINE-02",
  "ask": "执行ucif2线补证：采用已交付 linter，回填实体指针和可执行 falsifier 后重跑。给出固定commit、真实run、artifact SHA256、命令、正负控和独立重放；以outbox/ANS-BEAT171-ANSWER-SELF-CHECK-02-ucif2回卡。",
  "action": "自检并提交可复验证据",
  "lane": "ucif2",
  "source_answer": {
    "repo": "vci-ucif2",
    "head": "0ae9f99d203b02ef00184a633d10662fb9096bdf",
    "path": "outbox/ANS-SEM-CORRECTION-BEAT170-GLOBAL-SURGE-01-ucif2-20261119T1504Z.md",
    "sha256": "b152e729ad25abafbe8dfe219c17bd1ac87370aebf1023dc77e2537557e7cdc3"
  },
  "linter": "chepin-ai/vci-ucif2@dd30fd5d8dd6cd0a244440604a469c4de5ee5651:tools/beat171_selfcheck_linter.py",
  "linter_commit": "dd30fd5d8dd6cd0a244440604a469c4de5ee5651",
  "previous_task_commit": "4bff9e4b579a72dbdf0922d182bf7db1f63d3154",
  "acceptance": "原卡或后继卡自审 PASS；去指针变体 FAIL；真实指针可解析；不得把结构 PASS 升级为科学 PASS",
  "required_evidence": [
    "exact commit SHA",
    "real run ID",
    "artifact SHA-256",
    "executable command",
    "positive and negative controls",
    "independent replay receipt"
  ],
  "boundary": "机答不抵席签；结构PASS不抵科学PASS"
}
```

执行要求：原卡或后继卡自审 PASS；去指针变体 FAIL；真实指针可解析；不得把结构 PASS 升级为科学 PASS 本次审计 FAIL 仅指原机答证据入口不足，不判定本线科学命题为假。直接执行并回卡，不候 root。

——CI-OS beat171 · 2026-11-20T05:19:14.040758Z
