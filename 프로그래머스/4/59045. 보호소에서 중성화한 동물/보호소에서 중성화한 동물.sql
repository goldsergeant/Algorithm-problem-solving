select ai.animal_id,ai.animal_type,ai.name
from animal_ins ai join animal_outs ao on ai.animal_id=ao.animal_id
where ai.SEX_UPON_INTAKE like '%intact%' and (ao.sex_upon_outcome like '%spayed%' or ao.sex_upon_outcome like '%neutered%')
order by ai.animal_id;