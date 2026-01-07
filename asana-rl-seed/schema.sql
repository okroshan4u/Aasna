-- =========================================================
-- Asana RL Seed Data Schema (SQLite)
-- =========================================================

PRAGMA foreign_keys = ON;

-- =========================================================
-- Organizations / Workspaces
-- =========================================================
CREATE TABLE organizations (
    organization_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    domain TEXT,
    created_at TIMESTAMP
);

-- =========================================================
-- Users
-- =========================================================
CREATE TABLE users (
    user_id TEXT PRIMARY KEY,
    organization_id TEXT NOT NULL,
    full_name TEXT NOT NULL,
    email TEXT UNIQUE,
    role TEXT,
    is_active INTEGER,
    joined_at TIMESTAMP,
    FOREIGN KEY (organization_id) REFERENCES organizations(organization_id)
);

-- =========================================================
-- Teams
-- =========================================================
CREATE TABLE teams (
    team_id TEXT PRIMARY KEY,
    organization_id TEXT NOT NULL,
    name TEXT NOT NULL,
    team_type TEXT,
    created_at TIMESTAMP,
    FOREIGN KEY (organization_id) REFERENCES organizations(organization_id)
);

-- =========================================================
-- Team Memberships
-- =========================================================
CREATE TABLE team_memberships (
    team_id TEXT NOT NULL,
    user_id TEXT NOT NULL,
    joined_at TIMESTAMP,
    PRIMARY KEY (team_id, user_id),
    FOREIGN KEY (team_id) REFERENCES teams(team_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- =========================================================
-- Projects
-- =========================================================
CREATE TABLE projects (
    project_id TEXT PRIMARY KEY,
    team_id TEXT NOT NULL,
    name TEXT NOT NULL,
    project_type TEXT,
    start_date DATE,
    end_date DATE,
    status TEXT,
    created_at TIMESTAMP,
    FOREIGN KEY (team_id) REFERENCES teams(team_id)
);

-- =========================================================
-- Sections
-- =========================================================
CREATE TABLE sections (
    section_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    name TEXT NOT NULL,
    position INTEGER,
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- =========================================================
-- Tasks
-- =========================================================
CREATE TABLE tasks (
    task_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    section_id TEXT,
    assignee_id TEXT,
    name TEXT NOT NULL,
    description TEXT,
    due_date DATE,
    priority TEXT,
    completed INTEGER,
    created_at TIMESTAMP,
    completed_at TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id),
    FOREIGN KEY (section_id) REFERENCES sections(section_id),
    FOREIGN KEY (assignee_id) REFERENCES users(user_id)
);

-- =========================================================
-- Subtasks
-- =========================================================
CREATE TABLE subtasks (
    subtask_id TEXT PRIMARY KEY,
    parent_task_id TEXT NOT NULL,
    assignee_id TEXT,
    name TEXT NOT NULL,
    completed INTEGER,
    created_at TIMESTAMP,
    FOREIGN KEY (parent_task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (assignee_id) REFERENCES users(user_id)
);

-- =========================================================
-- Comments / Stories
-- =========================================================
CREATE TABLE comments (
    comment_id TEXT PRIMARY KEY,
    task_id TEXT NOT NULL,
    author_id TEXT NOT NULL,
    body TEXT,
    created_at TIMESTAMP,
    FOREIGN KEY (task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (author_id) REFERENCES users(user_id)
);

-- =========================================================
-- Tags
-- =========================================================
CREATE TABLE tags (
    tag_id TEXT PRIMARY KEY,
    name TEXT UNIQUE
);

-- =========================================================
-- Task–Tag Associations
-- =========================================================
CREATE TABLE task_tags (
    task_id TEXT NOT NULL,
    tag_id TEXT NOT NULL,
    PRIMARY KEY (task_id, tag_id),
    FOREIGN KEY (task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id)
);

-- =========================================================
-- Custom Field Definitions
-- =========================================================
CREATE TABLE custom_field_definitions (
    field_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    field_type TEXT,
    applicable_project_id TEXT,
    FOREIGN KEY (applicable_project_id) REFERENCES projects(project_id)
);

-- =========================================================
-- Custom Field Values
-- =========================================================
CREATE TABLE custom_field_values (
    field_id TEXT NOT NULL,
    task_id TEXT NOT NULL,
    value TEXT,
    PRIMARY KEY (field_id, task_id),
    FOREIGN KEY (field_id) REFERENCES custom_field_definitions(field_id),
    FOREIGN KEY (task_id) REFERENCES tasks(task_id)
);
