# Feature Specification: Module 4 — Vision-Language-Action (VLA)

**Feature Branch**: `4-vision-language-action`
**Created**: 2026-01-04
**Status**: Draft
**Input**: User description: "Module 4 — Vision-Language-Action (VLA)"

---

## User Scenarios & Testing

### User Story 1 - Student Understands VLA as Agentic AI System (Priority: P1)

A learner coming from Modules 1–3 (ROS 2, Digital Twin, Isaac) needs to understand **VLA as an agentic cognitive layer**—not a pipeline of isolated components, but a **closed-loop reasoning system** that continuously perceives, plans, acts, observes, and replans.

**Why this priority**: Without this framing, VLA appears as a disconnected perception-language-action pipeline. With it, students see an agent capable of handling uncertainty, failure, and dynamic environments.

**Independent Test**: A student can:
1. Explain the VLA agent loop (perceive → plan → act → observe → replan)
2. Distinguish between pipelines and agents
3. Articulate the role of memory and world state in agentic reasoning

**Acceptance Scenarios**:

1. **Given** a student familiar with ROS 2 nodes and perception pipelines, **When** they encounter VLA, **Then** they recognize it as an agent, not a sequence of transforms.

2. **Given** a robot receiving a voice command, **When** asked how it handles unexpected obstacles, **Then** the student explains the replanning loop: perception → updated world state → revised plan → new actions.

3. **Given** a description of "language model + perception," **When** asked what's missing, **Then** the student identifies memory, planning, execution monitoring, and replanning.

---

### User Story 2 - Student Understands Language-to-Goal Mapping (Priority: P1)

A learner needs to understand how **natural language inputs are transformed into structured goals, plans, and executable actions**—handling ambiguity, clarification, and constraint reasoning.

**Why this priority**: This is the cognitive heart of VLA. Students must understand both the power and limitations of language understanding.

**Independent Test**: A student can:
1. Trace how a natural language command becomes a goal
2. Explain how ambiguities are resolved
3. Reason about constraints that shape plans

**Acceptance Scenarios**:

1. **Given** a voice command like "Go to the kitchen and bring me a glass of water," **When** asked to decompose it, **Then** the student identifies sub-goals: navigate to kitchen, find water glass, grasp, return, place safely.

2. **Given** an ambiguous command ("Pick up the red thing"), **When** asked how the system handles it, **Then** the student explains perception (visual grounding), world state (which red objects exist), and possible clarification.

3. **Given** a plan to navigate, **When** asked about safety constraints, **Then** the student identifies collision avoidance, force limits, velocity bounds from the execution layer.

---

### User Story 3 - Student Grasps Perception-Language Grounding (Priority: P1)

A learner needs to understand how **visual perception outputs ground language understanding**—objects, spatial relationships, state changes—and how **world state and memory** enable the agent to reason about the environment.

**Why this priority**: Perception grounds language; without this link, the agent operates on abstract goals disconnected from reality.

**Independent Test**: A student can:
1. Explain how object detection outputs inform language understanding
2. Describe what "world state" contains and why it matters
3. Reason about memory: short-term (current task state) vs. long-term (learned models)

**Acceptance Scenarios**:

1. **Given** a scene with multiple objects and a command "Put the blue cup on the table," **When** the agent reasons about it, **Then** the student traces: perception outputs detected objects → matching "blue cup" to one object → planning the placement action.

2. **Given** an agent operating in a dynamic environment, **When** asked how it knows if a previous action succeeded, **Then** the student explains: execute action → perceive updated state → compare to expected state → replanning if needed.

3. **Given** a reference to "where I put the cup earlier," **When** asked how the agent understands this, **Then** the student identifies short-term memory of task state and spatial reasoning.

---

### User Story 4 - Student Understands Planning & Replanning Loops (Priority: P1)

A learner needs to grasp the **closed-loop planning process**—initial plan generation, execution monitoring, failure detection, and adaptive replanning.

