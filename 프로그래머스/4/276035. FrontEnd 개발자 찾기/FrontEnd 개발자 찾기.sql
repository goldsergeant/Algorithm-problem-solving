select id,email,first_name,last_name
from developers d
where exists (select 1 from skillcodes s where s.category='front end' and d.skill_code&s.code)
order by id;