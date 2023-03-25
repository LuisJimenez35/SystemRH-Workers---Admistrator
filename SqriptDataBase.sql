USE [Db_prueba_py]
GO
/****** Object:  Table [dbo].[Beneficios]    Script Date: 24/3/2023 21:20:51 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Beneficios](
	[id_beneficio] [int] NOT NULL,
	[nombre_beneficio] [varchar](50) NULL,
	[descripcion_beneficio] [varchar](255) NULL,
PRIMARY KEY CLUSTERED 
(
	[id_beneficio] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Candidatos]    Script Date: 24/3/2023 21:20:51 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Candidatos](
	[CandidatoID] [int] NOT NULL,
	[NombreCompleto] [nvarchar](100) NULL,
	[FechaNacimiento] [date] NULL,
	[Direccion] [nvarchar](200) NULL,
	[Telefono] [nvarchar](20) NULL,
	[Email] [nvarchar](100) NULL,
	[UltimoTrabajo] [nvarchar](200) NULL,
PRIMARY KEY CLUSTERED 
(
	[CandidatoID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[CandidatosHabilidades]    Script Date: 24/3/2023 21:20:51 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CandidatosHabilidades](
	[CandidatoID] [int] NOT NULL,
	[HabilidadID] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[CandidatoID] ASC,
	[HabilidadID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Conceptos_Pago]    Script Date: 24/3/2023 21:20:51 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Conceptos_Pago](
	[id_concepto] [int] NOT NULL,
	[nombre_concepto] [varchar](50) NULL,
	[descripcion_concepto] [varchar](255) NULL,
PRIMARY KEY CLUSTERED 
(
	[id_concepto] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Departamentos]    Script Date: 24/3/2023 21:20:51 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Departamentos](
	[id_departamento] [int] NOT NULL,
	[nombre_departamento] [varchar](50) NULL,
	[descripcion_departamento] [varchar](255) NULL,
PRIMARY KEY CLUSTERED 
(
	[id_departamento] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Detalles_Pago]    Script Date: 24/3/2023 21:20:51 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Detalles_Pago](
	[id_detalle] [int] NOT NULL,
	[id_pago] [int] NULL,
	[id_concepto] [int] NULL,
	[cantidad] [int] NULL,
	[monto_unitario] [decimal](10, 2) NULL,
PRIMARY KEY CLUSTERED 
(
	[id_detalle] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Empleados]    Script Date: 24/3/2023 21:20:51 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Empleados](
	[id_empleado] [int] NOT NULL,
	[nombre] [varchar](50) NULL,
	[apellido] [varchar](50) NULL,
	[fecha_nacimiento] [date] NULL,
	[correo_electronico] [varchar](100) NULL,
	[telefono] [varchar](20) NULL,
PRIMARY KEY CLUSTERED 
(
	[id_empleado] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Empleados_Beneficios]    Script Date: 24/3/2023 21:20:51 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Empleados_Beneficios](
	[id_empleado] [int] NOT NULL,
	[id_beneficio] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id_empleado] ASC,
	[id_beneficio] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Habilidades]    Script Date: 24/3/2023 21:20:51 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Habilidades](
	[HabilidadID] [int] NOT NULL,
	[Descripcion] [nvarchar](100) NULL,
PRIMARY KEY CLUSTERED 
(
	[HabilidadID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Historial_Laboral]    Script Date: 24/3/2023 21:20:51 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Historial_Laboral](
	[id_historial] [int] NOT NULL,
	[id_empleado] [int] NULL,
	[id_puesto] [int] NULL,
	[id_departamento] [int] NULL,
	[fecha_inicio] [date] NULL,
	[fecha_fin] [date] NULL,
PRIMARY KEY CLUSTERED 
(
	[id_historial] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Pagos]    Script Date: 24/3/2023 21:20:51 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Pagos](
	[id_pago] [int] NOT NULL,
	[id_empleado] [int] NULL,
	[fecha_pago] [date] NULL,
	[monto_pago] [decimal](10, 2) NULL,
PRIMARY KEY CLUSTERED 
(
	[id_pago] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Postulaciones]    Script Date: 24/3/2023 21:20:51 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Postulaciones](
	[PostulacionID] [int] NOT NULL,
	[CandidatoID] [int] NULL,
	[PuestoID] [int] NULL,
	[FechaPostulacion] [datetime] NULL,
PRIMARY KEY CLUSTERED 
(
	[PostulacionID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Puestos]    Script Date: 24/3/2023 21:20:51 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Puestos](
	[id_puesto] [int] NOT NULL,
	[nombre_puesto] [varchar](50) NULL,
	[descripcion_puesto] [varchar](255) NULL,
PRIMARY KEY CLUSTERED 
(
	[id_puesto] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[RequisitosPuesto]    Script Date: 24/3/2023 21:20:51 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[RequisitosPuesto](
	[PuestoID] [int] NOT NULL,
	[HabilidadID] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[PuestoID] ASC,
	[HabilidadID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[users]    Script Date: 24/3/2023 21:20:51 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[users](
	[UserName] [varchar](50) NOT NULL,
	[Email] [varchar](50) NOT NULL,
	[SecurityQuestion] [varchar](50) NOT NULL,
	[Pass] [varchar](50) NOT NULL
) ON [PRIMARY]
GO
INSERT [dbo].[users] ([UserName], [Email], [SecurityQuestion], [Pass]) VALUES (N'Admin121', N'luismorajimenez35@gmail.com', N'SanJuan', N'RU4050')
GO
INSERT [dbo].[users] ([UserName], [Email], [SecurityQuestion], [Pass]) VALUES (N'Admin800', N'soportprimeprogram@gmail.com', N'Barbacoas', N'SP2023')
GO
INSERT [dbo].[users] ([UserName], [Email], [SecurityQuestion], [Pass]) VALUES (N'Admin670', N'lmj14356@gmail.com', N'Cortezal', N'IL3000')
GO
ALTER TABLE [dbo].[CandidatosHabilidades]  WITH CHECK ADD FOREIGN KEY([CandidatoID])
REFERENCES [dbo].[Candidatos] ([CandidatoID])
GO
ALTER TABLE [dbo].[CandidatosHabilidades]  WITH CHECK ADD FOREIGN KEY([HabilidadID])
REFERENCES [dbo].[Habilidades] ([HabilidadID])
GO
ALTER TABLE [dbo].[Detalles_Pago]  WITH CHECK ADD FOREIGN KEY([id_concepto])
REFERENCES [dbo].[Conceptos_Pago] ([id_concepto])
GO
ALTER TABLE [dbo].[Detalles_Pago]  WITH CHECK ADD FOREIGN KEY([id_pago])
REFERENCES [dbo].[Pagos] ([id_pago])
GO
ALTER TABLE [dbo].[Empleados_Beneficios]  WITH CHECK ADD FOREIGN KEY([id_beneficio])
REFERENCES [dbo].[Beneficios] ([id_beneficio])
GO
ALTER TABLE [dbo].[Empleados_Beneficios]  WITH CHECK ADD FOREIGN KEY([id_empleado])
REFERENCES [dbo].[Empleados] ([id_empleado])
GO
ALTER TABLE [dbo].[Historial_Laboral]  WITH CHECK ADD FOREIGN KEY([id_departamento])
REFERENCES [dbo].[Departamentos] ([id_departamento])
GO
ALTER TABLE [dbo].[Historial_Laboral]  WITH CHECK ADD FOREIGN KEY([id_empleado])
REFERENCES [dbo].[Empleados] ([id_empleado])
GO
ALTER TABLE [dbo].[Historial_Laboral]  WITH CHECK ADD FOREIGN KEY([id_puesto])
REFERENCES [dbo].[Puestos] ([id_puesto])
GO
ALTER TABLE [dbo].[Pagos]  WITH CHECK ADD FOREIGN KEY([id_empleado])
REFERENCES [dbo].[Empleados] ([id_empleado])
GO
ALTER TABLE [dbo].[Postulaciones]  WITH CHECK ADD FOREIGN KEY([CandidatoID])
REFERENCES [dbo].[Candidatos] ([CandidatoID])
GO
ALTER TABLE [dbo].[Postulaciones]  WITH CHECK ADD FOREIGN KEY([PuestoID])
REFERENCES [dbo].[Puestos] ([id_puesto])
GO
ALTER TABLE [dbo].[RequisitosPuesto]  WITH CHECK ADD FOREIGN KEY([HabilidadID])
REFERENCES [dbo].[Habilidades] ([HabilidadID])
GO
ALTER TABLE [dbo].[RequisitosPuesto]  WITH CHECK ADD FOREIGN KEY([PuestoID])
REFERENCES [dbo].[Puestos] ([id_puesto])
GO