**Why this priority**: Replanning is what makes the system robust to uncertainty. Without this, students see VLA as brittle.

**Independent Test**: A student can:
1. Explain the planning loop: plan → execute → monitor → replan
2. Identify failure modes and recovery strategies
3. Reason about when and why plans change

**Acceptance Scenarios**:

1. **Given** a humanoid following a navigation plan, **When** asked what happens if it detects a new obstacle, **Then** the student explains: perception updates world state → planner identifies conflict → new plan generated → execution resumes.

2. **Given** a task like "grasp the cup and move it," **When** asked how the system handles a failed grasp, **Then** the student describes: failure detection → world state update (object not grasped) → adjusted plan (retry or alternative approach).

3. **Given** a complex task sequence, **When** asked about dynamic changes, **Then** the student explains that the agent continuously replans based on perception, not rigidly following the initial plan.

---

### User Story 5 - Student Reasons About Safety, Uncertainty & Failure (Priority: P1)

A learner needs to understand how **safety constraints are architecturally enforced** in the VLA → execution pipeline, and how the system handles **uncertainty and graceful degradation**.

**Why this priority**: Safety is non-negotiable in Physical AI. Students must understand that cognitive freedom is bounded by execution constraints.

**Independent Test**: A student can:
1. Explain how safety is enforced (at planning, execution, and monitoring layers)
2. Reason about uncertainty in perception and planning
3. Describe recovery and fallback strategies

**Acceptance Scenarios**:

1. **Given** a humanoid commanded to push an object, **When** asked about safety, **Then** the student identifies constraints: force limits, collision detection, human proximity monitoring—enforced in Isaac ROS/ROS 2, not just cognition.

2. **Given** perceptual uncertainty (e.g., object detection confidence < threshold), **When** asked how the agent handles it, **Then** the student explains: either seek clarification, or proceed with risk awareness and enhanced monitoring.

3. **Given** an action that fails multiple times, **When** asked how the system responds, **Then** the student describes fallback behavior: report failure to human supervisor, or attempt alternative strategy.

---

### User Story 6 - Student Sees VLA as Capstone Cognitive Core (Priority: P1)

A learner needs to understand that **VLA is the cognitive backbone of the Capstone Autonomous Humanoid** project—integrating everything from Modules 1–3 into a unified system.

**Why this priority**: This provides motivation and context for the final project. Students should see how all pieces connect.

**Independent Test**: A student can:
1. Trace how Module 1–3 concepts flow into the Capstone
2. Identify what each module contributes to the final system
3. Understand their role in building the cognitive layer

**Acceptance Scenarios**:

1. **Given** the Capstone project description, **When** asked where VLA appears, **Then** the student identifies it as the decision-making layer receiving voice commands and coordinating all actions.

2. **Given** the full system architecture (ROS 2 + Gazebo + Isaac + VLA), **When** asked how it works, **Then** the student correctly traces: voice command → VLA (cognitive) → ROS 2 (execution) → Isaac perception → feedback loop.

---

### User Story 7 - Student Understands RAG Tutor as Reasoning Supervisor (Priority: P2)

A learner needs to understand that the **embedded RAG tutor plays a unique role in Module 4**—not just explaining concepts, but helping reason about VLA systems and debug agent behavior.

**Why this priority**: This extends the RAG tutor's role from explanation to reasoning, supporting AI-supervising-AI workflows.

**Independent Test**: A student can:
1. Ask the tutor to compare alternative plans
2. Request explanation of why a plan failed
3. Reason through edge cases with tutor assistance

**Acceptance Scenarios**:

1. **Given** a humanoid facing two possible navigation routes, **When** asked which is better, **Then** the student consults the tutor, which compares routes based on module content (path length, obstacles, energy, safety).

2. **Given** an agent failure scenario, **When** asked what went wrong, **Then** the student uses the tutor to trace through perception → planning → execution, identifying root cause.

