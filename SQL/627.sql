-- 交换工资

-- 给定一个 salary 表，如下所示，有 m = 男性 和 f = 女性 的值。交换所有的 f 和 m 值（例如，将所有 f 值更改为 m，反之亦然）。要求只使用一个更新（Update）语句，并且没有中间的临时表。

-- | id | name | sex | salary |
-- |----|------|-----|--------|
-- | 1  | A    | m   | 2500   |
-- | 2  | B    | f   | 1500   |
-- | 3  | C    | m   | 5500   |
-- | 4  | D    | f   | 500    |

-- 注意，您必只能写一个 Update 语句，请不要编写任何 Select 语句。


-- way 1
update salary
set sex = (
    case sex when 'm' then 'f' else 'm' end
);

-- way 2
update salary set sex = if(sex='m','f','m');


