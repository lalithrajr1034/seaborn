"""
- Relational plot
  scatterplot        --- Bivariate/Multivariate | Numerical vs Numerical
  lineplot           --- Univariate/Bivariate   | Numerical vs (categorical or numerical)

- Distribution plot
  Histogram          --- Univariate            | Numerical
  kdeplot            --- Univariate/Bivariate  | Numerical
  ecdfplot           --- Univariate            | Numerical
  rugplot            --- Univariate            | Numerical

- Categorical plot
  countplot          --- Univariate            | Categorical
  barplot            --- Bivariate             | Categorical (x) + Numerical (y)
  boxplot            --- Bivariate/Multivariate| Categorical (x) + Numerical (y)
  violinplot         --- Bivariate/Multivariate| Categorical (x) + Numerical (y)
  swarmplot          --- Bivariate/Multivariate| Categorical (x) + Numerical (y)

- Matrix plot
  heatmap            --- Multivariate          | Numerical (correlations/matrices)
  clustermap         --- Multivariate          | Numerical (clusters/matrix)

# commonly this are numerical plot data
  
- Multi plot
  jointplot          --- Bivariate             | Numerical vs Numerical
  pairplot           --- Multivariate          | Numerical (multiple columns)

- Regression plot
  regplot            --- Bivariate             | Numerical vs Numerical
  lmplot             --- Bivariate/Multivariate| Numerical vs Numerical (+ categorical via hue/col)
  residplot          --- Univariate/Bivariate  | Numerical (residuals)

"""