---

### User Story 8 - Educator Evaluates Module for Capstone Integration (Priority: P2)

An instructor needs to understand how Module 4 serves as the cognitive foundation for the Capstone and integrates with all prior modules.

**Why this priority**: Educator alignment ensures smooth transition to the Capstone project.

**Independent Test**: An instructor can:
1. Verify that Module 4 integrates Modules 1–3
2. Assess learning objectives for Capstone readiness
3. Plan Capstone scaffolding based on VLA concepts

**Acceptance Scenarios**:

1. **Given** the course syllabus, **When** an instructor reviews Module 4, **Then** they confirm it fits Weeks 11–12 and directly enables the Week 13 Capstone.

---

## Edge Cases

- **What if the LLM generates unsafe plans?** (Addressed in Safety & Constraints; execution layer enforces physical limits regardless of cognitive output.)

- **What if perception fails or is ambiguous?** (Addressed in Uncertainty section; agent has fallback strategies and escalation to human supervision.)

- **What if the humanoid can't execute a planned action?** (Addressed in Replanning & Failure Handling; detection and recovery loops.)

- **What if language is ambiguous?** (Addressed in Language Understanding; clarification mechanisms and constraint reasoning.)

- **What if a student tries to implement a full RL training system?** (Out-of-scope; module focuses on reasoning, not training algorithms.)

---

## Requirements

### Functional Requirements

- **FR-001**: The module MUST frame **VLA as an agentic AI system**, not a pipeline—with explicit closed-loop architecture (perceive → plan → act → observe → replan).

- **FR-002**: The module MUST explain **perception grounding**: how vision systems provide objects, spatial relationships, and state information to inform language understanding.

- **FR-003**: The module MUST define and emphasize **world state and memory** as central to agentic reasoning—distinguishing short-term (task state) from long-term (learned models).

- **FR-004**: The module MUST explain **language understanding and intent parsing**—goal extraction, ambiguity handling, and constraint reasoning.

- **FR-005**: The module MUST describe the **planning and replanning process**, including closed-loop execution monitoring and failure detection.

- **FR-006**: The module MUST articulate how **VLA decisions map to ROS 2 actions** and how the execution layer enforces safety.

- **FR-007**: The module MUST emphasize **safety and uncertainty**: perception uncertainty, planning uncertainty, graceful degradation, and fallback strategies.

- **FR-008**: The module MUST establish that **VLA proposes; execution constraints enforce**—cognitive freedom bounded by physical limits.

- **FR-009**: The module MUST include **guided conceptual exercises**: voice command → goal → plan → action → observation → replanning scenarios.

- **FR-010**: The module MUST position **VLA as the cognitive core of the Capstone Autonomous Humanoid** project, integrating Modules 1–3.

- **FR-011**: The module MUST establish the canonical **reference environment** (OpenAI-compatible LLMs, Whisper-style speech-to-text, Isaac ROS perception, ROS 2 execution).

- **FR-012**: The module MUST NOT implement full agent frameworks, train language models, provide low-level control logic, or require hardware deployment.

- **FR-013**: The module MUST be structured for the embedded RAG tutor to support **AI-supervising-AI reasoning workflows**—comparing plans, debugging behavior, explaining decisions.

- **FR-014**: The module MUST NOT include Module 3 content (Isaac perception details); perception is treated as an input source.

### Key Entities

- **VLA Agent**: An agentic system integrating language understanding, perception, memory, planning, and execution in a closed loop.
- **Agent Loop**: The cycle of perceive → plan → act → observe → replan that defines agentic behavior.
- **World State**: The agent's representation of the environment—objects, spatial relationships, state of ongoing tasks.
- **Memory**: Short-term (current task state) and long-term (learned models, world models) information.
- **Intent**: The goal or task extracted from natural language.
- **Plan**: A sequence of actions designed to achieve the intent.
- **Perception Grounding**: The link between visual perception outputs and language understanding.
- **Replanning**: The process of updating and re-executing plans in response to environmental changes or failures.
- **Safety Constraint**: Physical or logical limit enforced by the execution layer (force limits, collision avoidance, velocity bounds).
- **Fallback Strategy**: Alternative plan or escalation (e.g., human supervision) when primary plan fails.

