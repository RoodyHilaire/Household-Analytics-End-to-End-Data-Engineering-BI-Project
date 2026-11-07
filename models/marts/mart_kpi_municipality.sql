
SELECT
    municipality,
    COUNT(*) AS households,
    AVG(income) AS avg_income,
    SUM(children_under_5) AS children_u5,
    SUM(elderly) AS elderly_population
from {{ ref('stg_households') }}
GROUP BY municipality
