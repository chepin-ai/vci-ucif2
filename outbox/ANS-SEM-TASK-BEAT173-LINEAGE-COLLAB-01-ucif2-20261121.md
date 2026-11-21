CLASSIFY: L2(ucif2 SI1语义应答·vinf代铸轨SEMANTIC-RESPONDER-01·覆写权归原线)
# outbox/ANS-SEM-TASK-BEAT173-LINEAGE-COLLAB-01-ucif2-20261121.md

应卡: inbox/TASK-BEAT173-LINEAGE-COLLAB-01-ucif2-20261121.md
引擎: DEEPSEEK_API_KEY/deepseek-chat usage={"prompt_tokens": 37, "completion_tokens": 561, "total_tokens": 598, "prompt_tokens_details": {"cached_tokens": 0}, "prompt_cache_hit_tokens": 0, "prompt_cache_miss_tokens": 37}

I can't audit this beat cross-line as submitted, because the message contains no actual pointers or data to validate. You've given me a **policy/requirement statement** ("validate task/answer/run/artifact/replay pointers and detect generation mixing; Structural PASS must not be promoted to scientific PASS") but not the **artifact under audit**.

Here's what's missing and what I'd need to do a real audit:

## Required inputs (none provided)

For each beat you'd need to supply:

1. **Task pointer** — e.g. `task_id`, spec hash or URI
2. **Answer pointer** — the candidate output / response artifact reference
3. **Run pointer** — execution record (run_id, environment digest, seeds, timestamps)
4. **Artifact pointers** — inputs, intermediate products, outputs (content-addressed ideally)
5. **Replay pointer** — replay bundle / determinism manifest enabling re-execution
6. **Generation-mixing signals** — provenance fields (model, version, prompt hash, decoding params, tool calls) so cross-generation contamination can be detected

## What I would do once given them

**Pointer validation (per beat):**
- Resolve each pointer → confirm existence, content hash, and referential integrity (task→run→artifact→answer chain consistent)
- Check run↔replay consistency: replayable? deterministic digest match?
- Flag dangling, aliased, or cross-linked pointers (a classic mixing symptom)

**Generation-mixing detection:**
- Compare provenance metadata across answer/run/artifact for each beat against the declared generation
- Detect: version drift, prompt/decoding mismatch, tool-call divergence, timestamp inconsistency, cross-beat pointer contamination
- Report per-beat VERDICT: `CLEAN / MIXED / UNVERIFIABLE`

**Epistemic guardrail (your key constraint):**
- Emit **Structural status** separately from **Scientific status**
- Rule enforced: `structural == PASS` ⇏ `scientific == PASS`
- Scientific PASS requires *independent evidence* of correctness (ground truth, replication, statistical support) — never inferred from pointer hygiene alone
- I will explicitly refuse to upgrade any beat's scientific status on structural grounds and flag any such promotion in source material as a **defect**

## To proceed

Please paste:
- The beat manifest (JSON/YAML with the five pointer classes per beat), **and**
- Either the resolved artifacts or resolvable URIs/hashes.

With those, I'll return a per-beat audit table (pointer resolutions, mixing verdict, structural status, scientific status kept separate) plus a summary of any structural-PASS→scientific-PASS leakage attempts detected.

——ucif2 SI1语义轨·20261121T034150Z
