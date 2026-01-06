-- Physical AI Textbook RAG Database Schema
-- Neon Serverless Postgres Database: physical_ai_textbook

-- Drop existing tables if they exist (for clean setup)
DROP TABLE IF EXISTS queries CASCADE;
DROP TABLE IF EXISTS chunks CASCADE;
DROP TABLE IF EXISTS modules CASCADE;

-- Modules Table: Store module metadata
CREATE TABLE modules (
  id SERIAL PRIMARY KEY,
  module_id VARCHAR(50) UNIQUE NOT NULL,
  module_name VARCHAR(100) NOT NULL,
  module_number INTEGER NOT NULL,
  sections INTEGER NOT NULL,
  word_count INTEGER NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Chunks Table: Store textbook chunks and their metadata
CREATE TABLE chunks (
  id SERIAL PRIMARY KEY,
  chunk_id VARCHAR(50) UNIQUE NOT NULL,
  module_id VARCHAR(50) NOT NULL REFERENCES modules(module_id),
  module_number INTEGER NOT NULL,
  section_number INTEGER NOT NULL,
  section_title VARCHAR(200) NOT NULL,
  content TEXT NOT NULL,
  embedding_id VARCHAR(100),  -- Reference to Qdrant vector ID
  citation_id VARCHAR(50) NOT NULL,
  concepts TEXT[],  -- Array of key concepts
  word_count INTEGER,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Queries Table: Store user queries and RAG responses for analytics
CREATE TABLE queries (
  id SERIAL PRIMARY KEY,
  query TEXT NOT NULL,
  response TEXT NOT NULL,
  citations JSONB,  -- Store array of citation IDs as JSON
  top_k INTEGER DEFAULT 3,
  min_confidence FLOAT DEFAULT 0.7,
  chunks_retrieved INTEGER,
  execution_time_ms INTEGER,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Indexes for performance
CREATE INDEX idx_chunks_module_id ON chunks(module_id);
CREATE INDEX idx_chunks_citation_id ON chunks(citation_id);
CREATE INDEX idx_chunks_embedding_id ON chunks(embedding_id);
CREATE INDEX idx_queries_created_at ON queries(created_at);

-- Insert module metadata
INSERT INTO modules (module_id, module_name, module_number, sections, word_count) VALUES
  ('intro', 'introduction', 0, 10, 1087),
  ('ros2', 'ros2-nervous-system', 1, 7, 5800),
  ('digital-twin', 'digital-twin', 2, 8, 6400),
  ('vla', 'vision-language-action', 4, 9, 5900),
  ('capstone', 'capstone-autonomous-humanoid', 5, 10, 8500);

-- Views for analytics

-- View: Queries per day
CREATE VIEW queries_per_day AS
SELECT
  DATE(created_at) as query_date,
  COUNT(*) as query_count
FROM queries
GROUP BY DATE(created_at)
ORDER BY query_date DESC;

-- View: Most queried modules
CREATE VIEW most_queried_modules AS
SELECT
  module_id,
  COUNT(*) as query_count
FROM chunks
WHERE embedding_id IN (
  SELECT DISTINCT jsonb_array_elements_text(citations)
  FROM queries
)
GROUP BY module_id
ORDER BY query_count DESC;

-- View: Average execution time
CREATE VIEW avg_execution_time AS
SELECT
  AVG(execution_time_ms) as avg_time_ms,
  MAX(execution_time_ms) as max_time_ms,
  MIN(execution_time_ms) as min_time_ms
FROM queries;

-- Comments
COMMENT ON TABLE modules IS 'Stores metadata for each textbook module';
COMMENT ON TABLE chunks IS 'Stores chunked textbook content with citation anchors';
COMMENT ON TABLE queries IS 'Stores user queries and RAG responses for analytics';

-- Grant permissions (adjust as needed for your Neon setup)
-- GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO your_user;
-- GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO your_user;
