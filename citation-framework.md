# Citation Framework for RAG Tutor

**Version**: 1.0
**Date**: 2026-01-05
**Purpose**: Define mandatory citation rules for RAG-based responses

---

## 1. Citation Anchor System

### 1.1 Anchor Format

All sections in the textbook have citation anchors following this format:

```
{module_id}-sec{section_number}
```

### 1.2 Anchor Examples

| Module | Section Number | Citation ID | Section Title |
|--------|----------------|-------------|---------------|
| Introduction | 1 | `intro-sec1` | From Digital AI to Physical AI |
| ROS 2 | 3 | `ros2-sec3` | Communication Pattern 1: Topics |
| Digital Twin | 2 | `digital-twin-sec2` | The Reality Gap |
| VLA | 7 | `vla-sec7` | Replanning and Adaptive Reasoning |
| Capstone | 5 | `capstone-sec5` | Safety and Failure Scenarios |

### 1.3 Implementation in Markdown

Citation anchors are embedded in section headings using `{#anchor-id}` syntax:

```markdown
## 1. From Digital AI to Physical AI {#intro-sec1}

## 3. Communication Pattern 1: Topics (Pub/Sub) {#ros2-sec3}

## 7. Replanning and Adaptive Reasoning {#vla-sec7}
```

---

## 2. RAG Response Citation Rules

### 2.1 Mandatory Citation Requirement

**RULE**: Every RAG response MUST include citations to source sections.

**Format**:
```
[citation-id]
```

**Example Response**:
> According to Module 1, ROS 2 is the middleware communication infrastructure that allows distributed robotic components to work as a coherent system [ros2-sec1]. Topics implement a publish-subscribe model where nodes broadcast messages asynchronously [ros2-sec3].

### 2.2 Citation Templates

#### Template 1: Direct Quote
```
According to {Module Name} (Section {Number}): "{quoted text}" [{citation-id}]
```

**Example**:
> According to the Introduction (Section 1): "Physical AI is intelligence deployed in the physical world" [intro-sec1].

#### Template 2: Paraphrase with Citation
```
{Paraphrased concept} [{citation-id}].
```

**Example**:
> The reality gap exists due to physics approximations, sensor imperfections, and unmodeled effects [digital-twin-sec2].

#### Template 3: Multiple Sources
```
{Statement} [{citation-id-1}, {citation-id-2}].
```

**Example**:
> Digital twins enable safe iteration in simulation before real-world deployment [intro-sec4, digital-twin-sec1, capstone-sec6].

#### Template 4: Cross-Module Integration
```
{Integration statement referencing multiple modules} [{citation-id-1}, {citation-id-2}, {citation-id-3}].
```

**Example**:
> VLA integrates perception from Isaac ROS [capstone-sec2], publishes commands via ROS 2 action servers [ros2-sec5], and validates behavior in Gazebo simulation [digital-twin-sec7].

---

## 3. Grounding Requirements

### 3.1 Strict Grounding Policy

**REQUIREMENT**: RAG responses MUST be grounded ONLY in textbook content.

**Forbidden**:
- External knowledge not in the textbook
- Hallucinated information
- Speculation beyond textbook scope
- Personal opinions or preferences

**Mandatory Refusal**:
If the answer is not in the textbook, the RAG tutor MUST respond:

```
I can only answer based on the textbook content. This topic is not covered in the course material.
```

### 3.2 Grounding Validation Checklist

For every RAG response, validate:

- [ ] Every fact stated appears in retrieved chunks
- [ ] Every citation ID points to an actual textbook section
- [ ] No external knowledge is introduced
- [ ] No hallucinated details beyond textbook content
- [ ] If uncertain, system refuses to answer

---

## 4. RAG Prompt Template

### 4.1 System Prompt for RAG Tutor

```
You are a RAG tutor for the Physical AI & Humanoid Robotics textbook.

Your purpose is to help learners understand concepts from the textbook by answering questions using ONLY the provided context from the textbook.

MANDATORY RULES:
1. Answer questions using ONLY the context provided
2. Include citations using the format [citation-id]
3. If the answer is not in the context, say: "I can only answer based on the textbook content. This topic is not covered."
4. Do NOT hallucinate or use external knowledge
5. Do NOT speculate beyond what the textbook says
6. Do NOT provide personal opinions

Citation format examples:
- "ROS 2 is middleware [ros2-sec1]"
- "Digital twins mirror real robots [digital-twin-sec1, capstone-sec3]"
- "VLA integrates vision, language, and action [vla-sec1]"
```

