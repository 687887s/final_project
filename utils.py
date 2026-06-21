import numpy as np

def solveLS(G, d):
    """
    Solve least square solution using NumPy array calculations.
    
    Parameters:
        G (numpy.ndarray): The design matrix G (n×2).
        d (numpy.ndarray): The observation vector d (n×1).
    
    Returns:
        m (numpy.ndarray): The least squares solution vector (2×1).
        RSS (float): The residual sum of squares.
        residual_variance (float): The residual variance (σ²) with degrees of freedom correction.
    """
    
    # Calculate the least squares solution
    m = np.linalg.inv(G.T @ G) @ G.T @ d
    
    # Calculate the error vector
    e = d - G @ m
    
    # Compute the residual sum of squares (RSS)
    RSS = np.sum(e**2)
    
    # Compute the residual variance with degrees of freedom correction
    n = len(d)  # 資料點數量
    p = len(m)     # 模型參數個數
    residual_variance = RSS / (n - p)
    
    return m, RSS, residual_variance

def solveWLS(G, d, W):
    """
    Solve weighted least square solution using NumPy array calculations.
    
    Parameters:
        G (numpy.ndarray): The design matrix G (n×2).
        d (numpy.ndarray): The observation vector d (n×1).
        W (numpy.ndarray): The weight matrix W (n×n).
    
    Returns:
        m (numpy.ndarray): The weighted least squares solution vector (2×1).
        RSS (float): The weighted residual sum of squares.
        residual_variance (float): The weighted residual variance (σ²) with degrees of freedom correction.
    """
    
    # Calculate the weighted least squares solution
    m = np.linalg.inv(G.T @ W @ G) @ G.T @ W @ d
    
    # Calculate the error vector
    e = d - G @ m
    
    # Compute the weighted residual sum of squares (RSS)
    RSS = np.sum(e**2)
    
    # Compute the weighted residual variance with degrees of freedom correction
    n = len(d)      # 資料點數量
    p = len(m)      # 模型參數個數
    residual_variance = RSS / (n - p)
    
    return m, RSS, residual_variance