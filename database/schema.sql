-- Enable AGE extension
CREATE EXTENSION IF NOT EXISTS age;
LOAD 'age';
SET search_path = ag_catalog, "$user", public;

-- Create Graph
SELECT create_graph('skill_network');

-- Users Table
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username VARCHAR(50) UNIQUE NOT NULL,
    global_reputation_score FLOAT DEFAULT 0.0,
    reputation_stake_balance INT DEFAULT 100
);