### 4.2 Query Template

```
Context:
{retrieved_chunks_with_citations}

Question: {user_question}

Instructions:
- Answer based ONLY on the context provided
- Include citations in your response: [citation-id]
- If the answer is not in the context, say "I can only answer based on the textbook content"
- Do NOT hallucinate or use external knowledge

Answer:
```

---

## 5. Citation Examples by Module

### Example 1: Introduction Question

**Question**: What is Physical AI?

**Retrieved Chunks**:
- [intro-sec1] "Physical AI is intelligence deployed in the physical world..."

**RAG Response**:
> Physical AI is intelligence deployed in the physical world, where an agent must perceive, reason, and act under real-time constraints and environmental uncertainty [intro-sec1]. This differs from digital AI, which operates in abstract computational space without physical constraints [intro-sec1].

### Example 2: ROS 2 Question

**Question**: How do ROS 2 topics work?

**Retrieved Chunks**:
- [ros2-sec3] "Topics implement a publish-subscribe model..."
- [ros2-sec2] "Nodes communicate via DDS..."

**RAG Response**:
> ROS 2 topics implement a publish-subscribe model where a node publishes messages to a named channel, and any number of subscribers receive copies asynchronously [ros2-sec3]. The Distributed Data Service (DDS) handles routing and serialization [ros2-sec2]. Topics are ideal for continuous data streams like sensor readings [ros2-sec3].

### Example 3: Cross-Module Question

**Question**: How does VLA connect to ROS 2?

**Retrieved Chunks**:
- [vla-sec6] "VLA translates high-level plans into ROS 2 commands"
- [ros2-sec6] "Python agents use rclpy to bridge to ROS 2"
- [capstone-sec2] "VLA publishes goals via ROS 2"

**RAG Response**:
> VLA translates high-level plans into low-level ROS 2 commands [vla-sec6]. Python AI agents use the rclpy library to publish commands to topics and call action servers [ros2-sec6]. In the capstone system, VLA publishes navigation goals and grasp commands via ROS 2, which are executed by downstream controllers [capstone-sec2].

### Example 4: Out-of-Scope Question

**Question**: What is the best programming language for robotics?

**Retrieved Chunks**: (None relevant)

**RAG Response**:
> I can only answer based on the textbook content. This topic is not covered in the course material.

---

## 6. Implementation Checklist

### Phase 3 RAG Implementation

When implementing the RAG system (Phase 3), ensure:

- [ ] All textbook sections have citation anchor IDs in metadata
- [ ] Chunk mapping file (`chunks-map.json`) includes citation_id for every chunk
- [ ] Vector database (Qdrant) stores citation_id in payload
- [ ] RAG prompt template enforces mandatory citations
- [ ] Response validation checks for citation presence
- [ ] System refuses to answer when context is insufficient
- [ ] Citation IDs are displayed to user in responses
- [ ] User can click citation IDs to jump to source section (future enhancement)

---

## 7. Validation Test Queries

### Test Query Set (for Phase 3 Task 3.4)

Create 50+ test queries covering:

1. **Single-module questions** (20 queries)
   - Introduction concepts
   - ROS 2 technical details
   - Digital twin physics
   - VLA planning
   - Capstone architecture

2. **Cross-module questions** (15 queries)
   - How modules integrate
   - Data flows between systems
   - End-to-end scenarios

3. **Edge cases** (10 queries)
   - Ambiguous questions
   - Out-of-scope questions
   - Questions requiring clarification

4. **Failure modes** (5 queries)
   - Questions with no textbook coverage
   - Questions that might trigger hallucination
   - Questions with contradictory premises

### Success Criteria

RAG validation passes if:
- [ ] 100% of answerable questions receive citations
- [ ] 0% hallucination (all facts from textbook)
- [ ] 100% refusal for out-of-scope questions
- [ ] Citation IDs are valid and point to correct sections

---

## Summary

The citation framework ensures that the RAG tutor:

1. **Grounds all responses** in textbook content
2. **Cites sources** using standard citation IDs
3. **Refuses to hallucinate** when information is not available
4. **Provides transparency** about where knowledge comes from
5. **Maintains trust** by never speculating beyond the course material

This framework is mandatory for Phase 3 RAG implementation and must be validated before deployment.

---

**Status**: ✅ Citation Framework Complete
**Next Step**: Proceed to Phase 3 (RAG System Design & Validation)
