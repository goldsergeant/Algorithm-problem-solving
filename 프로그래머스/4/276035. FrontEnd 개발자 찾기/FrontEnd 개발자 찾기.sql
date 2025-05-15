select id,email,first_name,last_name
from developers d
where exists (select * from skillcodes where category='Front End' and code&d.skill_code)
order by id;