# Sovereign Enclave Pilot Playbook v1.0
## 30/60/90-Day Deployment Template
### Atlas Lattice Foundation | March 28, 2026

---

## 1. Purpose

This playbook provides a step-by-step deployment template for standing up a Tier 1 Sovereign Enclave pilot. It is designed for use with any of the framework's pilot deployments (GangaSeek, DragonSeek, or standalone sovereign compute). Adjust scale and specifics to the target deployment.

---

## 2. Prerequisites

Before Day 1, the following must be in place:

| Prerequisite | Owner | Status Check |
|-------------|-------|-------------|
| Signed Legal Addendum (per template) | Customer + Provider | Contract executed |
| Physical site selected and secured | Customer | Site survey complete |
| HSMs procured (FIPS 140-3 Level 3+) | Customer | Hardware received and inventoried |
| Key quorum holders designated (M-of-N) | Customer | Holders confirmed, trained |
| Network connectivity provisioned | Provider + Customer | Dual-path (primary + out-of-band for chaos node) |
| Asha Linter firmware baseline established | Provider | Known-good hash recorded |
| Independent auditor selected | Customer | Engagement letter signed |
| Kill switch hardware procured | Customer | Relays, scrub controllers received |

---

## 3. Phase 1: Foundation (Days 1-30)

### Week 1-2: Hardware Installation

| Task | Owner | Deliverable | Verification |
|------|-------|-------------|-------------|
| Rack and stack servers in sovereign facility | Provider (supervised by customer) | Installed hardware | Photo + inventory log on Optical Ledger |
| Install HSM cluster | Customer | Operational HSMs | HSM self-test attestation |
| Install kill switch hardware (relays, scrub controllers) | Customer | Operational kill switch | Hardware test — relay fires on command |
| Establish network connectivity | Provider + Customer | Dual-path network | Ping test + bandwidth verification |
| Initialize Optical Ledger | Joint | First ledger entry: "ENCLAVE INITIALIZED" | Hash chain starts |

### Week 3-4: Key Ceremony & Boot

| Task | Owner | Deliverable | Verification |
|------|-------|-------------|-------------|
| Key generation ceremony (MEK, attestation keys, kill switch key) | Customer (auditor present) | Keys generated in HSM; ceremony recorded | Ceremony video + ledger entry |
| First boot with Asha Linter attestation | Joint | Successful attestation report | Hash matches known-good baseline |
| TEE initialization and verification | Provider | TEEs operational; memory encryption confirmed | TEE attestation report |
| Encrypt storage with sovereign keys | Joint | All storage encrypted | Encryption verification scan |
| **Phase 1 Gate Review** | Independent auditor | Controls C1-C4, C14 verified | Audit report on Optical Ledger |

---

## 4. Phase 2: Hardening (Days 31-60)

### Week 5-6: Security Validation

| Task | Owner | Deliverable | Verification |
|------|-------|-------------|-------------|
| Kill switch tabletop exercise | Joint | Scenario walked through; quorum response tested | All holders reachable in < 30 min |
| Kill switch partial drill (Steps 1-3) | Customer | Successful isolation on test partition | Isolation in < 5 minutes |
| Foreign demand simulation | Legal teams | Notice and challenge process tested | Simulated demand → notice in < 48h |
| Penetration test (provider insider threat scenario) | Independent auditor | No plaintext data accessible from provider-side | Pen test report |

### Week 7-8: Operational Readiness

| Task | Owner | Deliverable | Verification |
|------|-------|-------------|-------------|
| Chaos node installation (if required for tier) | Customer | Backup facility operational | Encrypted backup stream verified |
| Chaos node failover test | Joint | Successful failover from primary to chaos | Workloads running from chaos node |
| NERM integration (if applicable) | Joint | Cooling, power, heat recovery connected | NERM output metrics confirmed |
| Monitoring dashboard operational | Provider | Health metrics visible to both parties | Dashboard walkthrough |
| **Phase 2 Gate Review** | Independent auditor | Controls C5-C12 verified | Audit report on Optical Ledger |

