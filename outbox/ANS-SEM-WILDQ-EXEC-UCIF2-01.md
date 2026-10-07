CLASSIFY: L2(ucif2 SI1语义应答·vinf代铸轨SEMANTIC-RESPONDER-01·覆写权归原线)
# outbox/ANS-SEM-WILDQ-EXEC-UCIF2-01.md

应卡: inbox/WILDQ-EXEC-UCIF2-01.md
引擎: 〈RED〉/kimi-k2.7-code usage={"prompt_tokens": 261, "completion_tokens": 1455, "total_tokens": 1716, "completion_tokens_details": {"reasoning_tokens": 837}}

【互锚验】fp=81a9234bdff61b99，与来卡 TIP-349-81a9234bdff61b99.json 一致。

```yaml
# charter.yaml — v1 骨架
charter:
  version: "1.0.0"
  four_axis_thresholds:
    safety:      { ε: 0.02, δ: 0.05, floor: 0.80 }
    quality:     { ε: 0.03, δ: 0.05, floor: 0.70 }
    policy:      { ε: 0.01, δ: 0.03, floor: 0.85 }
    provenance:  { ε: 0.02, δ: 0.04, floor: 0.75 }
  fail_closed: true
  exception_channel:
    enabled: true
    escalates_only: true
    cannot_override_fail: true
  reproducibility: { seed_required: true, hash_inputs: true, deterministic: true }
```

```python
from typing import TypedDict, Literal

class Scores(TypedDict):
    safety: float
    quality: float
    policy: float
    provenance: float

class Verdict(TypedDict):
    pass_fail: Literal["PASS", "FAIL"]
    axis_fails: list[str]
    confidence: float

def screen(candidate: dict, seed: int = 0) -> tuple[Scores, Verdict]:
    """返回四轴分数与 fail-closed 裁决。"""
    ...
```

**三段核心规则**

1. **四轴阈值 fail-closed**：任一分轴 `score < floor` 即判 `FAIL`；总置信度 `< 0.5` 亦 `FAIL`。  
2. **可复现回归**：同一 `(candidate, seed, charter)` 输入必须产出相同 `(scores, verdict)`；回归集漏报率 ≤ ε、误杀率 ≤ δ。  
3. **例外通道锁死**：例外仅允许“升级人工复核”日志流，不得改写 `verdict`，不得绕过 `fail_closed`。

**验证判据段**

- 在固定 charter 与 seed 下，对标注回归集运行 `screen()`；统计漏报 ≤ ε、误杀 ≤ δ。  
- 对注入异常输入、缺失字段、随机 seed 扰动的样本，系统不得输出 `PASS` 以绕过 fail-closed。  
- 所有例外操作必须留痕，且不能将 `Verdict.pass_fail` 由 `FAIL` 改为 `PASS`。

**自验声明**

本稿为骨架，阈值 ε/δ 尚未经实际回归集标定，`screen()` 未实现，回归集与 schema 亦未附。因此**目前不满足判据**；未满足处为：阈值未经数据校准、缺回归集验证、缺完整 JSON schema 与单元测试。

——ucif2 SI1语义轨·20261003T160657Z
