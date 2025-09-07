-- import
with source as (
    select
        "Date",
        "Close",
        "simbolo"
    from
        {{source('dbsales', 'tb_commodities')}}
),

-- renamed
renamed as (
    select
        cast("Date" as date) as data,
        "Close" as valor_fechamento,
        "simbolo" as simbolo
    from
        source
) 

-- select * from

select *
from renamed