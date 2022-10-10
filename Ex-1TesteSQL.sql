SELECT [dbo].[costumers].name,  [dbo].[orders].id_costumers FROM [dbo].[costumers], [dbo].[orders]
WHERE(

[dbo].[costumers].id = [dbo].[orders].id_costumers
AND
[dbo].[orders].[orders_date] <= '2016-06-01'

)