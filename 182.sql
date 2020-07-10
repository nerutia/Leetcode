# 查找重复的电子邮箱

# 编写一个 SQL 查询，查找 Person 表中所有重复的电子邮箱。


# Write your MySQL query statement below
select Email from Person group by Email having count(Email)>1




