select ao.animal_id,ao.name 
from animal_ins ai join animal_outs ao on ai.animal_id=ao.animal_id
order by ao.datetime - ai.datetime desc limit 2;