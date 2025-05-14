select fi.id,fn.fish_name,fi.length
from fish_info fi join fish_name_info fn using(fish_type)
where (fn.fish_type,fi.length) in (select fish_type,max(length) from fish_info
                     group by fish_type)
order by id;