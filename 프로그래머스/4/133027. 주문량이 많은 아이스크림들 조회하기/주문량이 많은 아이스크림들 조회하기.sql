select f.flavor
from first_half f join july j on(f.flavor=j.flavor)
group by j.flavor
order by f.total_order+sum(j.total_order) desc
limit 3