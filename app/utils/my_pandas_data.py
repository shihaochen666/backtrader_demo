import backtrader


class MyPandasData(backtrader.feeds.PandasData):
    lines = ('amount',)  # 要添加的列名
    # 设置 line 在数据源上新增的位置
    params = (
        ('amount', -1),  # turnover对应传入数据的列名，这个-1会自动匹配backtrader的数据类与原有pandas文件的列名
        # 如果是个大于等于0的数，比如8，那么backtrader会将原始数据下标8(第9列，下标从0开始)的列认为是turnover这一列
    )
