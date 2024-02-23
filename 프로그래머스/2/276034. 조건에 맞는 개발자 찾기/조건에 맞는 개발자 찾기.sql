select id,email,first_name,last_name
from developers d
where exists (select * from skillcodes s where d.skill_code&s.code and s.name in ('Python','C#') )
order by id;