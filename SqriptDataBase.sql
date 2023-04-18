USE [Db_prueba_py]
GO
/****** Object:  Table [dbo].[Users]    Script Date: 31/3/2023 15:59:44 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Users](
	[UserName] [varchar](max) NOT NULL,
	[Email] [varchar](max) NOT NULL,
	[SecurityQuestion] [varchar](max) NOT NULL,
	[Pass] [varchar](max) NOT NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Workers - Principal Data]    Script Date: 31/3/2023 15:59:44 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Workers - Principal Data](
	[DNI] [int] NOT NULL,
	[Full_name] [varchar](max) NOT NULL,
	[First_surname] [varchar](max) NOT NULL,
	[Second_name] [varchar](max) NOT NULL,
	[Birth_Day] [date] NOT NULL,
	[Hiring date] [date] NOT NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
INSERT [dbo].[Users] ([UserName], [Email], [SecurityQuestion], [Pass]) VALUES (N'Admin121', N'luismorajimenez35@gmail.com', N'San Juan', N'RH3090')
GO