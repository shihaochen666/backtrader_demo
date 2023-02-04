from _cython_0_29_32 import generator

from ..main import get_db


class BaseDao(object):
    """Base(基础)Dao，用于被继承.

    CRUD基础Dao类，拥有基本方法，可直接继承使用

    Attributes:
        user_id: 当前操作用户id
        db: db实体
    """
    Model = None

    def __init__(self):
        self.db = get_db()

    def create(self, model: Model):
        """
        创建一条数据
        :param model: 数据模型实例
        """
        self.db.sess.add(model)
        self.db.sess.flush()

    def read(self, id: int, user_id: int = None, is_deleted: int = 0) -> Model:
        """
        读取一条数据
        :param id: 数据id
        :param user_id: 用户id
        :param is_deleted: 是否为已删除数据
        :return: 数据模型实例
        """

        # 定义：query过滤条件
        filters = []

        # 判断：软删标记
        if is_deleted == 1:
            filters.append(self.Model.is_deleted == 1)
        elif is_deleted == 2:
            pass
        else:
            filters.append(self.Model.is_deleted == 0)

        # 判断：是否限制指定用户的数据
        if user_id:
            filters.append(self.Model.user_id == user_id)

        return self.db.sess.query(self.Model).filter(
            self.Model.id == id,
            *filters
        ).first()

    def update(self, model: Model):
        """
        更新一条数据
        :param model: 数据模型实例
        :return:
        """
        self.db.sess.add(model)
        self.db.sess.flush()

    def delete(self, model: Model):
        """
        删除一条数据，软删除
        :param model: 数据模型实体
        """
        model.is_deleted = 1
        self.update(model)
