
\connect iluminatti;

CREATE SCHEMA IF NOT EXISTS inside;

CREATE TABLE IF NOT EXISTS inside.users_surveys_responses_aux (
    id                   BIGINT PRIMARY KEY,
    origin               VARCHAR(15),
    response_status_id   INTEGER,
    created_at           TIMESTAMP WITH TIME ZONE DEFAULT now()
);

CREATE INDEX ON inside.users_surveys_responses_aux (created_at, origin, response_status_id);
CREATE INDEX ON inside.users_surveys_responses_aux (created_at DESC, origin, response_status_id);
CREATE INDEX ON inside.users_surveys_responses_aux (created_at, response_status_id, origin);

---- CREATE EXTENSION timescaledb;
---- SET TIME ZONE 'America/Sao_Paulo';
---- SET SEARCH_PATH TO inside;