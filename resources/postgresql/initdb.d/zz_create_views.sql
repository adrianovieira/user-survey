---- cria views materializadas com dados
---- para atualizar views materializadas
---- exemplo: REFRESH MATERIALIZED VIEW inside.mv_survey_periodo_origin_status;
CREATE MATERIALIZED VIEW IF NOT EXISTS inside.mv_survey_loaded_at_origin_status AS
    SELECT to_char(created_at, 'YYYY-MM-DD HH24:MI:SS')::TIMESTAMP AS loaded_at, 
        origin, 
        (CASE response_status_id
            WHEN 1 THEN 'Válido'
            WHEN 2 THEN 'Inválido'
            WHEN 3 THEN 'Incompleto'
            WHEN 4 THEN 'Pendente'
            WHEN 5 THEN 'Aberto'
            WHEN 6 THEN 'Visualizou'
        END) AS status,
        count(id) 
        FROM inside.users_surveys_responses_aux 
        GROUP BY loaded_at, origin, status;

CREATE INDEX ON inside.mv_survey_loaded_at_origin_status (loaded_at, origin, status);

CREATE MATERIALIZED VIEW IF NOT EXISTS inside.mv_survey_loaded_at_status AS
    SELECT to_char(created_at, 'YYYY-MM-DD HH24:MI:SS')::TIMESTAMP AS loaded_at, 
        (CASE response_status_id
            WHEN 1 THEN 'Válido'
            WHEN 2 THEN 'Inválido'
            WHEN 3 THEN 'Incompleto'
            WHEN 4 THEN 'Pendente'
            WHEN 5 THEN 'Aberto'
            WHEN 6 THEN 'Visualizou'
        END) AS status,
        count(id) 
        FROM inside.users_surveys_responses_aux 
        GROUP BY loaded_at, status;

CREATE INDEX ON inside.mv_survey_loaded_at_status (loaded_at, status);

CREATE MATERIALIZED VIEW inside.mv_survey_origin AS
    SELECT origin
        FROM inside.users_surveys_responses_aux
        GROUP BY origin;


---- cria views dinâmicas
CREATE OR REPLACE VIEW inside.v_survey_created_at_origin_status AS
    SELECT created_at, 
        origin, 
        (CASE response_status_id
            WHEN 1 THEN 'Válido'
            WHEN 2 THEN 'Inválido'
            WHEN 3 THEN 'Incompleto'
            WHEN 4 THEN 'Pendente'
            WHEN 5 THEN 'Aberto'
            WHEN 6 THEN 'Visualizou'
        END) AS status
        FROM inside.users_surveys_responses_aux 
        ORDER BY created_at, origin;
