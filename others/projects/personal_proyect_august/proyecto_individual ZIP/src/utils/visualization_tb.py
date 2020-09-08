import os, sys
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
import plotly.graph_objs as go
import plotly.express as px 
import plotly.io as pio
import folders_tb as ftb

def grafI_est (x_val, y_val, hue_val, df, inv_y): 

    """ Crea un gráfico INTERACTIVO con el valor de una columna de datos en un gráfico de línea
        Guarda el gráfico (.html) en el directorio TEND_EST"""

    tit = y_val.replace("_"," ").title() + " en Madrid "
    fig = px.line(df, x=x_val, y=y_val, color=hue_val, line_group=hue_val, hover_name=hue_val,
        line_shape="spline", render_mode="svg")
    fig.update_layout(     
            title = {"text" : tit, "x":0.5, "xanchor":"center"}, 
            xaxis_title = x_val.title(),
            yaxis_title = y_val.replace("_"," ").title(),
            legend=dict(title= "Country", y=0.5, font_size=12)
                    )
    file_name = y_val+ "_x_C_D"
    ftb.salvarI_plot(fig,"../resources/plots/TEND_EST/", file_name)
    fig.show()

def grafI_temp_medias (frec,col_dat, cname,cdf):

    """ Crea un gráfico dinámico por cada columna de datos indicada (col_dat)
        Guarda cada gráfico (html) en un directorio con el nombre del indicado en ccode
    """

    fig = px.line(cdf, x="fecha", y=col_dat, line_shape="spline", render_mode="svg")

    fig.update_layout(     
            title = {"text" : "Temperaturas medias"+ frec, "x":0.4, "xanchor":"center"}, 
            xaxis_title = "Año",
            yaxis_title = "Temperatura ºC",
            legend=dict(title= " ", y=0.5, font_size=12)
                    )
    filen=filen+ frec
    dirn = "../resources/plots/"+ frec+ "/"
    ftb.salvarI_plot(fig, dirn, filen)
    fig.show()



def graf_corr (df, col, f):

    """ Gráfico estático tipo mapa de calor (Heatmap) con las correlación entre las principales variables
        Guarda el gráfico (.png) en el directorio M_corr  
        Los parametros que recibe son: df= nombre dataframe, col=color y f=frecuencia de los datos  """ 

    plt.subplots(figsize=(16, 12)) 
    corr = df.corr() 
    sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool),  cmap= col, square=True,  annot=True)
    if f =="A":
        plt.title ("Datos anuales - Heatmap")
        file_name = f+"_heatmap" +  ".png"
        ftb.salvar_plot ( "../resources/plots/M_corr", file_name)
    elif f=="M":
        plt.title ("Datos mensuales - Heatmap")
        file_name = f + "_heatmap" +  ".png"
        ftb.salvar_plot ( "../resources/plots/M_corr/", file_name)
    else:
        plt.title ("Datos diarios - Heatmap")
        file_name = f+"_heatmap" +  ".png"
        ftb.salvar_plot ( "../resources/plots/M_corr/", file_name)
    plt.show()

def graf_hist (df, col, f):

    """ Trazará histogramas para todas las características que están presentes en el conjunto de datos.
        Guarda el gráfico (.htmlpng) en el directorio M_hist
        Los parametros que recibe son: df= nombre dataframe, col=color y f=frecuencia de los datos  """ 
    
    plt.subplots(figsize=(16, 12)) 
    corr = df.corr() 
    sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool),  cmap= col, square=True,  annot=True)
    if f =="A":
        plt.title ("Datos anuales - Heatmap")
        file_name = f+"_heatmap" +  ".png"
        ftb.salvar_plot ( "../resources/plots/M_corr", file_name)
    elif f=="M":
        plt.title ("Datos mensuales - Heatmap")
        file_name = f + "_heatmap" +  ".png"
        ftb.salvar_plot ( "../resources/plots/M_corr/", file_name)
    else:
        plt.title ("Datos diarios - Heatmap")
        file_name = f+"_heatmap" +  ".png"
        ftb.salvar_plot ( "../resources/plots/M_corr/", file_name)
    plt.show()

    #def tiempo_empleado(Tiempo):
    """
    Traza un gráfico circular con el tiempo empleado en cada parte del proyecto    """
    


    #plt.show()