get_ids_in_logs_1 = """SELECT distinct l.firm_id
from log_16.logs_user_stat l
join (select l.firm_id w1
from log_16.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_16.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_15.logs_user_stat l
join (select l.firm_id w1
from log_15.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_15.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_14.logs_user_stat l
join (select l.firm_id w1
from log_14.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_14.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_13.logs_user_stat l
join (select l.firm_id w1
from log_13.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_13.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_12.logs_user_stat l
join (select l.firm_id w1
from log_12.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_12.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_11.logs_user_stat l
join (select l.firm_id w1
from log_11.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_11.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_10.logs_user_stat l
join (select l.firm_id w1
from log_10.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_10.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_9.logs_user_stat l
join (select l.firm_id w1
from log_9.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_9.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_8.logs_user_stat l
join (select l.firm_id w1
from log_8.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_8.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_7.logs_user_stat l
join (select l.firm_id w1
from log_7.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_7.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_6.logs_user_stat l
join (select l.firm_id w1
from log_6.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_6.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_5.logs_user_stat l
join (select l.firm_id w1
from log_5.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_5.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_4.logs_user_stat l
join (select l.firm_id w1
from log_4.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_4.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_3.logs_user_stat l
join (select l.firm_id w1
from log_3.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_3.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_2.logs_user_stat l
join (select l.firm_id w1
from log_2.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_2.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_1.logs_user_stat l
join (select l.firm_id w1
from log_1.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_1.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)
;"""


get_ids_in_logs_2 = """SELECT distinct l.firm_id
from log_20.logs_user_stat l
join (select l.firm_id w1
from log_20.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_20.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_18.logs_user_stat l
join (select l.firm_id w1
from log_18.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_18.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_17.logs_user_stat l
join (select l.firm_id w1
from log_17.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_17.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_32.logs_user_stat l
join (select l.firm_id w1
from log_32.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_32.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_31.logs_user_stat l
join (select l.firm_id w1
from log_31.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_31.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_30.logs_user_stat l
join (select l.firm_id w1
from log_30.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_30.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_29.logs_user_stat l
join (select l.firm_id w1
from log_29.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_29.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_28.logs_user_stat l
join (select l.firm_id w1
from log_28.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_28.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_27.logs_user_stat l
join (select l.firm_id w1
from log_27.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_27.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_26.logs_user_stat l
join (select l.firm_id w1
from log_26.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_26.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_25.logs_user_stat l
join (select l.firm_id w1
from log_25.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_25.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_24.logs_user_stat l
join (select l.firm_id w1
from log_24.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_24.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_23.logs_user_stat l
join (select l.firm_id w1
from log_23.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_23.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_22.logs_user_stat l
join (select l.firm_id w1
from log_22.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_22.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_21.logs_user_stat l
join (select l.firm_id w1
from log_21.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_21.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)

union

select distinct l.firm_id
from log_19.logs_user_stat l
join (select l.firm_id w1
from log_19.logs_user_stat l
where l.logs_date between 20200101 and DATE_add(date(now()), INTERVAL -1 MONTH) and l.admin_id = 0)q on q.w1 = l.firm_id
where l.logs_date > date(now()) and l.admin_id = 0
and l.firm_id not in (select l.firm_id w1
from log_19.logs_user_stat l
where l.logs_date between DATE_add(date(now()), INTERVAL -1 MONTH) and date(now()) and l.admin_id = 0)
;"""


get_firm_info = """SELECT f.id as 'ID организации',
        ifnull(f.org_name_short, f.org_name) as 'Название организации',
        f.code_inn as 'ИНН организации', 
        ifnull(f.site_url, '-') as 'Сайт организации'
from fabrikant.firms f
where f.id in ({organization_ids})
;"""