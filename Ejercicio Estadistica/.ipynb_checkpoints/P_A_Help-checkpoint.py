import numpy as np

def eval_model(df_train,df_valid,binsA=10,binsP=10):
    hist_H = np.histogram2d(df_train[df_train["Genero"]=="Hombre"]["Altura"].values,
                          df_train[df_train["Genero"]=="Hombre"]["Peso"].values,
                          bins=[binsA,binsP],
                          range=[[df_train["Altura"].min(),df_train["Altura"].max()],
                                 [df_train["Peso"].min(),df_train["Peso"].max()]])
    hist_M = np.histogram2d(df_train[df_train["Genero"]=="Mujer"]["Altura"].values,
                          df_train[df_train["Genero"]=="Mujer"]["Peso"].values,
                          bins=[binsA,binsP],
                          range=[[df_train["Altura"].min(),df_train["Altura"].max()],
                                 [df_train["Peso"].min(),df_train["Peso"].max()]])
    idx_A = np.digitize(df_valid["Altura"].values,hist_M[1]) - 1
    idx_A[idx_A == -1] = 0
    idx_A[idx_A == binsA] = binsA - 1
    idx_P = np.digitize(df_valid["Peso"].values,hist_M[2]) - 1
    idx_P[idx_P == -1] = 0
    idx_P[idx_P == binsP] = binsP - 1
    
    pred = hist_M[0][list(idx_A),list(idx_P)]>hist_H[0][list(idx_A),list(idx_P)]
    pred = pred == (df_valid["Genero"] == "Mujer")
    
    return sum(pred) / len(pred)