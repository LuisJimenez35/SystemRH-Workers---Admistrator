USE [Db_prueba_py]
GO
/****** Object:  Table [dbo].[Users]    Script Date: 3/5/2023 21:13:17 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Users](
	[UserName] [varchar](max) NOT NULL,
	[Email] [varchar](max) NOT NULL,
	[SecurityQuestion] [varchar](max) NOT NULL,
	[Pass] [varchar](max) NOT NULL,
	[Position_Work] [nchar](100) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Workers]    Script Date: 3/5/2023 21:13:17 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Workers](
	[DNI] [nchar](100) NOT NULL,
	[Name] [nchar](100) NOT NULL,
	[LastName] [nchar](100) NOT NULL,
	[Position] [nchar](100) NOT NULL,
	[Salary] [float] NOT NULL,
 CONSTRAINT [PK_Workers] PRIMARY KEY CLUSTERED 
(
	[DNI] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Workers_Information]    Script Date: 3/5/2023 21:13:17 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Workers_Information](
	[DNI_Worker] [nchar](100) NOT NULL,
	[Email_Worker] [nchar](100) NOT NULL,
	[Cellphone] [nchar](100) NOT NULL,
	[Adress] [nchar](100) NOT NULL,
	[Contragting_Date] [date] NOT NULL,
	[Birthday] [date] NOT NULL
) ON [PRIMARY]
GO
INSERT [dbo].[Users] ([UserName], [Email], [SecurityQuestion], [Pass], [Position_Work]) VALUES (N'Admin121', N'luismorajimenez35@gmail.com', N'San Juan', N'RH4040', NULL)
GO
ALTER TABLE [dbo].[Users]  WITH CHECK ADD  CONSTRAINT [FK_Users_Workers] FOREIGN KEY([Position_Work])
REFERENCES [dbo].[Workers] ([DNI])
GO
ALTER TABLE [dbo].[Users] CHECK CONSTRAINT [FK_Users_Workers]
GO
ALTER TABLE [dbo].[Workers_Information]  WITH CHECK ADD  CONSTRAINT [FK_Workers_Information_Workers] FOREIGN KEY([DNI_Worker])
REFERENCES [dbo].[Workers] ([DNI])
GO
ALTER TABLE [dbo].[Workers_Information] CHECK CONSTRAINT [FK_Workers_Information_Workers]
GO