# Sovereign Enclave Controls Matrix v1.0
## Legal Obligations Mapped to Technical Evidence
### Atlas Lattice Foundation | March 28, 2026

**Purpose:** This matrix maps every legal commitment in the Sovereign Enclave Legal Addendum to the specific technical control that enforces it and the evidence artifact that proves compliance. This is the audit-ready document — the one an independent assessor uses to verify claims.

---

## 1. Controls Matrix

| # | Legal Obligation (Addendum Section) | Technical Control | Evidence Artifact | Verification Method | Failure Mode |
|---|--------------------------------------|-------------------|-------------------|--------------------|--------------| 
| C1 | Physical residency of hardware (§2.1) | GPS-tagged rack inventory; physical access logs | Rack manifest + geofence telemetry on Optical Ledger | Independent physical audit; geofence alert if hardware moves | Hardware relocation triggers kill switch alert |
| C2 | Key sovereignty — customer-held only (§2.2) | HSMs in sovereign territory; FIPS 140-3 Level 3+ | HSM attestation certificates; key generation logs on Optical Ledger | HSM vendor audit trail; no provider key escrow provable by absence | Any provider key access = critical breach; kill switch eligible |
| C3 | Boot attestation at every startup (§2.3) | Asha Linter hardware-rooted attestation; RISC-V extensions; OTP baseline | Boot attestation report on Optical Ledger per startup | Compare attestation hash to known-good baseline; any mismatch = investigation | 1 mismatch = warning; 3/24h = quarantine; firmware modification attempt = hard shutdown |
| C4 | No backdoors in hardware/software/firmware (§3.3) | Asha Linter continuous runtime verification; OTP memory prevents post-fab modification | Runtime attestation logs; OTP integrity checks | Quarterly independent hardware inspection; continuous runtime monitoring | Any unauthorized modification attempt = hard power-off per Asha Linter spec |
| C5 | Foreign demand notice within 48h (§3.1) | Legal compliance ticketing system; automated timestamp on Optical Ledger | Demand receipt timestamp + customer notification timestamp on Ledger | Time delta between receipt and notification must be ≤48h | Breach of notice obligation = contract violation; customer may trigger kill switch |
| C6 | Gag order challenge (§3.1) | Legal team SOP; court filing records | Court docket entries (redacted if necessary) on Optical Ledger post-gag expiry | Independent legal audit annually | Failure to challenge = contract violation |
| C7 | Minimization of compelled disclosure (§3.2) | Data segmentation; provider refers authority to sovereign for direct service | Minimization log showing scope reduction attempts | Independent legal audit | Over-disclosure = contract violation + damages |
| C8 | Optical Ledger — all significant events (§4.1) | Append-only cryptographic ledger; distributed across sovereign + provider + neutral third party | Ledger itself is the evidence | Hash chain verification; any gap = tamper indicator | Gap in ledger = presumption of tampering; kill switch eligible |
| C9 | Audit rights — any time, reasonable notice (§4.2) | Physical + logical access for auditor; read-only log access | Audit reports filed on Optical Ledger | Auditor confirms access was complete and unobstructed | Access obstruction = contract violation |
| C10 | Secure erasure on termination — NIST 800-88 (§5.1) | Cryptographic erasure + physical overwrite; NIST 800-88 compliant | Erasure attestation certificate on Optical Ledger | Independent verification of erasure completeness | Incomplete erasure = breach; provider liable |
| C11 | Kill switch — customer-triggered (§5.2) | Hardware-enforced isolation; key revocation; volatile memory wipe; network isolation | Kill switch activation log on Optical Ledger; migration initiation log | Quarterly drill testing; mean activation time < 5 min | Activation failure = critical control failure; escalate immediately |
| C12 | Kill switch — provider cannot trigger unilaterally (§5.3) | Kill switch control circuit accessible only via customer key quorum | Provider-side kill switch attempts logged and rejected unless physical security threat demonstrated | Log review; any unauthorized provider trigger = critical breach | Unauthorized trigger = contract violation + damages |
| C13 | 90-day notice for changes (§7) | Change management system; mandatory 90-day hold | Change request timestamp + customer response on Optical Ledger | Time delta between request and implementation must be ≥90d | Premature change = contract violation; customer may reject + trigger kill switch |
| C14 | TEE enforcement — no plaintext access (§ via Definition) | Intel TDX / ARM CCA / AMD SEV-SNP; data encrypted in use | TEE attestation reports; memory encryption verification | Continuous monitoring; any plaintext exposure = critical breach | Plaintext exposure = kill switch + full investigation |

---

## 2. Evidence Chain

Every control produces evidence that flows into the Optical Ledger:

```
Hardware Event → Asha Linter Attestation → Optical Ledger Entry → Auditor Verification
     ↓                    ↓                        ↓                      ↓
  Physical            Cryptographic            Immutable              Independent
  Reality             Proof                    Record                 Confirmation
```

The chain is unbroken. If any link is missing, the control is considered failed until proven otherwise.

---

## 3. Audit Schedule

| Audit Type | Frequency | Performed By | Scope |
|-----------|-----------|-------------|-------|
| Automated attestation verification | Continuous (every boot + runtime) | Asha Linter | C3, C4, C14 |
| Optical Ledger hash chain verification | Daily (automated) | Neutral third party | C8 |
| Physical hardware audit | Quarterly | Independent auditor chosen by customer | C1, C2, C4 |
| Legal compliance audit | Annually | Independent legal counsel | C5, C6, C7 |
| Kill switch drill | Quarterly | Joint customer-provider team | C11, C12 |
| Full comprehensive audit | Annually | Customer-chosen auditor | All controls |

---

## 4. Scoring

For each control, the audit produces a score:

| Score | Meaning | Action Required |
|-------|---------|----------------|
| **PASS** | Control operating as specified; evidence complete | None |
| **OBSERVATION** | Minor deviation; no security impact | Remediate within 30 days |
| **FINDING** | Control partially failed; potential security impact | Remediate within 7 days; customer notified |
| **CRITICAL** | Control failed; active security risk | Immediate kill switch consideration; customer notified within 1 hour |

---

## 5. Relationship to Other Documents

- **Sovereign_Enclave_Definition_v1.0.md** — defines the six criteria this matrix enforces
- **Sovereign_Enclave_Legal_Addendum_Template_v1.0.md** — the legal obligations mapped here
- **Asha_Linter_Hardware_Spec_v1.0.md** — the attestation engine producing evidence for C3, C4, C14
- **Kill_Switch_Governance_v1.0.md** — detailed spec for C11, C12
- **Compelled_Access_Reality_Check_v1.0.md** — context for C5, C6, C7

---

*Atlas Lattice Foundation | CC BY-SA 4.0*