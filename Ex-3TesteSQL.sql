SELECT [dbo].[categories].[name], SUM([dbo].[products].[amount]) as quantidade FROM [dbo].[categories], [dbo].[products]
WHERE [dbo].[products].[id_categories] = [dbo].[categories].[id]

GROUP BY [dbo].[categories].[name]