-- import

with commodities as (
    select
        data,
        simbolo,
        valor_fechamento
    from 
        {{ ref('stg_commodities') }}
),

movimentacao as (
    select
        data,
        simbolo,
        acao,
        quantidade
    from
        {{ ref('stg_movimentacao_commodities') }}

),

joined as (
    select
        com.data,
        com.simbolo,
        com.valor_fechamento,
        mov.acao,
        mov.quantidade,
        (mov.quantidade * com.valor_fechamento) as valor,
        case
            when mov.acao = 'sell' then (mov.quantidade * com.valor_fechamento)
            else - (mov.quantidade * com.valor_fechamento)
        end as ganho
        from 
            commodities as com
        inner join
            movimentacao as mov
        on
            com.data = mov.data
            and
            com.simbolo = mov.simbolo
),

last_day as (
    select
        max(data) as max_data
    from
        joined
),

filtered as (
    select
        *
    from joined
    where
        data = (select max_data from last_day)
)

-- select
select
    data,
    simbolo,
    valor_fechamento,
    acao,
    quantidade,
    valor,
    ganho
from filtered