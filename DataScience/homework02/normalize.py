def z_scaler(feature):
    """
    Нормализуем значения
    :param feature: выборка, которую надо нормализовать
    :return: нормализованная выборка
    """
    feature_scaled = 0  # будущая нормализованная выборка
    S = 0  # среднеквадратическое отклонение
    n = feature.size  # считаем размер выборки
    for i in range(n):
        """
        Цикл для произвеления нормализации
        """
        S = ((sum((feature[i] - feature.mean()) ** 0.5)) / n)  # cчитаем среднеквадратическое отклонение
    feature_scaled = (feature - feature.mean()) / S  # нормализуем
    
    return feature_scaled
