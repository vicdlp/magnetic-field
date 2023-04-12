import numpy as np

P = np.array([[0.0192, 0, 0],
             [0, 0.0148, 0],
             [0, 0, 0.0240]]) # matrice de passage entre le champ mesuré et le courant dans les bobines (A/µT)


I_normal = np.array([0.0514, 0.078, 0.756 ]) # courant sans perturbations

def conversion(B, B_normal):
    
    I = np.dot(P, B_normal - B) # multiplication de la matrice de passage avec lécart entre B mesuré et B sans perturbation
    return I_normal - I # donne le nouveau courant à envoyer
    

    