---

## 5. Phase 3: Production (Days 61-90)

### Week 9-10: Workload Migration

| Task | Owner | Deliverable | Verification |
|------|-------|-------------|-------------|
| Migrate first production workload | Customer + Provider | Workload running in enclave | Performance benchmarks met |
| Verify end-to-end encryption (at rest, in transit, in use) | Independent auditor | No plaintext exposure at any stage | Full-stack encryption audit |
| Verify Optical Ledger completeness | Independent auditor | All events from Day 1 present and hash-chain intact | Ledger integrity check |

### Week 11-12: Certification & Handover

| Task | Owner | Deliverable | Verification |
|------|-------|-------------|-------------|
| Full comprehensive audit (all 14 controls) | Independent auditor | PASS on all controls | Audit report on Optical Ledger |
| Surprise kill switch drill | Customer (unannounced) | Provider cannot delay or obstruct | Drill report |
| Operational handover | Joint | Customer team trained; SOPs documented | Training completion records |
| **Phase 3 Gate Review: ENCLAVE CERTIFIED** | Independent auditor + Customer | Certification attestation on Optical Ledger | Enclave operational |

---

## 6. Post-Certification: Ongoing Operations

| Activity | Frequency | Owner |
|----------|-----------|-------|
| Automated attestation verification | Continuous | Asha Linter |
| Optical Ledger hash chain check | Daily | Neutral third party |
| Kill switch tabletop | Monthly | Customer |
| Physical hardware audit | Quarterly | Independent auditor |
| Kill switch partial drill | Quarterly | Joint |
| Legal compliance audit | Annually | Independent legal counsel |
| Full comprehensive audit | Annually | Customer-chosen auditor |
| Surprise drill | Annually | Customer |

---

## 7. Scaling from Pilot to Production

| From → To | Key Changes | Timeline |
|-----------|-------------|----------|
| Tier 1 → Tier 2 (50-500 nodes) | Add chaos node (mandatory); add NERM (recommended); expand HSM cluster | 3-6 months |
| Tier 2 → Tier 3 (500+ nodes) | Asha Linter-integrated hardware; NERM mandatory; secondary chaos node; Maia/TPU v7 accelerators | 6-12 months |

Each tier transition requires a new comprehensive audit and certification.

---

## 8. Cost Estimate (Tier 1 Pilot)

| Item | Estimated Cost | Notes |
|------|---------------|-------|
| Server hardware (10-50 nodes) | $2-10M | COTS servers; scale-dependent |
| HSM cluster | $500K-1M | FIPS 140-3 Level 3+ |
| Kill switch hardware | $100-200K | Relays, scrub controllers, seal module |
| Network provisioning | $200-500K | Dual-path, sovereign firewall |
| Independent audit (3 gate reviews) | $300-500K | Depends on auditor |
| Legal costs (addendum negotiation) | $200-400K | Provider + customer counsel |
| NERM integration (optional at Tier 1) | $1-3M | If co-deployed |
| **Total Tier 1 Pilot** | **$3.5-15.5M** | Depends on scale and NERM |

---

## 9. Relationship to Other Documents

- **Sovereign_Enclave_Definition_v1.0.md** — the six criteria verified during gate reviews
- **Sovereign_Enclave_Controls_Matrix_v1.0.md** — the 14 controls audited at each gate
- **Sovereign_Enclave_Reference_Architecture_v1.0.md** — the architecture being deployed
- **Kill_Switch_Governance_v1.0.md** — kill switch testing procedures referenced in Phase 2
- **Sovereign_Enclave_Legal_Addendum_Template_v1.0.md** — must be signed before Day 1
- **GangaSeek_Pilot_Spec_v1.0.md** / **DragonSeek_Scaling_Spec_v1.0.md** — specific pilot parameters

---

*Atlas Lattice Foundation | CC BY-SA 4.0*