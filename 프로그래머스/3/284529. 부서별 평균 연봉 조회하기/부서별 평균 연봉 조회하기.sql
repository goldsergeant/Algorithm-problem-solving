select dept_id,dept_name_en,round(avg(sal)) as avg_sal
from hr_department join hr_employees using(dept_id)
group by dept_id
order by avg_sal desc;