---

## Success Criteria

### Measurable Outcomes

- **SC-001**: Students explain VLA as a closed-loop agentic system with explicit perceive → plan → act → observe → replan cycle.

- **SC-002**: Students articulate the role of perception grounding and world state in language understanding.

- **SC-003**: Students can trace a voice command through the entire VLA pipeline: language → goal → plan → action → perception → replanning.

- **SC-004**: Students understand how memory (short-term and long-term) enables reasoning about task state and world models.

- **SC-005**: Students explain how planning handles ambiguity, constraints, and dynamic environments.

- **SC-006**: Students understand how replanning responds to failures and environmental changes.

- **SC-007**: Students articulate that safety is architecturally enforced (in execution layer) regardless of cognitive output.

- **SC-008**: Students can reason about uncertainty at multiple layers (perception, planning, execution) and describe fallback strategies.

- **SC-009**: Students see VLA as the cognitive core of the Capstone and can trace module integration (Modules 1–4 → Capstone).

- **SC-010**: Students can use the RAG tutor to reason about VLA systems—comparing plans, debugging behavior, explaining decisions.

- **SC-011**: Module content supports RAG retrieval for AI-supervising-AI reasoning workflows.

- **SC-012**: Module aligns with curriculum positioning (Weeks 11–12, direct prerequisite for Capstone Week 13).

---

## Assumptions

- **Knowledge Assumption**: Learners have completed Modules 1–3 and understand ROS 2, simulation, and Isaac perception as foundational.

- **Language Model Assumption**: LLMs are accessed via APIs (OpenAI-compatible); training is out-of-scope. Students reason about LLMs as decision makers, not developers.

- **Perception Source Assumption**: Perception outputs (objects, spatial relationships) come from Isaac ROS or equivalent; perception implementation is Module 3 content.

- **Execution Assumption**: ROS 2 actions and controllers are the execution substrate; safety constraints are enforced at this layer.

- **Agentic Reasoning Assumption**: The module emphasizes reasoning under uncertainty, failure recovery, and replanning—not perfect execution.

- **Memory Assumption**: Both short-term (task state) and long-term (learned models) memory are part of the cognitive architecture.

- **Safety-First Assumption**: Safety is non-negotiable; the execution layer enforces limits regardless of cognitive decisions.

- **Capstone Integration Assumption**: Module 4 directly enables Week 13 Capstone project; all concepts should prepare for hands-on system design.

- **AI-Supervising-AI Assumption**: The RAG tutor extends its role from explanation to reasoning, supporting human supervision of VLA systems.

---

## Non-Goals

The module MUST NOT:

- **NG-001**: Implement full agent frameworks or orchestration systems.
- **NG-002**: Train language models or fine-tune LLMs.
- **NG-003**: Teach reinforcement learning or machine learning training.
- **NG-004**: Provide low-level control algorithms (kinematics, motor control).
- **NG-005**: Require real robot hardware deployment or testing.
- **NG-006**: Delve into Isaac Sim perception details (Module 3 content).
- **NG-007**: Cover natural language processing internals or transformer architectures.
- **NG-008**: Teach semantic parsing, knowledge graphs, or formal logic systems.

---

## Content Structure

The module is organized into **9 logically sequenced sections**:

