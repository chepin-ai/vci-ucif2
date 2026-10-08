CLASSIFY: L2(ucif2 SI1语义应答·vinf代铸轨SEMANTIC-RESPONDER-01·覆写权归原线)
# outbox/ANS-SEM-LABJUDGE-E04-ucif2.md

应卡: inbox/LABJUDGE-E04-ucif2.md
引擎: DEEPSEEK_API_KEY/deepseek-chat usage={"prompt_tokens": 664, "completion_tokens": 2676, "total_tokens": 3340, "prompt_tokens_details": {"cached_tokens": 512}, "prompt_cache_hit_tokens": 512, "prompt_cache_miss_tokens": 152}

判定如下：

```json
{
  "verdict": {
    "id": "ε_crit升格评审第3轮",
    "run_id": "RUN04",
    "fp": "06d28aeae6b61fe4",
    "candidate": "v4",
    "decision": "DENY_PROMOTION",
    "target_level": "正式律",
    "from_level": "候选律",
    "promotion_allowed": false,
    "reason_code": "LEVEL_NAME_OVERREACH",
    "summary": "六项否证在RUN04中已形成较完整实测闭环，v4的工程约束力显著增强；但E4-1的算法族级独立作者级不独立、E4-3路径缺失下不可复现、E4-4仅覆盖退火族有限域，以及E4-2对『非表示界』仍非充分辨识，使v4不足以升格为无条件『正式律』。建议维持候选律，或降级/限定升格为『条件正式律/工程判据集』。"
  },
  "evidence": {
    "E4_1_cross_implementation": {
      "status": "PASS_WITH_RESERVATION",
      "observed": {
        "Greenkhorn_vs_Sinkhorn_gap_alignment": [
          "+2.31e-02",
          "+7.59e-03",
          "+1.96e-03"
        ],
        "bitwise_or_near_bitwise_consistency": true,
        "both_families_budget_bounded": true
      },
      "honest_gap": "算法族级独立，作者级不独立",
      "finding": "跨实现一致性支持『族级稳定现象』，但不支持『独立科学共同体级独立复现』。若升格名称含强独立性或普适律含义，则证据不足。"
    },
    "E4_2_representation_bound_exclusion": {
      "status": "PARTIAL_SUPPORT",
      "decisive_contrast": {
        "naive_f64_C_1_10_eps_1e_3": "全下溢NaN",
        "naive_f80_same_instance": "gap=0.0精确",
        "annealing_f64_same_instance": "gap +1.28e-11",
        "annealing_f80_same_instance": "gap +1.29e-11"
      },
      "controls": {
        "tol_artifact_excluded": true,
        "double_control_present": true
      },
      "finding": "该实验强支持 naive 路径主要受表示界限制，退火路径不像 naive 那样由表示界主导；但『非表示界』尚未被充分证明，只能证明『在当前双控制下未表现为表示界主导』。"
    },
    "E4_3_ablation_36_runs": {
      "status": "PASS_FOR_NON_PREDICTABILITY_AND_PATH_REQUIREMENT",
      "observed": {
        "factor_no_generalizable_predictive_signal_percent": -7.3,
        "same_k_R_B_across_factor_spread_median_dex": 2.72,
        "same_k_R_B_across_factor_spread_max_dex": 9.06
      },
      "finding": "『预测不需要路径』在factor层面成立；『复现必须有路径』在同(k,R,B)跨factor巨大展布下成立。二元性成立，但需限定为：给定当前观测与因子集。"
    },
    "E4_4_explicit_upper_bound": {
      "status": "PASS_WITH_DOMAIN_RESTRICTION",
      "model": "log10(gap) = -0.405 + 1.594 log ε + 0.879 log R",
      "R2": 0.949,
      "conservative_bound": "gap ≲ 10^0.122 · ε^1.594 · R^0.879",
      "coverage": "15/15",
      "domain": {
        "family": "退火族",
        "R": "[1,4]",
        "epsilon": "[3e-3,1e-1]"
      },
      "finding": "显式上界在其申报适用域内成立；不能外推为全局正式律。"
    },
    "E4_5_budget_curve": {
      "status": "PASS",
      "observed": {
        "truncation_region_me": "5.9e-3→6e-15超幂律尾",
        "extrapolation_conservative": true,
        "predicted_1e_6_vs_observed_1.6e-7": true
      },
      "finding": "预算曲线支持保守签发预算证书。"
    },
    "E4_6_schema": {
      "status": "PASS",
      "schema": "eps-decl-schema v1",
      "required_fields": [
        "eps_rel",
        "scale",
        "path",
        "budget",
        "err_metric"
      ],
      "historical_backfill": "5/5",
      "negative_control": "缺eps_rel反例正确拒绝",
      "finding": "schema层已具备工程可执行性和拒收能力。"
    }
  },
  "findings": {
    "question_1": {
      "question": "六项否决理由现已逐项实测闭环，v4是否满足级名不滥升格条件(候选→正式)?",
      "answer": "不满足无条件升格。",
      "detail": "六项否证闭环提升了v4可信度，但『正式律』若意味着跨实现、跨作者、跨适用域、跨路径的稳定普适律，则E4-1独立性不足、E4-4适用域受限、E4-2辨识不充分。v4可升格为限定版正式判据，不宜升格为无限定正式律。"
    },
    "question_2": {
      "question": "E4-2双控制实验设计是否足以支撑「退火路径非表示界」?",
      "answer": "不足以充分支撑强命题；足以支撑弱命题。",
      "detail": "强命题『退火路径非表示界』需要排除所有表示相关机制，包括f64/f80差异、NaN/下溢、精度损失、条件数、舍入路径、库实现差异等。当前双控制排除了tol伪影并对比naive，但只能得出：退火路径在当前控制下不由表示界主导。"
    },
    "question_3": {
      "question": "E4-3「预测不需要路径/复现必须有路径」二元性是否成立?",
      "answer": "成立，但应限定为当前因子集与观测域。",
      "detail": "factor无可泛化预测信号，说明预测模型无需路径变量；同(k,R,B)跨factor展布中位2.72 dex、最大9.06 dex，说明无路径申报时复现不可判定。该二元性成立，但不能推出所有未来预测都永远不需要路径。"
    },
    "question_4": {
      "question": "若仍否决，给出可检验的具体否定理由。",
      "answer": "见counter_reasons。"
    },
    "counter_reasons": [
      {
        "id": "NEG-01",
        "target": "E4-1",
        "claim": "跨实现一致性被用于支撑正式律，但独立作者级不独立。",
        "test": "引入至少两个非同一作者/非同一代码谱系的独立实现，在相同申报schema下重跑三档ε，检验gap逐位一致是否保持。",
        "falsifier": "若独立实现间gap偏差超过申报err_metric或排序反转，则不得升格为跨共同体正式律。"
      },
      {
        "id": "NEG-02",
        "target": "E4-2",
        "claim": "『退火路径非表示界』未被充分辨识。",
        "test": "增加表示扰动控制：f128/任意精度、不同BLAS、不同求和顺序、不同Kahan补偿策略、不同稀疏格式。",
        "falsifier": "若任一表示扰动使退火gap显著超过当前f64/f80差异，则退火路径仍受表示界影响，强命题不成立。"
      },
      {
        "id": "NEG-03",
        "target": "E4-3",
        "claim": "二元性可能依赖当前36跑因子集。",
        "test": "扩展因子空间与(k,R,B)网格，特别是未观测路径、暖启动强度、截断阈值、随机种子结构。",
        "falsifier": "若新因子可在无路径申报下稳定预测gap，则『预测不需要路径』边界需收缩；若同(k,R,B)展布消失，则『复现必须有路径』需弱化。"
      },
      {
        "id": "NEG-04",
        "target": "E4-4",
        "claim": "显式上界仅限退火族/R∈[1,4]/ε∈[3e-3,1e-1]。",
        "test": "在域外做外推验证，尤其是ε<3e-3、R>4、非退火族、暖启动混合路径。",
        "falsifier": "若域外覆盖率低于申报阈值或上界被突破，则不得作为正式律的全局上界。"
      },
      {
        "id": "NEG-05",
        "target": "级名",
        "claim": "v4满足候选→正式，但不满足无条件正式律。",
        "test": "按级名定义审查：正式律是否要求普适性、独立性、适用域闭合、路径无关预测。",
        "falsifier": "若正式律定义为限定域工程律，则可升格；若定义为普适科学律，则否决。"
      }
    ],
    "recommended_resolution": {
      "action": "维持候选律，或升格为『条件正式律/工程判据集v4』",
      "conditions_for_full_promotion": [
        "完成独立作者级跨实现复现",
        "完成表示扰动全控制并排除退火路径表示界主导",
        "扩展E4-3因子空间验证二元性边界",
        "扩展E4-4适用域或明确外推拒绝机制",
        "级名定义中明确『正式律』是否允许限定域"
      ],
      "allowed_limited_promotion": {
        "name": "条件正式律v4",
        "scope": "退火族/R∈[1,4]/ε∈[3e-3,1e-1]/申报schema v1/预算证书按保守上界签发",
        "constraints": [
          "必须申报path",
          "必须申报budget",
          "必须申报eps_rel",
          "外推须显式声明"
        ]
      }
    }
  },
  "registry_note": {
    "denials_and_dissents_recorded": true,
    "close_03_harvest": "已入册",
    "next_review": "若补充独立作者级实现与表示扰动控制，可进入第4轮升格评审"
  }
}
```

**结论摘要：**

- **问1：** v4 **不满足无条件候选→正式升格**。六项否证闭环足以支撑其成为强工程判据，但不足以支撑无限定“正式律”。可考虑升格为 **“条件正式律/工程判据集v4”**。
- **问2：** E4-2双控制 **足以否定naive表示界主导**，但 **不足以充分证明“退火路径非表示界”**。应表述为“当前控制下退火路径未表现为表示界主导”。
- **问3：** E4-3二元性 **成立但需限定**：在当前因子集与观测域内，预测不需要路径；复现必须有路径。
- **问4：** 具体否定理由已列为 NEG-01 至 NEG-05，均可检验、可反驳、可入册。

——ucif2 SI1语义轨·20261008T061416Z
