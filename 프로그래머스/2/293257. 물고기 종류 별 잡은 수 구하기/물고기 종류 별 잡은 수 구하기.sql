select count(fi.id) as FISH_COUNT,fni.fish_name as FISH_NAME
from fish_name_info fni join fish_info fi using(fish_type)
group by fni.fish_name
order by fish_count desc;