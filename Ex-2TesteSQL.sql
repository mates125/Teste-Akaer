SELECT [dbo].[products].name, [dbo].[categories].name FROM [dbo].[categories], [dbo].[products]
WHERE (([dbo].[products].[amount] > 100) AND (
[dbo].[products].[id_categories] = 1 or
[dbo].[products].[id_categories] = 2 or
[dbo].[products].[id_categories] = 3 or
[dbo].[products].[id_categories] = 6 or
[dbo].[products].[id_categories] = 9) AND [dbo].[products].[id_categories] = [dbo].[categories].[id])

ORDER BY [dbo].[products].[id_categories]