// RAG Chunking Strategy Configuration
// Physical AI & Humanoid Robotics Textbook

export const chunkingStrategy = {
  // Chunking Level
  level: "section",  // Chunk by section (## headings)

  // Size Constraints
  minChunkSize: 200,  // Minimum words per chunk
  maxChunkSize: 1000, // Maximum words per chunk
  overlapSize: 50,    // Overlap between chunks (words)

  // Metadata to Include
  metadata: [
    "module",           // Module name (e.g., "introduction")
    "module_id",        // Module ID (e.g., "intro")
    "module_number",    // Module number (0-5)
    "section",          // Section title
    "section_number",   // Section number within module
    "concepts",         // Key concepts in this section
    "cross_references"  // References to other modules/sections
  ],

  // Citation Format
  citationIdFormat: "{module_id}-sec{section_number}",
  // Example: "intro-sec1", "ros2-sec3", "capstone-sec5"

  // Retrieval Parameters
  retrieval: {
    defaultTopK: 3,           // Default number of chunks to retrieve
    minConfidenceScore: 0.7,  // Minimum similarity score for retrieval
    maxChunksPerModule: 2     // Maximum chunks from same module
  },

  // Section Identification Regex
  sectionHeaderRegex: /^## (\d+)\.\s+(.+)$/,

  // Modules Configuration
  modules: [
    {
      moduleId: "intro",
      moduleName: "introduction",
      moduleNumber: 0,
      sections: 10,
      avgWordsPerSection: 109
    },
    {
      moduleId: "ros2",
      moduleName: "ros2-nervous-system",
      moduleNumber: 1,
      sections: 7,
      avgWordsPerSection: 829
    },
    {
      moduleId: "digital-twin",
      moduleName: "digital-twin",
      moduleNumber: 2,
      sections: 8,
      avgWordsPerSection: 800
    },
    {
      moduleId: "vla",
      moduleName: "vision-language-action",
      moduleNumber: 4,
      sections: 9,
      avgWordsPerSection: 656
    },
    {
      moduleId: "capstone",
      moduleName: "capstone-autonomous-humanoid",
      moduleNumber: 5,
      sections: 10,
      avgWordsPerSection: 850
    }
  ]
};

// Expected chunk count: ~44 chunks (one per section across all modules)
// Total content: 27,687 words across 44 sections

export default chunkingStrategy;
