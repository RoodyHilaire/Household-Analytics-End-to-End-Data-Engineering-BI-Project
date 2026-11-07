select
    *
from {{ source('raw', 'households') }}