1. **Vision-Language-Action as Agentic AI** — Motivation and agent loop definition
2. **Perception Grounding: From Vision to Language** — Objects, spatial relationships, state
3. **World State and Memory** — Short-term task state, long-term models, reasoning foundation
4. **Language Understanding and Intent Parsing** — Goals, constraints, ambiguity handling
5. **Planning and Task Decomposition** — High-level planning, sequencing, feasibility
6. **Closed-Loop Execution and Monitoring** — Mapping plans to actions, feedback, detection
7. **Replanning and Adaptive Reasoning** — Responding to changes, failure recovery, replanning
8. **Safety, Uncertainty, and Fallback Strategies** — Constraints, degradation, recovery
9. **VLA as Capstone Cognitive Core** — Integration of all modules, system architecture

**Optional Sections** (if needed after planning):
- 10. **Guided Conceptual Lab: Voice Command → Autonomous Action** — End-to-end scenario
- 11. **Common VLA Failure Modes and Reasoning Strategies** — Debugging and recovery
- 12. **AI Supervising AI: Using the RAG Tutor for System Reasoning** — Meta-level design

---

## Style & Tone Guidelines

- **Agentic Reasoning Emphasis**: Frame VLA as intelligent decision-making under uncertainty, not rigid automation.
- **Systems Integration**: Connect all modules to the Capstone; show how pieces fit together.
- **Practical Grounding**: Ground examples in humanoid robot tasks (navigation, manipulation, interaction).
- **Safety-First Framing**: Emphasize that cognitive freedom is bounded by execution constraints.
- **RAG-Friendly Structure**: Write so the tutor can reason about plans, failures, and alternatives step-by-step.

---

## Validation Checklist (Pre-Implementation)

- [ ] VLA framed explicitly as agentic system with closed-loop architecture
- [ ] Perception grounding and world state included as foundational
- [ ] Memory (short-term and long-term) integrated into reasoning
- [ ] Language understanding and intent parsing explained
- [ ] Planning and replanning clearly defined with failure modes
- [ ] Safety enforced architecturally (execution layer, not cognition)
- [ ] Uncertainty and fallback strategies covered
- [ ] VLA positioned as Capstone cognitive core
- [ ] RAG tutor role extended to reasoning supervision
- [ ] All 9 sections logically sequenced and scoped
- [ ] Non-goals prevent scope creep (no RL, no LLM training, no low-level control)
- [ ] Aligns with Constitution and Hackathon-1

---

## Assessment Integration

This module contributes to **Vision-Language-Action Design Assessment**:

- **Deliverable**: Learners produce a conceptual VLA system design artifact describing:
  - Language input handling (intent parsing, ambiguity resolution)
  - Perception grounding and world state (memory architecture)
  - Planning and replanning logic (failure handling, adaptation)
  - Action execution, safety, and monitoring (constraint enforcement, feedback loops)

- **Focus**: Cognitive architecture design and reasoning, not implementation.
- **Rubric Alignment**:
  - Correct identification of VLA components and their roles
  - Clear explanation of closed-loop agent reasoning
  - Evidence of understanding safety constraints and failure recovery
  - Integration with execution substrate (ROS 2, Isaac)

---

## Prerequisite & Downstream Dependencies

- **Prerequisite**: Modules 1–3 (ROS 2, Digital Twin, Isaac) — students must understand execution substrates and perception sources
- **Downstream**: Week 13 Capstone Project (Autonomous Humanoid) — VLA is the cognitive core
- **Integration**: All prior modules feed into VLA; VLA controls all prior systems

---

## Acceptance Gate

Module 4 is **ready for content development** when this specification is approved. The actual module content will be written using:

- **Primary Skill**: `robotics-explainer` (author agentic reasoning and cognitive architecture concepts)
- **Supporting Skill**: `section-writer` (polish prose and narrative flow)
- **AI Tool**: Claude Code (supervised authoring, not autonomous content generation)
- **Validation**: Content reviewed against all 14 functional requirements and 12 success criteria

All content will be grounded in the Physical AI Hackathon-1 Constitution and positioned as Weeks 11–12 of the 13-week curriculum, serving as the cognitive foundation for the Week 13 Capstone Project.
